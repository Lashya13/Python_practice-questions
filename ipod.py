def country():
    countryName = input("Enter the country name:")
    
    if (countryName == "Brazil"):
        stockInBrazil =100
        stockInArgentina = 100
        requiredIPOD = int(input("how many ipods do you want to buy?"))
        
        costOfEachInBrazil = 100
        costOfEachInArgentina =50

        print("country : ", countryName)
        if (requiredIPOD <=100):
            stockInBrazil = stockInBrazil - requiredIPOD
            print((requiredIPOD*costOfEachInBrazil), ":" ,(stockInBrazil), ':', stockInArgentina)
            stockInBrazil+=requiredIPOD
        elif (requiredIPOD == 100):
            stockInBrazil = stockInBrazil - requiredIPOD
            print((requiredIPOD*costOfEachInBrazil), ":" , (stockInBrazil), ':', stockInArgentina )
            #stockInBrazil+=requiredIPOD
        elif (requiredIPOD >100 and requiredIPOD<=200):
            required = 100
            brazilItem = requiredIPOD - required   #20
            stockInBrazil = stockInBrazil -  required
            stockInArgentina = stockInArgentina-brazilItem
            brazilString = str(brazilItem)
            result = brazilString[0]
            finalResult = int(result)
            print((required*costOfEachInBrazil)+(finalResult *400) + (brazilItem*costOfEachInArgentina) , ':', stockInBrazil , ':', stockInArgentina )
            stockInBrazil+=required
        else:
            print("out of stock!!!")   

    elif (countryName == "Argentina"):
        stockInBrazil =100
        stockInArgentina = 100
        requiredIPOD = int(input("how many ipods do you want to buy?"))
        #stockInArgentina = stockInArgentina - requiredIPOD
        costOfEachInBrazil = 100
        costOfEachInArgentina =50
        print("country : ", countryName)
        if (requiredIPOD <=100):
            stockInArgentina = stockInArgentina - requiredIPOD
            print((requiredIPOD*costOfEachInArgentina), ':', stockInBrazil ,":" ,(stockInArgentina) )
            stockInArgentina+=requiredIPOD
        elif (requiredIPOD == 100):
            stockInArgentina = stockInArgentina - requiredIPOD
            print((requiredIPOD*costOfEachInArgentina),  ':', stockInBrazil, ":" , (stockInArgentina), )
            #stockInBrazil+=requiredIPOD
        elif (requiredIPOD >100 and requiredIPOD<=200):
            required = 100
            argentinaItem = requiredIPOD - required   #20
            stockInArgentina = stockInArgentina - required
            stockInBrazil = stockInBrazil - argentinaItem
            argentinaString = str(argentinaItem)
            result = argentinaString[0]
            finalResult = int(result)
            print((required*costOfEachInArgentina)+(finalResult *400) + ( argentinaItem*costOfEachInBrazil) ,':',stockInBrazil, ':', stockInArgentina )
            stockInArgentina+=required
        else:
            print("out of stock!!")    


country()
           
   

