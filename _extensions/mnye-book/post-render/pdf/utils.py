import os
import yaml
import subprocess
import shutil


def quarto_metadata():
    # Read _quarto.yml
    with open("_quarto.yml", mode='r', encoding="utf8") as stream:
        metadata = yaml.safe_load(stream)
    return metadata

def mnye_metadata():
    # Read _extension.yml
    with open(os.path.join("_extensions", "mnye-book", "_extension.yml"), mode='r', encoding="utf8") as stream:
        metadata = yaml.safe_load(stream)
    return metadata

def quarto_book_output_file():
    """Obtener valor del campo `book.output_file` en el archivo `_quarto.yml`

    Returns:
        string: valor de `book.output_file`
    """
    metadata = quarto_metadata()
    return metadata["book"]["output-file"]

def output_dir():
    return os.getenv("QUARTO_PROJECT_OUTPUT_DIR")


def tex_file():
    book_output_file = quarto_book_output_file()
    return book_output_file + ".tex"

def pdf_file():
    book_output_file = quarto_book_output_file()
    return book_output_file + ".pdf"


def output_pdf_file():
    output_dir_ = output_dir()
    book_output_file = quarto_book_output_file()
    pdf_file_name = book_output_file + ".pdf"
    return os.path.join(output_dir_, pdf_file_name)

def recompile_tex():
    tex_file_ = tex_file()
    book_output_file = quarto_book_output_file()
    subprocess.run(f"pdflatex -halt-on-error -interaction=nonstopmode -file-line-error -shell-escape {tex_file_}", shell=True)
    subprocess.run(f"biber {book_output_file}", shell=True)
    subprocess.run(f"pdflatex -halt-on-error -interaction=nonstopmode -file-line-error -shell-escape {tex_file_}", shell=True)

def move_pdf_file_to_output_dir():
    
    output_pdf_file_ = output_pdf_file()
    if os.path.exists(output_pdf_file_):
        os.remove(output_pdf_file_)

    pdf_file_ = pdf_file()
    output_dir_ = output_dir()
    shutil.move(pdf_file_, output_dir_)

def regenerate_output_pdf_file():
    recompile_tex()
    move_pdf_file_to_output_dir()

def aux_files_exts():
    return ["aux", "auxlock", "bbl", "bcf", "blg", "log", "mw", "run.xml", "toc"]

def clean_tex_aux_files():
    book_output_file = quarto_book_output_file()
    for ext in aux_files_exts():
        book_aux_file = book_output_file + "." + ext    
        if os.path.exists(book_aux_file):
            os.remove(book_aux_file)
        index_aux_file = "index" + "." + ext    
        if os.path.exists(index_aux_file):
            os.remove(index_aux_file)

def replace_lines(path, lines): 
  with open(path, mode='w', encoding="utf8") as f:
    for line in lines:
        f.write(line)