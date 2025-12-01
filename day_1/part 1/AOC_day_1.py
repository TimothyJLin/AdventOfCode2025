def direction_to_sign(direction):
    if direction=="R":
        return 1
    elif direction=="L":
        return -1

day1input=open("day1input.txt", "r")
password=0
currentRotation=50
for line in day1input:
    distance=line[1:]

    currentRotation+=direction_to_sign(line[0])*int(distance)
    currentRotation=currentRotation%100
    if currentRotation==0:
        password+=1

print(password)