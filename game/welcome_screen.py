from game.clear_screen import clear_screen


def print_welcome_screen() -> None:
  '''
  Clears the terminal screen and prints a fancy welcome banner.
  '''
  clear_screen()
  print("""
    
 __    __    ___  _        __   ___   ___ ___    ___ 
|  |__|  |  /  _]| |      /  ] /   \ |   |   |  /  _]
|  |  |  | /  [_ | |     /  / |     || _   _ | /  [_ 
|  |  |  ||    _]| |___ /  /  |  O  ||  \_/  ||    _]
|  `  '  ||   [_ |     /   \_ |     ||   |   ||   [_ 
 \      / |     ||     \     ||     ||   |   ||     |
  \_/\_/  |_____||_____|\____| \___/ |___|___||_____|
                                                     

                       
            Welcome to Guess The State Capital!           
      Can you guess the captial of all 50 US states? 

           
""")
  input("Press any key to continue...")
