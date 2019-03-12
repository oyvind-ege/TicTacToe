class InputHandler:
    def __init__(self, helper_board, game_board):
        self.helper_board = helper_board
        self.game_board = game_board

    def fetch_input(self, player):
        while 1:
            print("------------------------")
            print("Player ", player, " - it is your turn.\n")
            choice = input("Please type in a number between 1 and 9, then hit Enter.\nIf you give up, type 'surrender'.\nType 'help' to see what the numbers mean.\n\nYour choice: ")
            try:
                if choice == 'help':
                    self.help_message()
                    continue
                elif choice == 'surrender':
                    print("\nPlayer ", player, " surrenders!\nAll hail the victor!\n\n")
                    return -1
                elif int(choice) in range(1, 10):
                    return choice
            except ValueError:
                print("Invalid input.")

    
    def get_player_choice(self, player) -> 'tuple':
        """This method transforms the numeric choice from fetch_input() into a x,y coordinate on the game board."""

        numeric_choice = self.fetch_input(player)

        if numeric_choice == '1':
            return (0,0)
        elif numeric_choice == '2':
            return (2, 0)
        elif numeric_choice == '3':
            return (4, 0)
        
        elif numeric_choice == '4':
            return (0, 2)
        elif numeric_choice == '5':
            return (2, 2)
        elif numeric_choice == '6':
            return (4, 2)
        
        elif numeric_choice == '7':
            return (0, 4)
        elif numeric_choice == '8':
            return (2, 4)
        elif numeric_choice == '9':
            return (4, 4)
        
        else:
            return numeric_choice

    def help_message(self):
        """This function prints the helper board to the terminal."""
        print("\nThe numbers 1-9 correspond to these slots on the board:")
        self.helper_board.draw()
        print("The board currently looks like this:")
        self.game_board.draw()
        print("\nSo, what's your move?\n\n")