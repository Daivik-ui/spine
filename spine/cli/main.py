# === cli/main.py ===
import argparse
import os
from ..converters.jpg_to_pdf import JPGToPDFConverter
from ..converters.word_to_pdf import WordToPDFConverter
from ..converters.png_to_pdf import PNGToPDFConverter
from ..converters.pptx_to_pdf import PPTXToPDFConverter
from ..converters.txt_to_pdf import TXTToPDFConverter
from spine.utils.logger import Logger



def convert_files(file_type, files, output):
    logger = Logger()

    if not files or not output:
        logger.log_error("Please provide both --files and --output.")
        logger.save()
        return

    if not os.path.exists(output):
        logger.log_error(f"Output folder '{output}' does not exist.")
        logger.save()
        return

    converters = {
        "jpg": JPGToPDFConverter,
        "word": WordToPDFConverter,
        "png": PNGToPDFConverter,
        "pptx": PPTXToPDFConverter,
        "txt": TXTToPDFConverter
    }

    converter_class = converters.get(file_type)

    if not converter_class:
        logger.log_error("Unsupported file type. Use one of: jpg, word, png, pptx, txt")
        logger.save()
        return

    converter = converter_class(files, output, logger)
    success = converter.convert()

    if success:
        logger.log("✅ All files converted successfully!")
    else:
        logger.log("⚠️ Some files failed to convert. Check log for details.")

    logger.save()


def run_cli():
    parser = argparse.ArgumentParser(description="📁 SPINE File Converter CLI Tool")
    subparsers = parser.add_subparsers(dest="command", help="Commands")

    convert_parser = subparsers.add_parser("convert", help="Convert files to PDF")
    convert_parser.add_argument("--type", required=True, choices=["jpg", "word", "png", "pptx", "txt"], help="Type of file to convert")
    convert_parser.add_argument("--files", nargs="+", required=True, help="List of files to convert")
    convert_parser.add_argument("--output", required=True, help="Output folder")

    args = parser.parse_args()

    if args.command == "convert":
        convert_files(args.type, args.files, args.output)
    else:
        parser.print_help()


if __name__ == "__main__":
    run_cli()
