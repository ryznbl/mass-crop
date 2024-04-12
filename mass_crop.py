import os
from PIL import Image

def crop_image(image_path, coords, output_path):
    """
    Crop the image to the specified coordinates and save to the output path.
    
    Args:
    image_path (str): Path to the input image file.
    coords (tuple): Tuple containing the coordinates (left, top, right, bottom) of the region to crop.
    output_path (str): Path where the cropped image will be saved.
    """
    image = Image.open(image_path)
    cropped_image = image.crop(coords)
    cropped_image.save(output_path)

input_folder = "uncroppedimages"
output_folder = "croppedimages"
crop_coords = (0, 0, 386, 234)
crop_coords_second = (386, 0, 748, 234)
crop_coords_third = (748, 0, 1125, 234)

for filename in os.listdir(input_folder):
    input_image_path = os.path.join(input_folder, filename) 
    output_image_path_1 = os.path.join(output_folder, f"1{filename}")
    output_image_path_2 = os.path.join(output_folder, f"2{filename}")
    output_image_path_3 = os.path.join(output_folder, f"3{filename}")
    crop_image(input_image_path, crop_coords, output_image_path_1)
    crop_image(input_image_path, crop_coords_second, output_image_path_2)
    crop_image(input_image_path, crop_coords_third, output_image_path_3)
