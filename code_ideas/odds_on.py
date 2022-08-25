"""Odds on is basically a dare game where someone says a number (the odds)."""
"""Then both people say a number ranging from 1 to that number."""

__author__ = "730561311"


print("Odds: a game of dares, where if the dared and the darer say the same number at the same time, the dared loses and has to do the dare.")
print("The darer, dares the person and that person gives their odds. Both people can say any number from 1 to odds.")
print("This is why most people increase the odds if they really don't want to do the dare.")
print("For example: I've been dared to scream in public, I give odds of 20. We both say our number at the same time. I say 2 and you say 17.")
print("I get away from doing that dare ;). If we both said 7 then I would have to scream in public :(")

starting_it: str = input("If you understand the game type okay: ") 

if starting_it == str("okay"): 
    give_me_odds: int = int(input("I dare you to play, odds? "))

    if give_me_odds >= 2:
        st_number: int = int(input("Ok now that we have odds, type your number and when you hit enter I will type mine. Enter number: "))
        if st_number <= give_me_odds:
            print("Your number: " + str(st_number))
            print("My number: " + str(st_number))
            print("Looks like I won! Now you have to play another game of odds. That was the dare after all.")
            print("I'm giving my odds of 10, if you don't guess my number then we're playing another game! :)")
            st_number: int = int(input("Ok now that we have odds, type your number and when you hit enter I will type mine. Enter number: "))
            if st_number <= 10:
                print("Your number: " + str(st_number))
                if st_number > 1:
                    my_number = st_number - 1
                    print("My number: " + str(my_number))
                    second_give: int = int(input("I win! You're really unlucky. Mabye your luck will change, we're going to find out. Odds out of 4. Enter number here: "))
                    if second_give <= 4:
                        print("Your number: " + str(second_give))
                        from random import randint
                        random_odd = randint(1,4)
                        print("My number: " + str(random_odd))
                        if random_odd != second_give:
                            print("Nice you won one. It's been fun but I gotta go. I swear I'm not a sore loser. I would never :/")
                        else:
                            random_odd == second_give
                            print("Wow, your luck is terrible. Welp, gotta go. It's been fun!")
                    else:
                        second_give > 4
                        print("My number: 4")
                        print("Your number: " + str(second_give))
                        print("Hey your'e not within our odds of 4.")
                        second_give: int = int(input("Enter number here: "))
                        if second_give <= 4: 
                            print("Your number: " + str(second_give))
                            from random import randint
                            random_odd = randint(1,4)
                            print("My number: " + str(random_odd))
                            if random_odd != second_give:
                                print("Nice you won one. It's been fun but I gotta go. I swear I'm not a sore loser. I would never :/")
                            else:
                                random_odd == second_give
                                print("Wow, your luck is terrible. Welp, gotta go. It's been fun!")
                        else:
                            second_give > 4
                            print("My number: 4")
                            print("Your number: " + str(second_give))
                            print("Wow can't even play the game properly, no wonder your'e doing so bad.")
                            exit()
                else:
                    st_number == 1
                    my_number = st_number + 3
                    print("My number: " + str(my_number))
                    second_give: int = int(input("I win! You're really unlucky. Mabye your luck will change, we're going to find out. Odds out of 4. Enter number here: "))
                    if second_give <= 4:
                        print("Your number: " + str(second_give))
                        from random import randint
                        random_odd = randint(1,4)
                        print("My number: " + str(random_odd))
                        if random_odd != second_give:
                            print("Nice you won one. It's been fun but I gotta go. I swear I'm not a sore loser. I would never :/")
                        else:
                            random_odd == second_give
                            print("Wow, your luck is terrible. Welp, gotta go. It's been fun!")
                    else:
                        second_give > 4
                        print("My number: 4")
                        print("Your number: " + str(second_give))
                        print("Hey your'e not within our odds of 4.")
                        second_give: int = int(input("Enter number here: "))
                        if second_give <= 4: 
                            print("Your number: " + str(second_give))
                            from random import randint
                            random_odd = randint(1,4)
                            print("My number: " + str(random_odd))
                            if random_odd != second_give:
                                print("Nice you won one. It's been fun but I gotta go. I swear I'm not a sore loser. I would never :/")
                            else:
                                random_odd == second_give
                                print("Wow, your luck is terrible. Welp, gotta go. It's been fun!")
                        else:
                            second_give > 4
                            print("My number: 4")
                            print("Your number: " + str(second_give))
                            print("Wow can't even play the game properly, no wonder your'e doing so bad.")
                            exit()
            else:
                st_number > give_me_odds
                print("My number: 1")
                print("Your number: " + str(st_number))
                print("Hey your number isn't within odds")
                st_number: int = int(input("Your number needs to be within your odds, it can't be over odds or below 1. Try again, enter your number: "))
                if st_number <= 10:
                    print("Your number: " + str(st_number))
                    if st_number > 1:
                        my_number = st_number - 1
                        print("My number: " + str(my_number))
                        second_give: int = int(input("I win! You're really unlucky. Mabye your luck will change, we're going to find out. Odds out of 4. Enter number here: "))
                        if second_give <= 4:
                            print("Your number: " + str(second_give))
                            from random import randint
                            random_odd = randint(1,4)
                            print("My number: " + str(random_odd))
                            if random_odd != second_give:
                                print("Nice you won one. It's been fun but I gotta go. I swear I'm not a sore loser. I would never :/")
                            else:
                                random_odd == second_give
                                print("Wow, your luck is terrible. Welp, gotta go. It's been fun!")
                        else:
                            second_give > 4
                            print("My number: 4")
                            print("Your number: " + str(second_give))
                            print("Hey your'e not within our odds of 4.")
                            second_give: int = int(input("Enter number here: "))
                            if second_give <= 4: 
                                print("Your number: " + str(second_give))
                                from random import randint
                                random_odd = randint(1,4)
                                print("My number: " + str(random_odd))
                                if random_odd != second_give:
                                    print("Nice you won one. It's been fun but I gotta go. I swear I'm not a sore loser. I would never :/")
                                else:
                                    random_odd == second_give
                                    print("Wow, your luck is terrible. Welp, gotta go. It's been fun!")
                            else:
                                second_give > 4
                                print("My number: 4")
                                print("Your number: " + str(second_give))
                                print("Wow can't even play the game properly, no wonder your'e doing so bad.")
                                exit()
                    else:
                        st_number == 1
                        my_number = st_number + 3
                        print("My number: " + str(my_number))
                        second_give: int = int(input("I win! You're really unlucky. Mabye your luck will change, we're going to find out. Odds out of 4. Enter number here: "))
                        if second_give <= 4:
                            print("Your number: " + str(second_give))
                            from random import randint
                            random_odd = randint(1,4)
                            print("My number: " + str(random_odd))
                            if random_odd != second_give:
                                print("Nice you won one. It's been fun but I gotta go. I swear I'm not a sore loser. I would never :/")
                            else:
                                random_odd == second_give
                                print("Wow, your luck is terrible. Welp, gotta go. It's been fun!")
                        else:
                            second_give > 4
                            print("My number: 4")
                            print("Your number: " + str(second_give))
                            print("Hey your'e not within our odds of 4.")
                            second_give: int = int(input("Enter number here: "))
                            if second_give <= 4: 
                                print("Your number: " + str(second_give))
                                from random import randint
                                random_odd = randint(1,4)
                                print("My number: " + str(random_odd))
                                if random_odd != second_give:
                                    print("Nice you won one. It's been fun but I gotta go. I swear I'm not a sore loser. I would never :/")
                                else:
                                    random_odd == second_give
                                    print("Wow, your luck is terrible. Welp, gotta go. It's been fun!")
                            else:
                                second_give > 4
                                print("My number: 4")
                                print("Your number: " + str(second_give))
                                print("Wow can't even play the game properly, no wonder your'e doing so bad.")
                                exit()
                else: 
                    st_number > 10
                    print("My number: 4")
                    print("Your number: " + str(st_number))
                    print("Well I can't play with you not following instructions.")  
                    exit()
    else:
        give_me_odds <= 2
        give_me_odds: int = int(input("You need to give me a number of 2 or above, otherwise it's just a dare. Odds? "))

        if give_me_odds >= 2:
            st_number: int = int(input("Ok now that we have odds, type your number and when you hit enter I will type mine. Enter number: "))
            print("Your number: " + str(st_number))
            print("My number: " + str(st_number))
            print("Looks like I won! Now you have to play another game of odds. That was the dare after all.")
            print("I'm giving my odds of 10, if you don't guess my number then we're playing another game! :)")
            st_number: int = int(input("Ok now that we have odds, type your number and when you hit enter I will type mine. Enter number: "))
            if st_number <= 10:
                print("Your number: " + str(st_number))
                if st_number > 1:
                    my_number = st_number - 1
                    print("My number: " + str(my_number))
                    second_give: int = int(input("I win! You're really unlucky. Mabye your luck will change, we're going to find out. Odds out of 4. Enter number here: "))
                    if second_give <= 4:
                        print("Your number: " + str(second_give))
                        from random import randint
                        random_odd = randint(1,4)
                        print("My number: " + str(random_odd))
                        if random_odd != second_give:
                            print("Nice you won one. It's been fun but I gotta go. I swear I'm not a sore loser. I would never :/")
                        else:
                            random_odd == second_give
                            print("Wow, your luck is terrible. Welp, gotta go. It's been fun!")
                    else:
                        second_give > 4
                        print("My number: 4")
                        print("Your number: " + str(second_give))
                        print("Hey your'e not within our odds of 4.")
                        second_give: int = int(input("Enter number here: "))
                        if second_give <= 4: 
                            print("Your number: " + str(second_give))
                            from random import randint
                            random_odd = randint(1,4)
                            print("My number: " + str(random_odd))
                            if random_odd != second_give:
                                print("Nice you won one. It's been fun but I gotta go. I swear I'm not a sore loser. I would never :/")
                            else:
                                random_odd == second_give
                                print("Wow, your luck is terrible. Welp, gotta go. It's been fun!")
                        else:
                            second_give > 4
                            print("My number: 4")
                            print("Your number: " + str(second_give))
                            print("Wow can't even play the game properly, no wonder your'e doing so bad.")
                            exit()
                else:
                    st_number == 1
                    my_number = st_number + 3
                    print("My number: " + str(my_number))
                    second_give: int = int(input("I win! You're really unlucky. Mabye your luck will change, we're going to find out. Odds out of 4. Enter number here: "))
                    if second_give <= 4:
                        print("Your number: " + str(second_give))
                        from random import randint
                        random_odd = randint(1,4)
                        print("My number: " + str(random_odd))
                        if random_odd != second_give:
                            print("Nice you won one. It's been fun but I gotta go. I swear I'm not a sore loser. I would never :/")
                        else:
                            random_odd == second_give
                            print("Wow, your luck is terrible. Welp, gotta go. It's been fun!")
                    else:
                        second_give > 4
                        print("My number: 4")
                        print("Your number: " + str(second_give))
                        print("Hey your'e not within our odds of 4.")
                        second_give: int = int(input("Enter number here: "))
                        if second_give <= 4: 
                            print("Your number: " + str(second_give))
                            from random import randint
                            random_odd = randint(1,4)
                            print("My number: " + str(random_odd))
                            if random_odd != second_give:
                                print("Nice you won one. It's been fun but I gotta go. I swear I'm not a sore loser. I would never :/")
                            else:
                                random_odd == second_give
                                print("Wow, your luck is terrible. Welp, gotta go. It's been fun!")
                        else:
                            second_give > 4
                            print("My number: 4")
                            print("Your number: " + str(second_give))
                            print("Wow can't even play the game properly, no wonder your'e doing so bad.")
                            exit()
            else:
                st_number > give_me_odds
                print("My number: 1")
                print("Your number: " + str(st_number))
                print("Hey your number isn't within odds")
                st_number: int = int(input("Your number needs to be within your odds, it can't be over odds or below 1. Try again, enter your number: "))
                if st_number <= 10:
                    print("Your number: " + str(st_number))
                    if st_number > 1:
                        my_number = st_number - 1
                        print("My number: " + str(my_number))
                        second_give: int = int(input("I win! You're really unlucky. Mabye your luck will change, we're going to find out. Odds out of 4. Enter number here: "))
                        if second_give <= 4:
                            print("Your number: " + str(second_give))
                            from random import randint
                            random_odd = randint(1,4)
                            print("My number: " + random_odd)
                            if random_odd != second_give:
                                print("Nice you won one. It's been fun but I gotta go. I swear I'm not a sore loser. I would never :/")
                            else:
                                random_odd == second_give
                                print("Wow, your luck is terrible. Welp, gotta go. It's been fun!")
                        else:
                            second_give > 4
                            print("My number: 4")
                            print("Your number: " + str(second_give))
                            print("Hey your'e not within our odds of 4.")
                            second_give: int = int(input("Enter number here: "))
                            if second_give <= 4: 
                                print("Your number: " + str(second_give))
                                from random import randint
                                random_odd = randint(1,4)
                                print("My number: " + str(random_odd))
                                if random_odd != second_give:
                                    print("Nice you won one. It's been fun but I gotta go. I swear I'm not a sore loser. I would never :/")
                                else:
                                    random_odd == second_give
                                    print("Wow, your luck is terrible. Welp, gotta go. It's been fun!")
                            else:
                                second_give > 4
                                print("My number: 4")
                                print("Your number: " + str(second_give))
                                print("Wow can't even play the game properly, no wonder your'e doing so bad.")
                                exit()
                    else:
                        st_number == 1
                        my_number = st_number + 3
                        print("My number: " + str(my_number))
                        second_give: int = int(input("I win! You're really unlucky. Mabye your luck will change, we're going to find out. Odds out of 4. Enter number here: "))
                        if second_give <= 4:
                            print("Your number: " + str(second_give))
                            from random import randint
                            random_odd = randint(1,4)
                            print("My number: " + str(random_odd))
                            if random_odd != second_give:
                                print("Nice you won one. It's been fun but I gotta go. I swear I'm not a sore loser. I would never :/")
                            else:
                                random_odd == second_give
                                print("Wow, your luck is terrible. Welp, gotta go. It's been fun!")
                        else:
                            second_give > 4
                            print("My number: 4")
                            print("Your number: " + str(second_give))
                            print("Hey your'e not within our odds of 4.")
                            second_give: int = int(input("Enter number here: "))
                            if second_give <= 4: 
                                print("Your number: " + str(second_give))
                                from random import randint
                                random_odd = randint(1,4)
                                print("My number: " + str(random_odd))
                                if random_odd != second_give:
                                    print("Nice you won one. It's been fun but I gotta go. I swear I'm not a sore loser. I would never :/")
                                else:
                                    random_odd == second_give
                                    print("Wow, your luck is terrible. Welp, gotta go. It's been fun!")
                            else:
                                second_give > 4
                                print("My number: 4")
                                print("Your number: " + str(second_give))
                                print("Wow can't even play the game properly, no wonder your'e doing so bad.")
                                exit()
                else: 
                    st_number > 10
                    print("My number: 4")
                    print("Your number: " + str(st_number))
                    print("Well I can't play with you not following instructions.")
                    exit()
        else:
            give_me_odds <= 2
            print("Wow, if you're going to be this stubborn, then I won't play. :( ")
            exit()  
