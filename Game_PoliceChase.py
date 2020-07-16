#Define Variable
lr = ["left", "right"]
yn = ["yes", "no"]
l_o=["law", "order"]
combat = ["shoot", "hold fire"]
detain = ["handcuff", "ignore"]

#Integer generator
from random import *
for x in range(1):
    value = randint(1, 9)

#Starting Condition
response = " "
while response not in yn:
    while True:
        print("\nA call comes in over the radio...\n")
        print("Shots fired at 38 Walnut... I repeat shots fired.")
        print("10-999 officer down, requesting backup immediately!")
        response = input("\nDo you take the call?\n...yes/no...\n")
        if response == "yes":
                print("\nYou turn on your sirens and race to the address!")
                break
        elif response == "no":
                print("\nThe donut you are eating is far too tasty to leave.")
                quit()
        else:
                print("\nApologies, dispatch didn't catch that. Come again?\n")

#Naked Charlie scenario
response = " "
while response not in combat:
    while True:
        print("\nA naked Man holding barbeque tongs charges at you from the front door.")
        print("Now the tongs don't seem that particularly dangerous.")
        print("This fellow however, is enormous in stature.")
        print("\nYou pull out your gun.")
        response = input("Do you take the shot?\n...shoot/hold fire...\n")
        if response == "shoot":
                print("\nYou shoot the man twice in the chest.")
                print("He hits the pavement so hard that some of his face peels off.")
                print("You move into the entrance of the house")
                break
        elif response == "hold fire":
                print("\nHe gashes out your windpipe. Your gargling does not resemble the scream")
                print("that you you attempt to make.")
                print("\nYou died, try again.")
                quit()
        else:
                print("\nApologies, dispatch didn't catch that. Come again?\n")

#Injured scenario
response = " "
while response not in detain:
    while True:
        print("\nYou check the mud room for signs of life. none.")
        print("You make your way into the living room, still nobody.")
        print("As you turn the corner to the staircase you see a middle-aged woman squirming on the floor.")
        print("It looks like she might be armed but you aren't sure.")
        response = input("\nShe seems totally distracted, should you handcuff her anyway?\n...handcuff/ignore...\n")
        if response == "handcuff":
                print("\nAs you approach her with the handcuffs she reveals a pistol she had been hiding.")
                print("She looks you dead in the face. Takes aim at your head; an pulls the trigger before you can flinch.")
                print("\nYou died, try again.")
                quit()
        elif response == "ignore":
                print("\nYou keep your distance and move towards the stairs. She ignores you.")
                print("As you walk past her you see there is a gun tucked into her pants.")
                print("You pull out your gun and command her to disarm herself.")
                break
        else:
                print("\nApologies, dispatch didn't catch that. Come again?\n")

#Nonsense gun jam
response = " "
while response not in combat:
    while True:
        print("\nShe reaches for her gun and takes it out slowly.")
        print("You warn her the if she moves the gun any more that you will open fire.")
        print("She quickly brings the barrel of the gun up to her chin.")
        response = input("Do you take the shot?\n...shoot/hold fire...\n")
        if response == "shoot":
                print("\nYour gun jams up.")
                print("She keeps the gun trained on herself.")
                print("You quickly fix the jam.")
                break
        elif response == "hold fire":
                print("\nShe keeps the gun trained on herself.")
                break
        else:
                print("\nApologies, dispatch didn't catch that. Come again?\n")

#Law or Order?
response = " "
while response not in l_o:
    while True:
        print("\nShe doesn't move at all. Her eyes are closed")
        print("She asks you")
        print("...What is more important, law or order?...")
        response = input("\nWhat is your reply?\n...law/order...\n")
        if response == "law":
                print("\nShe fires a bullet into her head.")
                print("The wall becomes splattered with blood.\n")
                break
        elif response == "order":
                print("\n...I'm glad we are on the same page...")
                print("With that she rolls along the floor.")
                print("You fire off a couple of shots but miss.")
                print("With a well placed bullet. She ends your life.")
                print("\nYou died, try again.")
                quit()
        else:
                print("\nApologies, dispatch didn't catch that. Come again?\n")

