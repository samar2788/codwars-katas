def check_exam(arr1,arr2):
    act, stu = arr1, arr2
    arlen = len(arr1)
    score = 0
    for i in range(arlen):
        if act[i] == stu[i]:
            score += 4
        elif stu[i] == "":
            score += 0
        else:
            score -= 1
    
    if score > 0:
        return score
    else:
        return 0
  
d = check_exam(["b", "c", "b", "a"], ["",  "a", "a", "c"])
print(d)