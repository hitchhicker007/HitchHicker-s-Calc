#Calculator script..made by Hitch_Hicker

import os

def main():
   print("""\033[1m\033[95m 
     _   _ _ _       _       _   _ _      _
    | | | (_) |_ ___| |__   | | | (_) ___| | _____ _ __
    | |_| | | __/ __| '_ \  | |_| | |/ __| |/ / _ \ '__|
    |  _  | | || (__| | | | |  _  | | (__|   <  __/ |
    |_| |_|_|\__\___|_| |_| |_| |_|_|\___|_|\_\___|_|   """)

   print("""
      \033[42m\033[1;30m===================Hitch_Hicker's Calculator===================\033[0;m
   \033[0;m
   1. Addition:   
   2. Subtraction:     
   3. Multiplication: 
   4. Devision:
   5. Exit:    """)

   #Code for user input..
   while True:
      try:
         a = int(input("   \33[104mPlease enter your choice [1-5]:\033[1;0m "))
         break
      except:
         continue

   yes = ["yes","y","Y","YES"]

   #Code for addition..
   if(a==1):
      while True:
         try:
            b = int(input("\n\033[1;33m   ENTER NO.1 =>\033[1;0m"))
            break
         except:
            continue
      while True:
         try:
            c = int(input("\033[1;33m   ENTER NO.2 =>\033[1;0m"))
            break
         except:
            continue
      ans = b + c
      print('\n\033[1m\033[95m   Answer : ',ans)

   #Code for subtraction..
   elif(a==2):
      while True:
         try:
            b = int(input("\n\033[1;33m   ENTER NO.1 =>\033[1;0m"))
            break
         except:
            continue
      while True:
         try:
            c = int(input("\033[1;33m   ENTER NO.2 =>\033[1;0m"))
            break
         except:
            continue
      ans = b - c
      print('\n\033[1m\033[95m   Answer : ',ans)

   #Code for multiplication..
   elif(a==3):
      while True:
         try:
            b = int(input("\n\033[1;33m   ENTER NO.1 =>\033[1;0m"))
            break
         except:
            continue
      while True:
         try:
            c = int(input("\033[1;33m   ENTER NO.2 =>\033[1;0m"))
            break
         except:
            continue
      ans = b*c
      print('\n\033[1m\033[95m   Answer : ',ans)

   #Code for division..n
   elif(a==4):
      while True:
         try:
            b = int(input("\n\033[1;33m   ENTER NO.1 =>\033[1;0m"))
            break
         except:
            continue
      while True:
         try:
            c = int(input("\033[1;33m   ENTER NO.2 =>\033[1;0m"))
            break
         except:
            continue
      ans = b / c
      print('\n\033[1m\033[95m   Answer : ',ans)

   #Code for Exit..
   elif(a==5):
      print("\033[42m\033[1;30m		Bye Bye! :)\033[1;0m")
      exit()

   #Code for wrong input..
   else:
       print("   \033[91mYou entered wrong choice! :(")

   #Code for re-run the script..
   restart = input("   \033[93mDO YOU WANT TO START AGAIN (y or n) : ")

   if restart in yes:
      os.system('clear')
      main()
   else:
      print("\033[42m\033[1;30m		Bye Bye! :)\033[1;0m")
      exit()

main()
