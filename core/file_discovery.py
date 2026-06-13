from pathlib import Path

def get_pdf_files(path, recursive=False):
    path = Path(path)
    if path.is_file() and path.suffix.lower() == '.pdf':
        return [path]
    elif path.is_dir():
        if recursive:
            return list(path.rglob('*.pdf'))
        else:
            return list(path.glob('*.pdf'))
    else:
        return []