def findErrors(min, max):
    lenMin=len(str(min))
    strMin=str(min)
    splitMin=strMin[0:int(lenMin/2)]
    splitMin=int(splitMin)
    errorSum=0
    error=int(str(splitMin)+str(splitMin))
    while error<=max:
        errorSum+=error
        splitMin+=1
        error=int(str(splitMin)+str(splitMin))
    return errorSum

def powerTo(base, exponent):
    value=1
    for i in range(exponent):
        value*=base
    return value


def findNearestError(min):
    lenMin=len(str(min))
    if lenMin%2==0:
        pass
    else:
        min=powerTo(10, lenMin)

    while True:
        minLenHalf=int(len(str(min))/2)
        firstHalfMin=int(min%powerTo(10, minLenHalf))
        secondHalfMin=int(min/powerTo(10, minLenHalf))
        if firstHalfMin==secondHalfMin:
            return min
        else:
            min+=1


day2input=open("./../day2input.txt", "r").read()
errorSum=0
splitInput=day2input.split(",")
for IdRange in splitInput:
    min, max=IdRange.split("-")
    errorSum+=findErrors(findNearestError(int(min)), int(max))
print(errorSum)
