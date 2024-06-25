import ftplib

def delete_and_upload_file_to_ftp(ftp_server, ftp_user, ftp_password, local_file_path, remote_file_path):
    try:
        # Connect to the FTP server
        ftp = ftplib.FTP(ftp_server)
        ftp.login(user=ftp_user, passwd=ftp_password)
        print(f"Connected to FTP server: {ftp_server}")
        
        # Try to delete the existing remote file
        try:
            ftp.delete(remote_file_path)
            print(f"Deleted existing file: {remote_file_path}")
        except ftplib.error_perm as e:
            # If the file does not exist, catch the exception and print a message
            print(f"File {remote_file_path} not found on FTP server. Proceeding with upload.")
        
        # Open the local file
        with open(local_file_path, 'rb') as file:
            # Use the storbinary method to upload the file
            ftp.storbinary(f'STOR {remote_file_path}', file)
            print(f"File {local_file_path} uploaded to {remote_file_path}")
        
        # Close the FTP connection
        ftp.quit()
        print("FTP connection closed.")
    
    except ftplib.all_errors as e:
        print(f"FTP error: {e}")


# Example usage
ftp_server = '10.10.253.10'  # Replace with your FTP server address
ftp_user = 'edf.ratan.jha'      # Replace with your FTP username
ftp_password = '*************'  # Replace with your FTP password
local_file_path = r'C:\Users\Ratan Kumar Jha\Desktop\MAIL_AUTO_DATA_DOWNLOAD\ASSET_INITIATION_INVENTORY_NB.csv'  # Replace with the path to your local CSV file
remote_file_path = '/EDF Code Automation/ASSET_INITIATION_INVENTORY_NB.csv'  # Replace with the desired remote path

delete_and_upload_file_to_ftp(ftp_server, ftp_user, ftp_password, local_file_path, remote_file_path)
