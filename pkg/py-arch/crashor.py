import os

class Crashor:
    def __init__(self, crash_directory):
        self.crash_directory = crash_directory
        self.counter = 0

    def collect(self, input_data, stdout, stderr):
        crash_filename = os.path.join(self.crash_directory, f"crash_{self.counter}.bin")
        with open(crash_filename, 'wb') as f:
            f.write(input_data)
        crash_output = os.path.join(self.crash_directory, f"crash_{self.counter}.txt")
        with open(crash_output, 'w') as f:
            f.write("STDOUT:\n")
            f.write(stdout.decode())
            f.write("\nSTDERR:\n")
            f.write(stderr.decode())
        self.counter += 1