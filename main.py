import copy
import itertools

print("\nWelcome to Corey’s chess program! Please enter a string of legal moves in Algebraic Chess notation,")
print("and the program will output the resulting position. For additional instructions, see below:")
print("\n- This program can handle all chess moves that could be legal for some existing chess position.")
print("- Enter moves <chess location> to see the legal movements of the piece on <chess location>.")
print("- Moves may be entered omitting the numbers that represent move number.")
print("- Enter a chess location to see all of the legal movements of the piece")
print("- You may go back to a previous positions by repeatedly entering Undo.")
print("- To cycle between appearances of the chess board, press enter.")
print("- The program stops running at checkmate or stalemate.")

Files = ["a", "b", "c", "d", "e", "f", "g", "h"]
Ranks = ["1", "2", "3", "4", "5", "6", "7", "8"]

White_Pieces = ["P", "R", "N", "B", "Q", "K"]
Black_Pieces = ["p", "r", "n", "b", 'q', 'k']

Moves = {"R": [], "r": [], "N": [], "n": [], "B": [], "b": [], "Q": [], "q": [], "K": [], "k": [], "P": [], "p": []}

for i in range(1, 8):
    Moves["B"] += [(i, i), (i, -i), (-i, i), (-i, -i)]
    Moves["R"] += [(i, 0), (-i, 0), (0, i), (0, -i)]

Moves["Q"] = Moves["R"] + Moves["B"]
Moves["N"] = [(-1, 2), (1, 2), (-1, -2), (1, -2), (-2, 1), (2, 1), (-2, -1), (2, -1)]
Moves["P"], Moves["p"] = [(0, 1), (0, 2), (-1, 1), (1, 1)], [(0, -1), (0, -2), (-1, -1), (1, -1)]
Moves["K"] = Moves["B"][:4] + Moves["R"][:4]
Moves["r"], Moves["n"], Moves["b"], Moves["q"], Moves["k"] = Moves["R"], Moves["N"], Moves["B"], Moves["Q"], Moves["K"]

Minor_Pieces = ["N", "n", "B", "b"]
Major_Pieces = ["R", "r", "Q", "q"]


def get_board_squares():
    return [''.join(e) for e in itertools.product(Files, Ranks)]


def current_board(board_history):
    return board_history[-1]


def notation_cleaning(notation):
    return list(filter(lambda x : not x.strip(".").isnumeric(), notation.split(" ")))


def current_move_number(board_history):
    return len(board_history)-1


def is_white_turn(board_history):
    return True if current_move_number(board_history) % 2 == 0 else False


def piece_symbol(move, board_history):
    if move[0] not in ["R", "N", "B", "Q", "K"]:
        return "P" if is_white_turn(board_history) else "p"

    elif is_white_turn(board_history):
        return move[0]

    return move[0].lower()


def color(string, coloring):
    if coloring == 0:
        return "\033[1;37;40m" + string + "\033[0m"
    if coloring == 1:
        return "\033[1;30;47m" + string + "\033[0m"

    if coloring == 2:
        return "\033[1;37;40m" + string + "\033[0m"
    if coloring == 3:
        return "\033[7;31;40m" + string + "\033[0m"

    if coloring == 4:
        return "\033[1;37;40m" + string + "\033[0m"
    if coloring == 5:
        return "\033[7;32;40m" + string + "\033[0m"

    if coloring == 6:
        return "\033[1;37;40m" + string + "\033[0m"
    if coloring == 7:
        return "\033[7;33;40m" + string + "\033[0m"

    if coloring == 8:
        return "\033[1;37;40m" + string + "\033[0m"
    if coloring == 9:
        return "\033[7;34;40m" + string + "\033[0m"

    if coloring == 10:
        return "\033[1;37;40m" + string + "\033[0m"
    if coloring == 11:
        return "\033[7;35;40m" + string + "\033[0m"

    if coloring == 12:
        return "\033[1;37;40m" + string + "\033[0m"
    if coloring == 13:
        return "\033[7;36;40m" + string + "\033[0m"


