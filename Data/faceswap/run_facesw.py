import os
import time

from gradio_client import Client
from tqdm import tqdm


client = Client("https://felixrosberg-face-swap.hf.space/", output_dir="output")

# loop through all images in the source folder and swap faces with the target image


start_time = time.time()
for target_image in tqdm(os.listdir("real")):
    target_image = "real_target/" + target_image
    for source_image in tqdm(os.listdir("fake")):
        source_image = "fake_source/" + source_image
        result = client.predict(
            # str (filepath or URL to image) in 'Target' Image component
            target_image,
            # str (filepath or URL to image) in 'Source' Image component
            source_image,
            # int | float (numeric value between 0 and 100) in 'Anonymization ratio (%)' Slider component
            0,
            # int | float (numeric value between 0 and 100) in 'Adversarial defense ratio (%)' Slider component
            0,
            "Compare",  # List[str]  in 'Mode' Checkboxgroup component
            fn_index=1,
        )

end_time = time.time()
print(f"Total time: {end_time - start_time}")
