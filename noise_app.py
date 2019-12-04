import os
import cv2

from noise.noises import gaussian_noise

if __name__ == '__main__':
    root_folder = './'
    input_folder = 'test_images'
    output_folder = 'test_images_normal_noise_20'

    for filename in os.listdir(input_folder):
        image = cv2.imread(os.path.join(input_folder, filename), 1)
        noise_image = gaussian_noise(image, sigma=20)
        cv2.imwrite(os.path.join(output_folder, filename), noise_image)
