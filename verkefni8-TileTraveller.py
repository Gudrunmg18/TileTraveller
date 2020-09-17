def position_change(direction,position):
    if direction == "N" or direction == "n":
        position[1] += 1
    if direction == "S" or direction == "s":
        position[1] -= 1
    if direction == "E" or direction == "e":
        position[0] += 1
    if direction == "W" or direction == "w":
        position[0] -= 1
    return position


hnit = [1,1]


while hnit != [3,1]:
    if hnit == [1,1] or hnit == [2,1]:
        print("You can travel: (N)orth.")
        direction = input("Direction: ")
        while direction != 'N' and direction != 'n':
            print("Not a valid direction!")
            print("You can travel: (N)orth.")
            direction = input("Direction: ")
        else:
            hnit = position_change(direction,hnit)
            #print(hnit)    
    elif hnit == [1,2]:
        print("You can travel: (N)orth or (E)ast or (S)outh.")
        direction = input("Direction: ")
        while direction != 'N' and direction != 'n' and direction != 'E' and direction != 'e' and direction != 'S' and direction != 's':
            print("Not a valid direction!")
            print("You can travel: (N)orth or (E)ast or (S)outh.")
            direction = input("Direction: ")
        else:
            hnit = position_change(direction,hnit)
            #print(hnit)
    elif hnit == [1,3]:
        print("You can travel: (E)ast or (S)outh.")
        direction = input("Direction: ")
        while direction != 'E' and direction != 'e' and direction != 'S' and direction != 's':
            print("Not a valid direction!")
            print("You can travel: (E)ast or (S)outh.")
            direction = input("Direction: ")
        else:
            hnit = position_change(direction,hnit)
            #print(hnit)
    elif hnit == [2,3]:
        print("You can travel: (E)ast or (W)est.")
        direction = input("Direction: ")
        while direction != 'E' and direction != 'e' and direction != 'W' and direction != 'w':
            print("Not a valid direction!")
            print("You can travel: (E)ast or (W)est.")
            direction = input("Direction: ")
        else:
            hnit = position_change(direction,hnit)
            #print(hnit)
    elif hnit == [2,2] or hnit == [3,3]:
        print("You can travel: (S)outh or (W)est.")
        direction = input("Direction: ")
        while direction != 'W' and direction != 'w' and direction != 'S' and direction != 's':
            print("Not a valid direction!")
            print("You can travel: (S)outh or (W)est.")
            direction = input("Direction: ")
        else:
            hnit = position_change(direction,hnit)
            #print(hnit)
    elif hnit == [3,2]:
        print("You can travel: (N)orth or (S)outh.")
        direction = input("Direction: ")
        while direction != 'N' and direction != 'n' and direction != 'S' and direction != 's':
            print("Not a valid direction!")
            print("You can travel: (N)orth or (S)outh.")
            direction = input("Direction: ")
        else:
            hnit = position_change(direction,hnit)
            #print(hnit)
        
            

print("Victory!")


#print("You can travel: (N)orth.")
#print("Not a valid direction!")

