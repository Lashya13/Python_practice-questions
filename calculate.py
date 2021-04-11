#Registered_user = {'mini':'9597965854','sedan':'9994042856','suv':'9362883601'}
Registered_user =[]
print("Mini")
def mini(distance):
    base_charge = 50
    if (distance <=3):
        return base_charge
    elif (distance>3 and distance<=15):
        baseDistance = distance - 3
        return base_charge + baseDistance*10
    elif (distance >15 and distance <75):
        baseDistance = distance - 3
        MiddleDistance = 15
        NextDistance = baseDistance-15
        return base_charge +MiddleDistance*10+ NextDistance*8  
    elif(distance>=75):
        return distance*8

print("sedan")
def sedan(distance):
    base_charge = 80
    if(distance<=5):
         return base_charge
    elif(distance>5 and distance<=15):
        baseDistance = distance-5 
        return base_charge + baseDistance*12   
    elif (distance>15 and distance<100):
        baseDistance = distance-5 
        MiddleDistance = 15
        NextDistance= baseDistance-MiddleDistance
        return base_charge + MiddleDistance*12 +NextDistance*10 
    elif(distance>=100):
        return distance*10         

print("SUV")
def suv(distance):
    base_charge = 100
    if(distance<=5):
        return base_charge
    elif(distance>5 and distance<=15):
        baseDistance = distance-5 
        return base_charge + baseDistance*15
    elif(distance>15):
        baseDistance = distance-5 
        MiddleDistance = 15
        NextDistance= baseDistance-MiddleDistance
        return base_charge + MiddleDistance*15+NextDistance*12

#print(Registered_user)
while True:
    question = input("Do you want to enter the kilometer y/n?").lower()
    if (question == 'y'):
        distance = int(input("enter the kilometers:"))
        mobile_number = int(input("enter mobile number:"))
        fare_of_mini = mini(distance)
        fare_of_sedan = sedan(distance)
        fare_of_suv = suv(distance)
        if mobile_number in Registered_user:
            print('Mini', fare_of_mini) 
            print('Sedan', fare_of_sedan) 
            print(fare_of_suv)   
            
        
        else:
            Registered_user.append(mobile_number)
            print(fare_of_mini*75/100)
            print(fare_of_sedan*75/100)
            print(fare_of_suv*75/100)

    elif(question == 'n'):
        print("Thank You!!!") 

         







