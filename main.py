from core.processor import process
from core.file_discovery import get_pdf_files

path = input("PDF or folder:").strip().strip('"')
recursive = (input("recursive? (y/n):").strip().lower()=="y")
regex_pattern = input("regex (blank = none):").strip()
if regex_pattern == "":
    regex_pattern = None

pdfs = get_pdf_files(path, recursive)
print(f"Found {len(pdfs)} PDF(s)")
outputs =  process(pdfs,regex_pattern)

for output in outputs:
    print(output)