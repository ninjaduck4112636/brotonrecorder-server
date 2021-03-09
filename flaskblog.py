from flask import Flask
import requests
import datetime
import time
from apscheduler.schedulers.background import BackgroundScheduler

def sensor():
	date_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	response = requests.get('https://brotonrecorder.gq').status_code
	res = {date_time:response}
	print(res)

sched = BackgroundScheduler(daemon=True)
sched.add_job(sensor,'interval',minutes=0.2)
sched.start()

app = Flask(__name__)

@app.route('/')
def hello_world():
	return '''
		<!DOCTYPE html>
<html>
<head>
	<meta http-equiv="refresh" content="120" >
	<title>brotonrecorder-server</title>
</head>
<body>
	website: brotonrecorder.gq
</body>
</html>
	'''


if __name__ == "__main__":
    app.run()	