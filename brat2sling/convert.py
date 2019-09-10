from bratreader.repomodel import RepoModel
from brat2sling.sling_commons import load_commons_store
from brat2sling.doc_converter import DocConverter
import argparse
import sling


def convert(brat_dir_path: str, output_dir_path: str, verbose: bool = False):
    # load the brat repository
    repo = RepoModel(brat_dir_path)
    if verbose: print('Loaded {} document(s) from {}'.format(len(repo.documents), brat_dir_path))

    # load the SLING commons store and the document schema
    commons = load_commons_store()
    schema = sling.DocumentSchema(commons)
    commons.freeze()

    for document in repo.documents:
        reader = DocReader
        converter = DocConverter(commons, schema)
        # TODO


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--brat_dir_path', dest='brat_dir_path', required=True,
                        help='The path to the directory holding the brat files.')
    parser.add_argument('-o', '--output', dest='output_dir_path', required=True,
                        help='The path to the directory that will hold the output SLING files.')
    parser.add_argument('-v', '--verbose', dest='verbose', action='store_true', required=False,
                        help='Whether or not to run in verbose mode.')
    args = parser.parse_args()
    convert(args.brat_dir_path, args.output_dir_path, args.verbose)