def printer(board_history, color_scheme):
    board = current_board(board_history)

    print("")
    for rank in [8, 6, 4, 2]:
        print(str(rank) + " " +
            color(" " + board["a" + str(rank)] + " ", color_scheme) + color(" " + board["b" + str(rank)] + " ", color_scheme + 1) +
            color(" " + board["c" + str(rank)] + " ", color_scheme) + color(" " + board["d" + str(rank)] + " ", color_scheme + 1) +
            color(" " + board["e" + str(rank)] + " ", color_scheme) + color(" " + board["f" + str(rank)] + " ", color_scheme + 1) +
            color(" " + board["g" + str(rank)] + " ", color_scheme) + color(" " + board["h" + str(rank)] + " ", color_scheme + 1))

        print(str(rank - 1) + " " +
            color(" " + board["a" + str(rank - 1)] + " ", color_scheme + 1) + color(" " + board["b" + str(rank - 1)] + " ", color_scheme) +
            color(" " + board["c" + str(rank - 1)] + " ", color_scheme + 1) + color(" " + board["d" + str(rank - 1)] + " ", color_scheme) +
            color(" " + board["e" + str(rank - 1)] + " ", color_scheme + 1) + color(" " + board["f" + str(rank - 1)] + " ", color_scheme) +
            color(" " + board["g" + str(rank - 1)] + " ", color_scheme + 1) + color(" " + board["h" + str(rank - 1)] + " ", color_scheme))

    print("   ", end="")
    for i in range(8):
        print(Files[i], end="  ")
    print("\n")


# This function takes in a board dictionary, and returns the "reverse relation" dictionary.
def location_constructor(board):
    loc = {"P": [], "R": [], "N": [], "B": [], "Q": [], "K": [],
           "p": [], "r": [], "n": [], "b": [], "q": [], "k": [], " ": []}

    for rank in Ranks:
        for file in Files:
            loc[board[file + rank]].append(file + rank)

    return loc


def square_to_coords(square):
    return ord(square[0]) - 96, int(square[1])


# This function translates a square by (horizontal, vertical).
# If the square is off the board, return None.
def T(square, horizontal, vertical):
    if chr(ord(square[0]) + horizontal) + str(int(square[1]) + vertical) in get_board_squares():
        return chr(ord(square[0]) + horizontal) + str(int(square[1]) + vertical)


# This function converts two chess locations into coordinates.
# It then returns the tuple that is the difference of the corresponding entries.
def differ_coords(loc1, loc2):
    x1, y1 = square_to_coords(loc1)
    x2, y2 = square_to_coords(loc2)

    return x2 - x1, y2 - y1


def is_on_board(square, horizontal, vertical):
    return True if T(square, horizontal, vertical) is not None else False


# This function returns a direction vector encoding direction between two chess squares.
# If the locations are not aligned, then return "not aligned".
def get_direction(loc1, loc2):
    x1, y1 = square_to_coords(loc1)
    x2, y2 = square_to_coords(loc2)

    if abs(x1 - x2) != abs(y1 - y2) and abs(x1 - x2) != 0 and abs(y1 - y2) != 0:
        return "not aligned"

    d1 = 1 if x1 < x2 else -1 if x1 > x2 else 0
    d2 = 1 if y1 < y2 else -1 if y1 > y2 else 0

    return d1, d2


# This function returns the set of squares between two chess locations.
# If the locations are not aligned, then return "not aligned".
def squares_between(loc1, loc2):
    dir = get_direction(loc1, loc2)
    squares = []
    i = 1

    if dir == "not aligned":
        return []

    while T(loc1, dir[0]*i, dir[1]*i) != loc2:
        squares.append(T(loc1, dir[0]*i, dir[1]*i))
        i += 1

    return squares


def is_squares_between(loc1, loc2):
    return True if len(squares_between(loc1, loc2)) != 0 else False


# This function checks to see if the in between squares of two chess locations are unoccupied, or loc1 holds a knight.
# If the locations are not aligned, return "not aligned".
def is_clear_path(loc1, loc2, board_history):
    if loc1 is None or loc2 is None:
        return False

    board = current_board(board_history)
    x1, y1 = square_to_coords(loc1)
    x2, y2 = square_to_coords(loc2)

    if abs(x1 - x2) != abs(y1 - y2) and abs(x1 - x2) != 0 and abs(y1 - y2) != 0:
        return "not aligned"

    if board[loc1] in ["N", "n"]:
        return True

    for square in squares_between(loc1, loc2):
        if board[square] != " ":
            return False

    return True


