# International Traffic Pack

This Git repository holds all the Python code used to create the International Traffic Pack for the game Euro Truck Simulator 2. 
The International Traffic Pack adds foreign vehicles, that is vehicles with foreign license plates, to the AI traffic for each of the countries featured in the game.
Currently, the set of foreign vehicles includes both cars and semi-trucks. I am planning on adding more traffic types in the future. 

## Motivation
The absence of foreign traffic in Euro Truck Simulator is a noticeable void in the game's otherwise immersive experience. Especially when it comes to foreign truck trucks, 
which hold a significant share in European traffic. For quite a while, the prospect of incorporating foreign traffic appeared to be a daunting challenge, seemingly impossible to achieve by both modders and even by SCS Software. As I was 
experimenting with custom license plates for the ProMods map mod, I discovered a novel approach that could make this long-awaited feature a reality. 
Hence, I was determined to show its potential and built custom code to produce this rather complex mod.

## Features
The mod...
* adds foreign car traffic to each of the countries featured in the vanilla game (including all map DLCs)
* adds foreign truck+trailer traffic to each of the countries featured in the vanilla game (including all map DLCs)
* features spawn rates per foreign country and vehicle type, based on statistics and expert evaluations, so that the real-life traffic distribution is accurately simulated
* adds traffic from random countries with a small probability
* allows foreign vehicles to spawn at parking spots
* maintains the native distribution of spawn rates for the different vehicles abroad so that those with high/low spawning rates have high/low spawning rates abroad as well 
* guarantees that vehicles maintain the steering wheel orientation of their origin country when driving in foreign countries
* features trucks, trailers, and cars from the vanilla game only
* features a subset of all trailers to appear abroad to prevent memory overflows and to filter out trailer types that generally appear only in national traffic

## Compatibility

### Map mods
The current edition is aimed at the vanilla game, but it can be used with any map mod that features (a subset of the) vanilla countries. 
However, do keep in mind that vehicles from non-vanilla countries will not appear abroad. I am currently working on a version aimed at ProMods, in which I will add vehicles from all the countries featured in their main map mod.

### Traffic mods
This mod works by adding a country-specific variant of each traffic vehicle to the AI traffic. The spawn rates are designed with the set of vanilla vehicles in mind.
Hence, any mod that adds additional AI vehicles will likely result in a reduction in the proportion of international traffic. Mods that alter the overall traffic density 
should work just fine in combination with this mod. I will work on an add-on featuring the cars from Jazzycats AI Traffic mod, and maybe a separate one for his Painted Truck Traffic Pack. 

## Contribute to this project
* Feel free to take a look at my open code repository to look at the technicalities of the mod.
* Feel free to produce add-ons featuring additional countries and/or vehicles yourself using my code or an adaptation of it, under the condition that credits are given.
* The spawn rate configuration for cars can be found here: 
* The spawn rate configuration for semi-trucks can be found here:
* If you have any feedback on how to improve the parameters, please let me know via the official thread in the SCS forum or open an issue on GitHub.

# Conditions for redistribution of the mod 
* You are allowed to publish this mod on other websites, under the condition that the original download link is featured and credits are given.
* You are allowed to create add-ons for this mod featuring additional vehicles or countries, under the condition that the original project is mentioned and credits are given. 

## Credits
Mod author: Elitesquad Modz
Research, reference & technical assist: The ProMods Team, Ultras KP, Daniminho 
