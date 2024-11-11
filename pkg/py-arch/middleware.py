import random

class Middleware:
    def __init__(self, description=""):
        self.description = description

    def mutate(self, data):
        raise NotImplementedError("Middleware subclasses must implement the mutate method")

class BitFlipMiddleware(Middleware):
    def __init__(self):
        super().__init__("Flips random bits in the input")

    def mutate(self, data):
        num = int((len(data)-8) * 0.01)
        idxs = range(4, (len(data)-4))
        chosen_idxs = []
        for i in range(num):
            chosen_idxs.append(random.choice(idxs))
        for x in chosen_idxs:
            curr = data[x]
            curr_bin = (bin(curr).replace("0b", "")).zfill(8)
            picked_idx = random.randint(0, 7)
            flipped_bin = curr_bin[:picked_idx] + str(int(curr_bin[picked_idx]) ^ 1) + curr_bin[picked_idx + 1:]
            data[x] = int(flipped_bin, 2)
        return data

class MagicModifyMiddleware(Middleware):
    def __init__(self):
        super().__init__("Modifies the input with magic values")
        self.magic_dict = {
            (1, 255): [255],
            (1, 127): [127],
            (1, 0): [0],
            (2, 255): [255, 255],
            (2, 0): [0, 0],
            (4, 255): [255, 255, 255, 255],
            (4, 0): [0, 0, 0, 0],
            (4, 128): [128, 0, 0, 0],
            (4, 64): [64, 0, 0, 0],
            (4, 127): [127, 255, 255, 255]
        }

    def mutate(self, data):
        picked_magic = random.choice(list(self.magic_dict.keys()))
        picked_index = random.randint(0, len(data) - 8)
        values = self.magic_dict[picked_magic]
        for i, v in enumerate(values):
            data[picked_index + i] = v
        return data