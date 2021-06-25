def drawBoard(field):
    for row in range(5):
        if row % 2 == 0:
            practicalRow = int(row/2)
            for column in range(5):
                if column % 2 == 0:
                    practicalColumn = int(column/2)
                    if column != 4:
                        print(field[practicalColumn][practicalRow], end="")
                    else:
                        print(field[practicalColumn][practicalRow])
                else:
                    print("|", end="")
        else:
            print("-----")

Player = 1
CurrentBoard = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
drawBoard(CurrentBoard)
while(True):
    print("Players turn: ", Player)
    Row = int(input("Select a row: "))
    Column = int(input("Select a column: "))

    if Player == 1:

        if CurrentBoard[Column][Row] == " ":
            CurrentBoard[Column][Row] = "X"
            Player = 2
    else:

        if CurrentBoard[Column][Row] == " ":
            CurrentBoard[Column][Row] = "O"
            Player = 1
    drawBoard(CurrentBoard)





