# # # # x = 1
# # # # while x <= 5:
# # # #     print("Hello World!")
# # # #     x += 1

# # # i = 1 
# # # while i <= 1000:
# # #     print("Hello")
# # #     i += 1


# # # print(i)

# # # print numbers from 5 to 1:

# # x = 5
# # while x >= 1:
# #     print(x)
# #     x -= 1

# # Print numbers from 1 to 100:

# a = 1
# while a <= 100:
#     print(a)
#     a += 1

#  Print numbers from 100 to 1:
 
# a = 100
# while a >= 1:
#     print(a)
#     a -= 1

# Print the multiplication table of a number n:

# n = int(input("Enter Number:"))
# i = 1
# while i<= 10:
#     multi = n * i
#     print(f"{n} * {i} = {multi}")
#     i += 1


        
# n = int(input("Enter Number:"))
# i = 1
# while i<= 10:
#     print(n*i)
#     i+=1

# Print the elements of the following list using a loop

# nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# heros = ["IronMan", "Thor", "Superman", "Batman"]

# index_value = 0
# while index_value < len(heros):
#     print(heros[index_value])
#     index_value+=1

# Search for a number x in this tuple using loop:

a = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

x = 36

i = 0
while i < len(a):
    if(a[i] == x):
        print("Found at index", i)
    else:
        print("Not Found")
    i+=1