# This function transports the mover's piece that's on previous, places it on destination, and
# then checks whether or not this puts the mover in check (hence the mutation of copies).
def oops_mover_check(previous, destination, board_history):
    board = current_board(board_history)
    board_copy = copy.deepcopy(board)
    board_history_copy = copy.deepcopy(board_history)
    board_history_copy[-1] = board_copy
    if previous is not None:
        board_copy[previous], board_copy[destination] = " ", board[previous]

    loc_copy = location_constructor(board_copy)

    if is_white_turn(board_history):
        king, attackers, dist = "K", ["r", "n", "b", "q", "p"], -1
    else:
        king, attackers, dist = "k", ["R", "N", "B", "Q", "P"], 1

    if board[destination] == king:
        return False

    for attacker in attackers:
        for attacker_location in loc_copy[attacker]:
            if attacker in ["P", "p"]:
                if not is_squares_between(attacker_location, loc_copy[king][0]):
                    if get_direction(attacker_location, loc_copy[king][0]) in [(1, dist), (-1, dist)]:
                        return True

            else:
                if is_clear_path(attacker_location, loc_copy[king][0], board_history_copy):
                    if differ_coords(attacker_location, loc_copy[king][0]) in Moves[attacker]:
                        return True

    return False


# This function determines whether or not there is a pawn on loc2 that a pawn on loc1 can en passant capture.
def can_en_passant(loc1, loc2, board_history):
    if len(board_history) < 2:
        return False

    dist = 1 if is_white_turn(board_history) else -1
    board = current_board(board_history)
    previous_board = board_history[-2]

    if board[loc1] not in ["P", "p"] or board[loc2] not in ["P", "p"]:
        return False

    if T(loc1, -1, 0) != loc2 and T(loc1, 1, 0) != loc2:
        return False

    if T(loc1, get_direction(loc1, loc2)[0], dist) != " ":
        return False

    if previous_board[loc2] in ["P", "p"] or board[T(loc2, 0, dist)] in ["P", "p"]:
        return False
    return True


# This function determines whether or not there is a pawn on square that can legally move two squares.
def can_push_twice(square, board_history):
    dist = 1 if is_white_turn(board_history) else -1
    board = current_board(board_history)
    movers_piece = piece_symbol(board[square], board_history)

    if movers_piece not in ["P", "p"]:
        return False

    if T(square, 0, 2 * dist) is None:
        return False

    if board[T(square, 0, dist)] != " " or board[T(square, 0, 2 * dist)] != " ":
        return False

    if oops_mover_check(square, T(square, 0, 2 * dist), board_history):
        return False
    return True


# This function returns the subset of the theoretical movements in which the piece on square can potentially move to.
def legal_movements(square, board_history):
    board = current_board(board_history)
    movers_piece = board[square]
    theoretical_movements = Moves[board[square]]
    legal_movements = []
    dist = 1 if is_white_turn(board_history) else -1
    enemy = Black_Pieces if is_white_turn(board_history) else White_Pieces

    for (x, y) in theoretical_movements:
        if movers_piece in ["P", "p"]:
            if not oops_mover_check(square, T(square, x, y), board_history):
                if (x, y) == (1, dist):
                    if can_en_passant(square, T(square, 1, 0), board_history) or board[T(square, 1, dist)] in enemy:
                        legal_movements.append((x, y))
                if (x, y) == (-1, dist):
                    if can_en_passant(square, T(square, -1, 0), board_history) or board[T(square, -1, dist)] in enemy:
                        legal_movements.append((x, y))
                if (x, y) == (0, dist):
                    if board[T(square, 0, dist)] == " ":
                        legal_movements.append((x, y))

        elif is_on_board(square, x, y) and is_clear_path(square, T(square, x, y), board_history):
            if is_white_turn(board_history):
                if board[T(square, x, y)] not in White_Pieces:
                    if not oops_mover_check(square, T(square, x, y), board_history):
                        legal_movements.append((x, y))
            else:
                if board[T(square, x, y)] not in Black_Pieces:
                    if not oops_mover_check(square, T(square, x, y), board_history):
                        legal_movements.append((x, y))

    if can_push_twice(square, board_history):
        legal_movements.append((0, 2 * dist))

    if len(legal_movements) == 0:
        return []
    return legal_movements


