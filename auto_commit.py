import os
import subprocess
import time

# Specify the local path to the Git repository
repository_path = r'C:\Users\might\Downloads\GitHub\sea.ftp.sh'

# Function to get all files in a directory and its subdirectories
def get_all_files(directory):
    all_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            all_files.append(file_path)
    return all_files

# Store the initial modification times for each file
initial_mod_times = {item: os.path.getmtime(item) for item in get_all_files(repository_path)}

while True:
    # Check the current modification times for each file
    current_mod_times = {item: os.path.getmtime(item) for item in get_all_files(repository_path)}

    # Compare with the initial modification times
    if current_mod_times != initial_mod_times:
        print("Changes detected in files or directories!")

        # Change to the repository directory
        os.chdir(repository_path)

        # Run git add .
        subprocess.run(["git", "add", "."])

        # Run git commit -m "Auto Commit"
        subprocess.run(["git", "commit", "-m", "Auto Commit"])

        # Run git push to the specified remote repository and branch
        subprocess.run(["git", "push", "origin", "master"])

        print("Git commands executed successfully.")

        # Update the initial modification times
        initial_mod_times = current_mod_times

        # Wait for a short interval before checking again (e.g., 1 second)
        time.sleep(1)
    else:
        # No changes detected, wait before checking again
        time.sleep(1)
