import paramiko

def find_files_with_keyword(server, username, password, search_path, keyword):
    try:
        # Establish SSH connection
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(server, username=username, password=password)

        # Search for files with the keyword
        stdin, stdout, stderr = client.exec_command("find {} -type f -iname '*{}*'".format(search_path, keyword))
        file_paths = stdout.read().decode().splitlines()

        return file_paths
    except paramiko.AuthenticationException:
        print(f"Authentication failed for {server}")
    except paramiko.SSHException as e:
        print(f"SSH connection failed for {server}: {str(e)}")
    finally:
        client.close()

def update_config(server, username, password, file_paths, new_password):
    try:
        # Establish SSH connection
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(server, username=username, password=password)

        for file_path in file_paths:
            # Read the existing config file
            stdin, stdout, stderr = client.exec_command('cat ' + file_path)
            current_content = stdout.read().decode()

            # Replace the password with the new password
            updated_content = current_content.replace('password', new_password)

            # Write the updated config file
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
servers = ['Add server names or IP']
username = 'your_username'
password = 'your_password'

# Search path and keyword
search_path = '/path/to/search'  # Update with the appropriate search path
keyword = 'config'

# New password
new_password = 'new_password'

# Find files with the keyword on each server
file_paths = []
for server in servers:
    found_files = find_files_with_keyword(server, username, password, search_path, keyword)
    file_paths.extend(found_files)

# Update config files on each server
for server in servers:
    update_config(server, username, password, file_paths, new_password)