else:
    starting_it != str("okay")
    starting_it: str = input("So you dont want to play a practice game? All you have to say type is \"okay\": ") 

    if starting_it == str("okay"): 
        give_me_odds: int = int(input("I dare you to play, odds? "))
        st_number: int = int(input("Ok now that we have odds, type your number and when you hit enter I will type mine. Enter number: "))
        if st_number <= give_me_odds:
            print("Your number: " + str(st_number))
            print("My number: " + str(st_number))
            print("Looks like I won! Now you have to play another game of odds. That was the dare after all.")
            print("I'm giving my odds of 10, if you don't guess my number then we're playing another game! :)")
            st_number: int = int(input("Ok now that we have odds, type your number and when you hit enter I will type mine. Enter number: "))
            if st_number <= 10:
                print("Your number: " + str(st_number))
                if st_number > 1:
                    my_number = st_number - 1
                    print("My number: " + str(my_number))
                    second_give: int = int(input("I win! You're really unlucky. Mabye your luck will change, we're going to find out. Odds out of 4. Enter number here: "))
                    if second_give <= 4:
                        print("Your number: " + str(second_give))
                        from random import randint
                        random_odd = randint(1,4)
                        print("My number: " + str(random_odd))
                        if random_odd != second_give:
                            print("Nice you won one. It's been fun but I gotta go. I swear I'm not a sore loser. I would never :/")
                        else:
                            random_odd == second_give
                            print("Wow, your luck is terrible. Welp, gotta go. It's been fun!")
                    else:
                        second_give > 4
                        print("My number: 4")
                        print("Your number: " + str(second_give))
                        print("Hey your'e not within our odds of 4.")
                        second_give: int = int(input("Enter number here: "))
                        if second_give <= 4: 
                            print("Your number: " + str(second_give))
                            from random import randint
                            random_odd = randint(1,4)
                            print("My number: " + str(random_odd))
                            if random_odd != second_give:
                                print("Nice you won one. It's been fun but I gotta go. I swear I'm not a sore loser. I would never :/")
                            else:
                                random_odd == second_give
                                print("Wow, your luck is terrible. Welp, gotta go. It's been fun!")
                        else:
                            second_give > 4
                            print("My number: 4")
                            print("Your number: " + str(second_give))
                            print("Wow can't even play the game properly, no wonder your'e doing so bad.")
                            exit()
                else:
                    st_number == 1
                    my_number = st_number + 3
                    print("My number: " + str(my_number))
                    second_give: int = int(input("I win! You're really unlucky. Mabye your luck will change, we're going to find out. Odds out of 4. Enter number here: "))
                    if second_give <= 4:
                        print("Your number: " + str(second_give))
                        from random import randint
                        random_odd = randint(1,4)
                        print("My number: " + str(random_odd))
                        if random_odd != second_give:
                            print("Nice you won one. It's been fun but I gotta go. I swear I'm not a sore loser. I would never :/")
                        else:
                            random_odd == second_give
                            print("Wow, your luck is terrible. Welp, gotta go. It's been fun!")
                    else:
                        second_give > 4
                        print("My number: 4")
                        print("Your number: " + str(second_give))
                        print("Hey your'e not within our odds of 4.")
                        second_give: int = int(input("Enter number here: "))
                        if second_give <= 4: 
                            print("Your number: " + str(second_give))
                            from random import randint
                            random_odd = randint(1,4)
                            print("My number: " + str(random_odd))
                            if random_odd != second_give:
                                print("Nice you won one. It's been fun but I gotta go. I swear I'm not a sore loser. I would never :/")
                            else:
                                random_odd == second_give
                                print("Wow, your luck is terrible. Welp, gotta go. It's been fun!")
                        else:
                            second_give > 4
                            print("My number: 4")
                            print("Your number: " + str(second_give))
                            print("Wow can't even play the game properly, no wonder your'e doing so bad.")
                            exit()
            else:
                st_number > give_me_odds
                print("My number: 1")
                print("Your number: " + str(st_number))
                print("Hey your number isn't within odds")
                st_number: int = int(input("Your number needs to be within your odds, it can't be over odds or below 1. Try again, enter your number: "))
                if st_number <= 10:
                    print("Your number: " + str(st_number))
                    if st_number > 1:
                        my_number = st_number - 1
                        print("My number: " + str(my_number))
                        second_give: int = int(input("I win! You're really unlucky. Mabye your luck will change, we're going to find out. Odds out of 4. Enter number here: "))
                        if second_give <= 4:
                            print("Your number: " + str(second_give))
                            from random import randint
                            random_odd = randint(1,4)
                            print("My number: " + str(random_odd))
                            if random_odd != second_give:
                                print("Nice you won one. It's been fun but I gotta go. I swear I'm not a sore loser. I would never :/")
                            else:
                                random_odd == second_give
                                print("Wow, your luck is terrible. Welp, gotta go. It's been fun!")
                        else:
                            second_give > 4
                            print("My number: 4")
                            print("Your number: " + str(second_give))
                            print("Hey your'e not within our odds of 4.")
                            second_give: int = int(input("Enter number here: "))
                            if second_give <= 4: 
                                print("Your number: " + str(second_give))
                                from random import randint
                                random_odd = randint(1,4)
                                print("My number: " + str(random_odd))
                                if random_odd != second_give:
                                    print("Nice you won one. It's been fun but I gotta go. I swear I'm not a sore loser. I would never :/")
                                else:
                                    random_odd == second_give
                                    print("Wow, your luck is terrible. Welp, gotta go. It's been fun!")
                            else:
                                second_give > 4
                                print("My number: 4")
                                print("Your number: " + str(second_give))
                                print("Wow can't even play the game properly, no wonder your'e doing so bad.")
                                exit()
                    else:
                        st_number == 1
                        my_number = st_number + 3
                        print("My number: " + str(my_number))
                        second_give: int = int(input("I win! You're really unlucky. Mabye your luck will change, we're going to find out. Odds out of 4. Enter number here: "))
                        if second_give <= 4:
                            print("Your number: " + str(second_give))
                            from random import randint
                            random_odd = randint(1,4)
                            print("My number: " + str(random_odd))
                            if random_odd != second_give:
                                print("Nice you won one. It's been fun but I gotta go. I swear I'm not a sore loser. I would never :/")
                            else:
                                random_odd == second_give
                                print("Wow, your luck is terrible. Welp, gotta go. It's been fun!")
                        else:
                            second_give > 4
                            print("My number: 4")
                            print("Your number: " + str(second_give))
                            print("Hey your'e not within our odds of 4.")
                            second_give: int = int(input("Enter number here: "))
                            if second_give <= 4: 
                                print("Your number: " + str(second_give))
                                from random import randint
                                random_odd = randint(1,4)
                                print("My number: " + str(random_odd))
                                if random_odd != second_give:
                                    print("Nice you won one. It's been fun but I gotta go. I swear I'm not a sore loser. I would never :/")
                                else:
                                    random_odd == second_give
                                    print("Wow, your luck is terrible. Welp, gotta go. It's been fun!")
                            else:
                                second_give > 4
                                print("My number: 4")
                                print("Your number: " + str(second_give))
                                print("Wow can't even play the game properly, no wonder your'e doing so bad.")
                                exit()
                else: 
                    st_number > 10
                    print("My number: 4")
                    print("Your number: " + str(st_number))
                    print("Well I can't play with you not following instructions.")  
                    exit()
    else:
        give_me_odds <= 2
        give_me_odds: int = int(input("You need to give me a number of 2 or above, otherwise it's just a dare. Odds? "))

        if give_me_odds >= 2:
            st_number: int = int(input("Ok now that we have odds, type your number and when you hit enter I will type mine. Enter number: "))
            print("Your number: " + str(st_number))
            print("My number: " + str(st_number))
            print("Looks like I won! Now you have to play another game of odds. That was the dare after all.")
            print("I'm giving my odds of 10, if you don't guess my number then we're playing another game! :)")
            st_number: int = int(input("Ok now that we have odds, type your number and when you hit enter I will type mine. Enter number: "))
            if st_number <= 10:
                print("Your number: " + str(st_number))
                if st_number > 1:
                    my_number = st_number - 1
                    print("My number: " + str(my_number))
                    second_give: int = int(input("I win! You're really unlucky. Mabye your luck will change, we're going to find out. Odds out of 4. Enter number here: "))
                    if second_give <= 4:
                        print("Your number: " + str(second_give))
                        from random import randint
                        random_odd = randint(1,4)
                        print("My number: " + str(random_odd))
                        if random_odd != second_give:
                            print("Nice you won one. It's been fun but I gotta go. I swear I'm not a sore loser. I would never :/")
                        else:
                            random_odd == second_give
                            print("Wow, your luck is terrible. Welp, gotta go. It's been fun!")
                    else:
                        second_give > 4
                        print("My number: 4")
                        print("Your number: " + str(second_give))
                        print("Hey your'e not within our odds of 4.")
                        second_give: int = int(input("Enter number here: "))
                        if second_give <= 4: 
                            print("Your number: " + str(second_give))
                            from random import randint
                            random_odd = randint(1,4)
                            print("My number: " + str(random_odd))
                            if random_odd != second_give:
                                print("Nice you won one. It's been fun but I gotta go. I swear I'm not a sore loser. I would never :/")
                            else:
                                random_odd == second_give
                                print("Wow, your luck is terrible. Welp, gotta go. It's been fun!")
                        else:
                            second_give > 4
                            print("My number: 4")
                            print("Your number: " + str(second_give))
                            print("Wow can't even play the game properly, no wonder your'e doing so bad.")
                            exit()
                else:
                    st_number == 1
                    my_number = st_number + 3
                    print("My number: " + str(my_number))
                    second_give: int = int(input("I win! You're really unlucky. Mabye your luck will change, we're going to find out. Odds out of 4. Enter number here: "))
                    if second_give <= 4:
                        print("Your number: " + str(second_give))
                        from random import randint
                        random_odd = randint(1,4)
                        print("My number: " + str(random_odd))
                        if random_odd != second_give:
                            print("Nice you won one. It's been fun but I gotta go. I swear I'm not a sore loser. I would never :/")
                        else:
                            random_odd == second_give
                            print("Wow, your luck is terrible. Welp, gotta go. It's been fun!")
                    else:
                        second_give > 4
                        print("My number: 4")
                        print("Your number: " + str(second_give))
                        print("Hey your'e not within our odds of 4.")
                        second_give: int = int(input("Enter number here: "))
                        if second_give <= 4: 
                            print("Your number: " + str(second_give))
                            from random import randint
                            random_odd = randint(1,4)
                            print("My number: " + str(random_odd))
                            if random_odd != second_give:
                                print("Nice you won one. It's been fun but I gotta go. I swear I'm not a sore loser. I would never :/")
                            else:
                                random_odd == second_give
                                print("Wow, your luck is terrible. Welp, gotta go. It's been fun!")
                        else:
                            second_give > 4
                            print("My number: 4")
                            print("Your number: " + str(second_give))
                            print("Wow can't even play the game properly, no wonder your'e doing so bad.")
                            exit()
            else:
                st_number > give_me_odds
                print("My number: 1")
                print("Your number: " + str(st_number))
                print("Hey your number isn't within odds")
                st_number: int = int(input("Your number needs to be within your odds, it can't be over odds or below 1. Try again, enter your number: "))
                if st_number <= 10:
                    print("Your number: " + str(st_number))
                    if st_number > 1:
                        my_number = st_number - 1
                        print("My number: " + str(my_number))
                        second_give: int = int(input("I win! You're really unlucky. Mabye your luck will change, we're going to find out. Odds out of 4. Enter number here: "))
                        if second_give <= 4:
                            print("Your number: " + str(second_give))
                            from random import randint
                            random_odd = randint(1,4)
                            print("My number: " + random_odd)
                            if random_odd != second_give:
                                print("Nice you won one. It's been fun but I gotta go. I swear I'm not a sore loser. I would never :/")
                            else:
                                random_odd == second_give
                                print("Wow, your luck is terrible. Welp, gotta go. It's been fun!")
                        else:
                            second_give > 4
                            print("My number: 4")
                            print("Your number: " + str(second_give))
                            print("Hey your'e not within our odds of 4.")
                            second_give: int = int(input("Enter number here: "))
                            if second_give <= 4: 
                                print("Your number: " + str(second_give))
                                from random import randint
                                random_odd = randint(1,4)
                                print("My number: " + str(random_odd))
                                if random_odd != second_give:
                                    print("Nice you won one. It's been fun but I gotta go. I swear I'm not a sore loser. I would never :/")
                                else:
                                    random_odd == second_give
                                    print("Wow, your luck is terrible. Welp, gotta go. It's been fun!")
                            else:
                                second_give > 4
                                print("My number: 4")
                                print("Your number: " + str(second_give))
                                print("Wow can't even play the game properly, no wonder your'e doing so bad.")
                                exit()
                    else:
                        st_number == 1
                        my_number = st_number + 3
                        print("My number: " + str(my_number))
                        second_give: int = int(input("I win! You're really unlucky. Mabye your luck will change, we're going to find out. Odds out of 4. Enter number here: "))
                        if second_give <= 4:
                            print("Your number: " + str(second_give))
                            from random import randint
                            random_odd = randint(1,4)
                            print("My number: " + str(random_odd))
                            if random_odd != second_give:
                                print("Nice you won one. It's been fun but I gotta go. I swear I'm not a sore loser. I would never :/")
                            else:
                                random_odd == second_give
                                print("Wow, your luck is terrible. Welp, gotta go. It's been fun!")
                        else:
                            second_give > 4
                            print("My number: 4")
                            print("Your number: " + str(second_give))
                            print("Hey your'e not within our odds of 4.")
                            second_give: int = int(input("Enter number here: "))
                            if second_give <= 4: 
                                print("Your number: " + str(second_give))
                                from random import randint
                                random_odd = randint(1,4)
                                print("My number: " + str(random_odd))
                                if random_odd != second_give:
                                    print("Nice you won one. It's been fun but I gotta go. I swear I'm not a sore loser. I would never :/")
                                else:
                                    random_odd == second_give
                                    print("Wow, your luck is terrible. Welp, gotta go. It's been fun!")
                            else:
                                second_give > 4
                                print("My number: 4")
                                print("Your number: " + str(second_give))
                                print("Wow can't even play the game properly, no wonder your'e doing so bad.")
                                exit()
                else: 
                    st_number > 10
                    print("My number: 4")
                    print("Your number: " + str(st_number))
                    print("Well I can't play with you not following instructions.")
                    exit()
        else:
            give_me_odds <= 2
            print("Wow, if you're going to be this stubborn, then I won't play. :( ")
            exit()  