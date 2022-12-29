# Manual Testing


![error](/assets/images/error-github.png)

- These errors have been on my github from the start. I have ignored them, but have made sure it has never gone over 4 problems.

- As I worked on my project I have worked on the errors or warnings, any trailing white space or missing colon, or missing lines between functions was all delt with as I coded.

| Input Testing | Whats being tested, Any Issues | Result |
| --- | ---- | ---- |
| Option for all menus, validate input | Make sure check numbers No Issues, Tested putting in wrong number, blank and string. No issues correct error messgages ran. | Pass |
| Check username is not in use already | Took a bit of time and errors to work out how to do this but found a function on stackoverflow to help with this and now it works. Tested with exsisting username and correct errors show. Any string can be inputted, the initials and dob is guidance. | Pass |
| Input Phone Number |  Validate that it begins with +353 No issues. No other checks are in place, a string could be entered as longas it starts with +353. Future delvelopment could have more validation. | Pass |
| Input Kit Sizes | Created constant list to hold all Kit sizes, tested uppercase and lowercase, also entered string that is not in the list, numbers and blank all came back with correct error messages. | Pass |
| Delete player, ask for username | Have tested correct name, incorrect name numbers, strings and blank | Fail, found part of the if statement had mistakenly been removed, the error messages where not showing. I fixed it by adding else: part of the statement to print error message and return to the screen to try again |
| Input fee amount | check 180 is entered, tested with string, different numbers and blank correct error messages are in place. | Pass | Input username to pay fee | tested incorrect username, numbers, blank and correct username | Pass |
| Input fee or installment | tested correct amounts "60" or "180" and any other number, string or blank, also tried paying 180 from someone that owes less or try paying off someone that doesnt owe any money | Pass |
| back to main menu function, input y/n to return | Tested that uppercase and lowercase worked, blank and anything other than y/n had correct error message. | Pass |
| Quit, on main menu | tested correct number, string, incorrect number, empty string | Pass |


| User Goals | Result |
| ---- | ---- |
| As a user they want to see a list of all players to note their username before making changes. | ![Delete](/assets/images/delete-player.png) |
| | ![pay fee](/assets/images/pay-fee.png) |
| As a coach or director of the club they want a way to add new players to the team | Pass |
| As a user they want to be able to delete a player | Pass |
| As a user they want to be able to pay an installment or their fee off in full | Pass |
| As a user they want to be able to show the full list of player for the whole club. | Pass |
| As a user they woule like to look at total number of sizes in kits | Pass |
| As a user they would like to get random raffle numbers | Pass |

| Devepoler Goals | Result |
| --- | --- |
| I want to keep the program simple | Pass |
| I want to make navigating through straight forward and easy to follow | Pass |
|  I want to create a easy to read table to display information from the spreadsheet | Pass |


