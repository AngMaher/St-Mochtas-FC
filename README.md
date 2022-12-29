# St Mochtas Football Club Application

Please find live link here: [Live Link](https://st-mochtas-fc.herokuapp.com/)
Please find link to Github repository: [github](https://github.com/AngMaher/St-Mochtas-FC)

![amireponsive](/assets/images/amireponsive.png)

## Introduction
This is a program for a local football club, which can be easily be adapted to suit many different types of clubs.
The user (Club chair or coach) can add a new player to a spreadsheet and delete a player, clear off a players fees,
check outstanding fees, check how many kits are needed and in what sizes.
The club also do a raffle where the user can get random number for customers and save them to a worksheet.
They can then use the worksheet to randomly pick raffle ticket numbers.

# Table of Contents

- [User Experience](#user-experience)

  - [User Goals](#user-goals)

  - [Developer Goals](#developer-goals)

- [Logic and Features](#logic-and-features)

  - [Logic](#logic)

  - [Database Structure](#database-structure)

  - [Features](#features)

    - [Main Menu](#main-menu)

    - [Player Menu](#player-menu)

    - [Enter Player Details](#enter-player-details)

    - [Delete a Player](#delete-a-player)

    - [List of Outstanding Fees](#list-of-outstanding-fees)

    - [Pay Fees](#pay-fees)

    - [Check Kit Sizes](#check-kit-sizes)

    - [Raffle Menu](#raffle-menu)

    - [Finishing Screen](#finishing-screen)

- [Technology](#technology)

  - [Lanuages Used](#languages-used)

  - [Software Used](#software-used)

  - [Python Libraries/Modules](#python-librariesmodules)

- [Testing](#testing)

  - [Validation](#validation)

    - [PEP8CI](#pep8)

  - [Manual Testing](#manual-testing)

  - [Bugs/Known Issues](#bugsknown-issues)

- [Deployment](#deployment)

  - [Git and Github](#git-and-github)

  - [Deployment to Heroku](#deployment-to-heroku)

- [Future Development](#future-development)

- [Credits](#credits)

- [Acknowledgements](#acknowledgements)



# User Experience

## User Goals
  - As a user they want to see a list of all players to note their username before making changes.
  - As a coach or director of the club they want a way to add new players to the team.
  - As a user they want to be able to delete a player who has left the club.
  - As a user they want to be able to pay an installment or their fee off in full when payment is received.
  - As a user they want to be able to show the full list of player for the whole club.
  - As a user they woule like to look at total number of sizes in kits for when they want to order kits.
  - As a user they would like to get random raffle numbers to give to customers when they purchase raffle tickets.

## Developer Goals
  - As a developer, I want to keep the program simple
  - As a developer, I want to make navigating through straight forward and easy to follow.
  - As a developer, I want to create a easy to read table to display information from the spreadsheet.


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

### Finishing Screen

![Finishing screen](/assets/images/finishing-screen.png)

- This screen deploys when the programs ends


# Technology

## Languages Used

- [Python](https://www.python.org/) - high level programming language
- [Markdown](https://www.markdownguide.org/cheat-sheet) - language used to write README and TESTING documents.

## Software Used

- [LucidChart](https://lucidchart.com) - LucidChart was used to create flowchart for the project.
- [Git](https://git-scm.com/) - Git was used for version control by using the Gitpod terminal to commit to Git and push to Github.
- [Github](https://github.com/) - Github was used to write and store the projects code.
- [Google Sheets](https://www.google.com/sheets/about/) - Used to store all the data from the program.
- [Heroku](https://www.heroku.com/home) - Heroku was used to deploy the project.
- [Text ASCII Art Generator](https://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20) - Used to create the logo for the project.

## Python Libraries/Modules

- [gspread](https://docs.gspread.org/en/v5.7.0/) - used for control of Google Sheets 
- [OAuthLib](https://oauthlib.readthedocs.io/en/latest/) - needed to access google sheets
- [os](https://www.geeksforgeeks.org/os-module-python-examples/) - used to write the clear screen function
- [time](https://docs.python.org/3/library/time.html) - python module - used to pause screen before continuing
- [sys](https://superfastpython.com/exit-process/#What_is_sysexit) - Python Module used to exit the program
- [random](https://www.w3schools.com/python/ref_random_random.asp) - Python Module used to generate random numbers for raffle
- [tabulate](https://www.statology.org/create-table-in-python/) - Used to create the table to print the data from the player worksheet
- [colorama](https://pypi.org/project/colorama/) - Used to colour the text in terminal output.

# Testing

## Validation

### PEP8

- [PEP8CI](https://pep8ci.herokuapp.com/) - This was used test the code. No errors where found in the code. 

![PEP8CI](/assets/images/pep8.png)

## Manual Testing

Please find manual testing file here: [TESTING.md](/TESTING.md)

## Bugs/known issues

- In the function to collect only the players with fees due from the database, I found it hard to find a function to help with this.  I have worked out a way to do what I want, but it has resulted in the table being slow when it is loading to the screen.  I have not found a better way of doing this and I am aware it is a little slow.

- I use clear screen function, to clear up the screen when new menu etc is loaded. This is working fine on the github terminal, but I have noticed on heroku, it doesnt seem to clear fully and I dont know how to fix this.

![error heroku](/assets/images/heroku-error.png)

-  decided to change the year to a username, and it was not as straight forward as i thought, 
i worked out that I needed to pass all the data into the function, but was finding it difficult to iterate through the sublist to check if the username was already used. I found from a online search on the stackoverflow site that using a built-in function any() would work. [Link for any() function](https://stackoverflow.com/questions/40514139/check-if-an-item-is-in-a-nested-list)
from this i decided instead of calling all data from the spreadsheet I made it global.
 
 - When doing function to delete player didnt work got an error about int str and I realised the row number was a string and to changed to an int.
It worked but got a warning to use delete_rows() instead of delete_row() so changed that and worked fine after that.

- The below warnings are on githib and are out of my control to fix.
![warnings on github](/assets/images/error-github.png)

# Deployment

## Git and GitHub
- Code Institute template was used to create GitHub public repository st-mochtas-fc.

- I developed programm, often commiting changes using terminal commands.

- I made sure that all my libraries and packages are listed in requirements.txt.

- When program was ready for further deployment I visited heroku.com website to deploy on heroku.

## Deployment to Heroku
- I visited https://heroku.com/ and opened dashboard. Then I clicked button "New" and selected "Create new app" button.

- I entered my app name as "St-Mochtas-FC", region to Europe and clicked on "Create app" button

![create app](/assets/images/createapp.png)

- The next step was to go to "Deploy" tab and then to "Deployment method" section to authorize and connect my GitHub account.

![connect github](/assets/images/connectgithub.png)

- When succesfully connected I selected main branch from "St-Mochtas-FC" repository.

- Then I went to "Settings" tab

- In the next step I went to "Config Vars" section and added KEY "CREDS" with value of my credentials file creds.json (copy all and paste).

![config vars](/assets/images/configvars.png)

- Next to "Buildpacks" section. In the next step I added pyhton and nodejs buildpacks, making sure python was first then nodejs.

![buildpacks](/assets/images/buildpacks.png)

- In the next step I went back to "Deploy" tab and decided to use manual mode, however automatic mode is also available to deploy, which I done at a later time.

![connected screen](/assets/images/connected.png)

- The link to my deployed app was shown on screen: [Live Link](https://st-mochtas-fc.herokuapp.com/)

## Local Deployment
- To make a local copy of this project, you can clone it. In your IDE Terminal, type the following command to clone my repository:

- git clone https://github.com/AngMaher/St-Mochtas-FC

## To Fork the Repository
- To make a copy or ‘fork’ the repository
  - Log into GitHub and locate the repository
  - Select the ‘fork’ option to create and copy the original
  Link to Github repository: ![Github](https://github.com/AngMaher/St-Mochtas-FC)

# Future Development

- If I had more time or decided to develop my program further I would bring in object oriented programming, setting the player up as an object. 
- I would set it up that each manager could look after their own team by seaching under a team code.
- Maybe have a parents section where they could register for summer camps.
- I would bring in OOP if I had more time and create a class for player and maybe expand and do more functionality with player.

# Credits

## Code

- Line 17 - 26 connection to google sheets taken from Love Sandwiches
- Line 258 - any() found examples on w3schools [link](https://stackoverflow.com/questions/40514139/check-if-an-item-is-in-a-nested-list)
- Line 487 - found function to clear screen on stackoverflow [link](https://stackoverflow.com/questions/2084508/clear-terminal-in-python)
- Line 502 - found out about sys.exit() from superfastpython [link](https://superfastpython.com/exit-process/)

## Media

- [Text ASCII Art Generator](https://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20) - to create my logo

## Resources

 - Websites used along with course material were [StackOverFlow](https://stackoverflow.com/questions/18754276/python-for-beginners), and [W3Schools](https://www.w3schools.com/python/)

 # Acknowledgements
  
- I would like to thank my mentor Jubril for his guidance through the project and my many testers (family and friends).