# This function determines which square contains the piece being moved.
def where(move, board_history):
    board = current_board(board_history)
    loc = location_constructor(board)
    movers_piece = piece_symbol(move, board_history)
    clean_move = move[:]
    potential_squares = []

    if "x" in move:
        clean_move = move[:move.find("x")] + move[move.find("x") + 1:]
    if "+" in move or "#" in move:
        clean_move = clean_move[:-1]
    if "e.p." in move:
        clean_move = clean_move[:-4]

    destination = clean_move[-2] + clean_move[-1]

    if len(clean_move) == 5:
        return move[1] + move[2]

    if movers_piece in ["P", "p"]:
        dist = -1 if is_white_turn(board_history) else 1

        if "x" in move:
            return T(destination, (ord(move[0]) - 96) - (ord(destination[0]) - 96), dist)

        if destination[1] == "4" and movers_piece == "P":
            return T(destination, 0, 2 * dist) if board[destination[0] + "3"] != "P" else T(destination, 0, dist)

        if destination[1] == "5" and movers_piece == "p":
            return T(destination, 0, 2 * dist) if board[destination[0] + "6"] != "p" else T(destination, 0, dist)

        return T(destination, 0, dist) if board[T(destination, 0, dist)] == movers_piece else None

    for square in loc[movers_piece]:
        if differ_coords(square, destination) in legal_movements(square, board_history):
            potential_squares.append(square)

    if len(clean_move) == 4:
        for square in potential_squares:
            if square[0] != move[1] and square[1] != move[1]:
                potential_squares.remove(square)

    if len(potential_squares) == 1:
        return potential_squares[0]

    if len(potential_squares) > 1:
        print("User's move is ambiguous. Oops!")
        return None

    if len(potential_squares) == 0:
        print("There are no pieces which can make that move. Oops!")
        return None


# This function determines if the board is a stalemate.
def stalemate(board_history):
    loc = location_constructor(current_board(board_history))
    if is_white_turn(board_history):
        for piece in White_Pieces:
            for square in loc[piece]:
                if legal_movements(square, board_history) is not None:
                    return False
    else:
        for piece in Black_Pieces:
            for square in loc[piece]:
                if len(legal_movements(square, board_history)) > 0:
                    return False
    return True


def has_king_moved(board_history):
    king_square = "e1" if is_white_turn(board_history) else "e8"

    for board in board_history:
        if board[king_square] == " ":
            return True
    return False


