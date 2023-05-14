if __name__ == '__main__':
    name_score_list = []
    scores = []
    for _ in range(int(input())):
        name = input()
        score = float(input()) 
        
        name_score_list.append([name,score])
        scores.append(score)
        scores_set = set(scores)  #set only retains unique values
        
        SecondLowestScore = sorted(scores_set)  #set only retains unique values
        
    SecondLowestScore = SecondLowestScore[1]
  
    SecondLowestPeoples = []    
    for person, score in name_score_list:
        if score == SecondLowestScore:
            SecondLowestPeoples.append(person)
            
    SecondLowestPeoples.sort()
    for person in SecondLowestPeoples:
        print(person)
        
