#This is a script to check the stopping distance of car using different metrics
#Inspired by Requirment Engineering for Autonommous Driving (REAL)

print("\n=== Stopping distance and safety warning calculator ===")
print("--- Please Enter the values below---")


#Asking user for the required input data
speed_mph = float(input("Please enter the value in mph: "))
road_condition = str.lower(input("Please enter the road condition (Wet, Dry, icy):"))
pedistrian_distance = float(input("Please enter the pedistrian distance in meters (m): "))


#Converting speed from miles per hour (mph) to meters per second (ms)
#1mph = 0.447m/s
speed_in_ms = speed_mph / 2.237

#calculating the reaction distance
reaction_time = 1.5
reaction_distance = speed_in_ms * reaction_time


#Deceleration rates in dry, wet and icy condition
dry = 7.5
wet = 4.5
icy = 2.0


#Calculating breaking distance
if road_condition == "dry":
    breaking_distance = float((speed_in_ms**2)/(2*dry))
    #print(f"The Breaking distance is {breaking_distance} in dry condition.")
elif road_condition == "wet":
    breaking_distance = float((speed_in_ms**2)/(2*wet))
    #print(f"The Breaking distance is {breaking_distance} in wet condition.")
elif road_condition == "icy":
    breaking_distance = float((speed_in_ms**2)/(2*icy))
    #print(f"The Breaking distance is {breaking_distance} in icy condition.")
else:
    print("\nYou entered unrecognisable road conditon. Default dry condition will be used.")
    breaking_distance = float((speed_in_ms**2)/(2*dry))
    #print(f"The Breaking distance is {breaking_distance} in dry condition.")


#Calculating the total stopping distance including reaction and breaking distance
total_stopping_distance = reaction_distance + breaking_distance
#print(f"The total stopping distance in {road_condition} at {speed_mph} mph is {total_stopping_distance} m/s")


#Outputting the details to user
print("\n----------Calculations----------")
print(f"The speed of vehical is {speed_mph:.2f}mph ({speed_in_ms:.2f}m/s)")
print(f"Road condition is {road_condition}")
print(f"The Reaction distance is {reaction_distance:.2f} m")
print(f"The Breaking distance in {road_condition} is {breaking_distance:.2f} m.")
print(f"The total stopping distance is {total_stopping_distance:.2f} meter")
print(f"The pedistrian distance is {pedistrian_distance:.2f} m")


#Deciding if the car can stop safely.
print("\n----------Safety Assessment----------")

if total_stopping_distance <= pedistrian_distance:
    print("Status: SAFE")
    distance_gap = pedistrian_distance - total_stopping_distance
    print(f"The vehical will stop safely at {distance_gap:.2f} meters away from pedistrian.")
else:
    print("Status: DANGER")
    distance_gap = total_stopping_distance - pedistrian_distance
    print(f"The vehical will exceed the available space by {distance_gap:.2f} meters.")

