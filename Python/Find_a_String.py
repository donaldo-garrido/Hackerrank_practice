# Challenge: Find a String

# TASK:

# In this challenge, the user enters a string and a substring. 
# You have to print the number of times that the substring occurs in the given string. 
# String traversal will take place from left to right, not from right to left. 

def count_substring(string, sub_string):
    
    # Get length of strings to compute
    len_sub = len(sub_string)
    len_str = len(string)

    # Variable to count
    count = 0

    # Iterate over the string
    for s in range(len_str-len_sub+1):
        
        # Get the strings from string of length of sub_string
        partial_str = string[s:s+(len_sub)]
        
        # Check if are the same to count
        if partial_str == sub_string:
            count+=1
    return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)




