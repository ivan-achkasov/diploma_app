import os

from yolo import YOLO
from PIL import Image


def detect_imges(input_folder, output_folder, yolo):
    for filename in os.listdir(input_folder):
        try:
            image = Image.open(open(os.path.join(input_folder, filename), 'rb'))
        except:
            print('Open Error! Try again!')
            continue
        else:
            try:
                r_image = yolo.detect_image(image)
                r_image.save(open(os.path.join(output_folder, filename), 'wb'))
            except:
                continue


FLAGS = None

if __name__ == '__main__':
    rootFolder = "./"
    input_folder = rootFolder + "test_images_normal_noise_100"
    output_folder = rootFolder + "out_images_noise_100"

    yolo = YOLO()
    detect_imges(input_folder, output_folder, yolo)
    yolo.close_session()
