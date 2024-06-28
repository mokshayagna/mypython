flowerbed = [1,0,0,0,1]
n =2
count = 0
length = len(flowerbed)

for flower in range(length):
    if flowerbed[flower] == 0:
        prev_empty = (flower == 0) or (flowerbed[flower - 1] == 0)
        next_empty = (flower == length - 1) or (flowerbed[flower + 1] == 0)

        if prev_empty and next_empty:
            flowerbed[flower] = 1
            count = count +1
        
        
        if count >= n:
            break
if count >= n:
    print(True)
else:
    print(False)