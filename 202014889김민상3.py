import turtle as t
import random
from tkinter.simpledialog import askstring

inStr = ''
swidth, sheight = 400, 400
tX, tY, txtSize = [0]*3

t.title("거북이 글자쓰기")
t.shape("turtle")
t.setup(width=swidth + 50, height=sheight + 50)
t.screensize(swidth, sheight)
t.penup()
inStr = askstring("문자열 입력", "거북이 쓸 문자열 입력")

for ch in inStr:
    tX = random.randrange(-swidth // 2, swidth // 2)
    tY = random.randrange(-sheight // 2, sheight // 2)
    r = random.random()
    g = random.random()
    b = random.random()
    txtSize = random.randrange(10, 50)
    t.goto(tX, tY)
    t.pencolor((r, g, b))
    t.write(ch, font=("맑은고딕", txtSize, "bold"))
t.done()
