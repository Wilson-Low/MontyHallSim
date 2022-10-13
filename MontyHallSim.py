import random

# Set up simulation stats
simulationCount = 10000
switchChoiceWins = 0
keepChoiceWins = 0

# Run simulation
for i in range(simulationCount):
    # Set up game with initial choice
    closedDoors = [0, 1, 2]
    car = random.randint(0, 2)
    choice = random.randint(0, 2)

    # Open a door
    openableDoors = [door for door in closedDoors if door !=
                     car and door != choice]
    closedDoors.remove(random.choice(openableDoors))

    # Simulate result if you keep your choice
    if choice == car:
        keepChoiceWins += 1

    # Simulate result if you switch your choice
    closedDoors.remove(choice)
    choice = random.choice(closedDoors)
    if choice == car:
        switchChoiceWins += 1

# Print simulation stats
print("Keep choice win rate: ", keepChoiceWins/simulationCount)
print("Switch choice win rate: ", switchChoiceWins/simulationCount)
