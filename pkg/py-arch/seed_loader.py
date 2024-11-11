import os

class SeedLoader:
    def __init__(self, seed_directory):
        self.seed_directory = seed_directory

    def load_seeds(self):
        seeds = []
        for filename in os.listdir(self.seed_directory):
            filepath = os.path.join(self.seed_directory, filename)
            with open(filepath, 'rb') as f:
                seeds.append(bytearray(f.read()))
        return seeds