"""Odds on is basically a dare game where someone says a number (the odds)."""
"""Then both people say a number ranging from 1 to that number."""

__author__ = "730561311"


print("Odds is a game where a person will give a number \"odds\" and both that person and the person giving a dare say a number within the odds.")
print("If they both say the same number, then the person who gave odds loses and has to do the dare.")
print("This is why most people increase the odds if they really don't want to do the dare.")

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
                my_number = st_number - 1
                print("My number: " + str(my_number))




                
            else:
                st_number > give_me_odds
                print("My number: 1")
                print("Your number: " + str(st_number))
                print("Hey your number isn't within odds")
                st_number: int = int(input("Your number needs to be within your odds, it can't be over odds or below 1. Try again, enter your number: "))
                if st_number <= 10:
                    print("Your number: " + str(st_number))
                    my_number = st_number - 1
                    print("My number: " + str(my_number))





                else: 
                    st_number > 10
                    print("My number: 4")
                    print("Your number: " + str(st_number))
                    print("Well I can't play with you not following instructions.")  
                    exit()          
        else:
            st_number > give_me_odds
            print("My number: 1")
            print("Your number: " + str(st_number))
            print("Hey your number isn't within odds")
            st_number: int = int(input("Your number needs to be within your odds, it can't be over odds or below 1. Try again, enter your number: "))

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
                my_number = st_number - 1
                print("My number: " + str(my_number))




            else:
                st_number > give_me_odds
                print("My number: 1")
                print("Your number: " + str(st_number))
                print("Hey your number isn't within odds")
                st_number: int = int(input("Your number needs to be within your odds, it can't be over odds or below 1. Try again, enter your number: "))
                if st_number <= 10:
                    print("Your number: " + str(st_number))
                    my_number = st_number - 1
                    print("My number: " + str(my_number))





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

        if give_me_odds >= 2:
            st_number: int = int(input("Ok now that we have odds, type your number and when you hit enter I will type mine. Enter number: "))
            if st_number <= give_me_odds:
                print("Your number: " + str(st_number))
                print("My number: " + str(st_number))
                print("Looks like I won! Now you have to play another game of odds. That was the dare after all.")
            else:
                st_number > give_me_odds
                print("My number: 1")
                print("Your number: " + str(st_number))
                st_number: int = int(input("Hey your number isn't within odds. Try again please, enter your number: "))
                if st_number <= give_me_odds:
                    print("Your number: " + str(st_number))
                    print("My number: " + str(st_number))
                    print("Looks like I won! Now you have to play another game of odds. That was the dare after all.")
                    print("I'm giving my odds of 10, if you don't guess my number then we're playing another game! :)")
                    st_number: int = int(input("Ok now that we have odds, type your number and when you hit enter I will type mine. Enter number: "))
                    if st_number <= 10:
                        print("Your number: " + str(st_number))
                        my_number = st_number - 1
                        print("My number: " + str(my_number))




                    else:
                        st_number > give_me_odds
                        print("My number: 1")
                        print("Your number: " + str(st_number))
                        print("Hey your number isn't within odds")
                        st_number: int = int(input("Your number needs to be within your odds, it can't be over odds or below 1. Try again, enter your number: "))
                        if st_number <= 10:
                            print("Your number: " + str(st_number))
                            my_number = st_number - 1
                            print("My number: " + str(my_number))




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
                    my_number = st_number - 1
                    print("My number: " + str(my_number))




                else:
                    st_number > give_me_odds
                    print("My number: 1")
                    print("Your number: " + str(st_number))
                    print("Hey your number isn't within odds")
                    st_number: int = int(input("Your number needs to be within your odds, it can't be over odds or below 1. Try again, enter your number: "))
                    if st_number <= 10:
                        print("Your number: " + str(st_number))
                        my_number = st_number - 1
                        print("My number: " + str(my_number))




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
        print("Can't follow instructions? If you really want to play press the up arrows until you see python - m code_ideas.odd_on and press enter.")