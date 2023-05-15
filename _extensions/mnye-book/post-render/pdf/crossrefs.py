import os

import utils

# Para PDF hacer que los links incluyan el prefijo.
# Por ejemplo: "Ejercicio \ref{exr-label}" -> \exref{exr-label}.
# https://github.com/quarto-dev/quarto-cli/issues/2770
# https://github.com/quarto-dev/quarto-cli/issues/1108


def crossref_dict(): 
    """Diccionario con comando y prefijo para cada tipo de referencia.
    Las claves del diccionario son los prefijos de las etiquetas, ej. `thm`.
    Los valores son un diccionario con el nombre del comando, ej. `thmref`, y el prefijo, ej. "Teorema".

    Returns:
        dict: Diccionario con comando y prefijo para cada tipo de referencia.
    """
    # Inicializamos el diccionario con los nombres de los comandos
    crossref = {
        "fig": {"csname": "figref"}, 
        "tbl": {"csname": "tblref"}, 
        "sec": {"csname": "secref"},
        "thm": {"csname": "thmref"},
        "def": {"csname": "defref"},
        "exr": {"csname": "exrref"},
        "exm": {"csname": "exmref"},
    }

    # Inicializamos el diccionario con los prefijos
    metadata = utils.mnye_metadata()
    crossref_metadata = metadata["contributes"]["project"]["crossref"]
    for label_prefix in crossref:
        metadata_key = label_prefix + "-prefix"
        if metadata_key in crossref_metadata:
            crossref[label_prefix]["prefix"] = crossref_metadata[metadata_key]
            
    return crossref 

def prettify_line_refs(line, dict = crossref_dict()):
   for label_prefix in dict:
       prefix = dict[label_prefix]["prefix"]
       fragment = prefix + "~\\ref" 
       if fragment in line:
           csname = dict[label_prefix]["csname"]
           new_fragment = "\\" + csname
           line = new_fragment.join(line.split(fragment))
   return line

def prettify_refs(tex_file):
    lines = []
    dict = crossref_dict()
    with open(tex_file, encoding="utf8") as f:
        for old_line in f:
            new_line = prettify_line_refs(old_line, dict)
            lines.append(new_line)
    utils.replace_lines(tex_file, lines)
  

if ".pdf" in os.getenv("QUARTO_PROJECT_OUTPUT_FILES"):
    tex_file = utils.tex_file() # path relativo al proyecto, no a este script
    prettify_refs(tex_file) 

