import verification
import config
import savefile
import sys
from colorama import Fore, Style

extraction_name = None
Discovered = set()

def select_option():
    global Discovered
    for number,value in enumerate(Discovered, start=1):
        print(f"{Fore.GREEN}{Style.BRIGHT}{number}: {value.capitalize()}")
    print("Would you like to move to the next phase of extraction? (Y/N)")
    while True:
        text_input = input().capitalize()
        if text_input == "Y":
            int_input = int(input(f"Select the {extraction_name.capitalize()} index: "))
            if 1 <= int_input <= len(Discovered):
                value = Discovered[int_input - 1]
                if extraction_name == "schema":
                    config.schema_result = value
                if extraction_name == "table":
                    config.table_result = value
                if extraction_name == "column":
                    config.column_result = value
                if extraction_name == "row":
                    config.row_result = value
                if extraction_name == "password":
                    config.password_result = value
                    savefile.save_resume()
                    if config.filename:
                        savefile.General_Save()
                    sys.exit(1)
                savefile.save_resume()
                Discovered = set()
                config.count_limit = 0
                if config.verbose:
                    print(f"You selected: {Fore.YELLOW}{Style.BRIGHT}{value.capitalize()}")
                    print("Moving to the next extraction phase")
            break
        if text_input == "N":
            print("Program Exited Successfully")
            sys.exit(0)
        else:
            print("[!] Invalid input. Please try again.")
        

def heart(payload,counts,extraction_type):
    global extraction_name
    global Discovered
    extraction_name = extraction_type
    if extraction_type == "password":
        if config.verbose:
            print(f"[!] {extraction_type.capitalize()} Length: {counts}")
        counts = 1
    try:
        if config.verbose:
            print(f"[!] {extraction_type.capitalize()} count: {counts}")
        if config.verbose:
            print(f"[+] {extraction_type.capitalize()} Extraction Started")
            print("[+] Processing...")
        while len(Discovered) != int(counts):
            word = verification.verify(payload=payload)
            if word:
                Discovered.add(word)
        if config.verbose:
            print("[+] Operation Completed")
        Discovered = list(Discovered)
        if config.filename:
            savefile.Category_save(category=extraction_type.capitalize(), results=Discovered)
        if config.verbose:
            print(f"Saved output to {config.filename}")
        select_option()
    except KeyboardInterrupt:
        print("[WARN] Extraction was interrupted Ctrl-C")
        sys.exit(1)
    