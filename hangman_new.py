


def hangman(word):
    wrong = 0 #間違えた回数
    stages = ["",
             "______     ",
             "|          ",
             "|     |    ",
             "|     0    ",
             "|   ／|＼  ",
             "|   ／ ＼  ",
             "|          "
             ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("Welcome to hangman!")



    
    while wrong < len(stages) - 1:
        print("\n")
        msg = "1文字を予想してね"
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = "$"
        else:
            wrong += 1
        print(" ".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("あなたの勝ちです")
            print(" ".join(board))
            win = True
            break
    if not win:
            print("\n".join(stages[0:wrong + 1]))
            print("あなたの負け正解は{}".format(word))

ans = ["cat","dog","pig"]

import random

"""
デバック
print(random.choice(ans))

"""

hangman(random.choice(ans))
