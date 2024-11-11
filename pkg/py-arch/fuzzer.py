from seed_loader import SeedLoader
from program_runner import ProgramRunner
from crashor import Crashor

class Fuzzer:
    def __init__(self, seed_directory, program_path, crash_directory):
        self.middlewares = []
        self.seed_loader = SeedLoader(seed_directory)
        self.program_runner = ProgramRunner(program_path)
        self.crash_collector = Crashor(crash_directory)

    def add_middleware(self, middleware):
        self.middlewares.append(middleware)
        print(f"Registered middleware: {middleware.description}")

    def fuzz(self):
        seeds = self.seed_loader.load_seeds()
        for seed in seeds:
            for _ in range(1000):  # 每个种子变异10次
                mutated_data = seed
                for middleware in self.middlewares:
                    mutated_data = middleware.mutate(mutated_data)
                returncode, stdout, stderr = self.program_runner.run(mutated_data)
                if returncode != 0:  # 假设非零返回码表示崩溃或异常
                    self.crash_collector.collect(mutated_data, stdout, stderr)