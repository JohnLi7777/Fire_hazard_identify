import os
import random
import shutil


def split_data(image_folder, label_folder, train_image_folder, train_label_folder, val_image_folder, val_label_folder):
    # 确保目标文件夹存在
    # for folder in [train_image_folder, train_label_folder, val_image_folder, val_label_folder]:
    #     if not os.path.exists(folder):
    #         os.makedirs(folder)

    # 获取图片文件列表
    image_files = [f for f in os.listdir(image_folder) if f.endswith(('.jpg', '.jpeg', '.png'))]

    # 计算 80% 的数量
    train_size = int(len(image_files) * 0.8)

    # 随机打乱图片文件列表
    random.shuffle(image_files)

    # 划分训练集和验证集
    train_files = image_files[:train_size]
    val_files = image_files[train_size:]

    # 复制训练集数据
    for file in train_files:
        image_src = os.path.join(image_folder, file)
        image_dst = os.path.join(train_image_folder, file)
        shutil.copy2(image_src, image_dst)

        label_name = os.path.splitext(file)[0] + '.txt'
        label_src = os.path.join(label_folder, label_name)
        label_dst = os.path.join(train_label_folder, label_name)
        if os.path.exists(label_src):
            shutil.copy2(label_src, label_dst)

    # 复制验证集数据
    for file in val_files:
        image_src = os.path.join(image_folder, file)
        image_dst = os.path.join(val_image_folder, file)
        shutil.copy2(image_src, image_dst)

        label_name = os.path.splitext(file)[0] + '.txt'
        label_src = os.path.join(label_folder, label_name)
        label_dst = os.path.join(val_label_folder, label_name)
        if os.path.exists(label_src):
            shutil.copy2(label_src, label_dst)


if __name__ == "__main__":
    # 替换为实际的文件夹路径
    image_folder = "九分类"
    label_folder = "九分类标注文件"
    train_image_folder = "123/images/train"
    train_label_folder = "123/labels/train"
    val_image_folder = "123/images/val"
    val_label_folder = "123/labels/val"

    split_data(image_folder, label_folder, train_image_folder,
               train_label_folder, val_image_folder, val_label_folder)