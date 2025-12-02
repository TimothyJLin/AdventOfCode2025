def direction_to_sign(direction):
    if direction=="R":
        return 1
    elif direction=="L":
        return -1

day1input=open("./../day1input.txt", "r")
password=0
currentRotation=50
rotationIsZero=False
for line in day1input:
    distance=int(line[1:])
    direction=direction_to_sign(line[0])
    directional_distance=direction*distance

    if rotationIsZero:
        if direction==-1:
            currentRotation=100
        elif direction==1:
            currentRotation=0
        rotationIsZero=False

    if directional_distance>100:
        password+=int(directional_distance/100)
        directional_distance=directional_distance%100

    elif directional_distance<-100:
        password+=int(-1*(directional_distance/100))
        directional_distance=directional_distance%-100
    currentRotation+=directional_distance
    if currentRotation>=100 or currentRotation<=0:

        password+=1
    currentRotation=currentRotation%100
    if currentRotation==0:
        rotationIsZero=True

print(password)