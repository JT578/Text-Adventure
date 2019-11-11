import random
import time



print(
    "You are walking on a trail in a  wide plain. There a no trees or animals in site.You can only see two things: An old run-down house, and a castle off in the distance.")


def main(money=0):
    health = 10
    ans = input("Which way would you choose? 1) 2)")
    # SECTION 1
    if ans == "1":
        print("You walk to the house. . .")
        time.sleep(2)
        print(
            "At the Entrance of the House there is a sign that says 'He who enters, shall not leave. He who goes, shall be a toad'")
        ans1 = input(" Do you go in? yes or no ")
        if ans1 == "yes":
            door_close = random.randint(1, 100)
            if door_close > 99:
                # FIX FIX TO WORK. THIS IS FOR GETTING DIFFERENT PATH
                print("\nAll of a sudden the door slams behind you. You are now locked in. . .")
                time.sleep(2)
                print("\nYou have come to the conculsion you have to look around to get out.")
                time.sleep(1)
                print("\nYou start looking around. . .")
                time.sleep(4)
                print("You see on a table something shiny. You walk over to it.")
                print("It Turns out you found $10! You now have $10 in your account!")
                money += 10
                time.sleep(5)
                print("You decide to keep looking")
                print("\nThere is a door that leads to the basement and a door that leads to the attic.")

                goin = input("Which do you choose? 1) 2)")

                if goin == "2":
                    print("You walk up the stairs. . .  WORK ON")

                else:
                    print("You walk down the dark stairs to the basement. WORK ON ")
            else:
                print("The door started to close but you quickly lept outside.")
                time.sleep(4)
                creature_attack = random.randint(0, 100)
                if creature_attack > 20:
                    #CHANGE TO MAKE IT WORK. FOR THE PROGRAM MAINTENANCE
                    print("You start to wander back to the trail, but all of a sudden you see a huge creature running at you from a long distance")
                    fight_run = input("You you fight or do you run? 1) 2)")
                    if fight_run == "1":
                        print("The monster rushes up to you.")
                        fight_random = random.randint(0, 100)
                        if fight_random < 30:
                            #CHANGE TO MAKE IT WORK. FOR THE PROGRAM MAINTENANCE
                            print("The beast slashed you with his tail of knives. - 3 hp.")
                            health -= 3
                            print(health)
                            print("Total Hp")
                            fight_random_2 = random.randint(0, 100)
                            if fight_random_2 > 30:
                                attack_monster_1 = input("Quick, push a to attack")
                                if attack_monster_1 == "a" or "A":
                                    print("You punch his face as hard as you can, and you luckily knocked him out.")

                                else:
                                    "Please Enter a Valid Answer. (a, or A)"
                            elif fight_random_2 < 30:
                                attack_montster_2 = input("Quick, push a to attack.")
                                if attack_montster_2 == "a" or "A":
                                    print("You punch the beast, but he rams his tail into you agian.")
                                    print("There is blood everywhere. Everything is starting to go dim. . . ")
                                    time.sleep(3)
                                    print("You Died")


                        elif fight_random < 40:
                            print("The beast charged into you and threw you to the ground. -2hp")
                            health -= 2
                            print(health)
                            print("Total Hp")
                            print("WORK ON THIS")


                    elif fight_run == "2":
                        print("You run qucikly away from the beast. You keep running, and running and running.")
                        print("Eventually the creature gets tired from running and turns around. Your now in the clear.")
                else:
                    print("The moster saw you, but instead of attacking you, it sprinted in the opposite direction. Hmm weird.")
                    print("WORK ON THIS")
    elif ans == "2":
        print("You run to the castle because you really don't want to be around here anymore. It's kind of a creepy, eerie place.")
        time.sleep(5)
        print("Once you reach the castle, immediately you notice movement in the left tower.")
        go_in2 = input("Do you want to knock on the doors and find a backdoor? 1) 2)")
        if go_in2 == "1":
            print("WORK ON")







    else:
        # SECTION 2
        print("Section 2")


main()
