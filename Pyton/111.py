A=int (input("Введите первое число:"))
B=int (input("Введите второе число:"))
operaciya= input("Что вы хотите с ними сделать?\n"
                "Введите\n+ для сожения,\n"
                 "- для вычитания\n"
                 "* для умножения\n"
                 "/ для деления\n")
                 
if (operaciya == '+'):
                 print (A+B)

elif (operaciya == '-'):
                 print (A-B)

elif (operaciya == '*'):
                 print (A*B)
elif (operaciya == '/'):
                 print (A/B)

else:
                 print("Ща разберемпся")



