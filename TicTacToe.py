import random

def print_board():
    for i in range(0,3):
        for j in range(0,3):
            print map[2-i][j],
            if j != 2:
                print "|",
        print ""

########

def check_done():
    for i in range(0,3):
        if map[i][0] == map[i][1] == map[i][2] != " " \
        or map[0][i] == map[1][i] == map[2][i] != " ":
            print turn, "won!!!"
            return True
        
    if map[0][0] == map[1][1] == map[2][2] != " " \
    or map[0][2] == map[1][1] == map[2][0] != " ":
        print turn, "won!!!"
        return True

    if " " not in map[0] and " " not in map[1] and " " not in map[2]:
        print "Draw"
        return True
        
    return False

########
#determines the location from main
def calculate_position(pos):
    Y = pos/3
    X = pos%3
    
    if X != 0:
        X -=1
    else:
         X = 2
         Y -=1
    
    if map[Y][X] == " ":
        return True
    else:
        return False

#determines the location in map
def make_move(sent_pos,sent_turn):
    moved = False
    while moved != True:

        try:
            pos = sent_pos
            
            if pos <=9 and pos >=1:
                Y = pos/3
                X = pos%3
                if X != 0:
                    X -=1
                else:
                     X = 2
                     Y -=1
                    
                if map[Y][X] == " ":
                    map[Y][X] = sent_turn
                    moved = True
                    done = check_done()
                

                    
        except TypeError:
            print "You need to add a numeric value"
    
    return done

######## to win or block the opponent from winning
def attack_defend(pawn):
    
    count = 0
    for i in range (0,3):
        for j in range (0,3):
            if map[i][j] != " ":
                count = count + 1

    if pawn == comp and count == 2:
        
        if map[1][0] != " ":
            return (True,random.choice([3,9]))

        if map[0][1] != " ":
            return (True,random.choice([7,9]))

        if map[1][2] != " ":
            return (True,random.choice([1,7]))

        if map[2][1] != " ":
            return (True,random.choice([1,3]))


    replaced = False

    for k in range (0,4):        
        for i in range (0,3):
           
            L = []
            
            for j in range (0,3):
                if k == 0:
                    L.insert(j,map[i][j])

                elif k == 1:
                    L.insert(j,map[j][i])

                elif k == 2:
                    L.insert(0,map[2][0])
                    L.insert(1,map[1][1])
                    L.insert(2,map[0][2])
                    break

                else:
                    L.insert(0,map[2][2])
                    L.insert(1,map[1][1])
                    L.insert(2,map[0][0])
                    break


            if " " in L and L.count(pawn) == 2:
            
                val = L.index(" ")
                replaced = True
                
            if replaced == True:

                if k == 0:
                    pos = (3*i) + val + 1

                elif k == 1:
                    pos = (3*val) + i + 1

                elif k == 2:
                    
                    if val == 0:
                        pos = 7
                    elif val == 1:
                        pos = 5
                    else:
                        pos = 3

                else:
                    
                    if val == 0:
                        pos = 9
                    elif val == 1:
                        pos = 5
                    else:
                        pos = 1

                return (True,pos)

            del L[:] 

    return (False, -1)


######## If the opponent has pawns at the diagonal ends, then it is better to place in one of the inner positions
def check_diagonal():
    count = 0
    for i in range (0,3):
        for j in range (0,3):
            if map[i][j] == " ":
                count = count + 1

    if count == 6:
        if map[0][0] == map[2][2] !=" " or  map[0][2] == map[2][0] != " ":
            return (True,random.choice([2,4,6,8]))
        else:
            return (False, -1)
    else:
            return (False, -1)

# main control for computer 
def computer_control(comp,user):
    reacted = False    
    L_corner = [1,3,7,9]
    L1 =[2,4,6,8]

    (reacted,pos) = check_diagonal()
    if reacted == True:
        return pos

    #attack
    (reacted, pos) = attack_defend(comp)
    if reacted == True:
        return pos

    #defend
    (reacted, pos) = attack_defend(user)
    if reacted == True:
        return pos

    if map[1][1] == " ":
        return 5

    else:
        return_val = -1

        while return_val == -1 or len(L_corner) > 0:

            option = random.choice(L_corner)
            print option 
            print 

            if option == 1 and map[0][0] == " ":
                return_val = option
                break

            elif option == 3 and map[0][2] == " ":
                return_val = option
                break

            elif option == 7 and map[2][0] == " ":
                return_val = option
                break

            elif option == 9 and map[2][2] == " ":
                return_val = option
                break

            elif map[0][0] != " " and map[2][0] != " " and map[0][2] != " " and map[2][2] != " ": 
                print "last elif"

                option1 = random.choice(L1)

                if option1 == 2 and map[0][1] == " ":
                    return_val = option1
                    break

                elif option1 == 4 and map[1][0] == " ":
                    return_val = option1
                    break

                elif option1 == 6 and map[1][2] == " ":
                    return_val = option1
                    break

                elif option1 == 8 and map[2][1] == " ":
                    return_val = option1
                    break
                            
            L_corner.remove(option)

        return return_val  

#STARTS HERE------------------------------------------------

#**********************initializations********
turn = "X"
map = [[" "," "," "],
       [" "," "," "],
       [" "," "," "]]

done = False
first = False
comp = ""
user = ""
rand = 99;
returned_comp_pos = ""
user_pos = u"10"
final_result = False
num_test = False
#**********************************************

print "enter choice: 1 to play first, 2 to play second"   
while rand not in [1,2]:
    rand = input("Choice:")

while final_result != True:
    if rand%2 == 0:
        
        if first == False:
            comp = "X"
            user = "O"
            first = True
            print "Computer plays first"
            print "Computer's Pawn: X"
            print "Your Pawn: O"
            raw_input ('Press enter to continue:')
            print

        turn = comp
        returned_comp_pos = computer_control(comp,user)
        final_result = make_move(returned_comp_pos,comp)
        rand = rand + 1
        print "Computer's turn"

    else:
        
        repeat = 1
        if first == False:
            user = "X"
            comp = "O"
            first = True
            print "You play first"
            print "Your Pawn: X"
            print "Computer's Pawn: O"
            raw_input ('Press enter to continue:')
            print

        turn = user
        print "Please select position by typing in a number between 1 and 9, see below for which number that is which position..."
        print "7|8|9"
        print "4|5|6"
        print "1|2|3"
        user_pos = raw_input("Enter a position:")

        while(1):

            try:
                if int(user_pos) in range(1,10) and calculate_position(int(user_pos)) is True:
                    break
                    
                else:
                    print "enter a number in range of 1-9 inclusive"
                    user_pos = raw_input("Enter a position:")
                    
            except ValueError:
                
                print "Enter a valid number"
                user_pos = raw_input("Enter a position:")


        final_result = make_move(int(user_pos),user)        
        rand = rand + 1
        
    print
    print_board() 