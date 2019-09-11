from brat2sling.mention import Mention


class Slot:
    head_id: int
    mention: Mention
    slot_name: str

    def __init__(self, head_id: int, mention: Mention, slot_name: str):
        self.head_id = head_id
        self.mention = mention
        self.slot_name = slot_name
