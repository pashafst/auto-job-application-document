#!/usr/bin/python3
import PyPDF2
import argparse

"""
autoBewerbungData
=================

Tool to Auto Complete my Bewerbung for job.

TODO:
    - Add feature
        - Edit template Latex file, add the name of job.
"""
# constants
OUTPUT_FILE_DEFAULT = "bewerbung.pdf"

def create_merged_pdf(files, output_file):
    print("Creating merged pdf...")
    merger = PyPDF2.PdfFileMerger() 
    for file in files:
        merger.append(file)
    merger.write(output_file)

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('pdf_file', nargs='+')
    parser.add_argument('-f','--output',help="Name of Output file.")
    return parser.parse_args()

def check_files(files):
    print("Checking files' extension...")
    for file in files:
        if not file.endswith(".pdf"):
            raise Exception("Must be a pdf file!")

def main():
    args = parse_args()
    files = args.pdf_file
    output_file = args.output if args.output is not None else OUTPUT_FILE_DEFAULT
    check_files(files)
    create_merged_pdf(files, output_file)
    print("New PDF created.")

if __name__ == "__main__":
    main()
