import os
import re
import struct
import numpy as np
from PIL import Image
from codecs import decode

TRAIN_DATA_PATH="G:/Dataset/CASIA-HWDB/HWDB1.1 gnt/HWDB1.1trn_gnt"       
TEST_DATA_PATH="G:/Dataset/CASIA-HWDB/HWDB1.1 gnt/HWDB1.1tst_gnt"          
TRAIN_IMG_PATH="G:/Dataset/CASIA-HWDB/HWDB1.1 img/train"                  
TEST_IMG_PATH="G:/Dataset/CASIA-HWDB/HWDB1.1 img/test"   

TEMP_PATH = "H:/test/HandwritingRecognition/CASIA-HWDB/HWDB1.1_data/HWDB1.1tst_img"

TARGET_CHARACTERS = []

class Reader:
    def load_gnt_file(self, filename):
        """
        Load characters and images from a given GNT file.
        :param filename: The file path to load.
        :return: (image: Pillow.Image.Image, character) tuples
        """
        print(filename)
        with open(filename, "rb") as f:
            while True:
                packed_length = f.read(4)
                if packed_length == b'':
                    break
                #length = struct.unpack("<I", packed_length)[0]
                raw_label = struct.unpack(">cc", f.read(2))
                width = struct.unpack("<H", f.read(2))[0]
                height = struct.unpack("<H", f.read(2))[0]
                photo_bytes = f.read(height * width)
                label = decode(raw_label[0] + raw_label[1], encoding="gb2312")
                image = Image.frombytes('L', (width, height), photo_bytes)

                yield image, label

    def read_gnt_image(self, gnt_path):
        data = self.load_gnt_file(gnt_path)
        data_list = []       

        while True:
            try:
                image, label = next(data)
                image = image.resize((32, 32))  # 图像缩放
                #image = PIL.ImageOps.invert(image)  # 图像反色

                if label in TARGET_CHARACTERS:
                    data_list.append((image, label))
            except StopIteration:
                break
           
        return data_list

    def save_gnt_image(self, gnt_path, save_path):
        """
        Save characters and images from a given GNT file as JPG file.
        :param gnt_path: The file path to load.
               save_path: The png files path to save.
        :return: (image: Pillow.Image.Image, character) tuples
        """
        data = self.read_gnt_image(gnt_path)

        num = re.findall('\d+', gnt_path)[-1]
        for d in data:
            if not os.path.exists(save_path + "/" + d[1]):
                os.mkdir(save_path + "/" + d[1] + "/")

            d[0].save(save_path + "/" + d[1] + "/" + str(num) + ".jpg")
            print('save jpg: tag %s gnt_id: %s' % (d[1], str(num)))


# 选取数据集
for i, file in enumerate(os.listdir(TEMP_PATH)):
    if i < 100:
        print(file)
        TARGET_CHARACTERS.append(file)
    else:
        break

reader = Reader()

files = os.listdir(TEST_DATA_PATH)
for file in files:
    reader.save_gnt_image(TEST_DATA_PATH + "/" + file, TEST_IMG_PATH)

files = os.listdir(TRAIN_DATA_PATH)
for file in files:
    reader.save_gnt_image(TRAIN_DATA_PATH + "/" + file, TRAIN_IMG_PATH)


