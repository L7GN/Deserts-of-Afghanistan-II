
answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
Flag = True
while Flag == True:
    try:
        print ("WELCOME TO THE NEW WORLD")
        print ("A: NEW GAME")
        print ("B: Load Game")
        print ("C: Story so far")
        choice = input(">>>")
        if choice in answer_A:
            import CharacterCreator
        if choice in answer_B:
            import Save
        if choice in answer_C:
            import Prologue
        else:
            print ("A,B OR C")
    except:
        print ("A,B OR C")