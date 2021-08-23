"""
This is a word adventure mini-game where the User interface is your own imagination.
Enjoy !!!
"""

name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

answer = input(
    "You are on a road, it has come to an fork and you can go left or right. Which way would you like to go? ").lower()

if answer == "left":
    answer = input(
        "You come to a river, you can walk around it or take tha boat ? Type walk to walk around and boat to take the boat : ")

    if answer == "boat":
        print("The guy rowing the boat is Charon and he takes you to underworld so you are dead now ")
    elif answer == "walk":
        print("You walked for many miles, dehydrated and died  ")
    else:
        print('Not a valid option. You lose.')

elif answer == "right":
    answer = input(
        "You come to a bridge, it looks wobbly, do you want to cross it or head back (cross/back)? ")

    if answer == "back":
        print("You get into a recursive function and lose.")
    elif answer == "cross":
        answer = input(
            "You barely cross the bridge and meet a stranger. Do you talk to them (yes/no)? ")

        if answer == "yes":
            print(
                "You talk to the stanger he transforms into your anime waifu and You WIN!")
        elif answer == "no":
            print(
                "You ignore the stranger and he turns into a crazy moster and kills you ")
        else:
            print('Not a valid option. You lose.')
    else:
        print('Not a valid option. You lose.')

else:
    print('Not a valid option. You lose.')

print("Thank you for trying", name)
