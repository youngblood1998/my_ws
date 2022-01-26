#!/bin/sh

if [ -n "$DESTDIR" ] ; then
    case $DESTDIR in
        /*) # ok
            ;;
        *)
            /bin/echo "DESTDIR argument must be absolute... "
            /bin/echo "otherwise python's distutils will bork things."
            exit 1
    esac
fi

echo_and_run() { echo "+ $@" ; "$@" ; }

echo_and_run cd "/home/jay/my_ws/src/easy_handeye/easy_handeye"

# ensure that Python install destination exists
echo_and_run mkdir -p "$DESTDIR/home/jay/my_ws/install/lib/python2.7/dist-packages"

# Note that PYTHONPATH is pulled from the environment to support installing
# into one location when some dependencies were installed in another
# location, #123.
echo_and_run /usr/bin/env \
    PYTHONPATH="/home/jay/my_ws/install/lib/python2.7/dist-packages:/home/jay/my_ws/build/lib/python2.7/dist-packages:$PYTHONPATH" \
    CATKIN_BINARY_DIR="/home/jay/my_ws/build" \
    "/usr/bin/python2" \
    "/home/jay/my_ws/src/easy_handeye/easy_handeye/setup.py" \
    egg_info --egg-base /home/jay/my_ws/build/easy_handeye/easy_handeye \
    build --build-base "/home/jay/my_ws/build/easy_handeye/easy_handeye" \
    install \
    --root="${DESTDIR-/}" \
    --install-layout=deb --prefix="/home/jay/my_ws/install" --install-scripts="/home/jay/my_ws/install/bin"
