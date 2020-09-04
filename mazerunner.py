def maze_runner(maze, directions):
    n = len(maze)
    print(n)

    # find start point
    for i in range(n):
        if 2 in maze[i]:
            row = i
            print(row)
            col = maze[row].index(2)
            print(col)
            break

    # follow directions
    for step in directions:
        if step == "N":
            row -= 1
            print(row)
        elif step == "S":
            row += 1
            print(row)
        elif step == "E":
            col += 1
            print(col)
        elif step == "W":
            col -= 1
            print(col)

        # check the result
        if row < 0 or col < 0 or row == n or col == n or maze[row][col] == 1:
            return "Dead"
        elif maze[row][col] == 3:
            return "Finish"

    return "Lost"


print(maze_runner([[1, 1, 1, 1, 1, 1, 1],
             [1, 0, 0, 0, 0, 0, 3],
             [1, 0, 1, 0, 1, 0, 1],
             [0, 0, 1, 0, 0, 0, 1],
             [1, 0, 1, 0, 1, 0, 1],
             [1, 0, 0, 0, 0, 0, 1],
             [1, 2, 1, 0, 1, 0, 1]], ["N", "N", "N", "N", "N", "E", "E", "E", "E", "E"]))
