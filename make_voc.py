import os
import shutil
from lxml import etree

def create_voc_directories(base_dir):
    annotations_dir = os.path.join(base_dir, 'Annotations')
    imagesets_main_dir = os.path.join(base_dir, 'ImageSets/Main')
    jpegimages_dir = os.path.join(base_dir, 'JPEGImages')

    os.makedirs(annotations_dir, exist_ok=True)
    os.makedirs(imagesets_main_dir, exist_ok=True)
    os.makedirs(jpegimages_dir, exist_ok=True)

    return annotations_dir, imagesets_main_dir, jpegimages_dir

def process_dataset(dataset_dir, base_dir, dataset_type):
    annotations_dir, imagesets_main_dir, jpegimages_dir = create_voc_directories(base_dir)

    image_filenames = []
    for filename in os.listdir(dataset_dir):
        if filename.endswith('.xml'):
            xml_path = os.path.join(dataset_dir, filename)
            img_filename = filename.replace('.xml', '.jpg')
            img_path = os.path.join(dataset_dir, img_filename)

            shutil.copy(xml_path, os.path.join(annotations_dir, filename))
            shutil.copy(img_path, os.path.join(jpegimages_dir, img_filename))

            image_filenames.append(os.path.splitext(img_filename)[0])

    with open(os.path.join(imagesets_main_dir, f'{dataset_type}.txt'), 'w') as f:
        for filename in image_filenames:
            f.write(f"{filename}\n")

# Example usage
base_dir = 'faster_rcnn/VOCdevkit2007/VOC2007'
train_dir = 'train'
test_dir = 'test'

process_dataset(train_dir, base_dir, 'train')
process_dataset(test_dir, base_dir, 'val')
