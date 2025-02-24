import os
import cv2

# Folder containing images
IMAGE_FOLDER = "data/"

# Image filenames
IMAGE_FILES = ["Plaksha_Faculty.jpg", "Dr_Shashi_Tharoor.jpg"]

# Dictionary to store loaded images
dataset = {}

# Load images
for img_file in IMAGE_FILES:
    dataset[img_file] = cv2.imread(img_file)
    if dataset[img_file] is not None:
        print(f"✅ Image '{img_file}' loaded successfully.")
    else:
        print(f"⚠️ Image '{img_file}' not found.")

# Make dataset available when imported
def get_dataset():
    return dataset
