Distance=int(input("Enter the distance in Kilometer"))
print("Mini ")
def mini(distance):
    if (distance<=75):
        return estimatedCostWithBaseCharge(distance)
    else:
        return estimatedCostWithoutBaseCharge(distance)
def estimatedCostWithBaseCharge(distance):
    baseDistance = distance - 3
    if (baseDistance<=15):
        return estimatedCostWithoutAdditionalCharge(baseDistance)
    else:
        return estimatedCostWithAdditionalCharge(baseDistance)
def estimatedCostWithoutBaseCharge(distance):
    cost = distance*8
    print("Estimated cost - ", cost)
def estimatedCostWithoutAdditionalCharge(baseDistance):
    baseCharge = 50
    cost = baseCharge + (baseDistance * 10)
    print("Estimated cost - ", cost)
def estimatedCostWithAdditionalCharge(baseDistance):
    baseCharge = 50
    additionalCharge = baseDistance - 15
    cost = baseCharge + (15 * 10) + (additionalCharge * 8)
    print("Estimated cost - ", cost)
mini(Distance)

print("Sedan ")
if (Distance<=100):
    base = Distance - 5
    if (base<=15):
        cost = 80+(base*12)
        print("Estimated cost - ",cost)
    else:
        additionalCharge = base - 15
        cost = 80+(15*12)+(additionalCharge*10)
        print("Estimated cost - ", cost)
else:
    cost = Distance*10
    print("Estimated cost - ", cost)
print('SUV')
base = Distance - 5
if (base<=15):
    cost = 100+(base*15)
    print("Estimated cost - ",cost)
else:
    additionalCharge = base - 15
    cost = 100+(15*15)+(additionalCharge*12)
    print("Estimated cost - ", cost)