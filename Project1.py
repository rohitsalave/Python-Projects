# Website checker
print("🔍WEBSITE CHECKER🔍")


url = input("\nEnter Yor website's Complete url:")


if url.startswith("https://"):
    print("this website is secure ✅")
elif url.startswith("http://"):
    print("this is not a secure connection❌")
else:
    print("(Recheck) this not look's like a complete url🤔")
