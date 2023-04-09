import os
filenames = os.listdir(r"D:\clips")  

# creates a list of filenames at the location D:\clips [Change location accordingly]
print(filenames)

# printing the list of all file names
with open(r"......\Desktop\file.txt", "w", encoding="utf-8") as file:
    for i in filenames:
        file.write(i)
        file.write("\n")
        
file.close()
    
    
# file.txt will now have all the filenames in a separate line
