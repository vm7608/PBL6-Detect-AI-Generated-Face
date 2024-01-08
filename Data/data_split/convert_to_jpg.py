import os

from PIL import Image
from tqdm import tqdm


# Set the paths for the input and output directories
input_dir = "face_swap_data"
output_dir = "Face_swap"

# Create the output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Loop through all the files in the input directory

for filename in tqdm(os.listdir(input_dir)):
    # Check if the file is a PNG image
    if filename.endswith(".png"):
        # Open the image and convert it to RGB
        with Image.open(os.path.join(input_dir, filename)) as im:
            rgb_im = im.convert("RGB")
            # Save the image as a JPEG in the output directory
            new_filename = os.path.splitext(filename)[0] + ".jpg"
            rgb_im.save(os.path.join(output_dir, new_filename), "JPEG")
