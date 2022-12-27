# St Mochtas Football Club Application

[Live Link](https://st-mochtas-fc.herokuapp.com/)

## Introduction
This is a program for a local football club, which can be easily be adapted to suit many different types of clubs.
The user can add a new player to a spreadsheet, clear off a players fees, check outstanding fees, and put in an order 
for kits for the team. The club also do a lotto each week and the user can get lotto numbers for doing quick pick.

# User Experience

- User Goals
  - As a user they want to see a list of all players to note their username before making changes.
  - As a coach or director of the club they want a way to add new players to the team.
  - As a user they want to be able to delete a player.
  - As a user they want to be able to pay an installment or their fee off in full.
  - As a user they want to be able to show the full list of player for the whole clib or for an individual team.
  - As a user they woule like to look at total number of sizes in kits and confirm to order
  - As a user they would like to when all orders are confirmed they can view, total of each size before getting onto to the company

- Developer Goals
  - As a developer, I want to keep the program simple
  - As a developer, I want to make navigating through straight forward and easy to follow.
  - As a developer, I want to create a easy to read tablr to display information from the spreadsheet.

worked on bugs and warnings as they came along. when doing try/excpet got on error and realsied i had a second try the same further down.

used love sandwiches as referrence for validating and writing player details

decided tp change the year to a username, and it was not as straight forward as i thought, 
i worked out that I needed to pass all the data into the function, but was finding it difficult to iterate through the sublist to check if the username was already used. I found from a online search on the stackoverflow site that using a built-in function any() would work. https://stackoverflow.com/questions/40514139/check-if-an-item-is-in-a-nested-list
from this i decided instead of calling all data from the spreadsheet i made it global.

when adding delete player didnt work got an error about int str and I realised the row number was a string to changed to an int.
it worked by got a warning to use delete_rows() instead of delete_row() so changed that and worked fine after that


# Logic and Features

## Logic

- I created a flowchart using Lucid Charts 
![flow chart](/assets/images/flowchart.jpeg)
[Link to Flow Chart](https://lucid.app/lucidchart/a7266b3b-06cc-49f8-b512-7ef2e880f1b5/edit?viewport_loc=-671%2C-132%2C4933%2C2267%2C0_0&invitationId=inv_2b70d115-293e-4ac8-8826-07a126004676)

## Database structure

I used Google Sheets to store the progects database in the spreadsheet. This project has two worksheets, the first holds all the players information the second holds
each line of raffle numbers that are saved.

Worksheet "player" holds all the players details:

![player worksheet](/assets/images/player-worksheet.png)

It had a username column, which is made from the players initials and their date of birth. Next is a column for their name, then one for a contact mobile number prompting user to start the number +353. Next column is to store the players Kit Size and finally the fee amount due.

The second worksheet is to store the raffle numbers:

![raffle worksheet](/assets/images/raffle-worksheet.png)

## Features

### Main Menu

![main menu](/assets/images/main-menu.png)

- The main screen features the logo for the app.
- The main menu has an option to go to the player menu, to pick raffle numbers, to pick overall raffle winning numbers, or quit the program.

### Player Menu

![player menu](/assets/images/player-menu.png)

- This screen shows the logo on top
- User has options to add a new player
- Delete a player from the database
- Print a list of all outstanding fees
- Pay fees off for a player
- Show how many kits need ordering for each size
- Option to quit the program or return to main menu

### Enter player Details

![enter player](/assets/images/enter-player.png)

- This screen gives the user details and instructions on how to enter the players details to save to the worksheet

### Delete a Player

![delete a player](/assets/images/delete-player.png)

- This screen shows a list of players so the user can find the username of the player they want to delete.
- Enter in the username and the player is removed from the database.

### List of outstanding fees

![list of outstanding fees](/assets/images/loading-screen.png)

- screen to show the program is fetching and loading the players with outstanding fees.

![list of outstanding fees](/assets/images/list-of-fees.png)

- screen to show all players who owe fees, in order of how much they owe.

### Pay fees

![pay fees](/assets/images/pay-fee.png)

- Screen shows a list of all players from the database and asks of the username.

![paying amount off](/assets/images/check-fee-amount.png)

- This gives the option to the user to pay an installment of 60 off or pay the fee in full.
- It shows how much the player owe and then how they now owe.

### Check Kit Sizes

![Kit sizes](/assets/images/kit-sizes.png)

- This screen shows the user how much of each kit size is needed to be ordered.

### Raffle Menu

![raffle menu](/assets/images/raffle-menu.png)

- This is screen for the user to choose either 1 line of numbers or 3

![one line](/assets/images/one-line.png)

- Prints one line of numbers to the screen
- Asks if user wants to save to database

![three lines](/assets/images/three-lines.png)

- Prints three lines of numbers to the screen
- Asks if user wants to save to database

![raffle winners](/assets/images/raffle-winners.png)

- This screen radomly picks a row of numbers from the database as the winning ticket numbers.


# Deployment

## Git and GitHub
Code Institute template was used to create GitHub public repository st-mochtas-fc. 

I developed programm, often commiting changes using terminal commands.
I made sure that all my libraries and packages are listed in requirements.txt.

When program was ready for further deployment I visited heroku.com website to deploy on heroku.

## Deployment to Heroku
I visited https://heroku.com/ and opened dashboard. Then I clicked button "New" and selected "Create new app" button.

I entered my app name as "St-Mochtas-FC", region to Europe and clicked on "Create app" button

![create app](/assets/images/createapp.png)

The next step was to go to "Deploy" tab and then to "Deployment method" section to authorize and connect my GitHub account.

![connect github](/assets/images/connectgithub.png)

When succesfully connected I selected main branch from "St-Mochtas-FC" repository.

Then I went to "Settings" tab

In the next step I went to "Config Vars" section and added KEY "CREDS" with value of my credentials file creds.json (copy all and paste).

![config vars](/assets/images/configvars.png)

Next to "Buildpacks" section. In the next step I added pyhton and nodejs buildpacks, making sure python was first then nodejs.

![buildpacks](/assets/images/buildpacks.png)

In the next step I went back to "Deploy" tab and decided to use manual mode, however automatic mode is also available to deploy, which I done at a later time.

![connected screen](/assets/images/connected.png)

The link to my deployed app was shown on screen: [Live Link](https://st-mochtas-fc.herokuapp.com/)
