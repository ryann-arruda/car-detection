from utils_detector import create_data_lists
import os

if __name__ == '__main__':
    create_data_lists(dataset_path= os.getcwd() + '\\dataset',
                      output_folder='./')
