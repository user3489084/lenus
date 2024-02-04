import requests
import sys
import time
from colorama import init, Fore, Style

init(autoreset=True)

def scrape_proxies():
    url = "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all, https://hidemy.io/en/proxy-list/"

    try:
        clear_screen()
        print_static_logo()
        print("\nLoading... ", end='')

        loading_bar_width = 50
        for _ in range(loading_bar_width):
            sys.stdout.write(Fore.GREEN + "\u2588" + Style.RESET_ALL)
            sys.stdout.flush()
            time.sleep(0.1)

        response = requests.get(url)
        response.raise_for_status()

        if response.status_code == 200:
            proxies = response.text.split('\r\n')
            if proxies:
                print(Fore.GREEN + f"\nSuccessfully scraped {len(proxies)} proxies." + Style.RESET_ALL)
                # You can store or use the proxies as needed in your application
            else:
                print(Fore.RED + "\nNo proxies were scraped." + Style.RESET_ALL)
        else:
            print(Fore.RED + f"\nFailed to fetch proxies. Status code: {response.status_code}" + Style.RESET_ALL)

    except requests.exceptions.HTTPError as e:
        print(Fore.RED + f"\nHTTP error scraping proxies: {e}" + Style.RESET_ALL)
    except requests.exceptions.Timeout as e:
        print(Fore.RED + f"\nTimeout error scraping proxies: {e}" + Style.RESET_ALL)
    except requests.exceptions.RequestException as e:
        print(Fore.RED + f"\nError scraping proxies: {e}" + Style.RESET_ALL)

    time.sleep(0.8)

def print_static_logo():
    logo = """
    ██████  ▄████▄   ██▀███   ▄▄▄       ██▓███   ██▓ ███▄    █   ▄████ 
    ▒██    ▒ ▒██▀ ▀█  ▓██ ▒ ██▒▒████▄    ▓██░  ██▒▓██▒ ██ ▀█   █  ██▒ ▀█▒
    ░ ▓██▄   ▒▓█    ▄ ▓██ ░▄█ ▒▒██  ▀█▄  ▓██░ ██▓▒▒██▒▓██  ▀█ ██▒▒██░▄▄▄░
    ▒   ██▒▒▓▓▄ ▄██▒▒██▀▀█▄  ░██▄▄▄▄██ ▒██▄█▓▒ ▒░██░▓██▒  ▐▌██▒░▓█  ██▓
    ▒██████▒▒▒ ▓███▀ ░░██▓ ▒██▒ ▓█   ▓██▒▒██▒ ░  ░░██░▒██░   ▓██░░▒▓███▀▒
    ▒ ▒▓▒ ▒ ░░ ░▒ ▒  ░░ ▒▓ ░▒▓░ ▒▒   ▓▒█░▒▓▒░ ░  ░░▓  ░ ▒░   ▒ ▒  ░▒   ▒ 
    ░ ░▒  ░ ░  ░  ▒     ░▒ ░ ▒░  ▒   ▒▒ ░░▒ ░      ▒ ░░ ░░   ░ ▒░  ░   ░ 
    ░  ░  ░  ░          ░░   ░   ░   ▒   ░░        ▒ ░   ░   ░ ░ ░ ░   ░ 
                        ░          ░           ░           ░       ░ 
    """

    lines = logo.split('\n')
    width = max(len(line) for line in lines)
    empty_lines = (50 - len(lines)) // 2
    centered_logo = '\n'.join(' ' * (width - len(line)) + line for line in lines)

    print(centered_logo)

def clear_screen():
    sys.stdout.write('\033[H')  # Move cursor to the top left corner
    sys.stdout.write('\033[J')  # Clear the screen

if __name__ == "__main__":
    scrape_proxies()
