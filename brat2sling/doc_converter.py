import sling
from brat2sling.brat_frames import BRAT_TO_SLING_FRAME, BRAT_TO_SLING_RELATION


class DocConverter:
    store: sling.Store
    schema: sling.DocumentSchema
    doc: sling.Document

    def __init__(self, commons_store: sling.Store, schema: sling.DocumentSchema):
        self.store = sling.Store(commons_store)
        self.schema = schema
        self.doc = sling.Document(None, self.store, self.schema)

    def __get_frame_type(self, frame_name: str) -> sling.Frame:
        if frame_name in BRAT_TO_SLING_FRAME:
            return self.store[BRAT_TO_SLING_FRAME[frame_name]]
        else:
            raise ValueError('Encountered unknown frame name: {}'.format(frame_name))

    def __get_role_type(self, relation_name: str) -> sling.Frame:
        if relation_name in BRAT_TO_SLING_RELATION:
            return self.store[BRAT_TO_SLING_RELATION[relation_name]]
        else:
            raise ValueError('Encountered unknown relation name: {}'.format(relation_name))


