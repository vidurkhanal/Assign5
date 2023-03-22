from game.welcome_screen import print_welcome_screen
from utils.csv_to_dict import load
from game.engine import run as run_game
from game.engine.printers import print_congratulations, print_loss_message


def main() -> None:
  state_capital_dict = dict()
  load(dictionary_to_load=state_capital_dict, file_path="state_capitals.csv")
  print_welcome_screen()
  while 1:
    has_won, state = run_game(question_answer_dictionary=state_capital_dict)
    if has_won:
      print_congratulations(state, state_capital_dict[state])
    else:
      print_loss_message(state_capital_dict[state])

    print("Do you want to continue playing...")
    user_input = input("Press Y to keep playing.")
    if user_input.strip().lower() != "y":
      break


main()
