import random
import timeit
i = random.randint(1, 10000)
print(i)
guess = 500
print("Секретный номер:", i)
highest = 10000
lowest = 0
counter = 0
ctrl = True
while ctrl != False:
    if guess < i:
        lowest = guess
        nguess = lowest + (highest - guess)/2
        print(guess, "Мало")
        guess = nguess 
        counter = counter + 1
    if guess > i:
        highest = guess
        nguess = (highest - lowest)/2
        print(guess, "Много")
        guess = nguess 
        counter = counter + 1
   
    elif round(guess) == i:
        break



print("guessed!", guess, i, counter + 1)

        






    
















            
        



            

        


	


