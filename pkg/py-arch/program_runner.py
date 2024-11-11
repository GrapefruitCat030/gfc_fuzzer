import subprocess

class ProgramRunner:
    def __init__(self, program_path):
        self.program_path = program_path

    def run(self, input_data):
        process = subprocess.Popen(self.program_path, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate(input=input_data)
        return process.returncode, stdout, stderr