import select
import os
import time
def follow( *filelist ):
    bufs = {}
    p = select.poll()
    flist = [open(f, "r") for f in filelist]
    for f in flist:
        bufs[f.fileno()] = ""

    for f in flist:
        p.register( f, select.POLLIN )
    while True:
        fds = p.poll( )
        for fd, ev in fds:
            tmp = os.read(fd, 1024)
            if tmp == "":
                continue
            bufs[fd] += tmp
            x = bufs[fd].find("\n")
            if x > 0:
                yield bufs[fd][:x]
                bufs[fd] = bufs[fd][x+1:]
        time.sleep(2)


for line in follow("a","b","c"):
    print line
