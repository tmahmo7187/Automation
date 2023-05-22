#Imports necessary modules and classes required for subprocess management, email sending, time manipulation, and MIME text formatting
import subprocess
import smtplib
import time
from email.mime.text import MIMEText


#Defines a function named send_email that takes parameters such as subject, body, sender, receiver, and SMTP server. Inside the function, it creates an instance of MIMEText to construct the email message. Then, it sets the subject, sender, and receiver fields. It attempts to establish an SMTP connection using the provided SMTP server, sends the email using sendmail(), and closes the connection with quit(). If any exception occurs during the process, it prints an error message.
def send_email(subject, body, sender, receiver, smtp_server):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = receiver

    try:
        smtp = smtplib.SMTP(smtp_server)
        smtp.sendmail(sender, receiver, msg.as_string())
        smtp.quit()
        print("Email notification sent successfully.")
    except smtplib.SMTPException as e:
        print("Error sending email notification:", str(e))

def monitor_log_file(log_file, error_patterns, sender, receiver, smtp_server):
    try:
        # Open a subprocess to tail the log file
        tail_process = subprocess.Popen(['tail', '-f', log_file], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        while True:
            line = tail_process.stdout.readline().decode().strip()

            # Check for error patterns in the log line
            for error_pattern in error_patterns:
                if error_pattern in line:
                    subject = f"Error detected in log file: {log_file}"
                    body = f"Error pattern '{error_pattern}' found in log file:\n\n{line}"

                    # Send email notification
                    send_email(subject, body, sender, receiver, smtp_server)

    except subprocess.CalledProcessError as e:
        print("Error executing tail command:", str(e))
    except KeyboardInterrupt:
        print("Monitoring stopped.")

# Log file to monitor
log_file = "/path/to/logfile.log"

# Error patterns to detect
error_patterns = ["ERROR", "Exception"]

# Email settings
sender = "sender@example.com"
receiver = "receiver@example.com"
smtp_server = "smtp.example.com"

# Start monitoring the log file
monitor_log_file(log_file, error_patterns, sender, receiver, smtp_server)
