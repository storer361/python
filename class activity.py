medical_cause=input("did u have a medical cause y or n:")
atten=int(input("enter the attendence of the student:"))
if medical_cause == 'y': #checking the condition 1
    print("you are allowed")
else:
    if atten>=75: #checking the condition 2
       print ("Allowed")
    else:
        print ("Not allowed")