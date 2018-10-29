#Cody Dzierzon
#10/22/18
#1st term Final Project


def opening_page():

        art_1 = print("""
                              ___  ____   __    ___  ____ 
                             / __)(  _ \ /__\  / __)( ___)
                             \__ \ )___//(__)\( (__  )__) 
                             (___/(__) (__)(__)\___)(____)
          ____  _  _  ____  __    _____  ____    __   ____  ____  _____  _  _ 
         ( ___)( \/ )(  _ \(  )  (  _  )(  _ \  /__\ (_  _)(_  _)(  _  )( \( )
          )__)  )  (  )___/ )(__  )(_)(  )   / /(__)\  )(   _)(_  )(_)(  )  ( 
         (____)(_/\_)(__)  (____)(_____)(_)\_)(__)(__)(__) (____)(_____)(_)\_)""")

        print()
        print()

        art_2 = print("""
        / \ / \ / \ / \ / \ / \ / \   / \ / \   / \ / \ / \ / \ / \ / \ / \ / \ 
       ( J | o | u | r | n | e | y ) ( t | o ) ( M | e | r | a | k | o | o | o )
        \_/ \_/ \_/ \_/ \_/ \_/ \_/   \_/ \_/   \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ """)
        print()
        print()
        print("""
        You have recently finished your training to be a NASA astronaut, and you are preparing for your first mission.
         """)
        the_ship()



def game_over():

        art_3 = print("""

 #####     #    #     # #######    ####### #     # ####### ######  
#     #   # #   ##   ## #          #     # #     # #       #     # 
#        #   #  # # # # #          #     # #     # #       #     # 
#  #### #     # #  #  # #####      #     # #     # #####   ######  
#     # ####### #     # #          #     #  #   #  #       #   #   
#     # #     # #     # #          #     #   # #   #       #    #  
 #####  #     # #     # #######    #######    #    ####### #     # 
                                                                    """)
        return opening_page()

def game_won():

        art_4 = print("""

#     # ####### #     #    #     # ####### #     # ### 
 #   #  #     # #     #    #  #  # #     # ##    # ### 
  # #   #     # #     #    #  #  # #     # # #   # ### 
   #    #     # #     #    #  #  # #     # #  #  #  #  
   #    #     # #     #    #  #  # #     # #   # #     
   #    #     # #     #    #  #  # #     # #    ## ### 
   #    #######  #####      ## ##  ####### #     # ### """)

        return opening_page()

def the_ship():
        print("""
        You and your team have entered the spaceship and are ready to take off. You still don't know why you are going
        or where you are going, but you are still excited to be going to space.""")
        print()
        launch = input("Would you like to proceed in launching? yes or no: ").lower()

        if launch == "yes":
                print("10..9..8..7..6..5..4..3..2..1.. LIFT OFF")
                return destination_one()

        if launch == "no":
                return game_over()

        else:
                print("that is not a valid response")
                return the_ship()

def destination_one():
        print("""As soon as you left the Earth's atmosphere, you lost communication with the control room, because you and your
        team were never told where you were going, you get to decide.""")
        print()
        dec_des = input("Where would you like to go? Moon or Venus: ").lower()

        if dec_des == "moon":
                print("great choice")
                return the_moon()

        if dec_des == "venus":
                print("That is not the best choice you have ever made, you and your team aren't equipped to survive on Venus")
                return game_over()
                
        else:
                print("that is not a valid response")
                return destination_one()

def the_moon():
        print("""
#    #  ####   ####  #    # 
##  ## #    # #    # ##   # 
# ## # #    # #    # # #  # 
#    # #    # #    # #  # # 
#    # #    # #    # #   ## 
#    #  ####   ####  #    # """)
        print("""

You have successfully landed on the Moon, the radar on your ship says that there is something to the east and to the west.""")
        print()
        dec_ex = input("Would you like to explore the Moon or continue traveling? east, west or continue: ").lower()

        if dec_ex == "east":
                print("You traveled east with your team for almost an hour before you came upon the American flag.")
                return american_flag()

        if dec_ex == "west":
                print("It didn't take long for you and your team to find a giant crater that looked like it never ended.")
                return big_crater()

        if dec_ex == "continue":
                return mars_jup()

        else:
                print("that is not a valid response")
                return the_moon()

def american_flag():
        print("""
  ##   #    # ###### #####  #  ####    ##   #    #    ###### #        ##    ####  
 #  #  ##  ## #      #    # # #    #  #  #  ##   #    #      #       #  #  #    # 
#    # # ## # #####  #    # # #      #    # # #  #    #####  #      #    # #      
###### #    # #      #####  # #      ###### #  # #    #      #      ###### #  ### 
#    # #    # #      #   #  # #    # #    # #   ##    #      #      #    # #    # 
#    # #    # ###### #    # #  ####  #    # #    #    #      ###### #    #  ####  """)
        print("You have found an historic monument of when man first stepped on the moon.")
        ret_ship1 = input("Do you want to go back to the ship? yes or no: ").lower()
        
        if ret_ship1 == "yes":
                return the_moon()

        if ret_ship1 == "no":
                return american_flag()
        
        else:
                print("that is not a valid response")
                return american_flag()

