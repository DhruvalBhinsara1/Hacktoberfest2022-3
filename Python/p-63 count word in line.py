#p-63 count word in line
line=input("Enter any line:- ")
count=1
for ch in line:
   if ch.isspace():
      count+=1
print("the no. of words in the line are:-  ",count)      
