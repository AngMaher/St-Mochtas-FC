"""
This program is based on a local football club, where player details are stored
in a spreadsheet and can be amended
"""
import os
import time
import sys
import random
import re
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
player_worksheet = SHEET.worksheet('player')
all_data = player_worksheet.get_all_values()
raffle_worksheet = SHEET.worksheet('raffle')


def welcome_logo():
    """
    Function to hold welcome title for program
    """
    print(Fore.LIGHTYELLOW_EX + """
 _     _ _______ ___     _______ _______ __   __ _______   _______ _______
| | _ | |       |   |   |       |       |  |_|  |       | |       |       |
| || || |    ___|   |   |       |   _   |       |    ___| |_     _|   _   |
|       |   |___|   |   |       |  | |  |       |   |___    |   | |  | |  |
|       |    ___|   |___|      _|  |_|  |       |    ___|   |   | |  |_|  |
|   _   |   |___|       |     |_|       | ||_|| |   |___    |   | |       |
|__| |__|_______|_______|_______|_______|_|   |_|_______|   |___| |_______|
    """)
    print(Fore.LIGHTYELLOW_EX + """
 _______ _______   __   __ _______ _______ __   __ _______ _______ _______
|       |       | |  |_|  |       |       |  | |  |       |   _   |       |
|  _____|_     _| |       |   _   |       |  |_|  |_     _|  |_|  |  _____|
| |_____  |   |   |       |  | |  |       |       | |   | |       | |_____
|_____  | |   |   |       |  |_|  |      _|       | |   | |       |_____  |
 _____| | |   |   | ||_|| |       |     |_|   _   | |   | |   _   |_____| |
|_______| |___|   |_|   |_|_______|_______|__| |__| |___| |__| |__|_______|
    """ + Style.RESET_ALL)


def main_menu():
    """
    This function checks the input and loads the correct
    function based on the answer.
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    welcome_logo()
    print("Please choose from the following options:\n")
    print(Fore.LIGHTBLUE_EX + """
    1. Work with player details.
    2. Get 1 line to 3 lines of raffle numbers.
    3. Pick Raffle winners.
    4. Quit.\n""" + Style.RESET_ALL)
    menu_one = input("Please Enter 1 or 2 or 3: ")
    if menu_one == '1':
        player_menu()
    elif menu_one == '2':
        raffle_numbers()
    elif menu_one == '3':
        pick_raffle_winners()
    elif menu_one == '4':
        sys.exit()
    else:
        print("Invaid! Please try again")
        time.sleep(2)
        main_menu()


def raffle_numbers():
    """
    function to choose how many lines of numbers to enter raffle
    and to display ramdon numbers to the screen and save to spreadsheet
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.LIGHTYELLOW_EX + """
 +-+-+-+-+-+-+ +-+-+-+-+
 |R|a|f|f|l|e| |M|e|n|u|
 +-+-+-+-+-+-+ +-+-+-+-+
    """ + Style.RESET_ALL)
    print(Fore.LIGHTBLUE_EX + """
For 1 Line of Raffle Ticket numbers - 1
For 3 Lines of Raffle Ticket numbers - 3
    """ + Style.RESET_ALL)
    num_of_lines = input("Please enter 1 or 3: ")
    if num_of_lines == '1':
        lotto_line = random.sample(range(1, 28), 5)
        print(Fore.LIGHTBLUE_EX + """\nRaffle Numbers Line One:
        """ + Style.RESET_ALL)
        print(*lotto_line)
        submit_numbers = input("Do you wish to submit? y/n: ")
        if submit_numbers.upper() == 'Y':
            print("Your Numbers are being submitted to raffle..")
            raffle_worksheet.append_row(lotto_line)
        elif submit_numbers.upper() == 'N':
            print("Not Submitted")
        else:
            back_to_main_menu()
        back_to_main_menu()
    elif num_of_lines == '3':
        lotto_line = random.sample(range(1, 28), 5)
        lotto_line2 = random.sample(range(1, 28), 5)
        lotto_line3 = random.sample(range(1, 28), 5)
        print(Fore.LIGHTBLUE_EX + """\nRaffle Numbers Line One:
        """ + Style.RESET_ALL)
        print(*lotto_line)
        print(Fore.LIGHTBLUE_EX + """Raffle Numbers Line Two:
        """ + Style.RESET_ALL)
        print(*lotto_line2)
        print(Fore.LIGHTBLUE_EX + """Raffle NumbersLine Three:
        """ + Style.RESET_ALL)
        print(*lotto_line3)
        submit_numbers = input("Do you wish to submit? y/n: ")
        if submit_numbers.upper() == 'Y':
            print("Your Numbers are being submitted to raffle..")
            raffle_worksheet.append_row(lotto_line)
            raffle_worksheet.append_row(lotto_line2)
            raffle_worksheet.append_row(lotto_line3)
        elif submit_numbers.upper() == 'N':
            print("Not Submitted")
        else:
            back_to_main_menu()
        back_to_main_menu()
    else:
        print("\nYou entered incorrect, please enter again")
        time.sleep(2)
        raffle_numbers()


