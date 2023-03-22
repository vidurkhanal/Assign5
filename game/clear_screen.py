import os


def clear_screen() -> None:
  '''
  This method clears the terminal screen.
  '''
  if os.name == "nt":
    os.system("cls")
  else:
    os.system("clear")
