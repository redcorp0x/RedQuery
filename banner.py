import pyfiglet
from colorama import Fore, Style, init

init(autoreset=True)

banner = pyfiglet.figlet_format("RedQuery", font="slant")

print(Fore.RED + banner)

print(Fore.WHITE + Style.BRIGHT +
      "       Boolean-Based SQL Injection Tool")

print(Fore.CYAN + "               Built by Redcorp\n")


print(Fore.WHITE + "  Version 1.0.1")
print(Fore.GREEN + "  Automated Testing | Custom Payload Engine")
print(Fore.GREEN + "  Proxy Support | Session Recovery | supports mysql and postgresql DB")

print(Fore.RED + "-" * 59)
print(Fore.CYAN + "  Usage: Type redquery --help to display available options.")
print(Fore.RED + "-" * 59)