import os
import shutil


NUM_IMAGES = 10000
BREAK_POINT = 5000

# set the paths to the source folders and the destination folders
generated_face_src = "D:\\School\\04_PBL6\\PBL6\\_pbl6_data\\GeneratedFace"
ffhq_src = "D:\\School\\04_PBL6\\PBL6\\_pbl6_data\\FFHQ52k_512"
fake_folder_first_5k = "D:\\School\\04_PBL6\\PBL6\\_pbl6_data\\faceswap\\fake_source1"
fake_folder_second_5k = "D:\\School\\04_PBL6\\PBL6\\_pbl6_data\\faceswap\\fake_source2"
real_folder_first_5k = "D:\\School\\04_PBL6\\PBL6\\_pbl6_data\\faceswap\\real_target1"
real_folder_second_5k = "D:\\School\\04_PBL6\\PBL6\\_pbl6_data\\faceswap\\real_target2"

# create the fake and real folders if they don't already exist
os.makedirs(fake_folder_first_5k, exist_ok=True)
os.makedirs(fake_folder_second_5k, exist_ok=True)
os.makedirs(real_folder_first_5k, exist_ok=True)
os.makedirs(real_folder_second_5k, exist_ok=True)

# copy fake images
for i, filename in enumerate(os.listdir(generated_face_src)):
    if i >= NUM_IMAGES:
        break

    if i < BREAK_POINT:
        fake_folder = fake_folder_first_5k
    else:
        fake_folder = fake_folder_second_5k

    shutil.copy(
        os.path.join(generated_face_src, filename), os.path.join(fake_folder, filename)
    )

# copy real images
for i, filename in enumerate(os.listdir(ffhq_src)):
    if i >= NUM_IMAGES:
        break

    if i < BREAK_POINT:
        real_folder = real_folder_first_5k
    else:
        real_folder = real_folder_second_5k

    shutil.copy(os.path.join(ffhq_src, filename), os.path.join(real_folder, filename))
