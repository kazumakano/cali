import asyncio
import os
import os.path as path
from asyncio import subprocess as async_subprocess

MAX_TASK_NUM  = 10

async def cali(board_file: str, result_dir: str, use_stream: bool = False) -> None:
    task_queue: dict[str, dict[str, async_subprocess.Process | asyncio.Task]] = {}

    try:
        while True:
            for cn_1 in os.listdir(result_dir):
                if not path.exists(path.join(result_dir, cn_1, "log1-camchain.yaml")):
                    if len(task_queue) >= MAX_TASK_NUM:
                        done_tasks, _ = await asyncio.wait([d["task"] for d in task_queue.values()], return_when=asyncio.FIRST_COMPLETED)
                        for cn_2, d in task_queue.copy().items():
                            if d["task"] in done_tasks:
                                print(f"calibration {'completed' if path.exists(path.join(result_dir, cn_2, 'log1-camchain.yaml')) else 'failed'} for camera {cn_2}")
                                task_queue.pop(cn_2)
                                break

                    proc = await asyncio.create_subprocess_shell(f"/app/calibrate.sh {board_file} {cn_1} {result_dir} {'stream' if use_stream else 'file'} > {path.join(result_dir, cn_1, 'log.txt')} 2> {path.join(result_dir, cn_1, 'error.txt')}")
                    task_queue[cn_1] = {"proc": proc, "task": asyncio.create_task(proc.wait())}

                await asyncio.sleep(1)

    except:
        for d in task_queue.values():
            d["proc"].terminate()
            await d["task"]

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("-b", "--board_file", required=True, help="specify board file", metavar="PATH_TO_BOARD_FILE")
    parser.add_argument("-r", "--result_dir", required=True, help="specify result directory", metavar="PATH_TO_RESULT_DIR")
    parser.add_argument("-s", "--use_stream", action="store_true", help="use stream instead of file")
    args = parser.parse_args()

    asyncio.run(cali(args.board_file, args.result_dir, args.use_stream))
