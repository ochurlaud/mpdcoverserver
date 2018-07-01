#/bin/sh

./setup.py install
cp unitfile/mpdcoverserver.service /usr/lib/systemd/system/
cp src/mpdcoverserver.conf /etc/
