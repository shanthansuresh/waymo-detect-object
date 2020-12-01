import argparse
import glob
import os
import random
import shutil

import numpy as np

from utils import get_module_logger


def split(data_dir):
    """
    Create three splits from the processed records. The files should be moved to new folders in the 
    same directory. This folder should be named train, val and test.

    args:
        - data_dir [str]: data directory, /mnt/data
    """
    # TODO: Implement function
   
    # Create train, val and test directories
    train_dir = data_dir + "/train"
    dir_exists = os.path.isdir(train_dir)
    if (dir_exists):
      shutil.rmtree(train_dir)

    val_dir = data_dir + "/val"
    dir_exists = os.path.isdir(val_dir)
    if (dir_exists):
      shutil.rmtree(val_dir)

    test_dir = data_dir + "/test"
    dir_exists = os.path.isdir(test_dir)
    if (dir_exists):
      shutil.rmtree(test_dir)

    tfrec_files_list = os.listdir(data_dir)
    num_tfrecs = len(tfrec_files_list)
    random.shuffle(tfrec_files_list)

    #Split in the ratio of 0.70 : 0.15 : 0.15 for the training, validation and test set
    train_size = int(num_tfrecs * 0.70)
    val_size   = int(num_tfrecs * 0.15)
    test_size  = int(num_tfrecs * 0.15)

    os.mkdir(train_dir)
    os.mkdir(val_dir)
    os.mkdir(test_dir)
 
    dest_dir = train_dir
    for i in range(train_size):
      #Copy training data
      src_file = data_dir + "/" + tfrec_files_list[i]
      shutil.copy2(src_file, dest_dir)

    dest_dir = val_dir
    for i in range(train_size, (train_size+val_size)):
        #Copy val data
        src_file = data_dir + "/" + tfrec_files_list[i]
        shutil.copy2(src_file, dest_dir)

    dest_dir = test_dir
    for i in range((train_size+val_size), (train_size+val_size+test_size)):
        #Copy test data
        src_file = data_dir + "/" + tfrec_files_list[i]
        shutil.copy2(src_file, dest_dir)
    

if __name__ == "__main__": 
    parser = argparse.ArgumentParser(description='Split data into training / validation / testing')
    parser.add_argument('--data_dir', required=True,
                        help='data directory')
    args = parser.parse_args()

    logger = get_module_logger(__name__)
    logger.info('Creating splits...')
    split(args.data_dir)
