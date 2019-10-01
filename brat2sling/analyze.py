from bratreader.repomodel import RepoModel
from brat2sling.doc_reader import DocReader
from brat2sling.doc_analyzer import DocAnalyzer
import argparse

def analyze(brat_dir_path: str):
    # load the brat repository
    repo = RepoModel(brat_dir_path)

    for document_name in repo.documents:
        document = repo.documents[document_name]
        reader = DocReader(document)
        DocAnalyzer().analyze(reader)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--brat_dir_path', dest='brat_dir_path', required=True,
                        help='The path to the directory holding the brat files.')
    args = parser.parse_args()
    analyze(args.brat_dir_path)


