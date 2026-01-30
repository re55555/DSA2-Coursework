import random

#Creating an empty board
def make_empty_board(size):
    board = []
    for r in range(size):
        row = []
        for c in range(size):
            row.append(".")
        board.append(row)
    return board

def print_board(board):
    for row in board:
        for cell in row:
            print(cell, end=" ")
        print()
    print()
        
#Showing the Queens on the board
def positions_to_board(size, positions):
    board = make_empty_board(size)

    for pos in positions:
        r = pos[0]
        c = pos[1]
        board[r][c] = "Q"

    return board


def visualize_end_state(size, success, positions):
    board = positions_to_board(size, positions)
    print("\nFinal board:")
    print_board(board)
    print("Success:", success)
    print("Queen positions:", positions)
    print()


#Las Vegas Algorithm
def nQueensLasVegas(size):
    cols = set()
    posDiag = set()
    negDiag = set()

    positions = []

    for r in range(size):
        #Loop through all cols. If attacked then skip, if safe then store.
        available_cols = []

        for c in range(size):
            if c in cols:
                continue
            if (r - c) in posDiag:
                continue
            if (r + c) in negDiag:
                continue
            available_cols.append(c)

        if len(available_cols) == 0:
            return False, positions

        c = random.choice(available_cols)

        positions.append([r, c])
        cols.add(c)
        posDiag.add(r - c)
        negDiag.add(r + c)

    return True, positions


# Backtracking algorithm
def nQueensBacktracking(size):
    print("This is the Backtracking Algorithm")

    cols = set()
    posDiag = set()
    negDiag = set()

    row_to_col = []
    for i in range(size):
        row_to_col.append(-1)

    def backtrack(r):
        if r == size:
            return True

        for c in range(size):
            if c in cols:
                continue
            if (r - c) in posDiag:
                continue
            if (r + c) in negDiag:
                continue

            row_to_col[r] = c
            cols.add(c)
            posDiag.add(r - c)
            negDiag.add(r + c)

            if backtrack(r + 1):
                return True

            row_to_col[r] = -1
            cols.remove(c)
            posDiag.remove(r - c)
            negDiag.remove(r + c)

        return False

    success = backtrack(0)

    positions = []
    for r in range(size):
        if row_to_col[r] != -1:
            positions.append([r, row_to_col[r]])

    if success:
        print("Success!")
    else:
        print("No solution found.")

    return success, positions



# Backtracking Version 2
def nQueensBacktrackingVersion2(size, startingPosition):
    print("This is Backtracking (Version 2)")

    fixed_r = startingPosition[0]
    fixed_c = startingPosition[1]

    cols = set()
    posDiag = set()
    negDiag = set()

    row_to_col = []
    for i in range(size):
        row_to_col.append(-1)

    def backtrack(r):
        if r == size:
            return True

        if r == fixed_r:
            if fixed_c in cols:
                return False
            if (r - fixed_c) in posDiag:
                return False
            if (r + fixed_c) in negDiag:
                return False

            row_to_col[r] = fixed_c
            cols.add(fixed_c)
            posDiag.add(r - fixed_c)
            negDiag.add(r + fixed_c)

            if backtrack(r + 1):
                return True

            row_to_col[r] = -1
            cols.remove(fixed_c)
            posDiag.remove(r - fixed_c)
            negDiag.remove(r + fixed_c)

            return False

        for c in range(size):
            if c in cols:
                continue
            if (r - c) in posDiag:
                continue
            if (r + c) in negDiag:
                continue

            row_to_col[r] = c
            cols.add(c)
            posDiag.add(r - c)
            negDiag.add(r + c)

            if backtrack(r + 1):
                return True

            row_to_col[r] = -1
            cols.remove(c)
            posDiag.remove(r - c)
            negDiag.remove(r + c)

        return False

    success = backtrack(0)

    positions = []
    for r in range(size):
        if row_to_col[r] != -1:
            positions.append([r, row_to_col[r]])

    if success:
        print("Success!")
    else:
        print("No solution found.")

    return success, positions


# Main program 
def main():
    print("N-Queens Solver")
    print("Type q at any time to quit.\n")

    while True:
        text = input("Enter board size n: ").strip().lower()
        if text == "q":
            print("Exiting program.")
            return

        try:
            size = int(text)
        except:
            print("Please enter a number.\n")
            continue

        print("\nEmpty board:")
        print_board(make_empty_board(size))

        print("Choose an option:")
        print("l  = Las Vegas")
        print("b  = Backtracking")
        print("b2 = Backtracking with starting queen")
        print("q  = Quit")

        choice = input("Your choice: ").strip().lower()
        if choice == "q":
            print("Exiting program.")
            return

        if choice == "l":
            success, positions = nQueensLasVegas(size)
            visualize_end_state(size, success, positions)

        elif choice == "b":
            success, positions = nQueensBacktracking(size)
            visualize_end_state(size, success, positions)

        elif choice == "b2":
            r = input("Enter starting queen row: ").strip()
            if r.lower() == "q":
                print("Exiting program.")
                return

            c = input("Enter starting queen column: ").strip()
            if c.lower() == "q":
                print("Exiting program.")
                return

            try:
                r = int(r)
                c = int(c)
            except:
                print("Please enter numbers only.\n")
                continue

            success, positions = nQueensBacktrackingVersion2(size, (r, c))
            visualize_end_state(size, success, positions)

        else:
            print("Invalid choice.\n")


if __name__ == "__main__":
    main()
