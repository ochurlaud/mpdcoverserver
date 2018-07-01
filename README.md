# MPDCoverServer

## Try it

Download this, customize `src/mpdcoverserer.conf', go to src and run `mpdcoverserver:

```
cd src
./mpdcoverserver
```

## Install

To install the package, 2 steps are needed:

1) run `./setup.py install` to deploy `src/mpdcoverserver` as a script and `src/songconver` as lib.
2) copy `src/mpdcoverserver.conf` to `/etc/`and `unitfile/mpdcoverserver.service` to `/usr/lib/systemd/system`

