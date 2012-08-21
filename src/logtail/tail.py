import  time
c = open("1.txt","r")
while 1:
    d = c.tell()
    e = c.readlines()
    f = "".join(e) 
    if not e:
        time.sleep(3)
        c.seek(d)
    else: 
        if "4" in f:
            print f
             