# This function updates the board_history.
def update(move, board_history):
    board_copy = dict(current_board(board_history))
    move_copy = move[:]
    movers_piece = piece_symbol(move, board_history)

    if "x" in move:
        move_copy = move[:move.find("x")] + move[move.find("x") + 1:]
    if "+" in move or "#" in move:
        move_copy = move_copy[:-1]
    if "e.p." in move:
        move_copy = move_copy[:-4]

    if len(move) == 0:
        return

    if move_copy in ["O-O", "0-0", "O-O-O", "0-0-0"]:
        if has_king_moved(board_history):
            print("Illegal castle.")
            return "invalid move"

        if move_copy in ["O-O", "0-0"]:
            if is_white_turn(board_history):
                if is_clear_path("e1", "h1", board_history):
                    board_copy["e1"], board_copy["g1"], board_copy["h1"], board_copy["f1"] = " ", "K", " ", "R"
                else:
                    print("Illegal castle.")
                    return "invalid move"
            else:
                if is_clear_path("e8", "h8", board_history):
                    board_copy["e8"], board_copy["g8"], board_copy["h8"], board_copy["f8"] = " ", "k", " ", "r"
                else:
                    print("Illegal castle.")
                    return "invalid move"
        elif move_copy in ["O-O-O", "0-0-0"]:
            if is_white_turn(board_history):
                if is_clear_path("e1", "a1", board_history):
                    board_copy["e1"], board_copy["c1"], board_copy["a1"], board_copy["d1"] = " ", "K", " ", "R"
                else:
                    print("Illegal castle.")
                    return "invalid move"
            else:
                if is_clear_path("e8", "a8", board_history):
                    board_copy["e8"], board_copy["c8"], board_copy["a8"], board_copy["d8"] = " ", "k", " ", "r"
                else:
                    print("Illegal castle.")
                    return "invalid move"

    else:
        previously = where(move, board_history)
        destination = move_copy[-2] + move_copy[-1]

        if previously is None:
            return "invalid move"

        if move[-1] in Minor_Pieces + Major_Pieces:
            board_copy[destination] = move[-1]
            board_copy[previously] = " "

        if "e.p." in move:
            if can_en_passant(previously, destination, board_history):
                dist = 1 if is_white_turn(board_history) else -1
                board_copy[destination] = movers_piece
                board_copy[T(destination, 0, -dist)] = " "
                board_copy[previously] = " "
            else:
                print("Illegal en passant")
                return "invalid move"
        else:
            board_copy[destination] = movers_piece
            board_copy[previously] = " "

    board_history.append(board_copy)
    if oops_mover_check(None, None, board_history):
        return "invalid move"
    return board_history


# This function takes in a numberless (or numbered) string of algebraic chess notation, and prints the numbered version.
def print_game_so_far(game_so_far):
    for i in range(len(game_so_far)):
        if i == 0:
            print("1.", end=" ")
            print(game_so_far[i], end=" ")
        elif i % 2 == 0:
            print(str(int(i / 2 + 1)) + ".", end=" ")
            print(game_so_far[i], end=" ")
        else:
            print(game_so_far[i], end=" ")
    print("")


def initialize_board():

    locations = {"P": ["a2", "b2", "c2", "d2", "e2", "f2", "g2", "h2"], "R": ["a1", "h1"], "N": ["b1", "g1"],
                 "B": ["c1", "f1"], "Q": ["d1"], "K": ["e1"],
                 "p": ["a7", "b7", "c7", "d7", "e7", "f7", "g7", "h7"], "r": ["a8", "h8"], "n": ["b8", "g8"],
                 "b": ["c8", "f8"], "q": ["d8"], "k": ["e8"], " ": []}

    for rank in Ranks[2:6]:
        for file in Files:
            locations[" "].append(file + rank)

    board_history = []
    starting_board = {None: None}

    for piece in locations:
        for square in locations[piece]:
            starting_board[square] = piece

    board_history.append(starting_board)

    return board_history


# This is where the functions are used for the finished product!
def main():

    board_history = initialize_board()
    color_scheme = 0
    game_so_far = []
    printer(board_history, color_scheme)
    play = True

    while play:
        users_input = input()
        cleaned_notation = notation_cleaning(users_input)

        if users_input == "":
            color_scheme = 0 if color_scheme == 12 else color_scheme + 2
            printer(board_history, color_scheme)
            continue

        if users_input[:4] == "q":
            exit(0)

        if users_input[:4] == "Undo":
            board_history = board_history[:-1]
            game_so_far = game_so_far[:-1]

            printer(board_history, color_scheme)
            continue

        if users_input[:5] == "moves":
            print(legal_movements(users_input[6:], board_history))
            continue

        for move in cleaned_notation:

            try:
                update_board_history = update(move, board_history)

                if update_board_history != "invalid move":
                    game_so_far.append(move)

                    printer(update_board_history, color_scheme)
                    print(move)
                    if "#" not in users_input:
                        if stalemate(update_board_history):
                            print("Stalemate :)")
                            print_game_so_far(game_so_far)
                            play = False
            except (ValueError, IndexError):
                print("Invalid move.")

        if "#" in users_input:
            if is_white_turn(board_history):
                print("The white king has been checkmated. Black wins!")
            else:
                print("The black king has been checkmated. White wins!")
            print_game_so_far(game_so_far)
            play = False


if __name__ == "__main__":
    main()
