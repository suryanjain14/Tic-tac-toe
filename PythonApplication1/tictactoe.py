def nameinput():
    global play1
    global play2
    play1 =input('Enter the name of player 1:')
    play2 =input('Enter the name of player 2:')

def win(nums):


     winlst =[[1,4,7,'x'],[2,5,8,"c"],[3,6,9,'x'],[7,8,9,'x'],[4,5,6,'x'],[1,2,3,'x'],[1,5,9,'x'],[3,5,7,'x']]

     code = [0,0,7,'x']
    
     for list in winlist:
         code == list
         for numb in nums:
            if numb == code[0]:
                code.pop(0)
     if len(code)==1:
         print('Player one wins')
     else :
         print('player two wins')
def sett():
    global a
    global b
    global c
    global d
    global e
    global f
    global g
    global h
    global i
    global lst
    a=' '
    b=' '
    c=' ' 
    d=' '
    e=' '
    f=' '
    g=' '
    h=' '
    i=' '
    lst=[]

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
def eng1():
    global a
    global b
    global c
    global d
    global e
    global f
    global g
    global h
    global i
    global lst 
    no=int (input (f"player {play1}'s chance:"))
    lst.append(no)
    if no==7:
        print(a)
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
       lst.pop()
       print('sda')
       print('asd')
       eng1()
    print('\n'*100)
    structure()

def eng2():
    global a
    global b
    global c
    global d
    global e
    global f
    global g
    global h
    global i
    no=int (input (f"player {play2}'s chance:"))
    if no==7:
        print(a)
        a='O'
        print(a)
    elif no==8:
        b='O'
    elif no==9:
        c='O'
    elif no==4:
        d='O'
    elif no==5:
        e='O'
    elif no==6:
        f='O'
    elif no==1:
        g='O'
    elif no==2:
        h='O'
    elif no==3:
        i='O'
    else:
       print('Wrong entry,')
       eng2()
    print('\n'*100)
    structure()




def main():
    sett()
    print('Welcome to Tic Tac Toe')
    print('X is for player one')
    print('O is for player Two')
    nameinput()
    print("\n"*11)
    structure()
    k=0
    while k<=9:
       eng1()
       k=k+1
       if k==9:
           while 1<3:
               ext =input('if you want to play again press Y if you want to exit press N')
               if   ext == 'y':
                   main()
               elif ext==  'n':
                   break
               else:
                   print('Error')
       if k==9:
           break
       eng2()
       k=k+1
       
main()
