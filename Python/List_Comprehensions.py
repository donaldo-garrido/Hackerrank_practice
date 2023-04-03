# Challenge: List Comprehensions

# List comprehension offers a shorter syntax when you want to 
# create a new list based on the values of an existing list.

# The syntax:
# newlist = [expression for item in iterable if condition == True]


# TASK:

# Print a list of all possible coordinates given by (i,j,k 
# on a 3D grid where the sum of i+j+k is not equal to n. 



if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    # AS reference, I will calculate using for loops
    final_list = []

    for ii in range(x+1):
        for jj in range(y+1):
            for kk in range(z+1):
                
                if (ii + jj + kk) != n:
                    final_list.append([ii, jj, kk])
    print(final_list)

    # Using List Comprehensions as was suggested by the task
    newlist = [[ii, jj, kk] for ii in range(x+1) for jj in range(y+1) for kk in range(z+1) if (ii + jj + kk) != n]
    print(newlist)
    
