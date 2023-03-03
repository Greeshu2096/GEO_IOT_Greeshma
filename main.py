#The IoT device get three sensor inputs A, B and C
a1= (int)(input("please enter the sensor data of a1\n",))
a2= (int)(input("please enter the sensor data of a2\n",))
a3= (int)(input("please enter the sensor data of a3\n",))
a4= (int)(input("please enter the sensor data of a4\n",))
a5= (int)(input("please enter the sensor data of a5\n",))
b1= (int)(input("please enter the sensor data of b1\n",))
b2= (int)(input("please enter the sensor data of b2\n",))
b3= (int)(input("please enter the sensor data of b3\n",))
b4= (int)(input("please enter the sensor data of b4\n",))
b5= (int)(input("please enter the sensor data of b5\n",))
c1= (int)(input("please enter the sensor data of c1\n",))
c2= (int)(input("please enter the sensor data of c2\n",))
c3= (int)(input("please enter the sensor data of c3\n",))
c4= (int)(input("please enter the sensor data of c4\n",))
c5= (int)(input("please enter the sensor data of c5\n",))
#b.	The sensor values are stored in variables and displayed on the screen
A=[a1,a2,a3,a4,a5]
B=[b1,b2,b3,b4,b5]
C=[c1,c2,c3,c4,c5]
print("Sensor A's collected datas are",A)
print("Sensor B's collected datas are",B)
print("Sensor C's collected datas are",C)
#c.The IoT device calculates the average of each sensor data at every five inputs and displays the average value on the screen
m= (a1+a2+a3+a4+a5)/5
n= (b1+b2+b3+b4+b5)/5
o= (c1+c2+c3+c4+c5)/5
print("Sensor A's collected data's average is",m)
print("Sensor B's collected data's average is",n)
print("Sensor C's collected data's average is",o)
#d.If the sensor A value is below a threshold value, the device will give a warning message on the screen
t1= (int)(input("please enter the threshold value of A\n",))
t2= (int)(input("please enter the threshold value of B\n",))
t3= (int)(input("please enter the threshold value of C\n",))
if(m<t1):
    print(" Warning 1, Data error")
    print(" Hey, you have to re check the input data")
else:
    print("We are on the right track")
#e.If the sensor B average value
#is above a threshold value,
#the device will recompute the
#average value with 5 inputs and
#displays the new average value on the screen.

if(n<t2):
    print(" Go ahead")
else:
    print("Sorry, please re - do the procedure")
    b1 = (int)(input("please re-enter the sensor data of b1\n", ))
    b2 = (int)(input("please re-enter the sensor data of b2\n", ))
    b3 = (int)(input("please re-enter the sensor data of b3\n", ))
    b4 = (int)(input("please re-enter the sensor data of b4\n", ))
    b5 = (int)(input("please re-enter the sensor data of b5\n", ))
    B = [b1, b2, b3, b4, b5]
    print("Sensor B's collected datas are", B)
    n = (b1 + b2 + b3 + b4 + b5) / 5
    print("Sensor B's collected data's average is", n)
    t2 = (int)(input("please enter the threshold value of B\n", ))
    if (n < t2):
        print(" Go ahead")
    else:
        print("error obtained")