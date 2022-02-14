input = "11931398"

hashmap = {}

for i in range(0, len(input)):
    if input[i] in hashmap.keys():
        hashmap[input[i]] = hashmap[input[i]] + 1
    else:
        hashmap[input[i]] = 1   	 	
    
print(hashmap)


max_key_values = {}
max_value = 0 
keys = []
for key, value in hashmap.items():
    if value > max_value:
        max_value = value
    

print(max_value)

num:int = 11931398
r1 = num % 10

digits = []
while True:
    r = int(num % 10)
    s = num - r
    print(r)
    print(s)
    digits.append(r)
    if s == 0:
        break 
    num = s/10
print(digits)








