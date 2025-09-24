# for i in range(1,6,1):
#     for j in range(5,i-1,-1):
#         print(j,end=" ")
#     print()    

# for i in range(1,6):
#     for j in range(5,i-1,-1):
#         print(i,end=" ")
#     print()        

#Triangle
for i in range(1,6):
    for j in range(1,6-i):
        print("   ",end=" ")
    for k in range(1,(2*i+1)-1):
        print(" * ",end=" ")
        
    print()    


# for i in range(1,5):
#     print("*"*i)
