def load(dictionary_to_load: dict, file_path: str) -> None:
  '''
    This function loads the csv data into native python dictionary.
  '''
  with open("state_capitals.csv") as data:
    for line in data:
      state, capital = line.split(",")
      dictionary_to_load[state] = capital.split('\n')[0]