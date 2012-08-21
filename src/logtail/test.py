###        thread_example.py   
import time  
import thread  
def timer(no,interval):  #
        while True:
                print "123"   
                return 'Thread :(%d) Time:%s'%(no,time.ctime())   
                time.sleep(interval)   
def test(): 
        print "twet"  
        thread.start_new_thread(timer,(1,1))     
        thread.start_new_thread(timer,(2,3))   
test()  
