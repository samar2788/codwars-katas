def solution(string, ending):
    le=len(ending)
    if le==0:
        return True
    if le>0 and string[-le:]==ending:
        return True
    else:
        return False



print(solution('abcde', 'cde'))
print(solution('abcde', 'abc'))
