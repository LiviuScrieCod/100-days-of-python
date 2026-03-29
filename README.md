# 🐍 100 Days of Code - The Complete Python Pro Bootcamp

Not just a simple Python course, but having fun while learning and also turning it into a hub of 100 challenges turned
portfolio.

### 🛠 Technologies used:

* PyScript - the heart of the project. Manages DOM and creates page elements. I chose it because I want more Python in
  my Python project!
* Python - I mean... it's a Python project.
* Vanilla CSS - keeping things simple in terms of UI/UX
* HTML5 - well... that's a given I guess

### 💡 The vision

The whole UI is basically fueled by a Python dictionary. I didn't want to waste time copy-pasting HTML all over the
place (plus, imagine the horror of changing anything). It's cleaner, faster, easier to edit and allows me to focus on
actual learning and coding.

## 📝 Day-by-day ***"happenings"***!

### Day 1: Planning & Pyscript integration

* Built the backbone of the hub
* Wrestled pyscript.json to get things displayed using localhost
* Managed to get 100 elements rendered on the page, proper info displayed
* Created a very basic CSS styling, just to get things looking ok-ish, proper design on the way.

### Day 2: First crack at the Python projects

* Band Name Generator - decided on a UI and solution for code execution on the page (literally)

### Day 3: Band Name Generator

* Implemented a default html/css for the first and future projects (old crt terminal vibe)
* Created a list of 10 questions to be prompted at random
* Added weight so that users get mostly 2-4 questions in order to avoid lengthy names
* Ability to check all names generated during a single session
* Added ASCII art for design
* Realize I bit off more than I could chew and decided to change my strategy: switch to individual projects while I
  figure out how to make a proper mvc-ish system

### Day 4: Still at Band Name Generator project

* Did some testing towards mimicking a mvc system; more work needs to be done
* Redid the BNG logic to include the option to try generating more names (refactoring)
* Merged branch

### Day 5: Opinionated tip calculator

* New branch, basic app logic developed, based on course instructions
* A simple "tip calculator" app, meant to take in the bill total, number of customers and tip amount (%) and return the
  user's amount (mean+tip)
* Decided to give it a sassy voice and include some "dialog"
* I'm still figuring out the mvc party of the whole project, so I focused on app logic exclusively
* Finished logic and tested, project done!

### Day 6: Text adventure

* New project, new branch
* I'll be creating a text adventure (and ascii art) game
* A hero enters a cave to resque the princess (classic) but perils await him at all steps. Will he be met with a
  gruesome fate or live on to tell the tale?
* Decided to have a logic file and an art&text file to keep things DRY and clean
* Set up a TODO list for implementation clarity
* Decided to implement keywords that can be used throughout the story - reduced the scope to "during the fight"
* Extended the scope of the story altogether - made it WAAAAAAAAY too complex compared to the course example
* Added "branching" options, an instakill option, an abandon quest option, HP and consumables
* Added a trap and a locked door hiding a treasure
* Added a B0$$ (chance to hit/miss, critical strikes, boss "phases") fight and covered retreat/defeat/victory
* Added ASCII art for key moments
* Added very basic music via PowerShell with parallel processing; music changes based on context (4 tracks in total)
* BBEG and player stats handled in dictionaries
* Game assets handled in a separate folder as dictionaries
* Sanitized user inputs in order to avoid user hassle/errors

### Day 7: Rock, paper, scissors

* New project, new branch
* I'll be recreating the classic with a couple of twists
* I'll add 3 game modes: classic highscore, championship and friendly:
    * ~~Classic highscore~~ Survival highscore - the classical way of playing the game, no game over, just win battles,
      get multipliers for consecutive wins, so how high you can get, beat opponents to get "warrior tags"
    * ~~Championship - story mode of sorts, face off opponents with "special" powers and face a boss that's more than
      meets the eye~~ Knockout - star in a classic tournament with qualifying groups, quarters, semi-finals and a
      final against a nasty B0$$; Do what must be done to win or go home covered in shame! Honor is for the weak.
    * ~~Friendly - but is it though? Similar to classic, but with special moves,"game balancing mechanics" and a
      powerup~~ Hunter - there is no "losing". This game mode focuses on beating certain objectives. The game ends
      once you nailed every single one!

