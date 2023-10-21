# Memory monitor>

Script controls memory usage and sends request to API if memory is exceeded


### Local setup:
##### Create virtual environment, activate it and install dependencies:
```
python -m venv venv
source venv/Scripts/Activate
pip install requirements.txt
```
##### Create .env file, for example:
```
ALERTS_LOGS=alerts.log
ALERT_PERCENT=50
ALERT_API=https://www.google.com
ALERT_API_ERROR=Memory exceeded, but alert error occurred
```
