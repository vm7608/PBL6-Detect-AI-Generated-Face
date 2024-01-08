import os
import shutil

from tqdm import tqdm


sfhq_dir = "data_source\\fake\\sfhq_src"
sfhq_pt1 = "data_source\\fake\\sfhq\\pt1"
sfhq_pt2 = "data_source\\fake\\sfhq\\pt2"
sfhq_pt3 = "data_source\\fake\\sfhq\\pt3"
sfhq_pt4 = "data_source\\fake\\sfhq\\pt4"

# Create sfhq_pt1, sfhq_pt2, sfhq_pt3, sfhq_pt4
os.makedirs(sfhq_pt1, exist_ok=True)
os.makedirs(sfhq_pt2, exist_ok=True)
os.makedirs(sfhq_pt3, exist_ok=True)
os.makedirs(sfhq_pt4, exist_ok=True)


# Get all image files in sfhq_dir
image_files = [
    file
    for file in os.listdir(sfhq_dir)
    if os.path.isfile(os.path.join(sfhq_dir, file))
]

# Loop through each image file

for file in tqdm(image_files):
    if "pt1" in file:
        # Move the image file to sfhq_pt1
        shutil.move(os.path.join(sfhq_dir, file), sfhq_pt1)
    elif "pt2" in file:
        # Move the image file to sfhq_pt2
        shutil.move(os.path.join(sfhq_dir, file), sfhq_pt2)
    elif "pt3" in file:
        # Move the image file to sfhq_pt3
        shutil.move(os.path.join(sfhq_dir, file), sfhq_pt3)
    elif "pt4" in file:
        # Move the image file to sfhq_pt4
        shutil.move(os.path.join(sfhq_dir, file), sfhq_pt4)
