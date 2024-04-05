import os
import paramiko

class SFTPExplorer:
    def __init__(self):
        self.sftp = None
        self.current_dir = "/"

    def connect(self, host, username, password):
        try:
            transport = paramiko.Transport((host, 22))
            transport.connect(username=username, password=password)
            self.sftp = paramiko.SFTPClient.from_transport(transport)
            self.refresh_file_list()
            print("Connected to SFTP server.")
        except Exception as e:
            print(f"Failed to connect: {e}")

    def refresh_file_list(self):
        files = self.sftp.listdir(self.current_dir)
        print(f"Files in directory {self.current_dir}:")
        for file in files:
            print(file)

    def download(self, remote_file, local_file):
        try:
            self.sftp.get(os.path.join(self.current_dir, remote_file), local_file)
            print(f"File downloaded to {local_file}")
        except Exception as e:
            print(f"Failed to download: {e}")

    def upload(self, local_file):
        try:
            self.sftp.put(local_file, os.path.join(self.current_dir, os.path.basename(local_file)))
            print(f"File uploaded to server")
            self.refresh_file_list()
        except Exception as e:
            print(f"Failed to upload: {e}")

    def change_directory(self, directory):
        try:
            self.sftp.chdir(directory)
            self.current_dir = self.sftp.getcwd()
            self.refresh_file_list()
        except Exception as e:
            print(f"Failed to change directory: {e}")

def main():
    explorer = SFTPExplorer()
    host = input("Enter host: ")
    username = input("Enter username: ")
    password = input("Enter password: ")

    explorer.connect(host, username, password)

    while True:
        print("\nOptions:")
        print("1. Refresh file list")
        print("2. Download file")
        print("3. Upload file")
        print("4. Change directory")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            explorer.refresh_file_list()
        elif choice == "2":
            remote_file = input("Enter remote file name: ")
            local_file = input("Enter local file name: ")
            explorer.download(remote_file, local_file)
        elif choice == "3":
            local_file = input("Enter local file name: ")
            explorer.upload(local_file)
        elif choice == "4":
            directory = input("Enter directory path: ")
            explorer.change_directory(directory)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
