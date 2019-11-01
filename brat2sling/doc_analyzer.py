from typing import Union, List, Dict

from brat2sling.brat_frames import BRAT_TO_SLING_FRAME, BRAT_TO_SLING_RELATION
from brat2sling.doc_reader import DocReader
from brat2sling.slot import Slot
from brat2sling.mention import Mention
from typing import Dict, List


class DocAnalyzer:
    @staticmethod
    def __record_slot(stats: Dict, head_mention: Mention, child_mention: Mention, relation: str):
        delta_sentence = child_mention.sentence_id - head_mention.sentence_id
        if relation in stats:
            current = stats[relation]
            current.append(delta_sentence)
            stats[relation] = current
        else:
            stats[relation] = [delta_sentence]

    def analyze(self, reader: DocReader) -> Dict[str, List[int]]:
        mentions = reader.get_all_mentions()

        # child is in another sentence (save delta sentence id), by type
        stats = {}
        for mention in mentions:
            current_sentence = mention.sentence_id
            # get the children of this mention
            slots_by_name = reader.get_slots_for_mention_by_name(mention)
            for slot_name in slots_by_name:
                for slot in slots_by_name[slot_name]:
                    self.__record_slot(stats, mention, slot.mention, slot_name)
        
        return stats
