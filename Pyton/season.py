def season(x):
    try:
        int(x)
        if x<3 or x==12:
                    print('Зима')
        elif 3<=x<=5:
                    print('Весна')
        elif 6<=x<=8:
                    print('Лето')
        elif 9<=x<=11:
                    print('Осень')
    except (TypeError, ValueError):
        print ('Это не целое число')





    
            
