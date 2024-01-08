from tqdm import tqdm
from threading import Thread
import requests
import os
import math
import hashlib

# constants
URL = "https://thispersondoesnotexist.com/"
OUTPUT_FOLDER = "data"
NUM_IMAGES = 100
NUM_THREADS = 5


def get_filename(response):
    h = hashlib.sha256()
    h.update(response.content)
    checksum = h.hexdigest()
    filename = os.path.join(OUTPUT_FOLDER, f"{checksum}.jpg")
    return filename


def download_images(start, end):
    for _ in range(start, end):
        pbar.update(1)
        response = requests.get(URL)
        filename = get_filename(response)
        save_image(response, filename)


def save_image(response, filename):
    with open(filename, "wb") as f:
        f.write(response.content)


def main():
    if not os.path.exists(OUTPUT_FOLDER):
        os.makedirs(OUTPUT_FOLDER)

    images_per_thread = math.ceil(NUM_IMAGES / NUM_THREADS)
    global pbar
    pbar = tqdm(total=NUM_IMAGES)

    threads = []
    for thread_id in range(NUM_THREADS):
        start = thread_id * images_per_thread
        end = min(start + images_per_thread, NUM_IMAGES)
        t = Thread(target=download_images, args=(start, end))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    pbar.close()


if __name__ == '__main__':
    main()
    print(len(os.listdir('data')))
