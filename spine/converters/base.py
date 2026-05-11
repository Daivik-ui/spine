from abc import ABC, abstractmethod

class FileConverter(ABC):
    def __init__(self, input_paths, output_folder):
        self.input_paths = input_paths
        self.output_folder = output_folder

    @abstractmethod
    def convert(self):
        pass
