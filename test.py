
burglary=0.001
earthquake=0.002

Alarm={
    "Btrue_Etrue":0.95,
    "Btrue_Efalse":0.94,
    "Bfalse_Etrue":0.29,
    "Bfalse_Efalse":0.001
}

JohnCalls={
    "Atrue":0.90,
    "Afalse":0.05
}

MaryCalls={
    "Atrue":0.70,
    "Afalse":0.01
}

# P(Alarm)
P_Alarm=Alarm["Btrue_Etrue"]*burglary*earthquake+Alarm["Btrue_Efalse"]*burglary*(1-earthquake)+Alarm["Bfalse_Etrue"]*(1-burglary)*(earthquake)+Alarm["Bfalse_Efalse"]*(1-burglary)*(1-earthquake)

# P(Alarm|Burglary)
P_Alarm_Burglary=(Alarm["Btrue_Etrue"]*burglary*earthquake+Alarm["Btrue_Efalse"]*burglary*(1-earthquake))/burglary

#P(Alarm|Earthquake)
P_Alarm_Earthquake=(Alarm["Bfalse_Etrue"]*burglary*earthquake+Alarm["Btrue_Efalse"]*burglary*(1-earthquake))/burglary

#P(JohnCalls)
P_JohnCalls=(JohnCalls["Atrue"]*P_Alarm)+(JohnCalls["Afalse"]*(1-P_Alarm))

#P(MaryCalls)
P_MaryCalls=(MaryCalls["Atrue"]*P_Alarm)+(MaryCalls["Afalse"]*(1-P_Alarm))

#P(JohnCalls|Burglary)
P_JohnCalls_Burglary=(Alarm["Btrue_Efalse"]*JohnCalls["Atrue"])+((1-Alarm["Btrue_Efalse"])*JohnCalls["Afalse"])

#P(MaryCalls|Burglary)
P_MaryCalls_Burglary=(Alarm["Btrue_Efalse"]*MaryCalls["Atrue"])+((1-Alarm["Btrue_Efalse"])*MaryCalls["Afalse"])

#P(JohnCalls|Earthquake)
P_JohnCalls_Earthquake=(Alarm["Bfalse_Etrue"]*JohnCalls["Atrue"])+((1-Alarm["Bfalse_Etrue"])*JohnCalls["Afalse"])

#P(MaryCalls|Earthquake)
P_MaryCalls_Earthquake=(Alarm["Bfalse_Etrue"]*MaryCalls["Atrue"])+((1-Alarm["Bfalse_Etrue"])*MaryCalls["Afalse"])

i=2

while i<3:  
    print("First terms - Alarm(A) , JohnCalls(J) , MaryCalls(M)\nSecond terms - Alarm(A) , Burglary(B) , Earthquake(E)")      
    firstTerm=input("Enter the first term: ")
    secondTerm=input("Enter the second term: ")

    if firstTerm=="Alarm" or firstTerm=="A":
        if secondTerm=="Burglary" or secondTerm=="B":
            print("P(Alarm|Burglary) : ",P_Alarm_Burglary)
        
        elif secondTerm=="Earthquake" or secondTerm=="E":
            print("P(Alarm|Earthquake) : ",P_Alarm_Earthquake)

    elif firstTerm=="JohnCalls" or firstTerm=="J":
        if secondTerm=="Alarm" or secondTerm=="A":
            print("P(JohnCalls|Alarm) : ",JohnCalls["Atrue"])
        
        elif secondTerm=="Burglary" or secondTerm=="B":
            print("P(JohnCalls|Burglary) : ",P_JohnCalls_Burglary)
        
        elif secondTerm=="Earthquake" or secondTerm=="E":
            print("P(JohnCalls|Earthquake) : ",P_JohnCalls_Earthquake)

    elif firstTerm=="MaryCalls" or firstTerm=="M":
        if secondTerm=="Alarm" or secondTerm=="A":
            print("P(MaryCalls|Alarm) : ",MaryCalls["Atrue"])

        elif secondTerm=="Burglary" or secondTerm=="B":
            print("P(MaryCalls|Burglary) : ",P_MaryCalls_Burglary)

        elif secondTerm=="Earthquake" or secondTerm=="E":
            print("P(MaryCalls|Earthquake) : ",P_MaryCalls_Earthquake)

    elif firstTerm=="Q" or firstTerm=="q":
        i=5

    else:
        print("Invlaid Input! try again!")
    
    print("\n")


