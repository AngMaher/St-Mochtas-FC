# St Mochtas Football Club Application

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

https://lucid.app/lucidchart/a7266b3b-06cc-49f8-b512-7ef2e880f1b5/edit?viewport_loc=-838%2C70%2C4451%2C2046%2C0_0&invitationId=inv_2b70d115-293e-4ac8-8826-07a126004676

![flow chart](/assets/images/flowchart.jpeg)

Git and GitHub
Code Institute template was used to create GitHub public repository home-library-app. In template repository I clicked on "use this template" --> "create new repository", I chose repository name and clicked on the green button "Create repository from template".

I cloned repository to my local machine using GitHub Desktop and opened it in PyCharm IDE.

I developed programm, often commiting changes using terminal commands:

git add .
git commit -m "Do something"
git push
I made sure that all my libraries and packages are listed in requirements.txt.

When program was ready for further deployment I visited heroku.com website to deploy on heroku.

Deployment to Heroku
I visited https://heroku.com/ and opened dashboard. Then I clicked button "New" and selected "Create new app" button.

I entered my app name as "home-library-app-ci", chose region to Europe and clicked on "Create app" button

deploy1

The next step was to go to "Deploy" tab and then to "Deployment method" section to authorize and connect my GitHub account.
deploy2

Upon succesfull connection I selected main branch from "home-library-app" repository.
deploy3

Then I went to "Settings" tab...
deploy4

... and next to "Buildpacks" section. In the next step I added pyhton and nodejs buildpacks. Order here is very important.
deploy5

In the next step I went to "Config Vars" section and added KEY "CREDS" - that maches my token name defined in python constant in api/google_sheets_api.py - with value of my credentials token (copy all and paste).

I added key "PORT" with value "8080" and save changes.

deploy6

In the next step I went back to "Deploy" tab and decided to use automatic deploys, however manual mode is also available to deploy chosen branch.
deploy7

The link to my deployed app was shown on screen: https://home-library-app-ci.herokuapp.com/
