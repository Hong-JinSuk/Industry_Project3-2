from flask import Flask, render_template
from datetime import datetime
import time
import psutil

from threading import Thread

app = Flask(__name__)

@app.route('/')
def home():
  global remained_time
  return render_template("time.html", time=remained_time, process_Name=process_name)

def set_time():
    global remained_time
    
    while True:
        remained_time -= 1
        time.sleep(1)
        
        #if remained_time==0, kill process

    return

def checkProcessRunning(processname):
    for proc in psutil.process_iter():
        if processname.lower() in proc.name().lower():
            return True
  
if __name__ == '__main__':
    remained_time = 300 # 관리자가 설정할 시간

    thread = Thread(target=set_time, daemon=True)
    thread.start()

    app.run(debug=True)
