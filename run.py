"""
This program is based on a local football club, where player details are stored
in a spreadsheet and can be amended
"""
import os
import sys
import random
from tabulate import tabulate
import gspread
from colorama import Fore, Style
from google.oauth2.service_account import Credentials

KIT_SIZES = ['YXS', 'YS', 'YM', 'YL', 'YXL', 'XS', 'S', 'M', 'L', 'XL']
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('st_mochtas_fc')


def welcome_logo():
    """
    Function to hold welcome title for program
    """
    print(Fore.BLUE + """
    Welcome to St Mochtas FC""" + Style.RESET_ALL)


def main_menu():
    """
    This function checks the input and loads the correct
    function based on the answer.
    """
    welcome_logo()
    print(Fore.LIGHTBLUE_EX + """Please chose:\n
    1. Work with player details.
    2. Get quick pick lotto numbers.
    3. Quit.\n""" + Style.RESET_ALL)
    menu_one = input("Please Enter 1 or 2 or 3: ")
    print(f'You have choosen {menu_one}')
    if menu_one == '1':
        player_menu()
    elif menu_one == '2':
        lotto_quickpick()
    elif menu_one == '3':
        sys.exit()
    else:
        main_menu()


def lotto_quickpick():
    """
    function to choose how many lines of numbers to enter raffle
    and to display ramdon numbers to the screen and save to spreadsheet
    """
    print()
    print('Do you want numbers for 1 line or 3?')
    num_of_lines = input("Please enter 1 or 3: ")
    if num_of_lines == '1':
        lotto_line = random.sample(range(1, 28), 5)
        print("\nQuickpick Line One: ")
        print(*lotto_line)
        back_to_main_menu()
    elif num_of_lines == '3':
        lotto_line = random.sample(range(1, 28), 5)
        lotto_line2 = random.sample(range(1, 28), 5)
        lotto_line3 = random.sample(range(1, 28), 5)
        print(Fore.LIGHTBLUE_EX + "Quickpick Line One: " + Style.RESET_ALL)
        print(*lotto_line)
        print(Fore.LIGHTBLUE_EX + "Quickpick Line Two: " + Style.RESET_ALL)
        print(*lotto_line2)
        print(Fore.LIGHTBLUE_EX + "Quickpick Line Three: " + Style.RESET_ALL)
        print(*lotto_line3)
        back_to_main_menu()


def player_menu():
    """
    Function to enter the player section and choose you option.
    """
    os.system('cls')
    print(Fore.LIGHTBLUE_EX + """
    Please choose from the following options:\n
    1. Register or delete a player on your team.
    2. Print a list of all your players and fees due.
    3. Pay instalment of fees.
    4. Confirm Order for Team Kits.
    5. Quit program.\n
    """ + Style.RESET_ALL)
    player_menu_choice = input("Please enter a number 1 to 5: \n")
    if player_menu_choice == '1':
        get_player_details()
    elif player_menu_choice == '2':
        show_all_outstanding_fees()
    elif player_menu_choice == '3':
        pay_fee_for_player()
    elif player_menu_choice == '4':
        confirm_kit_order()
    elif player_menu_choice == '5':
        print("Program is terminating...")
        sys.exit()
    else:
        player_menu()


def get_player_details():
    """
    Function to take in player details and append them to the spread sheet.
    Used the love sandwiches program to setup the while loop.
    """
    while True:
        print("To Enter New Player please follow the Instructions:\n")
        print(Fore.RED + """
    1. Format:  Year,Name,Mobile Nimber,kit size,fee due
    2. Example: U10,Joe Smith,+353866052459,YL,180
    3. Kit sizes: YXS, YS, YM, YL, YXL, XS, S, M, L
    4. Please note the annual fee is 180 euro, no exceptions.
            """ + Style.RESET_ALL)

        data_str = input("Please enter details here: ")
        player_data = data_str.split(",")

        if check_player_data(player_data):
            print("Thank you ")
            break
    update_player_worksheet(player_data)
    back_to_main_menu()


def update_player_worksheet(data):
    """
    Function to update player worksheet with player information.
    This code was used from the love sandwiches program
    """
    print("Updating player worksheet...\n")
    player_worksheet = SHEET.worksheet("player")
    player_worksheet.append_row(data)
    print("Player worksheet updated successfully.\n")


def check_player_data(values):
    """
    Function to check the values entered for player are valid

    """
    try:
        if len(values) != 5:
            raise ValueError(
                f"Exactly 5 values required, you provided {len(values)}"
            )
        if not values[0].upper().startswith("U"):
            raise ValueError(
                f"Should start with U for Under, you put {values[0]}"
            )
        if not values[2].startswith("+353"):
            raise ValueError(
                f"Please enter Mobile Number with +353, {values[2]} provided"
            )
        if values[3].upper() not in KIT_SIZES:
            raise ValueError(
                f"{values[3]} is not a size please check list of sizes above"
            )
        if values[4] != '180':
            raise ValueError(
                f"Fee is 180, you entered {values[4]}"
            )
    except ValueError as error:
        print(f"Invalid data {error}, please try again.\n")
        return False
    return True


def show_all_outstanding_fees():
    """
    Function to print a list of all players with outstanding fees to the
    terminal.
    """
    print("you are now in function to print players fees")
    print_all_data()


def pay_fee_for_player():
    """
    Function to pay eitheran agreed installment off the fee or pay the fee
    in full.
    """
    print("Please pay off fee")


def confirm_kit_order():
    """
    Function to display the amount of different sizes entered for a team and
    confirm them to order which will them write them to a different sheet on
    the spreadsheet.
    """
    print("Please order your kits for your team")


def back_to_main_menu():
    """
    Function to call to either go back to main menu or quit progam
    """
    to_end = input("Return to main menu? y/n: ")
    if to_end.upper() == 'Y':
        main_menu()
    elif to_end.upper() == 'N':
        sys.exit()
    else:
        print("Error Wrong input.. Please try again..")
        back_to_main_menu()


def print_all_data():
    """
    Function to print all data in a table using tabulate
    found on https://www.statology.org/create-table-in-python/
    """
    players_list = SHEET.worksheet('player')
    data = players_list.get_all_values()
    print(tabulate(data, headers=data[0], tablefmt="pretty"))


main_menu()
