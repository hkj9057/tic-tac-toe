import random

inp = 0
o = 'o'
x = 'x'
human = 0
ai = 0
turn = 0
ran = 0
pan = 0
result = 0

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

pan = ['#', '#', '#', '#', '#', '#', '#', '#', '#']

def pann(pan):
    for i in range(7):
        if(i == 0 or i == 3 or i == 6):
            print(pan[i], pan[i+1], pan[i+2])

def check(inp, pan):
    while (True):
        inp = int(input("말을 두세요(0~8).\n"))
        if (inp > 8 or inp < 0 or pan[inp] != '#'):
            continue
        return inp

human, ai = select(inp,o,x,human,ai)
turn = turnn(ran, turn)
pann(pan)

while(result == 0):
    if(turn == "human"):
        print("human turn")
        inp = check(inp, pan)
        pan[inp] = human
        print(pann(pan))
        turn = 'ai'
    else:
        pass