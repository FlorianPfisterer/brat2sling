import os
import argparse
from random import shuffle
import math
import shutil
from brat2sling.convert import convert

FILE_EXTS = ['.txt', '.ann']


def get_raw_recipe_names(brat_dir_path: str):
    all_files = os.listdir(brat_dir_path)
    recipe_names = set([])
    for file_name in all_files:
        if not file_name.startswith('.'):
            # the extension is either .txt or .ann, so remove the last 4 characters to the the name only
            recipe_names.add(file_name[:-4])
    return list(recipe_names)

def create_crossvalidation_splits(k: int, brat_dir_path: str, output_folder_path: str, verbose: bool = False):
    recipe_names = get_raw_recipe_names(brat_dir_path)
    shuffle(recipe_names)

    # split recipes up into k groups
    fold_size = math.floor(len(recipe_names) / k)
    folds_recipes = [[]] * k
    for i in range(k):
        start = i * fold_size
        end = -1 if i == (k - 1) else (i + 1) * fold_size 
        folds_recipes[i] = recipe_names[start:end]

    # for each fold, create a temporary folder that contains only that fold, and then
    # convert: a) this fold's recipes into a recordio dev set and b) all but this fold's
    # recipe into a recordio train set
    temp_folder = '{}/temp_fold'.format(output_folder_path)
    os.mkdir(temp_folder)
    for i in range(k):
        recipes = folds_recipes[i]
        # move files over and move them back afterwards
        for recipe in recipes:
            for ext in FILE_EXTS:
                shutil.move('{}/{}{}'.format(brat_dir_path, recipe, ext), '{}/{}{}'.format(temp_folder, recipe, ext))

        # now read the files in temp_folder and convert them
        dev_rec_file = '{}/fold_{}_dev.rec'.format(output_folder_path, i)
        train_rec_file = '{}/fold_{}_train.rec'.format(output_folder_path, i)

        convert(temp_folder, dev_rec_file, verbose)
        convert(brat_dir_path, train_rec_file, verbose)

        for recipe in recipes:
            for ext in FILE_EXTS:
                shutil.move('{}/{}{}'.format(temp_folder, recipe, ext), '{}/{}{}'.format(brat_dir_path, recipe, ext))
    shutil.rmtree(temp_folder)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--brat_dir_path', dest='brat_dir_path', required=True,
                        help='The path to the directory holding all of the brat files.')
    parser.add_argument('-o', '--output', dest='output_dir_path', required=True,
                        help='The path to the folder that will contain the output SLING recordio files for all folds.')
    parser.add_argument('-k', '--num_folds', dest='num_folds', required=False, default=10,
                        help='The number of folds to generate.')
    parser.add_argument('-v', '--verbose', dest='verbose', action='store_true', required=False,
                        help='Whether or not to run in verbose mode.')
    args = parser.parse_args()
    create_crossvalidation_splits(args.num_folds, args.brat_dir_path, args.output_dir_path, args.verbose)