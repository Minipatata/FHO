#Here is a file attached. You have to perform the following operations of File Handling using Python
with open("demo.txt","r") as f:
   for line  in f:
    print(line)
f.close()

with open("demo.txt","r") as f:
  data=f.readlines()
  for line in data:
    word=line.split()
    print(word)
f.close()