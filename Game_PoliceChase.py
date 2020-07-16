#Define Variable
lr = ["left", "right"]
yn = ["yes", "no"]
combat = ["shoot", "hold fire"]
detain = ["handcuff", "ignore"]

#Starting Condition
response = " "
while response not in yn:
    print("\nA call comes in over the radio...\n")
    print("Shots fired at 38 Walnut... I repeat shots fired.")
    print("10-999 officer down, requesting backup immediately!")
    response = input("\nDo you take the call?\nyes/no\n")
    if response == "yes":
            print("\nYou turn on your sirens and race to the address!")
    elif response == "no":
            print("\nThe donut you are eating is far too tasty to leave.")
            quit()
    else:
            print("Apologies, dispatch didn't catch that. Come again?")

#arrival scenario
response = " "
while response not in combat:
    print("\nA naked Charlie holding barbeque tongs charges at you from the front door.")
    print("\nYou pull out your gun.")
    response = input("Do you take the shot?\nyes/no\n")
    if response == "yes":
            print("\nYou drop the man with two shots in the chest. He is dead.")
            print("You move into the entrance of the house")
    elif response == "no":
            print("\nHe gashes out your windpipe. Your gargling does not resemble the scream you attempt to make.")
            quit()
    else:
            print("Apologies, dispatch didn't catch that. Come again?")
