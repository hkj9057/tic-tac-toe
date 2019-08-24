import random

inp = 0
inp_s = 0
o = 'o'
x = 'x'
human = 0
ai = 0
turn = 0
ran = 0
pan = 0
result = 0
pan = []
for i in range(15):
    pan.append([])
    for j in range(15):
        pan[i].append(0)

def select(inp,o,x,human,ai):
    inp = input("o 또는 x를 선택하세요.\n")
    if (inp == 'o'):
        human = o
        ai = x
    elif (inp == 'x'):
        human = x
        ai = o

    return human,ai

def turnn(ran, turn):
    ran = random.randrange(2)
    if(ran == 0):
        turn = "human"
    else:
        turn = "ai"
    return turn

def pann(pan):
    for i in range(len(pan)):
        print(pan[i])

def check(inp, pan):
    while (True):
        inp = int(input("말을 두세요.\n"))
        inp_s = int(input("2말을 두세요.\n"))
        print(pan[inp])
        if (inp > 15 or inp_s > 15 or inp < 0 or inp_s < 0 or pan[inp][inp_s] != '0'):
            continue
        return inp

"""def match_result(result):"""


human, ai = select(inp,o,x,human,ai)
turn = turnn(ran, turn)
pann(pan)

while(result == 0):
    if(turn == "human"):
        print("human turn")
        inp = check(inp, pan)
        pan[inp] = human
        print(pann(pan))
        turn = "ai"
    else:
        print("ai turn")
        while(True):
            inp = check(inp, pan)
        pan[inp] = ai
        print(pann(pan))
        turn = "human"