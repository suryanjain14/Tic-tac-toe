def nameinput():
    global play1
    global play2
    play1 =input('Enter the name of player 1:')
    play2 =input('Enter the name of player 2:')
def structure():
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
nameinput()
structure()
