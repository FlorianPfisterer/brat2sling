from bratreader.repomodel import RepoModel
from brat2sling.doc_reader import DocReader
from brat2sling.doc_analyzer import DocAnalyzer
import argparse
from typing import Dict
import pandas as pd

def add_to_total_stats(total_stats: Dict, stats: Dict):
    for key in stats:
        if key in total_stats:
            total_stats[key] = total_stats[key] + stats[key]
        else:
            total_stats[key] = stats[key]

def analyze(brat_dir_path: str):
    # load the brat repository
    repo = RepoModel(brat_dir_path)

    total_stats: Dict = {}
    for document_name in repo.documents:
        document = repo.documents[document_name]
        reader = DocReader(document)
        stats = DocAnalyzer().analyze(reader)
        add_to_total_stats(total_stats, stats)
    
    for slot_name in total_stats:
        print('Stats for {}:'.format(slot_name))
        series = pd.Series(total_stats[slot_name])
        print_stats(series)
        print('\n')

def print_stats(series: pd.Series):
    print('Total: {}'.format(len(series)))
    print('Mean: {}'.format(series.mean()))

    for value in series.unique():
        print('Frequency of {}: {}'.format(value, (series == value).sum()))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--brat_dir_path', dest='brat_dir_path', required=True,
                        help='The path to the directory holding the brat files.')
    args = parser.parse_args()
    analyze(args.brat_dir_path)


