import os
import xml.etree.ElementTree as ET

def check_and_delete_zero_dimension_files(directory):
    zero_dimension_files = []

    # 遍历目录下的所有文件
    for filename in os.listdir(directory):
        if filename.endswith('.xml'):
            file_path = os.path.join(directory, filename)

            # 解析XML文件
            tree = ET.parse(file_path)
            root = tree.getroot()

            # 获取width和height
            width = int(root.find('.//size/width').text)
            height = int(root.find('.//size/height').text)

            # 检查width和height是否为0
            if width == 0 or height == 0:
                zero_dimension_files.append(filename)
                # 删除XML文件
                os.remove(file_path)
                print(f"Deleted XML file: {filename}")

                # 删除对应的图片文件
                image_filename = filename.replace('.xml', '.jpg')  # 假设图片扩展名为.jpg
                image_path = os.path.join(directory, image_filename)
                if os.path.exists(image_path):
                    os.remove(image_path)
                    print(f"Deleted image file: {image_filename}")

    return zero_dimension_files

# 使用示例
directory = './test'  # 将此路径替换为你的XML文件所在的目录
files_with_zero_dimensions = check_and_delete_zero_dimension_files(directory)
if files_with_zero_dimensions:
    print("Processed files with zero dimensions:", files_with_zero_dimensions)
else:
    print("No files with zero dimensions found.")
