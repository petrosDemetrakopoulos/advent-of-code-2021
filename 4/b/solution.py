import numpy as np
with open('input.txt') as f:
    lines = map(lambda x: x, f.readlines())
    lines[0] = lines[0].split(',')
    random_nums = lines[0]
    del lines[0]
    for i in range(len(lines)):
        lines[i] = filter(lambda x: x != ',' and x != '\n', lines[i])

random_nums = map(lambda x: int(x.replace('\n', '')), random_nums)
lines = filter(lambda x: x != '', lines)

def transform_to_boards(lines):
    boards = []
    crn_board = []
    i = 0
    for line in lines:
        if i < 5:
            crn_board.append(map(lambda x: int(x), line))
            i += 1
        else:
            i = 1
            boards.append(crn_board)
            crn_board = [map(lambda x: int(x), line)]
    boards.append(crn_board)
    return boards

print random_nums
print "---------"

lines = map(lambda x: filter(lambda y: y != '', x.split(' ')), lines)

all_boards = transform_to_boards(lines)

def check_if_board_won(board):
    #check for complete rows
    for row in range(len(board)):
        marked_places = 0
        for k in range(len(board[row])):
            if board[row][k] == -1:
                marked_places += 1
        if marked_places == 5:
            return True
    #check for complete columns
    for col in range(len(zip(*board))):
        marked_places = 0
        for k in range(len(board[col])):
            if board[row][k] == -1:
                marked_places += 1
        if marked_places == 5:
            return True
    return False

def mark_board_for_number(board, number):
    for row in range(len(board)):
        for k in range(len(board[row])):
            if board[row][k] == number:
                board[row][k] = -1 
    return board  

def calculate_winning_board_score(board, called_num):
    score = 0
    for row in range(len(board)):
        for k in range(len(board[row])):
            if board[row][k] != -1:
                score += board[row][k]
    return score * called_num

won_boards = []
won_scores = []
for i in range(len(random_nums)):
    crn_num = random_nums[i]
    for j in range(len(all_boards)):
        marked_board = mark_board_for_number(all_boards[j], crn_num)
        board_won = check_if_board_won(marked_board)
        if board_won:
            score = calculate_winning_board_score(marked_board, crn_num)
            if j not in won_boards:
                won_boards.append(j)
                won_scores.append(score)

print("WON BOARDS:")
print(won_boards)
print(won_scores)