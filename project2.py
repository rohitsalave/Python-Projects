# step Counter
print("🚶‍➡️  STEPS GOAL COUNTER🚶‍♂️")

stepgoal = int(input("\n🎯What is your daily step goal ?:"))
steps = int(input("🤔How many steps you walked today ?:"))


if stepgoal == steps:
    print("\n🎉Congratulations!!! you completed your daily goal.")


elif stepgoal > steps:
    print("\n😓You are lacking behind your goal by :", stepgoal-steps, "steps")


elif stepgoal < steps:
    print("\n🎉Congratulations !! You exceed your daily Goal by: ",
          steps-stepgoal, "steps.")


else:
    print("\n😵Servers Down")
