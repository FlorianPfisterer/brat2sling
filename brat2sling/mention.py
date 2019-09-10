class Mention:
    id: int
    type: str
    from_idx: int
    to_idx: int

    def __init__(self, id: int, type: str, from_idx: int, to_idx: int):
        self.id = id
        self.type = type
        self.from_idx = from_idx
        self.to_idx = to_idx