import cv2
import numpy as np
from PIL import Image

def cv2_to_pil(cv2_img):
    pil_array = cv2.cvtColor(cv2_img, cv2.COLOR_BGR2RGB)
    pil_image = Image.fromarray(pil_array)
    return pil_image

def pil_to_cv2(pil_image):
    cv2_img = cv2.cvtColor(np.array(pil_image), cv2.COLOR_RBG2BGR)
    return cv2_img