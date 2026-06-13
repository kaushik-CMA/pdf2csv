import csv

# This function takes a list of lines and an output file path, and writes the lines to a CSV file.
def export_csv(lines, output_file):
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        for line in lines:
            writer.writerow([line])