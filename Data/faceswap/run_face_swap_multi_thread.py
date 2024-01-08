import os
from concurrent.futures import ThreadPoolExecutor

from gradio_client import Client
from tqdm import tqdm


client = Client("https://felixrosberg-face-swap.hf.space/", output_dir="1k_output")


def process_image(target_image, source_image):
    result = client.predict(
        target_image,
        source_image,
        0,
        0,
        "Compare",
        fn_index=1,
    )


import time

from tqdm import tqdm


start_time = time.time()
# # Create a ThreadPool, adjust the max_workers as necessary
# with ThreadPoolExecutor(max_workers=10) as executor:
#     for target_image in tqdm(os.listdir("real")):
#         target_image = "real/" + target_image
#         for source_image in tqdm(os.listdir("fake")):
#             source_image = "fake/" + source_image
#             executor.submit(process_image, target_image, source_image)

with ThreadPoolExecutor(max_workers=10) as executor:
    for target_image, source_image in tqdm(
        zip(os.listdir("real_target"), os.listdir("fake_source"))
    ):
        target_image = "real_target/" + target_image
        source_image = "fake_source/" + source_image
        executor.submit(process_image, target_image, source_image)

end_time = time.time()
print(f"Total time: {end_time - start_time}")
