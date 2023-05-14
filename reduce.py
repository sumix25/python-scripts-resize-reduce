from PIL import Image
import os
"""
Reduce the size of an image to a maximum size in bytes while preserving its aspect ratio.

Args:
        image_path (str): The path to the image file.
        max_size (int): The maximum size in bytes (default: 1000000).

Returns:
    str: The path to the reduced-size image file.

"""
# Set the folder path containing the images
folder_path = './'

# Set the output folder path for the resized images
output_path = './reduced'
max_size=10000000
for filename in os.listdir(folder_path):
    # Open the image file
    with Image.open(os.path.join(folder_path, filename)) as img:
        width, height = img.size
        ratio = height / width
        new_width = int((max_size / ratio) ** 0.5)
        new_height = int(new_width * ratio)

        # Resize the image
        resized_img = img.resize((new_width, new_height), Image.ANTIALIAS)
        resized_img.save(os.path.join(output_path, filename),optimize=True, quality=85)

        
