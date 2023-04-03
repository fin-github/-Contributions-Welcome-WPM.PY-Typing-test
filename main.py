from colorama import Fore, Style
from keyboard import is_pressed
from os import system as runCommand, name as osSysName
from time import sleep as wait
from random import choice

words=["bear","hand","dog","frank","predict","wage","bring","sector","chase","registration"]

def clr():
    runCommand("cls" if osSysName == "nt" else "clear")

text = """

          _______  _______     _______          
|\     /|(  ____ )(       )   (  ____ )|\     /|
| )   ( || (    )|| () () |   | (    )|( \   / )
| | _ | || (____)|| || || |   | (____)| \ (_) / 
| |( )| ||  _____)| |(_)| |   |  _____)  \   /  
| || || || (      | |   | |   | (         ) (   
| () () || )      | )   ( | _ | )         | |   
(_______)|/       |/     \|(_)|/          \_/   
                                                

"""

print(f"{Style.BRIGHT}{Fore.LIGHTBLUE_EX}{text}")
wait(2)
clr()
print(f"{Style.NORMAL}{Fore.GREEN}Generating prompt...")
prompt = ""
for i in range(0,10):
    prompt += f"{choice(words)} "
clr()
print(f"{Style.NORMAL}{Fore.GREEN}[p] Prompt Generated!")
wait(1)
currentletter = prompt[0]
currentletteri = 0
tick = 1
while True:
    tick += 1
    wait(0.1)
    clr()
    print(f""" S {Style.DIM}PROMPT     {Style.BRIGHT}{Fore.LIGHTWHITE_EX}WPM.PY{Style.NORMAL}
    {Fore.YELLOW}prompt: {prompt}

    Reading keystrokes...
    """)
    if is_pressed(prompt[currentletteri]):
        currentletteri += 1
        print(Fore.GREEN, currentletter)
        tick = 1
    else:
        if not tick == 5:
            print(Fore.RED, currentletter if not currentletter == " " else "space")
    try:
        currentletter = prompt[currentletteri]
    except IndexError:
        break
        pass
print(f"{Style.BRIGHT}{Fore.GREEN}Congrats! Complete. Prompt: {prompt}") #TODO: Add WPM