def big_crater():
        print("""
 ####  #   ##   #    # #####     ####  #####    ##   ##### ###### #####  
#    # #  #  #  ##   #   #      #    # #    #  #  #    #   #      #    # 
#      # #    # # #  #   #      #      #    # #    #   #   #####  #    # 
#  ### # ###### #  # #   #      #      #####  ######   #   #      #####  
#    # # #    # #   ##   #      #    # #   #  #    #   #   #      #   #  
 ####  # #    # #    #   #       ####  #    # #    #   #   ###### #    # """)
        print("you have found a giant crater.")
        ret_ship1 = input("Do you want to go back to the ship? yes or no: ").lower()
        
        if ret_ship1 == "yes":
                return the_moon()

        if ret_ship1 == "no":
                return big_crater()

        if ret_ship2 == "jump in":
                print("you have taken a short cut to the north city")
                return north_city()
        
        else:
                print("that is not a valid response")
                return big_crater()
def mars_jup():
        print("You and your team made a group decision to fly to Mars, but on your way to Mars when you found that you didn't have enough fuel to take off again once you have landed.")
        print()
        lan_m = input("Would you like to land on Mars or continue to Jupiter? Mars or Jupiter: ").lower()
        
        if lan_m == "jupiter":
                print("As you enter the enter the astroid belt, you feel some regret about your decision.")
                return astr_b() 

        if lan_m == "mars":
                print("""
#    #   ##   #####   ####  
##  ##  #  #  #    # #      
# ## # #    # #    #  ####  
#    # ###### #####       # 
#    # #    # #   #  #    # 
#    # #    # #    #  ####  """)
                print("Your team was very close to surviving, but it just didn't work out.")
                return game_over()
                
        else:
                print("that is not a valid response")
                return mars_jup()

def astr_b():
        print(""" 
  ##    ####  ##### ###### #####   ####  # #####     #####  ###### #      ##### 
 #  #  #        #   #      #    # #    # # #    #    #    # #      #        #   
#    #  ####    #   #####  #    # #    # # #    #    #####  #####  #        #   
######      #   #   #      #####  #    # # #    #    #    # #      #        #   
#    # #    #   #   #      #   #  #    # # #    #    #    # #      #        #   
#    #  ####    #   ###### #    #  ####  # #####     #####  ###### ######   #   """)
        print("Now that you have entered the asteroid belt, a astroid is coming right at you and you have and important decision to make, you need to decide which way to dodge it")
        print()
        dodge_astr = input("Do you want to dodge the asteroid by going left or right? ").lower()

        if dodge_astr == "left":
                print("It wasn't even close and your ship got crushed.")
                return game_over()
                
        if dodge_astr == "right":
                print("You went to the right and dodged the asteroid, but another one came in and destroyed your ship")
                return game_over()
                
        if dodge_astr == "straight":
                print("You went to the straight and successfully dodged all the asteroids")
                return space_storm()
        
        else:
                print("that is not a valid response")
                return astr_b()

def space_storm():
        print("You and your team are feeling pretty good for getting through the asteroid belt and you are now approaching Jupiter")
        print("But out of nowhere, a space storm comes and engulfs your ship sending you to another solar system")

        con_1 = input("Would you like to continue? yes or no: ").lower()

        if con_1 == "yes":
            return new_ss()

        if con_1 == "no":
            print("TO BAD!!! You are going to anyway")
            return new_ss()

        else:
            print("that is not a valid response")
            return space_storm()


def new_ss():
        print("""
#    # ###### #    #     ####   ####  #        ##   #####      ####  #   #  ####  ##### ###### #    # 
##   # #      #    #    #      #    # #       #  #  #    #    #       # #  #        #   #      ##  ## 
# #  # #####  #    #     ####  #    # #      #    # #    #     ####    #    ####    #   #####  # ## # 
#  # # #      # ## #         # #    # #      ###### #####          #   #        #   #   #      #    # 
#   ## #      ##  ##    #    # #    # #      #    # #   #     #    #   #   #    #   #   #      #    # 
#    # ###### #    #     ####   ####  ###### #    # #    #     ####    #    ####    #   ###### #    # """)
        print("As you and your team enter this new solar system, you need to land quickly, because you are running out of fuel.")
        print("As far as you can see ther are two planets, the one to the left of you is a bright blue and the one to the right is orange.")
        print()
        choice_p = input("Which planet would you like to land on? left or right: ").lower()

        if choice_p == "left":
                print("You are now landing on the bright blue planet")
                return left_planet()

        if choice_p == "right":
                print("You are now landing on the right planet")
                return right_planet()

        else:
                print("that is not a valid response")
                return new_ss()

