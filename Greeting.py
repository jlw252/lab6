name = input("Name: ")
hobbie = input("Hobbie: ")
month = int(input("Birthday Month: "))
day = int(input("Day Month: "))

print("Hey "+ name+", your hobbie is "+hobbie+".")

if (month == 3 and day >= 21) or (month == 4 and day <= 19):
    print("You are an Aries.")
elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
    print("You are a Taurus.")
elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
    print("You are a Gemini.")
elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
    print("You are a Cancer.")
elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
    print("You are a Leo.")
elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
    print("You are a Virgo.")
elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
    print("You are a Libra.")
elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
    print("You are a Scorpio.")
elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
    print("You are a Sagittarius.")
elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
    print("You are a Capricorn.")
elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
    print("You are an Aquarius.")
elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
    print("You are a Pisces.")
else:
    print("Invalid date.")
