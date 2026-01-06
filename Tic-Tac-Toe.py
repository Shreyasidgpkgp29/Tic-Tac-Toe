import random
xst=[0,0,0,0,0,0,0,0,0]
zst=[0,0,0,0,0,0,0,0,0]

def layout(xst,zst):
    zero="X" if xst[0] else("O" if zst[0] else " ")
    one="X" if xst[1] else("O" if zst[1] else " ")
    two="X" if xst[2] else("O" if zst[2] else " ")
    three="X" if xst[3] else("O" if zst[3] else " ")
    four="X" if xst[4] else("O" if zst[4] else " ")
    five="X" if xst[5] else("O" if zst[5] else " ")
    six="X" if xst[6] else("O" if zst[6] else " ")
    seven="X" if xst[7] else("O" if zst[7] else " ")
    eight="X" if xst[8] else("O" if zst[8] else " ")

    print("_____________")
    print(f"| {zero} | {one} | {two} |")
    print("|___|___|___|")
    print(f"| {three} | {four} | {five} |")
    print("|___|___|___|")
    print(f"| {six} | {seven} | {eight} |")
    print("|___|___|___|")


def win(xst,zst):
    win_case=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[3,4,6]]
    for k in win_case:
        if(xst[k[0]]+xst[k[1]]+xst[k[2]])==3:
            return "X"
        elif(zst[k[0]]+zst[k[1]]+zst[k[2]])==3:
            return "O"
        else:
            continue

turn=1
emp_space=[1,2,3,4,5,6,7,8,9]
global value

for i in range(9):
    layout(xst,zst)
    if turn==1:
        print("X's turn")
        value=int(input("Enter a value between 1 to 9"))
        xst[value-1]=1
        turn=0
        result=win(xst,zst)
        if result=="X":
            layout(xst,zst)
            print("X wins")
            break
    else:
        print("Computer aka O's turn")
        value_c=random.choice(emp_space)
        emp_space.remove(value_c)
        zst[value_c]=1
        turn=1
        result=win(xst,zst)
        if result=="O":
            layout(xst,zst)
            print("O wins")
            break