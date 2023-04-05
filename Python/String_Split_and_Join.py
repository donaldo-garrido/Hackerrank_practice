# Challenge: String Split and Join

# TASK:

# You are given a string. Split the string on a " " (space) delimiter 
# and join using a - hyphen. 

def split_and_join(line):
    # write your code here
    split_line = line.split(" ")
    string = '-'.join(split_line)
    return string

if __name__ == '__main__':