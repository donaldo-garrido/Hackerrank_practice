# Challenge: Mutations

# TASK:

# Read a given string, change the character at a given index and 
# then print the modified string. 

def mutate_string(string, position, character):
    
    lst = list(string)
    lst[position] = character
    altered = ''.join(lst)
    
    return altered

if __name__ == '__main__':