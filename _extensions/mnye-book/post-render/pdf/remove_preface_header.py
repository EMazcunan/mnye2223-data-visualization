import os
import utils

# Para PDF ignorar las cabeceras de la sección de  index.qmd de etiqueta `#preface`
# https://github.com/quarto-dev/quarto-cli/issues/2770
# https://github.com/quarto-dev/quarto-cli/issues/1108

def to_remove(line):
    result = False
    to_remove_keys = [
      "\\hypertarget{sec-preface}", 
      "\\label{sec-preface}"
    ]
    for key in to_remove_keys:
      if key in line:
         result = True
    return result

def lines_without_preface_header(tex_file):
    lines = []
    with open(tex_file, encoding="utf8") as f:
        for old_line in f:
            if not to_remove(old_line):
                lines.append(old_line)
    return lines


def remove_preface_header(tex_file):
    lines = lines_without_preface_header(tex_file)
    utils.replace_lines(tex_file, lines)

if ".pdf" in os.getenv("QUARTO_PROJECT_OUTPUT_FILES"):
    tex_file = utils.tex_file()
    remove_preface_header(tex_file) # path relativo al proyecto, no a este script