#Upstairs
response = " "
while response not in lr:
    while True:
        print("...Well alright then.\n")
        print("You make your way up the stairs.")
        print("At the top of the stairs are two doors.\n")
        print("The door to the left has a dog barking behind it. Sounds big.")
        print("The door to the right contains a man and a woman screaming. It sounds violent.")
        response = input("\nWhich door do you enter?\n...left/right...\n")
        if response == "left":
                print("You walk into the room and see a massive pitbull.")
                print("The pitbull poises for a fight.")
                print("A gunshot goes off in the room across.")
                print("The gunshot startles the dog who pounces on you.")
                print("Your jugular is cut within seconds.")
                print("\nYou died, try again.")
                quit()
        elif response == "right":
                print("\nYou enter the screaming match.\n")
                break
        else:
                print("\nApologies, dispatch didn't catch that. Come again?\n")

#Couple fighting
response = " "
while response not in combat:
    while True:
        print("Inside of the room you find a woman on top of the man choking him.")
        print("He looks near death.")
        print("A few feet from the door lies the dead officer.")
        print("You point your gun at the woman and command her to stand down.")
        print("She does not.\n")
        response = input("Do you shoot her?\n...shoot/hold fire...\n")
        if response == "shoot":
                print("\nYou hit her in the shoulder.")
                print("She falls down off of the man.")
                print("You move quickly to handcuff the two.")
                print("You do so handily. Neither are in a place to resist.")
                break
        elif response == "hold fire":
                print("You decide instead to tackle her off of him.")
                print("You charge, knocking her off of him.")
                print("As you work to handcuff her you feel a sharp pain in your thigh.")
                print("The man on the floor stabbed you")
                print("In this time. The woman goes for the dead officers gun.")
                print("She fires on the both of you.")
                print("\nYou died, try again.")
                quit()
        else:
                print("\nApologies, dispatch didn't catch that. Come again?\n")

#Help arrives
response = " "
while response not in yn:
    while True:
        print("\nAnother officer appears in the doorway. He says he's with two others.")
        print("You go back downstairs with the officers to regroup.")
        print("One of the officers notices a cavern dug into the ground")
        print("The rookie officer suggests going in.\n")
        response = input("Do you go in?\n...yes/no...\n")
        if response == "yes":
                print("\nThe four of you enter the cavern entrance.")
                print("The cavern only has room for one at a time.")
                print("You enter single file with guns drawn. You are at the front of course")
                break
        elif response == "no":
                print("\nWhat does the house cavern not interest you enough?")
                print("Try again.")
        else:
                print("\nApologies, dispatch didn't catch that. Come again?\n")

#Finale
response = " "
while response not in combat:
    while True:
        print("\nYou are the first to get to the end of the cavern due to a shoelace malfunction.")
        print("You find yourself in a full blown cave.")
        print("You enter into the cave and hide behind a boulder.\n")
        print("You see this many people patrolling a pile of dead bodies: {} people".format(value))
        print("They are armed, you have a clear shot and the element of surprise.")
        response = input("Do you begin firing?\n...shoot/hold fire...\n")
        if value>4:
                if response == "hold fire":
                    print("\nWise decision. You wait for your fellow officers.")
                    print("Once they arrive you open fire.")
                    print("All threats are neutralized.\n")
                    break
                elif response == "shoot":
                    print("\nYou open fire on the people.")
                    print("You tag a couple, however they have superior firepower.")
                    print("You are holier than the pope once they finish firing on you.")
                    quit()
                else:
                    print("\nApologies, dispatch didn't catch that. Come again?\n")
        else:
                if response == "shoot":
                    print("\nYou open fire without discretion.")
                    print("With the surprise nobody has time to shoot back.")
                    print("It's a massacre.\n")
                    break
                elif response == "hold fire":
                    print("\nYou wait for your fellow officers.")
                    print("In your clumsiness you fall out of cover.")
                    print("You are quickly shot dead.")
                    quit()
                else:
                    print("\nApologies, dispatch didn't catch that. Come again?\n")

#Epilogue
print("Following the firefight you leave the house.")
print("You can't stop shaking")
print("You'll surely get a medal for this\n")
print("YOU WIN")
