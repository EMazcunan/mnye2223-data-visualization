import os

import utils

def lines_without_blank_lines_after_exercises(tex_file):
    lines = []
    prev_line = "foo"
    trigger = "\\protect\\hypertarget"
    with open(tex_file, encoding="utf8") as f:
        for old_line in f:
            if not(trigger in prev_line and old_line.lstrip(' ').startswith("\n")): 
                lines.append(old_line)
            prev_line = old_line
    return lines


def remove_blank_lines_before_exercises(tex_file):
    new_lines = lines_without_blank_lines_after_exercises(tex_file)
    utils.replace_lines(tex_file, new_lines)


if ".pdf" in os.getenv("QUARTO_PROJECT_OUTPUT_FILES"):
    tex_file = utils.tex_file()
    remove_blank_lines_before_exercises(tex_file) # path relativo al proyecto, no a este script
