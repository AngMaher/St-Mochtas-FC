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