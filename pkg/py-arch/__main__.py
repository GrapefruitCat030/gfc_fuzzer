from fuzzer import Fuzzer
from middleware import BitFlipMiddleware, MagicModifyMiddleware

if __name__ == "__main__":
    seed_directory = "/root/project/gfc_fuzzer/seeds/tmp"
    program_path = "/root/project/gfc_fuzzer/tools/exif/exif"
    crash_directory = "/root/project/gfc_fuzzer/crashes"

    fuzzer = Fuzzer(seed_directory, program_path, crash_directory)
    fuzzer.add_middleware(BitFlipMiddleware())
    fuzzer.add_middleware(MagicModifyMiddleware())

    fuzzer.fuzz()