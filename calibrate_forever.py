import asyncio
import os
import os.path as path
from asyncio import subprocess as async_subprocess
from typing import Dict, List, Union

MAX_TASK_NUM  = 10

def _on_task_done(done_task: asyncio.Task, result_dir: str, task_queue: Dict[str, Dict[str, Union[List[str], async_subprocess.Process, asyncio.Task]]]) -> None:
    for cn, d in task_queue.items():
        if d["task"] == done_task:
            break

    if path.exists(path.join(result_dir, cn, "log1-camchain.yaml")):
        print(f"calibration completed for camera {cn}")
    else:
        print(f"calibration failed for camera {cn}")
        for e in d["errs"]:
            print(e)
    print()

    task_queue.pop(cn)

async def _parse_err(src: asyncio.StreamReader, tgt: List[str]) -> None:
    async for l in src:
        l = l.decode().strip()
        if "Error" in l:
            tgt.append(l)

async def cali(board_file: str, result_dir: str, use_stream: bool = False) -> None:
    task_queue: Dict[str, Dict[str, Union[List[str], async_subprocess.Process, asyncio.Task]]] = {}

    try:
        while True:
            for cn in os.listdir(result_dir):
                if path.exists(path.join(result_dir, cn, "video.bag")) and not path.exists(path.join(result_dir, cn, "log1-camchain.yaml")) and cn not in task_queue.keys():
                    if len(task_queue) >= MAX_TASK_NUM:
                        await asyncio.wait([d["task"] for d in task_queue.values()], return_when=asyncio.FIRST_COMPLETED)

                    proc = await asyncio.create_subprocess_shell(f"/app/calibrate.sh {board_file} {cn} {result_dir} {'stream' if use_stream else 'file'}", stdout=async_subprocess.DEVNULL, stderr=async_subprocess.PIPE)
                    task_queue[cn] = {"errs": [], "proc": proc, "task": asyncio.create_task(proc.wait())}
                    asyncio.create_task(_parse_err(task_queue[cn]["proc"].stderr, task_queue[cn]["errs"]))
                    task_queue[cn]["task"].add_done_callback(lambda t: _on_task_done(t, result_dir, task_queue))

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
