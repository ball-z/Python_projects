def leap_year(year):
    if year % 4 == 0:
        if year%100 == 0:
            if year % 400 == 0:
                print("This is a leap year")
            else:
                print("This isn't a leap year")
        else:
            print("This is a leap year")
    else:
        print("This isn't a leap year")

leap_year(2000)   
leap_year(2022)           

                
        
            
