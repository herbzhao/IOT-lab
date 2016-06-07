import subprocess
import time


subprocess.Popen(["rm","-r","w1.log"])
subprocess.Popen(["rm","-r","w1.pid"])

subprocess.Popen(["redis-server"])

time.sleep(0.5)

#subprocess.Popen(["celery","multi","start", "w1", "-A", "tasks" ,"-l" ,"info"])

subprocess.Popen(["celery","multi","start", "w1", "-A", "tasks" ,"-l" ,"info"])

#subprocess.Popen(["celery","-A","tasks","worker", "-l", "info"])


time.sleep(0.5)


#subprocess.call(["celery","multi","stop", "w1", "-A", "tasks" ,"-l" ,"info"])


from tasks import temp_control

result = temp_control.delay(17,37)

