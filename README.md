SFTP Explorer

SFTP Explorer is a simple Python console application that allows you to connect to an SFTP server and perform various file operations such as downloading, uploading, and navigating directories.

Features

- Connect to an SFTP server by providing the host, username, and password.
- View files in the current directory on the server.
- Download files from the server to the local machine.
- Upload files from the local machine to the server.
- Change directories on the server to navigate to different locations.

Installation

1. Clone the repository:

git clone https://github.com/your_username/sftp-explorer.git

2. Navigate to the project directory:

cd sftp-explorer

3. Run the application:

python sftp_explorer.py

Usage

1. Upon running the application, you will be prompted to enter the host, username, and password of the SFTP server you want to connect to.

2. After successfully connecting, you will see a list of available options:

    - Refresh file list: Updates the list of files in the current directory on the server.
    - Download file: Allows you to download a file from the server to your local machine.
    - Upload file: Enables you to upload a file from your local machine to the server.
    - Change directory: Lets you navigate to a different directory on the server.
    - Exit: Quits the application.

3. Choose the desired option by entering the corresponding number.

4. Follow the prompts to perform the selected operation.

Dependencies

- Paramiko: pip install paramiko

Contributing

Contributions are welcome! Please feel free to submit issues and pull requests.

License

This project is licensed under the MIT License.
