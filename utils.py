import os
from random import shuffle

def create_results_folder(target, video_name):
    os.makedirs('results', exist_ok=True)
    os.makedirs(f'results\\{target}', exist_ok=True)
    os.makedirs(f'results\\{target}\\{video_name}', exist_ok=True)

def train_test_split(dataset_path, train=0.7):
    image_ids = []

    for image in os.listdir(dataset_path + '\\images'):
        image_ids.append(image.split('.')[0])
    
    shuffle(image_ids)

    training_set_size = int(len(image_ids) * train)

    train_ids = image_ids[:training_set_size]
    test_ids = image_ids[training_set_size:]

    os.makedirs(dataset_path + '\\ImageSets\\', exist_ok=True)

    with open(dataset_path + '\\ImageSets\\' + 'train.txt', 'w') as f:
        for img_id in train_ids:
            f.write(img_id + '\n')
    
    with open(dataset_path + '\\ImageSets\\' + 'test.txt', 'w') as f:
        for img_id in test_ids:
            f.write(img_id + '\n')
        