print("DAILY STEP COUNTER")
goal = int(input("What's you todays steps goal ?:"))
steps = int(input("How many steps you walked today ?:"))

remaining = goal-steps

if remaining > 0:
    print(f"you need {remaining} steps to reach your daily goal!!!")

else:
    print(
        f"Congratulations !!! your exceed your daily goal by {-remaining} steps")
