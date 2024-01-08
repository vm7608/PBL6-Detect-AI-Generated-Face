import os
import shutil


# Create the new directory if it doesn't exist
os.makedirs("face_swap", exist_ok=True)

# Loop through all subdirectories in the output directory
for subdir in os.listdir("output"):
    subdir_path = os.path.join("output", subdir)
    if os.path.isdir(subdir_path):
        # Loop through all files in the subdirectory
        for file in os.listdir(subdir_path):
            file_path = os.path.join(subdir_path, file)
            if os.path.isfile(file_path):
                # Move the file to the total_output directory with the subdirectory name as the new file name
                new_file_name = (
                    subdir + ".jpg"
                )  # Change the extension to match your image format
                new_file_path = os.path.join("total_output", new_file_name)
                shutil.copy(file_path, new_file_path)
