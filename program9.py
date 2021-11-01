rollno= int(input('enter the rol number'))
phy_marks= int(input('enter the marks in physics'))
che_marks=int(input('enter th marks in chemistry'))
comp_science=int(input('enter the marks in computer science'))
total= rollno+phy_marks+che_marks+comp_science
percentage= (total/300)*100
print("Roll number:",rollno)
print("Physics marks",phy_marks)
print("Chemistry marks",che_marks)
print("Computer science marks",comp_science)
print("Total",total)
print("Percentage",percentage)
if percentage>=80:
    print('First class')
elif 70<=percentage>=79:
    print('Second class')
elif 60<=percentage>=69:
    print('Third class')
elif 50<=percentage>=59:
    print('Fourth class')
else:
    print('Fifth class')
