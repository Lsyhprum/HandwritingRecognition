import os
import re
import struct
import numpy as np
from PIL import Image
from codecs import decode 


class Reader:
    
    def __init__(self, target):
        ROOT = "G:/Dataset/CASIA-HWDB"

        self._target = target
        
        self.train_gnt = ROOT + "/gnt1.1/trn_gnt"
        self.test_gnt = ROOT + "/gnt1.1/tst_gnt"
        self.train_path = ROOT + "/HWDB-10/train"
        self.test_path = ROOT + "/HWDB-10/test"

    def get_dataset_info(self):
        cnt = 0
        files = os.listdir(self.train_path)
        for file in files:
            pics = os.listdir(self.train_path + "/" + file)
            cnt += len(pics)
            print("%s : %d" %(file, len(pics)))

        # train set 2400
        print("total train set: %d" % cnt)
        
        cnt = 0
        files = os.listdir(self.test_path)
        for file in files:
            pics = os.listdir(self.test_path + "/" + file)
            print("%s : %d" %(file, len(pics)))
        # test set 600
        print("total test set: %d" % cnt)

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

                if label in self._target:
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

    def generate_dataset(self):
        files = os.listdir(self.train_gnt)
        for file in files:
            reader.save_gnt_image(self.train_gnt + "/" + file, self.train_path)

        files = os.listdir(self.test_gnt)
        for file in files:
            reader.save_gnt_image(self.test_gnt + "/" + file, self.test_path)

TARGET_CHARACTERS = ['杭', '州', '电', '子', '科', '技', '大', '学', '中', '北']

reader = Reader(TARGET_CHARACTERS)

#reader.generate_dataset()

reader.get_dataset_info()