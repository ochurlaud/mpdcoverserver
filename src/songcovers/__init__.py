#!/usr/bin/python3

import mutagen
import os

ERROR_RET = None, None
JPEG_MIME = "image/jpeg"
PNG_MIME = "image/png"

def getsongpath(inputpath):
    if os.path.isdir(inputpath):
        songlist = [f for f in os.listdir(inputpath) if not f.startswith('.')]

        if len (songlist) == 0:
            print("Empty folder: {}".format(inputpath))
            return None

        songlist.sort()
        newpath = os.path.join(inputpath, songlist[0])
        if os.path.isfile(newpath):
            return newpath
        else:
            print("Not a file: {}".format(newpath))
            return None

    elif os.path.isfile(inputpath):
        return inputpath
    else:
        print("Invalid path: {}".format(inputpath))
        return None

def getcover(inputpath):

    songpath = getsongpath(inputpath)
    if songpath is None:
        return ERROR_RET

    print("Dealing with file {}".format(songpath))
    song = mutagen.File(songpath)
    
    if type(song) is mutagen.mp3.MP3:
        apic = song.tags.get('APIC:', None)
        if apic is not None:
            return apic.mime, apic.data
    if type(song) is mutagen.mp4.MP4:
        coverlist = song.tags.get('covr', None)
        if coverlist is not None and len(coverlist) > 0:
            cover = coverlist[0]
            if cover.imageformat == mutagen.mp4.AtomDataType.JPEG:
                mime = JPEG_MIME
            if cover.imageformat == mutagen.mp4.AtomDataType.PNG:
                mime = PNG_MIME

            return mime, bytes(cover)
    elif type(song) is mutagen.flac.FLAC:
        picts = song.pictures
        if len(picts) > 0:
            return picts[0].mime, picts[0].data
    else:
        return ERROR_RET
    
if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        sys.exit(-1)

    songname = sys.argv[1]
    mime, data = getcover(songname)
    if data is not None:
        print(data)

