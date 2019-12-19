def checkio(matrix):
    def forward(matrix, x, y, max_x):
        if x + 3 >= max_x:
            return False
        for i in range(1, 4):
            if matrix[y][x] != matrix[y][x + i]:
                return False
        return True
    def downward(matrix, x, y, max_y):
        if y + 3 >= max_y:
            return False
        for i in range(1, 4):
            if matrix[y][x] != matrix[y + i][x]:
                return False
        return True
    def forward_down(matrix, x, y, max):
        if x + 3 <= max - 1 and y + 3 <= max - 1:
            for i in range(1, 4):
                if matrix[y][x] != matrix[y + i][x + i]:
                    return False
            return True
        return False
    def backward_down(matrix, x, y, max_y):
        if x - 3 >= 0 and y + 3 <= max_y - 1:
            for i in range(1, 4):
                if matrix[y][x] != matrix[y + i][x - i]:
                    return False
            return True
        return False
    max = len(matrix)
    for x in range(max):
        for y in range(max):
            if forward(matrix,x,y,max):
                return True
            elif downward(matrix,x,y,max):
                return True
            elif forward_down(matrix, x, y, max):
                return True
            elif backward_down(matrix, x, y, max):
                return True
    return False



if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        [1, 2, 1, 1],
        [1, 1, 4, 1],
        [1, 3, 1, 6],
        [1, 7, 2, 5]
    ]) == True, "Vertical"
    assert checkio([
        [7, 1, 4, 1],
        [1, 2, 5, 2],
        [3, 4, 1, 3],
        [1, 1, 8, 1]
    ]) == False, "Nothing here"
    assert checkio([
        [2, 1, 1, 6, 1],
        [1, 3, 2, 1, 1],
        [4, 1, 1, 3, 1],
        [5, 5, 5, 5, 5],
        [1, 1, 3, 1, 1]
    ]) == True, "Long Horizontal"
    assert checkio([
        [7, 1, 1, 8, 1, 1],
        [1, 1, 7, 3, 1, 5],
        [2, 3, 1, 2, 5, 1],
        [1, 1, 1, 5, 1, 4],
        [4, 6, 5, 1, 3, 1],
        [1, 1, 9, 1, 2, 1]
    ]) == True, "Diagonal"