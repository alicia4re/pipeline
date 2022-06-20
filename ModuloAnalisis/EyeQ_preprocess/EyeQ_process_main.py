import fundus_prep 
import glob
import os
import cv2 as cv
from PIL import ImageFile

ImageFile.LOAD_TRUNCATED_IMAGES = True


def process(image_lista, g_path):
    for image_path in image_lista:
        dst_image = os.path.splitext(image_path.split('/')[-1])[0] + '.png'
        dst_path = os.path.join(g_path, dst_image)
        if os.path.exists(dst_path):
            print('continue...')
            continue
        try:
            img = fundus_prep.imread(image_path)
            r_img, borders, mask = fundus_prep.process_without_gb(img)
            r_img = cv.resize(r_img, (600, 600))
            fundus_prep.imwrite(dst_path, r_img)
            # mask = cv.resize(mask, (800, 800))
            # prep.imwrite(os.path.join('./original_mask', dst_image), mask)
        except:
            print(image_path)
            continue


def runPreProcessEyeQ():
    image_list = glob.glob(os.path.join('original_img', '*.jpeg'))
    save_path = fundus_prep.fold_dir('./pipeline/data/original_crop')

    process(image_list, save_path)


if __name__ == "__main__":
    runPreProcessEyeQ