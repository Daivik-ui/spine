# SPINE

> A modular Python-based document conversion engine for converting multiple file formats into PDF through a clean and extensible CLI architecture.

---

## Features

- Convert multiple file formats to PDF
- Modular converter-based architecture
- Clean CLI interface
- Automatic logging system
- Organized project structure
- Easy to extend with new converters
- Batch-processing ready architecture

---

## Supported Conversions

| Input Format | Output Format |
|-------------|---------------|
| `.docx`     | PDF           |
| `.txt`      | PDF           |
| `.pptx`     | PDF           |
| `.jpg`      | PDF           |
| `.png`      | PDF           |

---

## Project Structure

```bash
SPINE/
│
├── spine/
│   ├── cli/
│   │   └── main.py
│   │
│   ├── converters/
│   │   ├── base.py
│   │   ├── word_to_pdf.py
│   │   ├── txt_to_pdf.py
│   │   ├── pptx_to_pdf.py
│   │   ├── jpg_to_pdf.py
│   │   └── png_to_pdf.py
│   │
│   ├── utils/
│   │   ├── logger.py
│   │   └── file_utils.py
│   │
│   └── main.py
│
├── test/
├── logs/
├── output/
├── requirements.txt
├── setup.py
└── .gitignore
```

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/your-username/SPINE.git
cd SPINE
```

### Create Virtual Environment

```bash
python -m venv env
```

### Activate Environment

#### Windows

```bash
env\Scripts\activate
```

#### Linux / MacOS

```bash
source env/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Usage

### Basic Usage

```bash
python main.py
```

### Example Conversion

```bash
spine convert sample.docx
```

### Output

Converted files are automatically saved inside:

```bash
/output
```

Logs are generated inside:

```bash
/logs
```

---

## Architecture

SPINE follows a modular converter-based architecture.

Each file format has:
- its own converter module
- isolated conversion logic
- reusable utility support

This makes the system:
- scalable
- maintainable
- easy to extend

---

## Logging System

SPINE automatically generates detailed logs containing:
- conversion timestamps
- conversion status
- file information
- execution details

---

## Future Improvements

- Batch conversion support
- Drag-and-drop GUI
- Web-based interface
- API support using FastAPI
- Docker support
- Async conversion pipeline
- OCR support
- Cloud storage integration

---

## Why SPINE?

Most beginner converter projects are tightly coupled and difficult to scale.

SPINE focuses on:
- modular engineering
- clean architecture
- maintainability
- extensibility

instead of just “making conversion work”.

---

## Tech Stack

- Python
- Pillow
- python-docx
- reportlab
- python-pptx

---

## Contributing

Contributions are welcome.

If you'd like to improve SPINE:
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Open a pull request

---

## License

This project is licensed under the MIT License.

---

## Author

**Daivik Jain**

- Python Developer
- Generative AI Mentor
- Backend & AI Enthusiast

---
