def nameinput():
    global play1
    global play2
    play1 =input('Enter the name of player 1:')
    play2 =input('Enter the name of player 2:')
def structure():
    global no 
    no=0
    global a
    global b
    global c
    global d
    global e
    global f
    global g
    global h
    global i
    a=' '
    b=' '
    c=' ' 
    d=' '
    e=' '
    f=' '
    g=' '
    h=' '
    i=''
    print(f'     |     |     ')
    print(f'   {a} |  {b}  |  {c} ')
    print(f'     |     |     ')
    print(f'-----------------')
    print(f'     |     |     ')
    print(f'   {d} |  {e}  |  {f} ')
    print(f'     |     |     ')
    print(f'-----------------')
    print(f'     |     |     ')
    print(f'   {g} |  {h}  |  {i} ')
    print(f'     |     |     ')
def main():
    print('Welcome to Tic Tac Toe')
    print('X is for player one')
    print('O is for player Two')
def eng1():
    global no
    no=input('player ones chance')
    if no==7:
        a='X'
    elif no==8:
        b='X'
    elif no==9:
        c='X'
    elif no==4:
        d='X'
    elif no==5:
        e='X'
    elif no==6:
        f='X'
    elif no==1:
        g='X'
    elif no==2:
        h='X'
    elif no==3:
        i='X'
    else:
       print('Wrong entry,')
       eng1(no)
main()
nameinput()
structure()
print('hello')
no=input("player ones chance:")
structure()
eng1()
