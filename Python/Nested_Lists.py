# Challenge: Nested Lists


# TASK:

# Given the names and grades for each student in a class of N students, 
# store them in a nested list and print the name(s) of any student(s) 
# having the second lowest grade.

if __name__ == '__main__':
    records = []
    score_list = []
    for _ in range(int(input())):
        name = input()
        score = float(input())

        # Create the nested list
        records.append([name, score])

        # Create a list with scores
        if score not in score_list:
            score_list.append(score)
        
    # Sort scores and get the 2nd lowest
    sorted_score = sorted(score_list)
    lowest_2nd = sorted_score[1]
    
    # Get the names of the records with 2nd lowest score
    names_2nd = []
    for record in records:
        if record[1] == lowest_2nd:
            names_2nd.append(record[0])

    # Sort names and print them
    sorted_names = sorted(names_2nd)
    for s_name in sorted_names:
        print(s_name)
    

        