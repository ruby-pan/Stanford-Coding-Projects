"""
File: stanCodoshop.py
----------------------------------------------
SC101_Assignment3
Adapted from Nick Parlante's
Ghost assignment by Jerry Liao.

-----------------------------------------------
Photobomb eliminator.
"""

import os
import sys
from simpleimage import SimpleImage
import math


def get_pixel_dist(pixel, red, green, blue):
    """
    Returns the color distance between pixel and mean RGB value

    Input:
        pixel (Pixel): pixel with RGB values to be compared
        red (int): average red value across all images
        green (int): average green value across all images
        blue (int): average blue value across all images

    Returns:
        dist (int): color distance between red, green, and blue pixel values

    """
    inside = (red-pixel.red)**2 +(green-pixel.green)**2+(blue-pixel.blue)**2
    color_distance = math.sqrt(inside)
    return color_distance


def get_average(pixels):
    """
    Given a list of pixels, finds the average red, blue, and green values

    Input:
        pixels (List[Pixel]): list of pixels to be averaged
    Returns:
        rgb (List[int]): list of average red, green, blue values across pixels respectively

    Assumes you are returning in the order: [red, green, blue]

    """
    rgb = []
    total_red= 0
    total_green= 0
    total_blue= 0
    red_lst = []
    green_lst = []
    blue_lst = []
    for set in pixels:
        total_red += set.red
        total_green += set.green
        total_blue += set.blue
    red_lst = total_red / len(pixels)
    green_lst = total_green / len(pixels)
    blue_lst = total_blue / len(pixels)
    rgb.append(red_lst)
    rgb.append(green_lst)
    rgb.append(blue_lst)
    return rgb


def get_best_pixel(pixels):
    """
    Given a list of pixels, returns the pixel with the smallest
    distance from the average red, green, and blue values across all pixels.

    Input:
        pixels (List[Pixel]): list of pixels to be averaged and compared
    Returns:
        best (Pixel): pixel closest to RGB averages

    """
    num = float('inf')
    best = pixels[0]
    avg_lst = get_average(pixels)       # 先求avg
    for pixel in pixels:      # 丟回distance
        color_dist = get_pixel_dist(pixel, avg_lst[0], avg_lst[1], avg_lst[2])     # 在pixel輪替中找距離最短的
        if num > color_dist:
            num = color_dist
            best = pixel
    return best    # 將找到的距離return成pixel本人


def solve(images):
    """
    Given a list of image objects, compute and display a Ghost solution image
    based on these images. There will be at least 3 images and they will all
    be the same size.

    Input:
        images (List[SimpleImage]): list of images to be processed
    """
    width = images[0].width
    height = images[0].height
    result = SimpleImage.blank(width, height)
    ######## YOUR CODE STARTS HERE #########
    pixels = []
    for y in range(height):
        for x in range(width):
            for image in images: #比較n張照片的同一格pixel

                pixel = image.get_pixel(x, y)
                pixels.append(pixel)
                best = get_best_pixel(pixels) #選出最好的pixel, 貼到result上

                paste = result.get_pixel(x, y)
                paste.red = best.red
                paste.green = best.green
                paste.blue = best.blue

            pixels = []

    ######## YOUR CODE ENDS HERE ###########
    print("Displaying image!")
    result.show()


def jpgs_in_dir(dir):
    """
    (provided, DO NOT MODIFY)
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
    return filenames


def load_images(dir):
    """
    (provided, DO NOT MODIFY)
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    solve(images)


if __name__ == '__main__':
    main()
