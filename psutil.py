import psutil # type: ignore
import time
import smtplib
from email.mime.text import MIMEText

# Thresholds
CPU_THRESHOLD = 80
MEMORY_THRESHOLD = 80
DISK_THRESHOLD = 80

# Email configuration
SMTP_SERVER = 'smtp.example.com'
SMTP_PORT = 587
EMAIL_ADDRESS = 'you@example.com'
EMAIL_PASSWORD = 'your-password'
TO_ADDRESS = 'recipient@example.com'

def check_cpu():
    cpu_percent = psutil.cpu_percent(interval=1)
    return cpu_percent > CPU_THRESHOLD

def check_memory():
    memory_info = psutil.virtual_memory()
    memory_percent = memory_info.percent
    return memory_percent > MEMORY_THRESHOLD

def check_disk():
    disk_info = psutil.disk_usage('/')
    disk_percent = disk_info.percent
    return disk_percent > DISK_THRESHOLD

def send_alert(message):
    msg = MIMEText(message)
    msg['Subject'] = 'System Health Alert'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = TO_ADDRESS

    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.sendmail(EMAIL_ADDRESS, [TO_ADDRESS], msg.as_string())
        server.quit()
        print('Alert sent successfully')
    except Exception as e:
        print(f'Error sending alert: {e}')

def main():
    while True:
        if check_cpu() or check_memory() or check_disk():
            alert_message = 'System health warning:\n'
            alert_message += f'CPU: {psutil.cpu_percent()}%\n'
            alert_message += f'Memory: {psutil.virtual_memory().percent}%\n'
            alert_message += f'Disk: {psutil.disk_usage("/").percent}%\n'
            send_alert(alert_message)
        time.sleep(60)  # Check every minute

if __name__ == '__main__':
    main()