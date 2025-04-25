print("📱Grade Calculator")

marks = []


while True:
    score = input("\n🔍Enter a test score (or 'done'):")
    if score.lower() == "done":
        print("Good bye 👋")
        break

    marks.append(float(score))
    average = sum(marks) / len(marks)
    print(f"Average:{average:.1f}")
    if average >= 90:
        print("Grade:A 🎯")
    elif average >= 80:
        print("Grade:B 🆙")
    elif average >= 70:
        print("Grade:C 😓")
    else:
        print("Grade:D or F 😵")
