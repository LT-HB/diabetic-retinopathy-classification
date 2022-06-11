import os
from os import getcwd
import numpy as np

# ---------------------------------------------------#
#   训练自己的数据集的时候一定要注意修改classes
#   修改成自己数据集所区分的种类
#
#   种类顺序需要和训练时用到的model_data下的txt一样
#   生成cls_train_val.txt 和 cls.test.txt
# ---------------------------------------------------#
classes = ["Retinopathy_grade_0","Retinopathy_grade_1", "Retinopathy_grade_2","Retinopathy_grade_3"]
#classes = ["no_sick", "sick"]
#sets = ["test"]
# sets = ["train"]
test_split = 0.2

if __name__ == "__main__":
    #wd = getcwd()

    #for se in sets:
    list_file_train_val = open('cls_' + 'train_val' + '.txt', 'w')
    list_file_test = open('cls_' + 'test' + '.txt', 'w')

    datasets_path = 'Data' #所在文件夹的路径
    #datasets_path = "D:/class_PR/dataset/" + se
    types_name = os.listdir(datasets_path)
    #types_name.pop(0)
    for type_name in types_name:
        if type_name not in classes:
            continue
        cls_id = classes.index(type_name)

        photos_path = os.path.join(datasets_path, type_name)
        photos_name = os.listdir(photos_path)
        np.random.seed(10101)
        np.random.shuffle(photos_name)
        np.random.seed(None)

        N = len(photos_name)
        num_test = int(N * test_split)
        num_train = N - num_test

        for i, photo_name in enumerate(photos_name):
            _, postfix = os.path.splitext(photo_name)
            if postfix not in ['.jpg', '.png', '.jpeg']:
                continue

            if i+1 <= num_test:
                list_file_test.write(str(cls_id) + ";" + '%s' % (os.path.join(photos_path, photo_name)))
                list_file_test.write('\n')
            else:
                list_file_train_val.write(str(cls_id) + ";" + '%s' % (os.path.join(photos_path, photo_name)))
                list_file_train_val.write('\n')
    list_file_train_val.close()
    list_file_test.close()

