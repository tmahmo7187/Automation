#Imports the Paramiko library, which provides SSH functionality for Python.
import paramiko

#Defines a function named update_config that takes in parameters server, username, password, file_paths, and new_password. This function will update the configuration files on the specified server
def update_config(server, username, password, file_paths, new_password):


    #Attempts to establish an SSH connection with the server specified in the server parameter using the provided username and password. It creates an instance of SSHClient from Paramiko, sets the missing host key policy to automatically add new hosts, and connects to the server.
    try:
        # Establish SSH connection
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(server, username=username, password=password)

        #Iterates over each file_path in the file_paths list. It executes the cat command on the server to read the contents of the specified file and stores the output in current_content.       
        for file_path in file_paths:
            # Read the existing config file
            stdin, stdout, stderr = client.exec_command('cat ' + file_path)
            current_content = stdout.read().decode()

            #Replaces the string 'password' in current_content with the new_password provided. This updates the password in the configuration file content.
            updated_content = current_content.replace('password', new_password)

            #Opens an SFTP connection to the server using, Write the updated config file
            sftp = client.open_sftp()
            with sftp.file(file_path, 'w') as f:
                f.write(updated_content)

            print(f"Config file '{file_path}' updated on {server}")

        sftp.close()
    except paramiko.AuthenticationException:
        print(f"Authentication failed for {server}")
    except paramiko.SSHException as e:
        print(f"SSH connection failed for {server}: {str(e)}")
    finally:
        client.close()

# Server details
servers = ['vmat-engine-2-113862', 'vmat-engine-3-147250']
username = 'your_username'
password = 'your_password'

# File paths on the servers
file_paths = [
    './severity-data/conf.py_bkp',
    './tek-templates/etl/conf.php',
    './INEOQUEST/bin/db.pl',
    './OLY_2021/db.pl'
]

# New password
new_password = 'new_password'

# Update config files on each server
for server in servers:
    update_config(server, username, password, file_paths, new_password)
