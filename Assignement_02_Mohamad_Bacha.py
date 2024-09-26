# Exercise 1

# N=int(input("Please enter a number: "))

# def getFactoriel(N):
#     Sum=1
#     for i in range(1, N+1):
#             Sum*=i
#     return Sum

# Total=getFactoriel(N)

# getFactoriel(N)
# print("The factoriel of" , N , " is equal to :" , Total)



# Exercise 2

# Divisors=[]

# N=int(input("Please enter a number: "))

# for i in range(1, N+1):
#         if(N%i==0):
#             Divisors.append(i)
#             i+=1
# print(Divisors)





#Exercise 3

# Word=input("Please insert a word: ")

# while True: 
#     if(len(Word)!=0):
#         print(Word[::-1])
#         break
#     else:
#          Word=input("Please insert a word: ")





#Exercise 4   (NOT correct)

# def get_even_numbers():
#     List=input("Please enter a list of intergers: ")

#     even_numbers=[]

#     for i in List:
#         if i%2==0:
#             even_numbers.append(i)
#     return even_numbers

# even_numbers=get_even_numbers()
# print(even_numbers)        



    
    





#Exercise 5

# Password=input("Please enter a password: ")

# if(len(Password)>=8 and any(char.isdigit() for char in Password) and any(char.isupper() for char in Password) and any(char.islower() for char in Password) and any(char in "!@#$%^&*()_+=<>?" for char in Password )):
#     print("Strong Password")
# else:
#     print("Weak password")   
 




#Exercise 6


# IP=input("Please enter an IP address: ")

# X=IP.split(".")
# while(0<=int(X[0])<=255  and 0<=int(X[1])<=255 and 0<=int(X[2])<=255 and 0<=int(X[3])<=255):
#     print("The IP", IP , "provided is valid")
#     break
# else:
#     print("The IP", IP , "provided is Not valid")
    

    
    
