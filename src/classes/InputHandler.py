class InputHandler:
    def __init__(self, helper_board, board):
        self.helper_board = helper_board
        self.board = board

    def fetch_input(self, player):
        while 1:
            choice = input("Your choice: ")
            try:
                if choice == 'help':
                    self.help_message()
                    continue
                elif choice == 'surrender':
                    print("\nPlayer ", player, " surrenders!\nAll hail the victor!\n\n")
                    return 'surrender'
                elif int(choice) in range(1, 10):
                    return choice
            except ValueError:
                print("Invalid input.")

    
    def input_string_to_coordinates(self, player, input_string):
        """This method transforms a numeric string choice (1-10) into a x,y coordinate on the game board."""

        if input_string == '1':
            return (0,0)
        elif input_string == '2':
            return (2, 0)
        elif input_string == '3':
            return (4, 0)
        
        elif input_string == '4':
            return (0, 2)
        elif input_string == '5':
            return (2, 2)
        elif input_string == '6':
            return (4, 2)
        
        elif input_string == '7':
            return (0, 4)
        elif input_string == '8':
            return (2, 4)
        elif input_string == '9':
            return (4, 4)

    def get_player_choice(self, player):
        """Get input from the player; ensure the chosen spot has not been taken; return coordinates of valid spot."""
        
        print("Please type in a number between 1 and 9, then hit Enter.\nIf you give up, type 'surrender'.\nType 'help' to see what the numbers mean.\n\n")

        while 1:

            input_string = self.fetch_input(player) #Raw string input from player

            if input_string == 'surrender':
                return input_string

            choice_x, choice_y = self.input_string_to_coordinates(player, input_string) #Raw string has been transformed into a tuple (x,y)

            if self.board.game_board[choice_y][choice_x] != ' ': #If the chosen spot is not empty
                print("\n\t Spot already taken! Try again.\n")
                continue
            else:
                return (choice_x, choice_y)



    def help_message(self):
        """This function prints the helper board to the terminal."""
        print("\nThe numbers 1-9 correspond to these slots on the board:")
        self.helper_board.draw()
        print("The board currently looks like this:")
        self.board.draw()
        print("\nSo, what's your move?\n\n")