content = "precious oh my precious"

with open("content.txt", "r") as f:
    c = f.read()
    print(c)

# #1. open file
# f = open("content.txt","w") #w for write

# #2. write file
# f.write(content)

# #3. close file
# f.close()