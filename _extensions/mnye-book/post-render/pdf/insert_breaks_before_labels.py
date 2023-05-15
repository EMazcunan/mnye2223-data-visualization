import os

import utils


def lines_with_breaks_before_labels(tex_file):
  lines = []
  trigger = "\\protect\\hypertarget"
  with open(tex_file, encoding="utf8") as f:
    for old_line in f:
      if trigger in old_line and not old_line.lstrip(' ').startswith(trigger):
        old_line_before, old_line_after = old_line.split(trigger)
        lines.append(old_line_before + "% \n")
        lines.append(trigger + old_line_after.split("\n")[0] + "%\n")  
      else:
          lines.append(old_line)
  return lines


def insert_breaks_before_labels(tex_file):
  new_lines = lines_with_breaks_before_labels(tex_file)
  utils.replace_lines(tex_file, new_lines)

if ".pdf" in os.getenv("QUARTO_PROJECT_OUTPUT_FILES"):
  tex_file = utils.tex_file()
  insert_breaks_before_labels(tex_file) # path relativo al proyecto, no a este script



