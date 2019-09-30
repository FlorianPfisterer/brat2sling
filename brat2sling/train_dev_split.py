"""
Reads a .rec file with a set of frames and randomly
splits it into two separate sets, with a given size ratio.
"""
import argparse
import sling
from typing import Tuple, List
from random import shuffle


def create_train_dev_split(input_file: str, train_file: str, dev_file: str, ratio: float):
    reader = sling.RecordReader(input_file)
    frames: List[Tuple[str, str]] = []
    for key, value in reader:
        frames.append((key, value))

    shuffle(frames)

    total_count = len(frames)
    train_count = int(round((1 - ratio) * total_count))

    files = {'train': train_file, 'dev': dev_file}
    result_frames = {'train': frames[:train_count], 'dev': frames[train_count:]}
    for split in result_frames:
        writer = sling.RecordWriter(files[split])
        for (key, value) in result_frames[split]:
            writer.write(key, value)
        writer.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input_file', dest='input_file_path', required=True,
                        help='The path to the input .rec file with all farmes.')
    parser.add_argument('-r', '--ratio', dest='dev_ratio', default=0.3,
                        help='The ratio of the whole frames to use for the dev set (a float between 0 and 1).')
    parser.add_argument('--train', dest='train_file_path', default='train.rec',
                        help='The path to the training output .rec file.')
    parser.add_argument('--dev', dest='dev_file_path', default='dev.rec',
                        help='The path to the dev output .rec file.')
    args = parser.parse_args()
    create_train_dev_split(args.input_file_path, args.train_file_path, args.dev_file_path, args.dev_ratio)
