import os


# Define the path to the folder containing the images
folder_path = "FFHQ52k"

# Create a set of all possible image names
all_names = set([f"{i:05d}.png" for i in range(54100)])

# Create a set of the actual image names in the folder
actual_names = set(os.listdir(folder_path))

# Find the missing image name by subtracting the actual names from all names
missing_name = all_names - actual_names

# Print the missing image name
# sort missing_name to get the first missing image name
print(sorted(missing_name))
# save the missing image name to a file

with open("missing_name.txt", "w") as f:
    f.write(str(sorted(missing_name)))
