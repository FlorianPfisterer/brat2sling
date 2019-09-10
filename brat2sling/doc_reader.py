from bratreader.annotateddocument import AnnotatedDocument
from bratreader.word import Word
from bratreader.annotation import Annotation
from typing import Dict, List
from brat2sling.brat_frames import UNKNOWN_FRAME

ACTION = 'Action'
ENTITY = 'Entity'
FRAME = 'PrimaryFrame'


def __read_links(annotation: Annotation):
    for link in annotation.links:
        print('link', link)
        print(annotation.links[link])


class DocReader:
    doc: AnnotatedDocument
    __tokens: Dict[Word, int]

    def __init__(self, document: AnnotatedDocument):
        self.doc = document
        self.__read_document()

    def __read_document(self):
        self.__read_tokens()

        # go through all annotations
        for annotation in self.doc.annotations:
            word_indices = list(map(lambda w: self.__tokens[w], annotation.words))
            from_idx = word_indices[0]
            to_idx = word_indices[-1] + 1

            self.__read_links(annotation.links, from_idx, to_idx)
            self.__read_labels(annotation.labels, from_idx, to_idx)

    def __read_links(self, links, from_idx: int, to_idx: int):
        for link in links:
            print(link)
            print(links[link])

    def __read_labels(self, labels, from_idx: int, to_idx: int):
        if ACTION in labels:
            frame = UNKNOWN_FRAME
            if FRAME in labels:
                frame = labels[FRAME][0]
            # TODO create mention
        elif ENTITY in labels:
            # interpret as entity
            # TODO create mention
            pass

    def __read_tokens(self):
        self.__tokens = {}
        i = 0
        for sentence in self.doc.sentences:
            for word in sentence.words:
                self.__tokens[word] = i
                i = i + 1

    # Public
    def get_tokens(self) -> List[str]:
        tokens = [] * len(self.__tokens)
        for word in self.__tokens:
            tokens[self.__tokens[word]] = word.form
        return tokens
