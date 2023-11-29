prices = [7,1,5,3,6,4]
p = 0
k = prices[0]
for i in range(1,len(prices)):

    if prices[i] - k < p:
        if k > prices[i]:
            k = prices[i]
    else :
        p = prices[i] - k
    print(p,k)
print(p)