def pick_raffle_winners():
    """F"""
    print("winners")


def player_menu():
    """
    Function to enter the player section and choose you option.
    found clear screen:
    https://stackoverflow.com/questions/2084508/clear-terminal-in-python
    ASCII art:
    http://patorjk.com/software/taag/#p=display&h=2&v=2&f=Digital&t=Player%20Menu
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.LIGHTYELLOW_EX + """
     +-+-+-+-+-+-+ +-+-+-+-+
     |P|l|a|y|e|r| |M|e|n|u|
     +-+-+-+-+-+-+ +-+-+-+-+
     """ + Style.RESET_ALL)
    print("Please choose from the following options:\n")
    print(Fore.LIGHTBLUE_EX + """
    1. Register a player on your team.
    2. Delete player.
    3. Print a list of all players and fees due.
    4. Pay instalment of fees or in full.
    5. Confirm Order for Team Kits.
    6. Quit program.\n
    """ + Style.RESET_ALL)
    player_menu_choice = input("Please enter a number 1 to 6: ")
    if player_menu_choice == '1':
        get_player_details()
    elif player_menu_choice == '2':
        delete_player()
    elif player_menu_choice == '3':
        show_all_outstanding_fees()
    elif player_menu_choice == '4':
        pay_fee_for_player()
    elif player_menu_choice == '5':
        confirm_kit_order()
    elif player_menu_choice == '6':
        print("Program is terminating...")
        sys.exit()
    else:
        print("Invaid! Please try again")
        time.sleep(2)
        player_menu()


def get_player_details():
    """
    Function to take in player details and append them to the spread sheet.
    Used the love sandwiches program to setup the while loop.
    """
    while True:
        print("To Enter New Player please follow the Instructions:\n")
        print(Fore.RED + """
    1. Format:  Username(Initials DOB),Name,Mobile Number,Kit Size,Fee Due
    """ + Fore.LIGHTYELLOW_EX + """
    2. Example: JS12jan12,Joe Smith,+353866052459,YL,180
    """ + Style.RESET_ALL + Fore.RED + """
    3. Kit sizes: YXS, YS, YM, YL, YXL, XS, S, M, L
    4. Please note the annual fee is 180 euro, no exceptions.
            """ + Style.RESET_ALL)
        data_str = input("Please enter details here, or 'exit' to go back: ")
        if data_str.upper() == 'EXIT':
            back_to_main_menu()
        else:
            player_data = data_str.split(",")
            if check_player_data(player_data):
                print("Thank you ")
                break
    update_player_worksheet(player_data)
    back_to_main_menu()


def check_player_data(values):
    """
    Function to check the values entered for player are valid

    """
    try:
        if len(values) != 5:
            raise ValueError(
                f"Exactly 5 values required, you provided {len(values)}"
            )
        if any(values[0] in sl for sl in all_data):
            raise ValueError(
                f"\nUsername already in use, you put {values[0]}"
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


def delete_player():
    """
    Function to delete a player in the database using username
    """
    print_all_data()
    row_delete = input("""
    \nPlease enter Username of person you wish to delete, or exit:
                """)
    if row_delete.upper() == 'EXIT':
        back_to_main_menu()
    else:
        row_number = player_worksheet.findall(row_delete)
        row_player = re.search('R(.+?)C', str(row_number))
        if row_player:
            found = row_player.group(1)
            player_worksheet.delete_rows(int(found))
        print(f"You have sucessfully deleted {row_delete}")
        back_to_main_menu()


def update_player_worksheet(data):
    """
    Function to update player worksheet with player information.
    This code was used from the love sandwiches program
    """
    print("Updating player worksheet...\n")
    player_worksheet.append_row(data)
    print("Player worksheet updated successfully.\n")


def show_all_outstanding_fees():
    """
    Function to print a list of all players with outstanding fees to the
    terminal.
    used .findall() to find each of the amounts, could not find all the
    amounts at one time, so I created different list and joined them into
    one list.
    Imported re to use function search to search through each string
    and extract the row number. Then stored all row numbers in a list.
    Found this on stckoverflow:
    https://stackoverflow.com/questions/4666973/how-to-extract-the
    -substring-between-two-markers
    At this stage I iterated through list of all data from spreadsheet and
    printed each row.
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Find below a list of all players in order of what they owe.\n")
    print("Loading...\n")
    total_fees = player_worksheet.findall("60")
    fees_120 = player_worksheet.findall("120")
    fees_180 = player_worksheet.findall("180")
    total_fees.extend(fees_120)
    total_fees.extend(fees_180)
    total_row_nums = []
    for text in total_fees:
        row_num = re.search('R(.+?)C', str(text))  # stackoverflow link above
        if row_num:
            found = row_num.group(1)
            total_row_nums.append(found)
    list_of_owed = []
    for rows in total_row_nums:
        each_row = player_worksheet.row_values(rows)
        list_of_owed.append(each_row)
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Find below a list of all players in order of what they owe.\n")
    print(tabulate(list_of_owed[1:], headers=all_data[0], tablefmt="pretty"))
    back_to_main_menu()


