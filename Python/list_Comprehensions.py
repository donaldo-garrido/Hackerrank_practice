if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    original_list = [x,y,x]
    newlist = [[x,y,z] for item in original_list if x+y+z != n]
    print(newlist)
