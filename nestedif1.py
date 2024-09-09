exam_marks=int(input("Enter your exam marks"))
if exam_marks>=40:
    print("Congrats,You are eligible for next HR INTERVIEW round")
    hr_interview=int(input("If u pass the interview then enter 1 or 0"))
    if hr_interview==1:
        print("Congrats,You are eligible for next FINAL INTERVIEW round")
        final_interview=int(input("If u pass the interview then enter 1 or 0"))
        if final_interview==1:
            print("Congrats,Please submit your original documents on time")
        
        else:
            print("Sorry, bater luck next time")
    else:
        print("Sorry, bater luck next time")
else:
    print("Sorry, bater luck next time") 