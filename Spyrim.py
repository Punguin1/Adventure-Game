from SpyrimFunc import print_slow
from SpyrimFunc import checkStr as cs
import cmd, sys, textwrap

intro = """\n

      #######
    /       ###                                           #
   /         ##                                          ###
   ##        #                                            #
    ###
   ## ###           /###    ##   ####      ###  /###    ###     ### /### /###
    ### ###        / ###  /  ##    ###  /   ###/ #### /  ###     ##/ ###/ /##  /
      ### ###     /   ###/   ##     ###/     ##   ###/    ##      ##  ###/ ###/
        ### /##  ##    ##    ##      ##      ##           ##      ##   ##   ##
          #/ /## ##    ##    ##      ##      ##           ##      ##   ##   ##
           #/ ## ##    ##    ##      ##      ##           ##      ##   ##   ##
            # /  ##    ##    ##      ##      ##           ##      ##   ##   ##
  /##        /   ##    ##    ##      ##      ##           ##      ##   ##   ##
 /  ########/    #######      #########      ###          ### /   ###  ###  ###
/     #####      ######         #### ###      ###          ##/     ###  ###  ###
|                ##                   ###
 \)              ##            #####   ###
                 ##          /#######  /#
                  ##        /      ###/

"""
death = """\n
               ...
             ;::::;
           ;::::; :;
         ;:::::'   :;
        ;:::::;     ;.
       ,:::::'       ;           OOO
       ::::::;       ;          OOOOO        you died
       ;:::::;       ;         OOOOOOOO
      ,;::::::;     ;'         / OOOOOOO
    ;:::::::::`. ,,,;.        /  / DOOOOOO
  .';:::::::::::::::::;,     /  /     DOOOO
 ,::::::;::::::;;;;::::;,   /  /        DOOO
;`::::::`'::::::;;;::::: ,#/  /          DOOO
:`:::::::`;::::::;;::: ;::#  /            DOOO
::`:::::::`;:::::::: ;::::# /              DOO
`:`:::::::`;:::::: ;::::::#/               DOO
 :::`:::::::`;; ;:::::::::##                OO
 ::::`:::::::`;::::::::;:::#                OO
 `:::::`::::::::::::;'`:;::#                O
  `:::::`::::::::;' /  / `:#
   ::::::`:::::;'  /  /   `#
"""

cs(intro + "\nPress enter to start. if you cant figure out what to do, read the code", [""], 0, False)

preAns = cs("You sneak around outside of the castle and meet with a tall wall made of stone bricks. You look closer and see some bricks are conveniently sticking out of the wall", ["climb", "scale"])

preAns = cs("You " + preAns + " up the wall using the bricks that are sticking out. As you reach the top, you notice a balcony a jump away from where you are.", ["jump", "hop", "leap", "vault", "spring"])

preAns = cs("You " + preAns + " across the gap and reach the balcony of the castle. You look inside the room and see a large library with few signs of life. To the left you see the only person in this entire room. He is sitting on a chair with a table in front and newspaper over their head to hide the fact that he is sleeping on his job. When you saw that it was safe, you silently enter the room. Behind the guard there is a vent, and to the right of him there is an exit door.", ["vent", "behind", "right", "door", "exit"])

if (preAns == "vent" or preAns == "behind"):
    preAns = cs("You sneak around the guard and go inside the vent. You hear a familiar tune from a certain one eyed astronaut. You ignore it and start crawling. It's a tight fit, but the rats that are skittering in the vent still find a way to go through you. It feels disgusting. The displeasure continues until you reach the first exit of the vent. You kick the vent open and crawl outside. Your stinky smell permeates throughout the room and immediately calls attention to the conglomerate of people inside. You are in the King's Throne Room. There seems to be a party of some kind. Your target, the King immediately calls for the guards to apprehend you.", ["fight", "kill", "beat", "battle", "brawl", "clash", "sneak", "avoid", "run", "chase", "king"])

    if (preAns == "fight" or preAns == "kill" or preAns == "beat" or preAns == "battle" or preAns == "brawl" or preAns == "clash"):
        print_slow("You try to " + preAns + " the guards and you realize they are the king's guards for a reason. You realize how stupid it is to try to kill multiple military, high ranked, royal, ARMED guards. You are immediately skewered by their spears at the first sign of threat")
        print_slow(death, 0)
        exit()
    if (preAns == "sneak" or preAns == "avoid" or preAns == "run" or preAns == "chase"):
        preAns = cs("You throw a smoke bomb and chase after the king, who is pulling a lever behind the throne, and leave the guards confused. You see a passage open behind the throne and the king go inside of it. Suddenly, two guards appear and block your way towards the passage. You look around and notice an exit door free from any guards, but it would mean abandoning your mission. The more you hesitate, the more the king gets away", ["exit", "door", "abandon", "leave", "kill", "chase", "king"])
        if (preAns == "kill" or preAns == "fight" or preAns == "chase" or preAns == "king"):
            print_slow("You chase after the king, fighting the guards along the way. The guards are more focused on keeping you away from the King. You briefly fight for way of passage and when they seemed most vulnerable you throw a knife to both of their necks, killing them instantly. After picking up one of the spears, you chase after the king and kill him right then and there. You did your job, good job")
            exit()
        if (preAns == "exit" or preAns == "door" or preAns == "abandon"):
                 print_slow("You decided your life is more important, so you go towards the exit door and realize that backup was called. The guards swarm in and impale you with their spears.")
                 print_slow(death)
                 exit()

else:
    preAns == cs("You sneak around the guard and slowly open the exit door. Inside you see a short hallway leading up to a door.", ["open", "door"])
    print_slow("You open the door and the two guards guarding the door outside immediately notice you. They immediately figure out you're an intruder due to the way you dress. You are immediately arrested.")
    print(death)
    exit()
