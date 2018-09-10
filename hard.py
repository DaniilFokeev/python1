name = input("введите ваше имя")
age = int(input("сколько вам лет?"))
weight = int (input("каков ваш вес?"))

if (age < 30 and 50 <= weight <= 120):
    print ("вы в хорошем состоянии")
elif (age > 30 and (50 > weight or weight > 120)):
    print ("вам следует начать вести правильный образ жизни")
elif (age > 40 and (50 > weight or weight > 120)):
    print ("СРОЧНО ОБРАТИТЕСЬ К ВРАЧУ")
else:
    print ("данная формула не до конца доработана!!!")