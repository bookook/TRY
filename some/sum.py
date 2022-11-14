if __name__ == "__main__" :
 
    # take input from user
    a = [1,2,3]
    b = [4,5,6]
 
    for i in range(len(a)-1):
        x=a[i]
        y=a[i+1]
        if x + y == 5:
         print(i,i+1) 
