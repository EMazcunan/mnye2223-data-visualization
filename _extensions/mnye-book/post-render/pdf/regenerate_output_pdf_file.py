import os
import utils

if ".pdf" in os.getenv("QUARTO_PROJECT_OUTPUT_FILES"): 
    utils.regenerate_output_pdf_file()