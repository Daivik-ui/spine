import os
import time
from fpdf import FPDF

class TXTToPDFConverter:
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

                output_file = os.path.join(
                    self.output_folder,
                    os.path.splitext(os.path.basename(file))[0] + ".pdf"
                )

                pdf = FPDF()
                pdf.add_page()
                pdf.set_auto_page_break(auto=True, margin=15)
                pdf.set_font("Arial", size=12)

                with open(file, "r", encoding="utf-8") as f:
                    for line in f:
                        if line.strip() == "":
                            pdf.ln()
                        else:
                            pdf.multi_cell(0, 10, txt=line.strip())

                pdf.output(output_file)

                end = time.time()
                self.logger.log_conversion(file, output_file, end - start)

            except Exception as e:
                self.logger.log_error(f"Failed to convert {file}: {e}")
                success = False

        return success