### Day 8: Still at RPS

* finished and tested survival mode (classic highscore rebranding)
* new feat to implement - reputation and random opponents

### Days 9-13: Still at RPS

* implemented reputation and random opponents, as well as a reset caused by losing a match
* implemented a tournament style gameplay mode - groups, quarters, semi-finals and a boss fight.
* groups are 3 matches against random opponents, while quarters and up it's best out of 3/5 with a twist at the end.
* decided to implement an achievements run - no game over if you lose a match, but there are rotating goals to achieve
  during gameplay
* implemented a flagging/unlock system for achievements and powerups
* Gave up on the idea of refactoring the code - it's already far exceeded the intended scope of the course project and
  there's nothing to be gained by spending even more time on it
* Could do some more UI/UX improvements, but I've already spent too much on this project; it was a nice project, but
  it's time to move on!

### Day 14: Password Generator

* a classic password generator that takes random elements from several lists (letter, symbols and numbers) and
  concatenates them into a string (the password)
* I made sure users can only input digits and that they can't get to the next question without providing a valid
  answer (try-except for ValueError management)
* I made sure users can't request targeted characters if it exceeds the requested password length, handled in real time
* offered users a chance to review all generated passwords during the session (without exiting the program)
* added small UX elements (timers, ascii art, customer support lines)
* refactored code and replaced data structures (moved most things in a different file, in nested dictionaries)
* Among its features are:
    * the ability to customize password generation (choose specific types of characters as well as the password length)
    * the ability to leetify a "normal" password; each leetified password also gets a "cool rating"
    * the ability to audit each password, individually or bulk (a custom evaluation based on length, type of chars used
      and other variables)
    * the ability to review the passwords the user created as well as aditional info (generation type, security rating
      etc.)
    * a small search function in the vault which retrieves a password + info based on a full or partial user input
    * the ability to save the passwords collection in a file on the user's computer
* project done, time to move on!

### Day 15-20: Discounted generic get out of the maze game (in ASCII!)

* The project has me working on Reeborg's World, but doing so wouldn't allow me to add anything to the portfolio. As
  such, I decided to create the whole challenge in Python: create a random maze, add the robot and create an
  algorithm the robot may use to exit the maze. Easier said than done! 😅
* What I ended up doing was to create a "micro game engine" (wishful thinking allowed!) that facilitates the
  creation of fully randomized mazes. Each maze is unique, fully customizable (size, and # of obstacles) and I
  implemented an algorithm that makes sure each maze is solvable.
* Users are never spawned too close to the exit, nor is there any chance for the player to be walled in inside the
  maze (no no-win-scenario spawning)
* I implemented persistent highscore saving by creating a file in the user's local storage, which saves and
  overwrites (if necessary) the best 10 scores, even between sessions. I did reduce it in score as it only counts
  score from maze to maze, instead of gaming session to gaming session. (Yes, bigger, more complex mazes generate a
  higher score if
  completed). Scoring takes into account, movement and obstacle navigation inside the maze.
* I implemented resource management: users have a battery (max number of moves allowed) and encounter Traps (which
  drain the battery) while they navigate the maze (risk/reward balance)
* Minor UI/UX elements by formatting the maze and various elements of the game to resemble retro arcade style.
* Players move through the maze by using w,a,s,d, each move resetting the general view.
* The game handles state management, separates gameplay from game data, handles I/O in order to "render" graphics
  and has data persistence. It might not be much, but it's honest work ^_^!
* could be improved by adding sound, fog of war, battery recharge and other game features, but that would overkill
  the overkill that has been the project for this "day". Project done, time to move on!
