from game.clear_screen import clear_screen
import time


def print_question(state: str, attempts_left: int) -> None:
  '''
  This method prints the question in a fancy way.
  '''
  clear_screen()
  print("****************************************************")
  print("              Guess the Capital               ")
  print("****************************************************\n")
  print(f"ATTEMPTS LEFT: {attempts_left}\n")
  print(f"What is the capital of {state}?")


def print_congratulations(state: str, capital: str) -> None:
  '''
  This method just prints a fancy congralutory message
  '''
  clear_screen()
  print("*****************************************************")
  print("*             Congratulations!                       *")
  print("*****************************************************")
  print("     ___________      ___________      ___________    ")
  print("    '._==_==_=_.'    '._==_==_=_.'    '._==_==_=_.'   ")
  print("    .-\:      /-.    .-\:      /-.    .-\:      /-.   ")
  print("   | (|:.     |) |  | (|:.     |) |  | (|:.     |) |  ")
  print("    '-|:.     |-'    '-|:.     |-'    '-|:.     |-'   ")
  print("      \::.  . /        \::.  . /        \::.  . /     ")
  print("       '::::'          '::::'          '::::'        ")
  print(f"   You guessed it! {capital} is the capital of {state}.")
  time.sleep(1)
  print("        You're a geography whiz!")
  time.sleep(1)
  print("          Keep up the great work!")
  time.sleep(1)
  print("*****************************************************\n")


def print_loss_message(answer: str) -> None:
  '''
  This method just prints a fancy You lost message.
  '''
  clear_screen()
  print("*****************************************************")
  print("*                  Oh no! You lost.                  *")
  print("*****************************************************")
  print("         ___     .-''''-.       ___        ")
  print("       .'  /    /  _    \    \   \      ")
  print("      /   /    |  / \   |    \   \     ")
  print("     /   /     |  \_/   |     \   \    ")
  print("    /   /      `._____.'      \   \   ")
  print("   /   /       .       .       \   \  ")
  print("  /   /       /         \       \   \ ")
  print(" /   /       /           \       \   \ ")
  print("`--'       /_____________\       `--'")
  print(f"  The correct answer was {answer}. Better luck next time!")
  time.sleep(1)
  print("                  Don't give up!")
  time.sleep(1)
  print("*****************************************************\n")
