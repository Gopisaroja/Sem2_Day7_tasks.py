#find second largest
n=int(input("Enter how many elements:"))
num=list(map(int, (input().split())))
largest=float("-inf")
second=float("-inf")
for i in num:
	if i>largest:
		second=largest
		largest=i
	elif i>second and i<largest:
		second=i
if second==float("-inf"):
	print("No second largest element")			
else:
	print(second)
#count frequency using dictionary
freq={}
for i in num:
	 if i in freq:
	 	freq[i]+=1
	 else:
	 	freq[i]=1		 	
print(freq)	 
print(num)	
#Anagram or not
str1=input("Enter string1:").replace(" ","").lower()
str2=input("Enter string2:").replace(" ","").lower()
if sorted(str1)==sorted(str2):
	print("Anagram")
else:
	print("Not anagram")	
#remove duplicates
dup=[]
for i in num:
	if i not in dup:
		dup.append(i)
print(dup)	
#left shift and right shift
k=int(input("Enter k:"))
k=k%len(num)
rotatedl=num[k:]+num[:k]
rotatedr=num[-k:]+num[:-k]
print(rotatedl)	#left shift
print(rotatedr)	#right shift														