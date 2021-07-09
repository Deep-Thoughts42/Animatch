# %%
import cv2
from matplotlib import image
import numpy as np
from PIL import ImageEnhance
from PIL import Image
from numpy.core.fromnumeric import size
from helper.converter import cv2_to_pil, pil_to_cv2
import os



# This function assumes cwd is root
cur_dir = os.getcwd()

dir_path = os.path.join('scripts', 'characters')

def image_process(image_path):
    # Also serves as character name
    output_folder_name = image_path.split('/')[-1].split('.')[0]
    output_folder_path = os.path.join(cur_dir, "ProcessedFiles", output_folder_name)
    if not os.path.isdir(output_folder_path):
        os.mkdir(output_folder_path)
    
    size_list = [(16, 16), (18, 18), (25, 25), (40, 40), (65, 65)]
    saturation_list = [0.1, 0.2, 0.4, 0.8, 1]
    # file path to the image
    img = cv2.imread(image_path)
    height, width = img.shape[:2]

    for level in range(5):
        output_path = os.path.join(cur_dir, "ProcessedFiles", output_folder_name, f"Level{level}.jpg")
        temp_resize = cv2.resize(img, size_list[level], interpolation=cv2.INTER_LINEAR)
        output = cv2.resize(temp_resize, (width, height), interpolation=cv2.INTER_NEAREST)
        pil_image = cv2_to_pil(output)
        converted = ImageEnhance.Color(pil_image)
        final_img = converted.enhance(saturation_list[level])
        final_img.save(output_path)
        pass
    cv2.imwrite(os.path.join(cur_dir, "ProcessedFiles", output_folder_name, f"Level5.jpg"), img)

    # pil_image = cv2_to_pil(img)

    # converted = ImageEnhance.Color(pil_image)

    # desaturate = converted.enhance(0.1)
    # desaturate.save('test.jpg')

    # height, width = img.shape[:2]

    # w, h = (16, 16)

    # temp = cv2.resize(img, (w, h), interpolation=cv2.INTER_LINEAR)

    # output = cv2.resize(temp, (width, height), interpolation=cv2.INTER_NEAREST)

    # cv2.imshow('Input', img)
    # cv2.imshow('Output', output)

    # cv2.waitKey(0)


image_path = 'scripts/characters/Finn Pepperidge.jpg'
image_process(image_path)


# # name of frame and then the img requested
# cv2.imshow("TestNaruto", img)

# kernel = np.ones((20, 20), np.float32) / 225
# smoothed = cv2.filter2D(img, -1, kernel)

# # Gaussian Blur
# blur = cv2.GaussianBlur(img, (21, 21), 0)
# # Median blur
# median = cv2.medianBlur(img, 21)
# # bilateral blur
# bilat = cv2.bilateralFilter(img, 15, 75, 75)


# # cv2.imshow('frame', frame)
# cv2.imshow('res', img)
# cv2.imshow('smoothed', smoothed)
# cv2.imshow('blur', blur)
# cv2.imshow("median", median)
# cv2.imshow('bilateral', bilat)


# # if any key is pressed, exit out of the program
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# %%
