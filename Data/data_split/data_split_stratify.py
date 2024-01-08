import os
import random
import shutil

import tqdm


TRAIN_RATIO = 0.6
VALIDATE_RATIO = 0.2
TEST_RATIO = 0.2

real_folder = ["data_source\\ffhq"]
fake_folders = [
    "data_source\\fake\\faceswap",
    "data_source\\fake\\sfhq\\pt1",
    "data_source\\fake\\sfhq\\pt2",
    "data_source\\fake\\sfhq\\pt3",
    "data_source\\fake\\sfhq\\pt4",
    "data_source\\fake\\stable_diffusion",
    "data_source\\fake\\thisperson",
]

train_folder = 'dataset\\train'
validate_folder = 'dataset\\validate'
test_folder = 'dataset\\test'

os.makedirs(train_folder, exist_ok=True)
os.makedirs(validate_folder, exist_ok=True)
os.makedirs(test_folder, exist_ok=True)

# in each folder create 2 subfolders: 0 for real, 1 for fake
os.makedirs(os.path.join(train_folder, "0"), exist_ok=True)
os.makedirs(os.path.join(train_folder, "1"), exist_ok=True)
os.makedirs(os.path.join(validate_folder, "0"), exist_ok=True)
os.makedirs(os.path.join(validate_folder, "1"), exist_ok=True)
os.makedirs(os.path.join(test_folder, "0"), exist_ok=True)
os.makedirs(os.path.join(test_folder, "1"), exist_ok=True)

# split real images into train, validate, test with above ratios
for i in tqdm.tqdm(range(len(real_folder)), desc='Real Folders'):
    images = os.listdir(real_folder[i])
    num_images = len(images)

    num_train = int(TRAIN_RATIO * num_images)
    num_validate = int(VALIDATE_RATIO * num_images)
    num_test = int(TEST_RATIO * num_images)

    random.shuffle(images)

    train_images = images[:num_train]
    validate_images = images[num_train : num_train + num_validate]
    test_images = images[-num_test:]

    # ----
    train_subfolder_path = os.path.join(train_folder, "0")
    validate_subfolder_path = os.path.join(validate_folder, "0")
    test_subfolder_path = os.path.join(test_folder, "0")

    # ----
    # Copy images to respective folders
    for img in tqdm.tqdm(
        train_images, desc=f'Copying train images for {real_folder[i]}'
    ):
        shutil.copy(os.path.join(real_folder[i], img), train_subfolder_path)

    for img in tqdm.tqdm(
        validate_images, desc=f'Copying validation images for {real_folder[i]}'
    ):
        shutil.copy(os.path.join(real_folder[i], img), validate_subfolder_path)

    for img in tqdm.tqdm(test_images, desc=f'Copying test images for {real_folder[i]}'):
        shutil.copy(os.path.join(real_folder[i], img), test_subfolder_path)


# split fake images into train, validate, test with above ratios
for i in tqdm.tqdm(range(len(fake_folders)), desc='Fake Folders'):
    images = os.listdir(fake_folders[i])
    num_images = len(images)

    num_train = int(TRAIN_RATIO * num_images)
    num_validate = int(VALIDATE_RATIO * num_images)
    num_test = int(TEST_RATIO * num_images)

    random.shuffle(images)

    train_images = images[:num_train]
    validate_images = images[num_train : num_train + num_validate]
    test_images = images[-num_test:]

    # ----
    train_subfolder_path = os.path.join(train_folder, "1")
    validate_subfolder_path = os.path.join(validate_folder, "1")
    test_subfolder_path = os.path.join(test_folder, "1")

    # ----
    # Copy images to respective folders
    for img in tqdm.tqdm(
        train_images, desc=f'Copying train images for {fake_folders[i]}'
    ):
        shutil.copy(os.path.join(fake_folders[i], img), train_subfolder_path)

    for img in tqdm.tqdm(
        validate_images, desc=f'Copying validation images for {fake_folders[i]}'
    ):
        shutil.copy(os.path.join(fake_folders[i], img), validate_subfolder_path)

    for img in tqdm.tqdm(
        test_images, desc=f'Copying test images for {fake_folders[i]}'
    ):
        shutil.copy(os.path.join(fake_folders[i], img), test_subfolder_path)
