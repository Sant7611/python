# sub1 = input("Enter the subject first: ")
# mar1 = int(input("Enter the marks in first sub: "))
# sub2 = input("Enter the subject second: ")
# mar2 = int(input("Enter the marks in second sub: "))
# sub3 = input("Enter the subject third: ")
# mar3 = int(input("Enter the marks in third sub: "))

# totalMark = 300
# singlemark = 100
# allmark = mar1+mar2+mar3
# percentage = allmark/totalMark * 100

# if(percentage >= 40) or (mar1/singlemark * 100 >= 33 and mar2/singlemark * 100 >= 33 and mar3/singlemark * 100 >= 33 ):
#     print("You are pass.")
# else:
#     print("You are failed. ")


# # 4.
# char = input("Enter any username: ")
# if(len(char) <=10):
#     print("The username has less than 10 character")
# else:
#     print("The username has more than or equal to 10 character.")

# #5
# spam = ['make a lot of money', 'buy now', 'subscribe this', 'click this']

# msg = input("Enter any sentence: ").lower()


# if (spam[0] in msg or  spam[1] in msg or  spam[2] in msg or  spam[3] in msg):
    
#     print("This is a spam message.")
# else:
#     print("This is not a spam message.")


#6.
lst = ["ram", "shyam", 'hari', 'karan']
name = input("enter the name: ").lower()
if name in lst:
    print("Your name is in the list")
else:
    print("You don't have that name in the list.")