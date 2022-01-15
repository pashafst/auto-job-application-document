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

`OUTPUT` is the name of the desired output pdf file name.

`LATEX_FILE` specifies your Motivation Letter latex file.

`JOB_NAME` replaces xxJOBNAMExx from your template motivation letter latex file.

`pdf_file` is your pdf documents that you wish to merge together.

The program merges your pdf files to one pdf. if `LATEX_FILE` is specified, it will make pdf from it and merges to the ouput pdf on second page (used for your motivation letters). If you have a template latex file, use `JOB_NAME` to replace xxJOBNAMExx in your `LATEX_FILE`.

## Template Latex File

Variables:
- xxJOBNAMExx
