from typing import Union, List, Dict

from brat2sling.brat_frames import BRAT_TO_SLING_FRAME, BRAT_TO_SLING_RELATION
from brat2sling.doc_reader import DocReader
from brat2sling.slot import Slot


class DocAnalyzer:
    def analyze(self, reader: DocReader):
        # 1. add all tokens
        tokens = reader.get_tokens()

        # 2. add all mentions
        mentions = reader.get_all_mentions()
