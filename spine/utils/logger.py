# === spine/utils/logger.py ===
import os
from datetime import datetime

class Logger:
    def __init__(self):
        self.logs = []
        self.start_time = datetime.now()
        self.timestamp_str = self.start_time.strftime("%Y-%m-%d %H:%M:%S")
        self.filename = f"log_{self.start_time.strftime('%Y-%m-%d_%H-%M-%S')}.txt"

    def log(self, message):  # Generic log method
        print(message)
        self.logs.append(message)

    def log_conversion(self, input_file, output_file, duration):
        try:
            size_kb = os.path.getsize(output_file) / 1024
        except OSError:
            size_kb = 0
        message = (
            f"🗂️ Source File : {input_file}\n"
            f"📄 Output File : {output_file}\n"
            f"📦 Size        : {size_kb:.2f} KB\n"
            f"⏱️ Time Taken  : {duration:.2f} seconds\n"
            f"{'='*50}"
        )
        self.log(message)

    def log_error(self, message):
        self.log(f"❌ ERROR: {message}\n{'='*50}")

    def save(self, path="logs"):
        os.makedirs(path, exist_ok=True)
        full_path = os.path.join(path, self.filename)
        with open(full_path, "w", encoding="utf-8") as f:
            f.write("==== SPINE FILE CONVERTER LOG ====\n")
            f.write(f"🕒 Date: {self.timestamp_str}\n")
            f.write("=" * 50 + "\n\n")
            for entry in self.logs:
                f.write(entry + "\n")
        print(f"\n📁 Log saved at: {full_path}")
