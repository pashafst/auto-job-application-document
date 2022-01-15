# auto-job-application-document

Automate the creation of Job Application Document

## Recommended Formats
1. Resume
2. Motivation Letter
3. Extras

## Dependencies
PyPDF2

`pip install PyPDF2`

pdflatex

## How to use

`main.py [-h] [-o OUTPUT] [--latex-file LATEX_FILE] [--job-name JOB_NAME] pdf_file [pdf_file ...]`

`LATEX_FILE` specifies your Motivation Letter latex file.

`JOB_NAME` replaces xxJOBNAMExx from your template motivation letter latex file.
