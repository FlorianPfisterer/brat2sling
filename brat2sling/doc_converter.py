from typing import Union, List, Dict

import sling
from brat2sling.brat_frames import BRAT_TO_SLING_FRAME, BRAT_TO_SLING_RELATION
from brat2sling.doc_reader import DocReader
from brat2sling.slot import Slot


class DocConverter:
    store: sling.Store
    schema: sling.DocumentSchema
    doc: sling.Document
    doc_name: str

    def __init__(self, commons_store: sling.Store, schema: sling.DocumentSchema, doc_name: str):
        self.store = sling.Store(commons_store)
        self.schema = schema
        self.doc_name = doc_name
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

    def __slots_to_frames(self, slots: List[Slot], frames_by_mention_id: Dict[int, sling.Frame])\
            -> Union[sling.Frame, sling.Array]:
        def slot_to_frame(slot: Slot):
            return frames_by_mention_id[slot.mention.id]

        if len(slots) == 1:
            return slot_to_frame(slots[0])
        else:
            array = self.store.array(len(slots))
            for i, slot in slots:
                array[i] = slot_to_frame(slot)
            return array

    def convert(self, reader: DocReader, writer: sling.RecordWriter):
        # 1. add all tokens
        tokens = reader.get_tokens()
        for token in tokens:
            self.doc.add_token(token)

        # 2. add all mentions
        frames_by_mention_id = {}
        mentions = reader.get_all_mentions()
        for mention in mentions:
            frame_type = self.__get_frame_type(mention.type)
            frame = self.doc.evoke_type(mention.from_idx, mention.to_idx, frame_type)
            frames_by_mention_id[mention.id] = frame

        # 3. fill in slots
        for mention in mentions:
            slots_by_name = reader.get_slots_for_mention_by_name(mention)
            for slot_name in slots_by_name:
                role_type = self.__get_role_type(slot_name)
                slots = slots_by_name[slot_name]
                frames_by_mention_id[mention.id][role_type] = self.__slots_to_frames(slots, frames_by_mention_id)

        self.doc.update()
        writer.write(self.doc_name, self.doc.frame.data(binary=True))
