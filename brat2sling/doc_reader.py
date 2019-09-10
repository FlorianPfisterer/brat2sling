from bratreader.annotateddocument import AnnotatedDocument


class DocReader:
    doc: AnnotatedDocument

    def __init__(self, document: AnnotatedDocument):
        self.doc = document
