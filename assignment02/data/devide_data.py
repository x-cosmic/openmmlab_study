import os
import shutil
import random
import math


data_folder = "D:/mmpre/data/ori"


train_ratio = 0.8
val_ratio = 0.2


train_folder = "D:/mmpre/data/train_data"
val_folder = "D:/mmpre/data/val_data"
os.makedirs(train_folder, exist_ok=True)
os.makedirs(val_folder, exist_ok=True)


for class_name in os.listdir(data_folder):
    class_folder = os.path.join(data_folder, class_name)
    if not os.path.isdir(class_folder):
        continue


    train_class_folder = os.path.join(train_folder, class_name)
    val_class_folder = os.path.join(val_folder, class_name)
    os.makedirs(train_class_folder, exist_ok=True)
    os.makedirs(val_class_folder, exist_ok=True)


    image_files = [f for f in os.listdir(class_folder) if f.endswith(".jpg") or f.endswith(".png")]
    random.shuffle(image_files)

    train_split = math.floor(len(image_files) * train_ratio)


    train_files = image_files[:train_split]
    val_files = image_files[train_split:]


    for train_file in train_files:
        src_path = os.path.join(class_folder, train_file)
        dst_path = os.path.join(train_class_folder, train_file)
        shutil.copy(src_path, dst_path)


    for val_file in val_files:
        src_path = os.path.join(class_folder, val_file)
        dst_path = os.path.join(val_class_folder, val_file)
        shutil.copy(src_path, dst_path)

print("Finish!")
