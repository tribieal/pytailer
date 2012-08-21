import time,thread

def func():
    for i in range(5):
        print 'func'

        time.sleep(1)
    thread.exit()
if __name__ == "__main__": 
    thread.start_new(func, ())
    #func()
