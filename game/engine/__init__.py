import random
from game.engine.printers import print_question
from utils.parser import parse_answer


def run(question_answer_dictionary: dict) -> (bool, str):
  '''
  This method is the engine of the game. It gives user the ability to type their responses.
  '''

  TOTAL_ATTEMPTS = 3
  STATE = random.choice(list(question_answer_dictionary.keys()))
  CAPITAL = question_answer_dictionary[STATE]

  for current_attempt in range(TOTAL_ATTEMPTS):
    print_question(STATE, TOTAL_ATTEMPTS - current_attempt)
    answer = input(">> ")
    parsed_answer = parse_answer(answer)
    if parsed_answer == CAPITAL:
      return (True, STATE)
  return (False, STATE)
