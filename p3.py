# Write a Python function that accepts a string and calculate the number of 
# upper case letters and lower case letters.

str=input("Enter a string: ")
upper=0
lower=0
for i in range(len(str)):
      #to lower case letter
      if(str[i]>='a' and str[i]<='z'):
          lower+=1
      #to upper case letter
      elif(str[i]>='A' and str[i]<='Z'):
          upper+=1
print('Lower case letters= ',lower)
print('Upper case letters=' ,upper)

