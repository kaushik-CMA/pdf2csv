from pathlib import Path
from core.pdf_loader import extract_text
from core.normalizer import normalize
from exporters.csv_exporter import export_csv
from core.regex_filter import filter_lines

def process(pdf_files, regex_pattern=None):

    output =  []
    for pdf_file in pdf_files:
        text = extract_text(pdf_file)
        normalized_text = normalize(text)
        print("before:", len(normalized_text))
        normalized_text = filter_lines(normalized_text, regex_pattern)
        print("after:", len(normalized_text))
        output_file = pdf_file.with_suffix(".csv")
        export_csv(normalized_text, output_file)
        output.append(output_file)

    return output