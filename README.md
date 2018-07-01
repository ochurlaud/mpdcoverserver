# MPDCoverServer

A simple HTTP server in python that when queried

    GET /The%20Black%20Keys/Turn%20Blue/cover.jpg HTTP/1.1

return the cover contained within the first music file from

    <your_music_dir>/The Black Keys/Turn Blue/

## Usage

```
usage: MPDCoverServer [-h] [--port PORT] MUSIC_DIR

A simple HTTP server that serves covers from music files

positional arguments:
  MUSIC_DIR             the path to your music directory

optional arguments:
  -h, --help            show this help message and exit
  --port PORT, -p PORT  port to listen (default 8000)
```                                                     

## Install

To install the package, just use the `setup.py`:

```
cd mpdcoverserver
./setup.py install
```

You might want to run the server with systemd. A service unit file is in unitfile, to be copied to `/usr/lib/systemd/system/`


