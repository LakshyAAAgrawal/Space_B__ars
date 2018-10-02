# Space_B__ars
This is a game made on Python, and runs on the PyGame libraries. 

All the rogue keys have escaped your keyboard, except the loyal Space_B__ar.
Use the Space Bar to capture all of the other keys. Remember, if you try to capture an already captured key, it will escape, and so, avoid trying to capture the space bar at all costs.
The keys that you have captured can be used to form commands, which help you capture the other keys. So, you could use the command "slow" to slow down the stream of characters. And yes, even to save the game, use the command "save".

The main idea behind the game is to be an expansive user modded game. Thus, one of the goals is to have a large list of commands that the user can execute, and must explore to find out.
Some of the commands that have been thought of are - protect, reverse, slow, save, wildcard etc.
The player will not be knowing which all commands exist in the game, but rather be expected to try out the different words that can be formed with the available keys, and see what happens and works.

# Installation instructions
The game is written in python3 and therefore requires python3 to be installed along with the pygame library. It also uses the pickle library - which is inbuilt.
To install the pygame library using pip, execute
```
  pip3 install pygame
```
Then, Download the zip file from the here( https://github.com/LakshyAAAgrawal/Space_B__ars/archive/master.zip ) and extract it. Then go to the extracted folder, by using 
```
cd Space_B__ars
```
then, to run, execute -
```
  python3 game.py
```

Windows users can just execute -
```  
  pip install pygame
  python game.py
```
# Contribute
The project highly encourages any contributions, in any form - graphics, sounds, game commands, or code contributions. All suggestions, bug reports and idea contributions are welcome in the discussions. Please report as many bugs, and create issues.
Immediate requirement-
* Sounds
  * 1. Background Music
  * 2. In-game sounds
* Game Logo
* Documentation
* Code maintenance and cleaning
* Implementation of commands
  * 1. Protect/Shield - After the player uses this command, encountering a Spacebar will not kill, during the time the command is active.
  * 2. Wildcard - The player is given a choice to select any one of the characters from the keyboard which they wish to capture.
* Suggestions for new Commands.

Original Concept:-
* Lakshya A Agrawal
* Shrikant Garg
* Rahul Kukreja
* Nitish Gupta
