"""
dkajdkajk
"""

import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('st_mochtas_fc')

print("Welcome to St Mochtas Football club\n")


def choose_first_menu():
    """
    This function checks the inout and loads the correct
    function based on the answer.
    """
    print("Please chose:\n")
    print("1. Work with player details.")
    print("2. Get quick pick lotto numbers.\n")
    menu_one = input("Please Enter 1 or 2: ")
    print(f'You have choosen {menu_one}')
    if int(menu_one) == 1:
        player_menu()
    elif int(menu_one) == 1:
        lotto_quickpick()
    else:
        print("Error Wrong Number")


def lotto_quickpick():
    """
    function to choose how many lines of lotto you want numbers for, and to
    display ramdon lotto numbers to the screen.
    """
    print('Do you want numbers for 1 line or 3?\n')


def player_menu():
    """
    Function to enter the player section and choose you option.
    """
    print("Please choose from the following options:\n")
    print("1. Register a player to your team.")
    print("2. Print a list of all your players and fees due.")
    print("3. Pay instalment of fees.")
    print("4. Confirm Order for Team Kits.\n")
    player_menu_choice = input("Please enter a number 1 to 4:")
    if int(player_menu_choice) == 1:
        reg_new_player()
    elif int(player_menu_choice) == 2:
        show_all_outstanding_fees()
    elif int(player_menu_choice) == 3:
        pay_fee_for_player()
    elif int(player_menu_choice) == 4:
        confirm_kit_order()
    else:
        player_menu()


def reg_new_player():
    """
    Function to take in player details and append them to the spread sheet.
    """
    print("you are now in reg player function")


def show_all_outstanding_fees():
    """
    Function to print a list of all players with outstanding fees to the
    terminal.
    """
    print("you are now in function to print players fees")


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


choose_first_menu()
