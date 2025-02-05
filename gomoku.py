def init_board():
    """Initializes the game board as a 2D array with user-defined 
    dimensions. Each cell is initially set to None.

    Returns:
        list: A 2D list representing the empty game board.
    """

    initialized = False
    while(initialized == False):
        column_input = input("Enter the numbers of columns (< 100): ")
        row_input = input("Enter the numbers of rows (< 100): ")
        try:
            num_columns = int(column_input)
            num_rows = int(row_input)
            if(
                num_columns > 0 and 
                num_columns < 100 and 
                num_rows > 0 and
                num_rows < 100
                ):
                initialized = True
            else:
                print("Invalid Input! Try Again.")

        except ValueError:
            print("Type in numbers please!")

    board = []
    for _ in range(num_rows):
        board.append([None] * num_columns)
    return board


def get_column_label(board):
    """Generates column labels based on the board size for display
    purposes.
    
    Args:
        board (list): The current state of the game board.

    Returns:
        list: A list containing the formatted column labels.
    """
    column_label = ["     ", "     ", "   +-"]
    for index, _ in enumerate(board[0]):
        if(index < 10):
            column_label[0] += "  "
        else:
            column_label[0] += str(index // 10) + " "
        column_label[1] += str(index % 10) + " "
        column_label[2] += "--"

    column_label[2] += "+"
    return column_label
 


def print_board(board, column_label):
    """Displays the current game board with column and row indices.
    
    Args:
        board (list): The current state of the game board.
        column_label: The column labels including the indices in multiple rows and the upper and downer border
    """
    print(
        str(column_label[0]) + 
        "\n" + 
        str(column_label[1]) + 
        "\n" + 
        str(column_label[2])
        )
    for index, row in enumerate(board):
        row_string = ""
        if(index < 10):
            row_string += " "
        row_string += str(index) + " | "
        for cell in row:
            if(cell is None):
                row_string += ". "
            else:
                row_string += str(cell) + " "
        print(row_string + "|")

    print(column_label[2] + "\n")


def player_move(player, board):
    """Prompts the current player to enter a move (row and column).
    Validates the input to ensure it's within bounds and the selected 
    cell is empty. Only numeric input is accepted.
    
    Args:
        player (str): The current player's symbol ("X" or "O").
        board (list): The current game board.

    Returns:
        list: The coordinates of the selected move as [row, column].
    """
    validation = False
    print(
        "Player " + 
        str(player) + 
        " it's your turn!"
        )
    while(validation == False):
        column_input = input("Enter the column: ")
        row_input = input("Enter the row: ")
        try:
            column = int(column_input)
            row = int(row_input)
            if(
                column >= 0 and 
                column < len(board[0]) and 
                row >= 0 and 
                row < len(board) and 
                board[row][column] == None):
                validation = True
            else:
                print("Invalid Input! Try Again.")

        except ValueError:
            print("Type in numbers please!")
    board[row][column] = str(player)

    return [row, column]


def win_detection(last_move, player, board):
    """Checks if the current player has won forming a sequence of
    at least five consecutive pieces in a row, column, or diagonal.
    
    Args:
        last_move (list): The coordinates [row, column] of the last move.
        player (str): The current player's symbol.
        board (list): The game board.

    Returns:
        list or None: If a win is detected, returns the start and end 
        coordinates of the winning sequence. Otherwise, returns None.
    """

    # Check for horizontal winning condition
    consecutive_pieces = 1
    lowest_row = last_move[0]
    highest_row = last_move[0]
    column = last_move[1]

    while(
        lowest_row - 1 >= 0 and 
        board[lowest_row - 1][column] == player
        ):
        lowest_row -= 1
        consecutive_pieces += 1

    while(
        highest_row + 1 < len(board) and 
        board[highest_row + 1][column] == player
        ):
        highest_row += 1
        consecutive_pieces += 1

    if(consecutive_pieces >= 5):
        return [
            [lowest_row, column],
            [highest_row, column]]
    
    # Check for vertical winning condition
    consecutive_pieces = 1
    row = last_move[0]
    lowest_column = last_move[1]
    highest_column = last_move[1]

    while(
        lowest_column - 1 >= 0 and 
        board[row][lowest_column - 1] == player
        ):
        lowest_column -= 1
        consecutive_pieces += 1
    
    while(
        highest_column + 1 < len(board[0]) and 
        board[row][highest_column + 1] == player
        ):
        highest_column += 1
        consecutive_pieces += 1

    if(consecutive_pieces >= 5):
        return [[row, lowest_column], [row, highest_column]]
    
    # Check for diagonal downwards winning condition
    consecutive_pieces = 1
    lowest_row = last_move[0]
    highest_row = last_move[0]
    lowest_column = last_move[1]
    highest_column = last_move[1]

    while(
        lowest_row - 1 >= 0 and 
        lowest_column - 1 >= 0 and 
        board[lowest_row - 1][lowest_column - 1] == player
        ):
        lowest_row -= 1
        lowest_column -= 1
        consecutive_pieces += 1

    while(
        highest_row + 1 < len(board) and 
        highest_column + 1 < len(board[0]) and 
        board[highest_row + 1][highest_column + 1] == player
        ):
        highest_row += 1
        highest_column += 1
        consecutive_pieces += 1

    if(consecutive_pieces >= 5):
        return [
            [lowest_row, lowest_column],
            [highest_row, highest_column]
            ]
    
    # Check for diagonal upwards winning condition
    consecutive_pieces = 1
    lowest_row = last_move[0]
    highest_row = last_move[0]
    lowest_column = last_move[1]
    highest_column = last_move[1]

    while(
        lowest_row - 1 >= 0 and 
        highest_column + 1 < len(board[0]) and 
        board[lowest_row - 1][highest_column + 1] == player
        ):
        lowest_row -= 1
        highest_column += 1
        consecutive_pieces += 1

    while(
        highest_row + 1 < len(board) and 
        lowest_column - 1 >= 0 and 
        board[highest_row + 1][lowest_column - 1] == player
        ):
        highest_row += 1
        lowest_column -= 1
        consecutive_pieces += 1

    if(consecutive_pieces >= 5):
        return [
            [lowest_row, highest_column],
            [highest_row, lowest_column]
            ]
    
    return None


def main():
    """Controls the game flow by managing turns and checking for a winner.
    The game continues until a player wins or the board is full (tie).
    """
    player = "X"
    turn_count = 0
    game_over = False
    board = init_board()
    column_label = get_column_label(board)

    while(game_over == False):
        turn_count += 1
        print_board(board, column_label)
        last_move = player_move(player, board)
        if(turn_count > len(board) * len(board[0])):
            print("TIE!")
            game_over = True
        if(turn_count >= 9):
            streak = win_detection(last_move, player, board)
            if(streak != None):
                game_over = True
                print_board(board, column_label)
                print(
                    player + 
                    " wins! (" + 
                    str(streak[0][0]) + 
                    "," + 
                    str(streak[0][1]) + 
                    " to " + 
                    str(streak[1][0]) + 
                    "," + 
                    str(streak[1][1]) + 
                    ")"
                    )
        if(player == "X"):
            player = "O"
        else:
            player = "X"


main()