def pay_fee_for_player():
    """
    Function to pay eitheran agreed installment off the fee or pay the fee
    in full.
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    print_all_data()
    print(Fore.RED + """
    Please look at table above and take note of the USERNAME of the player
    you would like to either pay an installment off full fee off.
        """ + Style.RESET_ALL)
    username = input("Please enter the username: ").upper()
    if any(username in sl for sl in all_data):
        amending_fee(username)
    else:
        print("Username is incorrect, please try again")
        time.sleep(3)
        pay_fee_for_player()


def amending_fee(name):
    """
    function to amend the new fee amount to the spreadsheet
    """
    username = player_worksheet.find(name)
    cell_info = username.row
    fee_due = player_worksheet.cell(cell_info, 5).value
    name_of_player = player_worksheet.cell(cell_info, 2).value
    if int(fee_due) == 0:
        print(f"{name_of_player} is fully paid.. Balance is zero")
        print("returning to player menu...")
        time.sleep(3)
        player_menu()
    else:
        print(f"\n{name_of_player} owes £{fee_due}")
    while True:
        print("Please Note: Please pay 1 installment of 60 or in full 180.")
        amount_pay = input("Please input amount you are paying off: ")
        if check_amount(amount_pay):
            new_amount = int(fee_due) - int(amount_pay)
            if new_amount < 0:
                print("Paid too much off, Please check table again...")
                time.sleep(5)
                pay_fee_for_player()
            else:
                print(f"{name_of_player} now owes {new_amount}")
                player_worksheet.update_cell(cell_info, 5, new_amount)
            break
    back_to_main_menu()


def check_amount(pay):
    """
    Function to check if the amount entered is either 60, 120, or 180
    """
    if pay in ('60', '180'):
        return True
    try:
        if pay not in ('60', '180'):
            raise ValueError(
                f"Please enter 60 or 180, {pay} provided"
            )
    except ValueError as error:
        print(f"Invalid data {error}, please try again.\n")
        return False


def confirm_kit_order():
    """
    Function to display the amount of different sizes entered for a team and
    confirm them to order which will them write them to a different sheet on
    the spreadsheet.
    found for loop on favtutor https://favtutor.com/blogs/python-count-
    occurrences-in-list#:~:text=1)%20Using%20count()%20method,occurrences
    %20is%20to%20be%20counted. Amended it to only go from second item.
    """
    print("Please order your kits for your team")
    kit_col = player_worksheet.col_values(4)
    kit_col_upper = [kit.upper() for kit in kit_col]
    kit_dict = {}
    for j in kit_col_upper[1:]:
        if j in kit_dict:
            kit_dict[j] += 1
        else:
            kit_dict[j] = 1
    print(Fore.LIGHTBLUE_EX + """
    The following is the total number of kits needed:
        """ + Style.RESET_ALL)
    for keys, val in kit_dict.items():
        print(keys, val)
    back_to_main_menu()


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
    data_table = player_worksheet.get_all_values()
    print(tabulate(data_table[1:], headers=all_data[0], tablefmt="pretty"))


main_menu()
