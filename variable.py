class Variable:
    def __init__(self, pos, size):
        self.pos = pos
        self.domain = set(range(1, size+1))
        self.value = None

    def clear(self):
        self.value = None

    def set_val(self, value):
        self.value = value

    def is_assigned(self):
        return self.value is not None

    def __eq__(self, other):
        return self.pos == other.pos

    def __hash__(self):
        return hash(self.pos)
