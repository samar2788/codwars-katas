import turtle

def tree(branchLen, t):
    if branchLen>5:
        t.forward(branchLen)
        t.right(20)
        tree(branchLen-4, t)
        t.left(40)
        tree(branchLen-4,t)
        t.right(20)
        t.color("purple")
        t.backward(branchLen)

def main():
    t=turtle.Turtle()
    myWin=turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("black")
    tree(50,t)
    myWin.exitonclick()

main()
