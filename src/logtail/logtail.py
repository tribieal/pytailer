import tailer,time,thread
import ConfigParser
config=ConfigParser.ConfigParser()
with open('init.cfg','rw') as cfgfile:
    config.readfp(cfgfile)
    hostip=config.get('remote_info','hostip')
    hostport=config.get('remote_info','hostport')
    logfile_absolute_path = config.get('log','logfile_absolute_path')
    alterfile_absolute_path = config.get('log','alterfile_absolute_path')
    key_words = config.get('log','key_words')
    
print key_words
key_words = key_words.split(",")
for i in key_words:
    print i
print key_words

print logfile_absolute_path
logfile_absolute_path = logfile_absolute_path.split(",")
for i in logfile_absolute_path:
    print i


def grepstatus(sStr1,sStr2,filelog):
    out = sStr1.find(sStr2)
    filelog = str(filelog)
    c = open(filelog,'a')
    if out != -1:
        nowtime = str(time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time())))
        sStr1time = sStr1+"--"+nowtime+"\n<br />"
        print sStr1time
        c.write(sStr1time,)

def followfile(filepath,keywords,filelog):
    filepath = str(filepath)
    for line in tailer.follow(open(filepath)):
        print line
        grepstatus(line,keywords,filelog)

def doit():    
    for i in logfile_absolute_path:
        for j in key_words:
            thread.start_new_thread(followfile,(i,j,alterfile_absolute_path))
#followfile('/home/hadoop/catalina/apache-tomcat-6.0.35.8081/logs/catalina.out','Exception','alter.html')


if __name__ == "__main__" :
    doit()
    while 1:
        time.sleep(1)



