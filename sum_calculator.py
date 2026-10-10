total = 0

while True:
    num = int(input("Enter a number (0 to stop): "))
    if num == 0 :
       break
    else :
       total = total + num
print(f"Total sum = {total}")    
