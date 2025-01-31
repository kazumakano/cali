FROM tartancalib_20230920

# remove these commands if rootless
ARG GID UID USER_NAME
RUN groupadd --gid $GID $USER_NAME
RUN useradd --gid $GID --create-home --shell /bin/bash --uid $UID $USER_NAME

USER $UID:$GID

RUN echo source /catkin_ws/devel/setup.bash >> ~/.bashrc

WORKDIR /app/
