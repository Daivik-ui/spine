import os
import time
import comtypes.client

class PPTXToPDFConverter:
    def __init__(self, input_files, output_folder, logger):
        self.input_files = input_files
        self.output_folder = output_folder
        self.logger = logger

    def convert(self):
        success = True
        try:
            powerpoint = comtypes.client.CreateObject("Powerpoint.Application")
            powerpoint.Visible = 1
        except Exception as e:
            self.logger.log_error(f"Could not start PowerPoint application: {e}")
            return False

        for file in self.input_files:
            if not os.path.exists(file):
                self.logger.log_error(f"File not found: {file}")
                success = False
                continue
            try:
                start = time.time()

                output_file = os.path.join(
                    self.output_folder,
                    os.path.splitext(os.path.basename(file))[0] + ".pdf"
                )

                presentation = powerpoint.Presentations.Open(file, WithWindow=False)
                presentation.SaveAs(output_file, 32)  # 32 = PDF format
                presentation.Close()

                end = time.time()
                self.logger.log_conversion(file, output_file, end - start)

            except Exception as e:
                self.logger.log_error(f"Failed to convert {file}: {e}")
                success = False

        powerpoint.Quit()
        return success
