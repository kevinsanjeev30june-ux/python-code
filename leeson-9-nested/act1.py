medical_cause = input("Did you have a medical cause? (Y/N)")
medical_cause = medical_cause.strip().upper()

if medical_cause == 'Y' or medical_cause == 'yes':
    print("You are allowed to the exam")
else:
    attendance = int(input("Enter your attendance:"))
    if attendance>= 70:
        print("Allow")
    else:
        print("Not allowed")
                  
                      