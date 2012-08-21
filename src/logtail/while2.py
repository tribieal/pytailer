import time
c = 1
while 1:
    e = c%5
#    print e
    if e == 4 :
        d = "\n"+"apple "+str(c)
    else:
        d = "\n"+str(c)
    f = open('2.log','a')
    f.write(d,)
    f.close
    c += 1
    time.sleep (2)
