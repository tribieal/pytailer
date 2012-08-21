###        thread_example.py   
import time  
import thread  
def timer(no,interval):  #
        while True:
                print no
                time.sleep(interval)   
def testt(): 
        print "twet"  
        thread.start_new_thread(timer,(1,1))     
        thread.start_new_thread(timer,(2,3))   
if __name__ == '__main__':
    testt()
    while 1:
        time.sleep(3)  
