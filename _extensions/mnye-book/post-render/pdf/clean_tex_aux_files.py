import os
import utils

if ".pdf" in os.getenv("QUARTO_PROJECT_OUTPUT_FILES") and os.getenv("QUARTO_PROJECT_RENDER_ALL") == 1:
    utils.clean_tex_aux_files()