import requests
import zipfile
import os
import shutil

# Function to download, unzip, and rename the latest source code from a GitHub repo
def download_rename_replace(repo_url, target_folder, new_folder_name='app'):
    # Get the last part of the GitHub repo URL (username/repo)
    repo_name = repo_url.rstrip('/').split('/')[-1]
    
    # Construct the URL for the latest source code zip file
    zip_url = f'{repo_url}/archive/refs/heads/main.zip'
    
    # Download the zip file
    print("Downloading .zip file...")
    r = requests.get(zip_url)
    zip_filename = f'{repo_name}.zip'
    
    # Save the zip file to the current directory
    with open(zip_filename, 'wb') as zip_file:
        zip_file.write(r.content)

    # Replace the contents of the target folder with the renamed folder
    if os.path.exists(target_folder):
        shutil.rmtree(target_folder)
        
    print("Unzipping .zip file...")
    # Unzip the file
    with zipfile.ZipFile(zip_filename, 'r') as zip_ref:
        zip_ref.extractall('.')
    
    # Remove the zip file after extraction
    os.remove(zip_filename)
    
    # Get the name of the unzipped folder
    unzipped_folder_name = f'{repo_name}-main'
    
    # Rename the unzipped folder
    os.rename(unzipped_folder_name, new_folder_name)
    print("Updating files...")
    
    shutil.move(new_folder_name, target_folder)
    print("Done!")

# Example usage
repo_url = 'https://github.com/Appelgames/appel'  # Replace with the actual GitHub repo URL
target_folder = 'app'  # Replace with the actual target folder path
download_rename_replace(repo_url, target_folder)
