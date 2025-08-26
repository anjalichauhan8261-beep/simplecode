while(1):
     secc=int(input("Enter the value of a second:="))

     if(secc>1):
        hour=secc//3600
        sec=secc%3600

        min=sec//60
        sec=sec%60
        print("Hour is:",hour)
        print("minu is:",min)
        print("sec is:",sec)
     else:
         print("Please enter second greater then 1")
         
