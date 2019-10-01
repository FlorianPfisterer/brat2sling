from bratreader.annotateddocument import AnnotatedDocument
from bratreader.word import Word
from bratreader.annotation import Annotation
from typing import Dict, List, Tuple
from brat2sling.brat_frames import UNKNOWN_FRAME, FRAME, ACTION, ENTITY, INPUT, LOCATION, UTENSIL, CONDITION
from brat2sling.mention import Mention
from brat2sling.slot import Slot


class DocReader:
    doc: AnnotatedDocument
    __tokens: Dict[Word, int]
    __mentions: List[Mention]
    __mentions_slots: Dict[int, List[Slot]]

    def __init__(self, document: AnnotatedDocument):
        self.doc = document
        self.__tokens = {}
        self.__mentions = []
        self.__mentions_slots = {}
        self.__read_document()

    def __read_document(self):
        self.__read_tokens()

        # go through all annotations
        for annotation in self.doc.annotations:
            self.__read_links_and_labels(annotation)

    def __read_links_and_labels(self, annotation: Annotation):
        from_idx, to_idx = self.__get_word_indices(annotation)
        labels: Dict[str, List[str]] = annotation.labels
        links: Dict[str, List[Annotation]] = annotation.links
        sentence_id = annotation.words[0].sentkey

        # first, determine the type of mention (if any)
        mention: Mention
        if ACTION in labels:
            frame = UNKNOWN_FRAME
            if FRAME in labels:
                frame = labels[FRAME][0]
            mention = Mention(annotation.id, frame, from_idx, to_idx, sentence_id)
        elif ENTITY in labels:
            mention = Mention(annotation.id, ENTITY, from_idx, to_idx, sentence_id)
        else:
            return

        self.__mentions.append(mention)

        def add_slot(head_id: int, slot_mention: Mention, slot_name: str):
            slot = Slot(head_id, slot_mention, slot_name)
            if head_id in self.__mentions_slots:
                self.__mentions_slots[head_id].append(slot)
            else:
                self.__mentions_slots[head_id] = [slot]

        # second, check if this mention fills any slot of another mention
        for relation_name in [INPUT, LOCATION, UTENSIL, CONDITION]:
            if relation_name in links:
                head_annotation: Annotation = links[relation_name][0]
                add_slot(head_annotation.id, mention, relation_name)

    def __read_tokens(self):
        self.__tokens = {}
        i = 0
        for sentence in self.doc.sentences:
            for word in sentence.words:
                self.__tokens[word] = i
                i = i + 1

    def __get_word_indices(self, annotation: Annotation) -> Tuple[int, int]:
        word_indices = list(map(lambda w: self.__tokens[w], annotation.words))
        from_idx = word_indices[0]
        to_idx = word_indices[-1] + 1
        return from_idx, to_idx

    # Public
    def get_tokens(self) -> List[str]:
        tokens = [[]] * len(self.__tokens)
        for word in self.__tokens:
            tokens[self.__tokens[word]] = word.form
        return tokens

    def get_all_mentions(self) -> List[Mention]:
        return self.__mentions

    def get_slots_for_mention_by_name(self, mention: Mention) -> Dict[str, List[Slot]]:
        if mention.id in self.__mentions_slots:
            slots_by_name = {}
            slots = self.__mentions_slots[mention.id]
            for slot in slots:
                if slot.slot_name in slots_by_name:
                    slots_by_name[slot.slot_name].append(slot)
                else:
                    slots_by_name[slot.slot_name] = [slot]
            return slots_by_name
        return {}