def right_planet():
        print(""" 
 ####  #####    ##   #    #  ####  ######    #####  #        ##   #    # ###### ##### 
#    # #    #  #  #  ##   # #    # #         #    # #       #  #  ##   # #        #   
#    # #    # #    # # #  # #      #####     #    # #      #    # # #  # #####    #   
#    # #####  ###### #  # # #  ### #         #####  #      ###### #  # # #        #   
#    # #   #  #    # #   ## #    # #         #      #      #    # #   ## #        #   
 ####  #    # #    # #    #  ####  ######    #      ###### #    # #    # ######   #   """)
        print("You and your team land on the orange planet, but aren't equiped to survive.")
        return game_over()
        

def left_planet():
        print("""
#####  #      #    # ######    #####  #        ##   #    # ###### ##### 
#    # #      #    # #         #    # #       #  #  ##   # #        #   
#####  #      #    # #####     #    # #      #    # # #  # #####    #   
#    # #      #    # #         #####  #      ###### #  # # #        #   
#    # #      #    # #         #      #      #    # #   ## #        #   
#####  ######  ####  ######    #      ###### #    # #    # ######   #   
                                                                        """)
        print("You have landed on the left planet, you and your team gets out to explore because you can see civilization")
        print("Your sense of direction is off, but in the distance you can see a city in what you think is north, and another city in what you think is south")
        print()
        dec_ex2 = input("What city will you travel to? north or south: ").lower()

        if dec_ex2 == "north":
                print("You and you team travel towards the north city")
                return north_city()

        if dec_ex2 == "south":
                print("You and you team travel towards the south city")
                return south_city()

        else:
                print("that is not a valid response")
                return left_planet()

def north_city():
        print("""
#    #  ####  #####  ##### #    #     ####  # ##### #   # 
##   # #    # #    #   #   #    #    #    # #   #    # #  
# #  # #    # #    #   #   ######    #      #   #     #   
#  # # #    # #####    #   #    #    #      #   #     #   
#   ## #    # #   #    #   #    #    #    # #   #     #   
#    #  ####  #    #   #   #    #     ####  #   #     #   """)
        print("When you arrive in the north city, you have a few options")
        print("There is a crowd of people you could approach, there are huts in the mountains that you see, and there is a huge stadium ")
        print()
        dec_ex3 = input("Where would you like to go? crowd, mountains, or stadium: ").lower()

        if dec_ex3 == "crowd":
                print("The crowd of people didn't like you")
                return game_over()
                
        if dec_ex3 == "mountains":
                print("Before you were able to make to the huts, a pack of strange animals attacked you")

        if dec_ex3 == "stadium":
                print("""As you enter the stadium, a strange old man approaches you. After you talk to him for a while, he tells you his
                 name is Merakooo and he offers to take you to his hut""")
                return merakooo_hut()

        else:
                print("that is not a valid response")
                return north_city()

def south_city():
        print(""" 
 ####   ####  #    # ##### #    #     ####  # ##### #   # 
#      #    # #    #   #   #    #    #    # #   #    # #  
 ####  #    # #    #   #   ######    #      #   #     #   
     # #    # #    #   #   #    #    #      #   #     #   
#    # #    # #    #   #   #    #    #    # #   #     #   
 ####   ####   ####    #   #    #     ####  #   #     #   """)
        print("You and your team arrive at the south city and can only see a few buildings and one hut")
        print()
        dec_ex4 = input("Which one will you enter? hut or buildings: ").lower()

        if dec_ex4 == "hut":
                print("The old man inside wasn't happy to see you")
                return game_over()
                
        if dec_ex4 == "buildings":
            print("That was not a good choice")
            return game_over()
            
        else:
            print("that is not a valid response")
            return south_city()

def merakooo_hut():
        print(""" 
                                             ###                               
 ####  #      #####     #    #   ##   #    # ###  ####     #    # #    # ##### 
#    # #      #    #    ##  ##  #  #  ##   #  #  #         #    # #    #   #   
#    # #      #    #    # ## # #    # # #  # #    ####     ###### #    #   #   
#    # #      #    #    #    # ###### #  # #          #    #    # #    #   #   
#    # #      #    #    #    # #    # #   ##     #    #    #    # #    #   #   
 ####  ###### #####     #    # #    # #    #      ####     #    #  ####    #   
                                                                               """)
        print("As soon as you enter the hut, the strange old man reveals his true identity...")
        print("YOU HAVE FOUND HARRY POTTER!!!")
        return game_won()
        


opening_page()
        
        



