import csv
import os
from io import BytesIO

import requests
from PIL import Image


def download_and_convert_to_jpg(url, output_folder, counter):
    response = requests.get(url)
    hotelId = 2629136
    if response.status_code == 200:
        image = Image.open(BytesIO(response.content))
        image = image.convert("RGB")

        output_path = os.path.join(output_folder, f"{counter}_{hotelId}.jpg")

        image.save(output_path, "JPEG")
        print(f"Image downloaded and converted to {output_path}")
    else:
        print(f"Failed to download image from {url}. Status code: {response.status_code}")


def process_csv(csv_file_path, output_folder):
    counter = 1
    with open(csv_file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            image_url = row['image_urls']
            download_and_convert_to_jpg(image_url, output_folder, counter)
            counter += 1


csv_file_path = '2629136_images.csv'
output_folder = 'output_images'

process_csv(csv_file_path, output_folder)
