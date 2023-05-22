import schedule   # Import the schedule library to schedule tasks
import time      #  Import the time module for sleep functionality
import subprocess   # Import the subprocess module to execute the file

def execute_file():
    # Define the command to execute the file
    command = 'python your_file.py'  # Replace 'your_file.py' with the name of your file to execute
    
    # Execute the command
    subprocess.call(command, shell=True)   # Execute the command to run the file
    print(f'Executed file at {time.ctime()}')   # Print the execution timestamp

# Schedule the file execution
schedule.every().day.at('10:00').do(execute_file)
# Schedule the execute_file() function to run every day at 10:00 AM
# You can modify the scheduling pattern as needed, e.g., schedule.every().hour.do(execute_file) for every hour

# Run the scheduler
while True:
    schedule.run_pending()   # Check for pending scheduled tasks and execute them if due
    time.sleep(1)   # Sleep for 1 second to avoid excessive CPU usage

