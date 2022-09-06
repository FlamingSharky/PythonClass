import random

timer = int(1)
number = int(random.randint(1, 3))
randomascii = int(random.randint(1, 3))
guess = int(input("Guess the number! 1 through 3, let's see if you get it right! Your number: "))
showguess = str(guess)
shownumber = str(number)
amogus = "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣤⣤⣤⣤⣤⣶⣦⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀" + "\n"\
     + "⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⡿⠛⠉⠙⠛⠛⠛⠛⠻⢿⣿⣷⣤⡀⠀⠀⠀⠀⠀ " + "\n"\
     + "⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⠋⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⠈⢻⣿⣿⡄⠀⠀⠀⠀" + "\n"\
     + "⠀⠀⠀⠀⠀⠀⠀⣸⣿⡏⠀⠀⠀⣠⣶⣾⣿⣿⣿⠿⠿⠿⢿⣿⣿⣿⣄⠀⠀⠀" + "\n"\
     + "⠀⠀⠀⠀⠀⠀⠀⣿⣿⠁⠀⠀⢰⣿⣿⣯⠁⠀⠀⠀⠀⠀⠀⠀⠈⠙⢿⣷⡄⠀" + "\n"\
     + "⠀⠀⣀⣤⣴⣶⣶⣿⡟⠀⠀⠀⢸⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣷⠀" + "\n"\
     + "⠀⢰⣿⡟⠋⠉⣹⣿⡇⠀⠀⠀⠘⣿⣿⣿⣿⣷⣦⣤⣤⣤⣶⣶⣶⣶⣿⣿⣿⠀" + "\n"\
     + "⠀⢸⣿⡇⠀⠀⣿⣿⡇⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠀" + "\n"\
     + "⠀⣸⣿⡇⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠉⠻⠿⣿⣿⣿⣿⡿⠿⠿⠛⢻⣿⡇⠀⠀" + "\n"\
     + "⠀⣿⣿⠁⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣧⠀⠀" + "\n"\
     + "⠀⣿⣿⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀" + "\n"\
     + "⠀⣿⣿⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀" + "\n"\
     + "⠀⢿⣿⡆⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡇⠀⠀" + "\n"\
     + "⠀⠸⣿⣧⡀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠃⠀⠀" + "\n"\
     + "⠀⠀⠛⢿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⣰⣿⣿⣷⣶⣶⣶⣶⠶⠀⢠⣿⣿⠀⠀⠀" + "\n"\
     + "⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⣿⣿⡇⠀⣽⣿⡏⠁⠀⠀⢸⣿⡇⠀⠀⠀" + "\n"\
     + "⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⣿⣿⡇⠀⢹⣿⡆⠀⠀⠀⣸⣿⠇⠀⠀⠀" + "\n"\
     + "⠀⠀⠀⠀⠀⠀⠀⢿⣿⣦⣄⣀⣠⣴⣿⣿⠁⠀⠈⠻⣿⣿⣿⣿⡿⠏⠀⠀⠀⠀" + "\n"\
     + "⠀⠀⠀⠀⠀⠀⠀⠈⠛⠻⠿⠿⠿⠿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀"
eagle = "       .------._ " + "\n"\
" .-\"\"\"`-.<')    `-._ " + "\n"\
"(.--. _   `._       `'---.__.-'" + "\n"\
" `   `;'-.-'         '-    ._ " + "\n"\
"   .--'``  '._      - '   ." + "\n"\
"    `\"\"'-.    `---'    ," + "\n"\
"          `\\" + "\n"\
"            `\      .'" + "\n"\
"              `'. '" + "\n"\
"       Art by jgs `'."
dragon = "       \****__              ____                                              " + "\n"\
"         |    *****\_      --/ *\-__                                          " + "\n"\
"         /_          (_    ./ ,/----'                                         " + "\n"\
"Art by     \__         (_./  /                                                " + "\n"\
" Ironwing     \__           \___----^__                                       " + "\n"\
"               _/   _                  \                                      " + "\n"\
"        |    _/  __/ )\\\"\ _____         *\                                    " + "\n"\
"        |\__/   /    ^ ^       \____      )                                   " + "\n"\
"         \___--\\\"                    \_____ )                                  " + "\n"\
"                                          \""
knife = "                                                       ___" + "\n"\
"                                                      |_  |" + "\n"\
"                                                        | |" + "\n"\
"__                      ____                            | |" + "\n"\
"\ ````''''----....____.'\   ````''''--------------------| |--.               _____      .-." + "\n"\
" :.                      `-._                           | |   `''-----''''```     ``''|`: :|" + "\n"\
"  '::.                       `'--.._____________________| |                           | : :|" + "\n"\
"    '::..       ----....._______________________________| |                           | : :|" + "\n"\
"      `'-::...__________________________________________| |   .-''-..-'`-..-'`-..-''-.cjr :|" + "\n"\
"           ```'''---------------------------------------| |--'                         `'-'" + "\n"\
"                                                        | |" + "\n"\
"                                                       _| |" + "\n"\
"                                                      |___| Art by cjr"

if guess == number: 
    print("With odds like those, you should try the lottery! Congrats on instead using your good fortune to be safe from the Among Us, your reward is a cool ascii art.")

if randomascii == 1 and guess == number:
    print(eagle)

if randomascii == 2 and guess == number:
    print(dragon)

if randomascii == 3 and guess == number:
    print(knife)

while guess != number:
    timer = 1+timer
    print(amogus)
    if timer == 6:
        break

if guess is not number:
    print("Boo hoo, you lost, big rip, 2/3 chances it happened so what can I say. The creator of the among us ascii is not worth crediting so fuck him for making this. Here's the actual number, maybe try harder next time: " + shownumber)