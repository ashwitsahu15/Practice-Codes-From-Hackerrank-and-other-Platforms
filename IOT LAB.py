# write a program to insert n values in a list and find the sum of all the even numbers and the odd numbers in a list
# l=[int(x) for x in input().split()]
# even=sum([x for x in l if x%2==0])
# odd=sum([x for x in l if x%2!=0])
# print(even,odd)


# write a program for leap year
# n=int(input())
# if n%100==0 :
#     if(n%4==0 and n%400==0) :
#         print("Leap Year")
#     else :
#         print("Not a Leap Year")
# elif (n%4==0) :
#     print("Leap Year")
# else :
#     print("Not a Leap Year")

# TIC-TAC-TOE 
# theBoard = {'7': ' ' , '8': ' ' , '9': ' ' ,
#             '4': ' ' , '5': ' ' , '6': ' ' ,
#             '1': ' ' , '2': ' ' , '3': ' ' }

# board_keys = []

# for key in theBoard:
#     board_keys.append(key)


# def printBoard(board):
#     print(board['7'] + '|' + board['8'] + '|' + board['9'])
#     print('-+-+-')
#     print(board['4'] + '|' + board['5'] + '|' + board['6'])
#     print('-+-+-')
#     print(board['1'] + '|' + board['2'] + '|' + board['3'])

# def game():

#     turn = 'X'
#     count = 0


#     for i in range(10):
#         printBoard(theBoard)
#         print(turn)

#         move=input()        

#         if theBoard[move] == ' ':
#             theBoard[move] = turn
#             count += 1
#         else:
#             print("That place is already filled.\nMove to which place?")
#             continue 
#         if count >= 5:
#             if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ': # across the top
#                 printBoard(theBoard)
#                 print("\nGame Over.\n")                
#                 print(turn + " won.")                
#                 break
#             elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ': # across the middle
#                 printBoard(theBoard)
#                 print("\nGame Over.\n")                
#                 print(turn + " won.")
#                 break
#             elif theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ': # across the bottom
#                 printBoard(theBoard)
#                 print("\nGame Over.\n")                
#                 print(turn + " won.")
#                 break
#             elif theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ': # down the left side
#                 printBoard(theBoard)
#                 print("\nGame Over.\n")                
#                 print(turn + " won.")
#                 break
#             elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ': # down the middle
#                 printBoard(theBoard)
#                 print("\nGame Over.\n")                
#                 print(turn + " won.")
#                 break
#             elif theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ': # down the right side
#                 printBoard(theBoard)
#                 print("\nGame Over.\n")                
#                 print(turn + " won.")
#                 break 
#             elif theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ': # diagonal
#                 printBoard(theBoard)
#                 print("\nGame Over.\n")                
#                 print(turn + " won.")
#                 break
#             elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ': # diagonal
#                 printBoard(theBoard)
#                 print("\nGame Over.\n")                
#                 print(turn + " won.")
#                 break 
#         if count == 9:
#             print("\nGame Over.\n")                
#             print("It's a Tie!!")

#         if turn =='X':
#             turn = 'O'
#         else:
#             turn = 'X'        
    

# if __name__ == "__main__":
#     game()



