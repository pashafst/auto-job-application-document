#!/usr/bin/python3
import PyPDF2
import argparse
import os
import subprocess 
import glob

"""
auto_bewerbung.py
=================

Tool to Auto Complete my Bewerbung for job.

FORMAT:
    - Resume
    - Motivation Letter
    - Extras

TODO:
    - Add feature
        - Edit template Latex file, add the name of job.
"""
# constants
OUTPUT_FILE_DEFAULT = "bewerbung"
OUTPUT_PDF = "output"

def run_pdflatex(filename, output_dir):
    args = ["pdflatex", "-jobname", OUTPUT_PDF, '-interaction', 'nonstopmode', '-output-directory', output_dir, filename]
    process = subprocess.run(args, stdout=subprocess.DEVNULL)
    if process.returncode != 0:
        raise Exception("pdflatex error!")

def create_pdf_from_latex(filename):
    print("Creating pdf file from latex...")
    dir_name = os.path.dirname(filename)
    file_name = os.path.basename(filename)
    current_dir = os.getcwd()
    os.chdir(dir_name)
    run_pdflatex(file_name, current_dir)
    os.chdir(current_dir)
    return f"{OUTPUT_PDF}.pdf"

def create_merged_pdf(files, output_file):
    print("Creating merged pdf...")
    merger = PyPDF2.PdfFileMerger() 
    for file in files:
        merger.append(file)
    merger.write(output_file)
    print(f"PDF created: {output_file}")

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('pdf_file', nargs='+')
    parser.add_argument('-o','--output',help="Name of Output file.")
    parser.add_argument('--latex-file', help="Name of Latex file.")
    return parser.parse_args()

def check_files(files):
    print("Checking files' extension...")
    for file in files:
        if not file.endswith(".pdf"):
            raise Exception("Must be a pdf file!")

def clean_latex_output():
    outputs = glob.glob(f"{OUTPUT_PDF}.*")
    for file in outputs:
        os.remove(file)

def main():
    args = parse_args()
    files = args.pdf_file
    output_file = args.output if args.output is not None else OUTPUT_FILE_DEFAULT
    output_file+=".pdf"
    latex_file = args.latex_file
    check_files(files)
    if latex_file:
        files.insert(1, create_pdf_from_latex(latex_file))
    create_merged_pdf(files, output_file)
    clean_latex_output()

if __name__ == "__main__":
    main()
