# Stopping Distance Calculator
 
A small Python command-line tool that checks whether a vehicle can stop before reaching a pedestrian, given its speed, the road condition and the distance to the pedestrian.
 
Inspired by the **REAL** framework (requirements engineering for machine-learning failures), where a safety requirement is checked against scenarios and failures show where the requirement needs refining. This project is a simple, single-scenario illustration of that idea. It does **not** implement REAL's method (no scenario generation, no simulator).
 
- REAL repository: https://github.com/darkaengl/REAL
- Paper: https://arxiv.org/abs/2606.31589
## What it does
 
1. Asks for three inputs: speed (mph), road condition (`dry`, `wet` or `icy`) and pedestrian distance (metres).
2. Converts the speed from mph to m/s.
3. Calculates the **reaction distance** (speed x a fixed 1.5 s reaction time).
4. Calculates the **braking distance** using `v² / (2a)`, with a deceleration value for each road condition.
5. Adds the two to get the **total stopping distance** and compares it with the pedestrian distance.
6. Prints `SAFE` with the spare distance, or `DANGER` with how far the vehicle overshoots.
## Assumptions
 
| Setting | Value |
|---|---|
| Reaction time | 1.5 s |
| Deceleration, dry | 7.5 m/s² |
| Deceleration, wet | 4.5 m/s² |
| Deceleration, icy | 2.0 m/s² |
 
These are simplified, illustrative values (flat road, constant deceleration, no tyre or brake modelling), not real-world safety figures.
 
## How to run
 
Requires Python 3.
 
```bash
python Stopping_distance_Calculator.py
```
 
### Example 1: safe
 
```
Please enter the value in mph: 30
Please enter the road condition (Wet, Dry, icy): dry
Please enter the pedestrian distance in meters (m): 40
 
The Reaction distance is 20.12 m
The Braking distance in dry is 11.99 m.
The total stopping distance is 32.11 meter
Status: SAFE
The vehicle will stop safely at 7.89 meters away from pedestrian.
```
 
### Example 2: danger
 
```
Please enter the value in mph: 50
Please enter the road condition (Wet, Dry, icy): wet
Please enter the pedestrian distance in meters (m): 40
 
The Reaction distance is 33.53 m
The Braking distance in wet is 55.51 m.
The total stopping distance is 89.04 meter
Status: DANGER
The vehicle will exceed the available space by 49.04 meters.
```
 
## Project structure
 
- `Stopping_distance_Calculator.py`: the script (input, calculation and safety assessment in one file)
- `README.md`: this file
## Known limitations
 
- Handles one scenario per run; there is no batch or sweep mode.
- No automated tests yet.
- No input validation: non-numeric or negative values are not handled.
- An unrecognised road condition currently falls back to `dry`.
- Does not yet suggest a safe speed when the check fails.
## Possible next steps
 
- Move the calculation into functions and add `pytest` tests.
- Sweep many speed and road-condition combinations against a safety requirement and report which ones fail.
- Calculate the maximum safe speed for each condition when a scenario fails.
- Make reaction time a parameter.
