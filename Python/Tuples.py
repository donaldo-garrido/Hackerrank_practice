# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
integers = list(input())
clean_list = []

for integer in integers:
    if (integer != ' '):
        clean_list.append(int(integer))
        
t = tuple(clean_list)

h = hash(t)

print(h)        