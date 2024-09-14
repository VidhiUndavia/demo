day=int(input("Enter your date of birth's day = "))
month=int(input("Enter your date of birth's month = "))

if day<=31 and month<=12:
    if month==1:
        if day>=20:
            print("Aquarious")
        else:
            print("Capricorn")
    elif month==2:
        if day>=19:
            print("Pieces")
        else:
            print("Aquarious")
    elif month==3:
        if day>=21:
            print("Aries")
        else:
            print("Pieces")
    elif month==4:
        if day>=20 and day<=30:
            print("Taurus")
        elif day<=20 and day>=1:
            print("Aries")
        else:
             print("Invalid Input")
    elif month==5:
        if day>=21:
            print("Gemini")
        else:
           print("Taurus")
    elif month==6:
        if day>=21:
            print("Cancer")
        else:
            print("Gemini")
    elif month==7:
        if day>=23:
            print("Leo")
        else:
             print("Cancer")
    elif month==8:
        if day>=23:
            print("Virgo")
        else:
             print("Leo")
    elif month==9:
        if day>=23:
            print("Libra")
        else:
            print("Virgo")
    elif month==10:
        if day>=23:
            print("Scorpio")
        else:
              print("Libra")
    elif month==11:
        if day>=22:
            print("Saggitarius")
        else:
             print("Scorpio")
    elif month==12:
        if day>=22:
            print("Capricorn")
        else:
            print("Saggitarius")
    else:
        print("Invalid Input") 
else:
    print("Invalid Input")