from brat2sling.mention import Mention


class Slot:
    mention: Mention
    slot_name: str

    def __init__(self, mention: Mention, slot_name: str):
        self.mention = mention
        self.slot_name = slot_name
