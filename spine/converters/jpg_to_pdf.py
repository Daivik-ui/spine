import os
import time
from PIL import Image, UnidentifiedImageError

class JPGToPDFConverter:
    def __init__(self, input_files, output_folder, logger):
        self.input_files = input_files
        self.output_folder = output_folder
        self.logger = logger

    def convert(self):
        success = True
        for file in self.input_files:
            if not os.path.exists(file):
                self.logger.log_error(f"File not found: {file}")
                success = False
                continue
            try:
                start = time.time()

                image = Image.open(file)
                output_file = os.path.join(
                    self.output_folder, os.path.splitext(os.path.basename(file))[0] + ".pdf"
                )
                image.convert("RGB").save(output_file)

                end = time.time()
                self.logger.log_conversion(file, output_file, end - start)

            except (FileNotFoundError, OSError, UnidentifiedImageError) as e:
                self.logger.log_error(f"Failed to convert {file}: {e}")
                success = False
        return success
