n1=int(input("Enter first grade: "))
n2=int(input("Enter second grade: "))
n3=int(input("Enter third grade: "))
average=(n1+n2+n3)/3
if(average>100):
    print("This mark is invalid")
elif(average<65):
    print(average)
    print("This mark is low for pass")
elif(average>65):
    print(average)
    if(average>=65 and average<=69):
        print("Your letter grade is CC")
    elif(average>=70 and average<=79):
        print("Your letter grade is CB")
    elif(average>=80 and average<=84):
        print("Your letter grade is BB")
    elif(average>=85 and average<=90):
        print("Your letter grade is BA")
    elif(average>=91 and average<=100):
        print("Your letter grade is AA")
