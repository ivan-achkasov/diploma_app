import cv2
import numpy as np


def gaussian_noise(image, mu=0, sigma=1):
    gaussian = np.random.normal(mu, sigma, image.shape)
    noisy_image = image + gaussian
    cv2.normalize(noisy_image, noisy_image, 0, 255, cv2.NORM_MINMAX, dtype=-1)
    noisy_image = noisy_image.astype(np.uint8)
    return noisy_image
