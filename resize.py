from PIL import Image
import os

# Set the folder path containing the images
folder_path = './'

# Set the output folder path for the resized images
output_path = './resized/'

# Set the desired dimensions for the resized images
width = 1200
height = 250


# Loop through each file in the folder
for filename in os.listdir(folder_path):
    # Open the image file
    with Image.open(os.path.join(folder_path,filename)) as img:
        # Resize the image
        resized_img = img.resize((width,height))
        # Save the resized image to the output folder
        resized_img.save(os.path.join(output_path, filename))