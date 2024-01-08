import os
import shutil

source_folder = 'archive'
target_folder = 'RealHuman'

num_images_to_copy = 30000

if not os.path.exists(target_folder):
    os.makedirs(target_folder)
    
images = os.listdir(source_folder)

count = 0
for image in images:
    if count == num_images_to_copy:
        break
    # change to cut imgae
    shutil.move(os.path.join(source_folder, image), target_folder)    
    count += 1