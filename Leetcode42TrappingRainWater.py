height = [0,1,0,2,1,0,1,3,2,1,2,1]
count = 0
left = 0
right = 0
temp = []
result = 0
while count < len(height):
    if height[left] > height[count]:
        right = count
        temp.append(count)
        count += 1

        
    else:
        if len(temp) > 1:
            temp.append(count)
            right = count

        for i in range(len(temp)):
            #print(height[left], height[right], height[temp[i]])
            temp[i] = max(0, min(height[left], height[right]) - height[temp[i]])

        result += sum(temp)
        temp = []
        left = count
        right = count
        count += 1
print(temp)
print(left,right)
'''
if left != right:
    while(right != left and height[right] < height[right - 1]):
        right -= 1
    #print(right, left)
    temp = temp[0 : right - left + 1]
    for i in range(0, right - left + 1):
        print(height[left], height[right], height[temp[i]])
        print(height[left], height[right], height[temp[i]])
        temp[i] = max(0, min(height[left], height[right]) - height[temp[i]])    
    print(temp)
    result += sum(temp[:-1])
'''
print(result)