# International Traffic Pack

This Git repository holds all the Python code used to create the International Traffic Pack for the game Euro Truck Simulator 2. 
The International Traffic Pack adds foreign vehicles, that is vehicles with foreign license plates, to the AI traffic for each of the countries featured in the game.
Currently, the set of foreign vehicles includes both cars and semi-trucks. I am planning on adding more traffic types in the future. 

### Motivation
The absence of foreign traffic in Euro Truck Simulator is a noticeable void in the game's otherwise immersive experience. Especially when it comes to foreign truck trucks, 
which hold a significant share in European traffic. For quite a while, the prospect of incorporating foreign traffic appeared to be a daunting challenge, seemingly impossible to achieve by both modders and even by SCS Software. As I was 
experimenting with custom license plates for the ProMods map mod, I discovered a novel approach that could make this long-awaited feature a reality. 
Hence, I was determined to show its potential and built custom code to produce this rather complex mod.

### Resulting mod
To download the resulting mods and find more information about them, please visit the [official forum thread](https://forum.scssoft.com/viewtopic.php?t=324065) on the SCS forum 

### Technicalities
* The code is written in Python
* Currently, code for trucks, trailers, and cars from the vanilla game has been implemented
* Dictionaries are used to specify the spawn configuration per country and vehicle type, including:
  * The probability of spawning national traffic
  * The probabilities of spawning traffic from explicitly defined countries
  * The probabilities of spawning random traffic, which is uniformly distributed over the unspecified countries 
* The spawn rate configuration for cars can be found [here](car_vanilla.py)  
* The spawn rate configuration for semi-trucks can be found [here](semi_vanilla.py) 

### Contribute to this project
* Feel free to produce add-ons featuring additional countries and/or vehicles yourself using my code or an adaptation of it, under the condition that credits are given.
* If you have any feedback on how to improve the parameters, please let me know via the official thread in the SCS forum or open an issue on GitHub.

### Credits
Code and mod author: Elitesquad Modz  
Research, reference & technical assist: The ProMods Team, Ultras KP, Daniminho 

Copyright © 2023 All Rights Reserved
