def solution(args):
    res = ''
    i = 0
    while i < len(args):
        res += str(args[i])

        if i + 2 < len(args) and (args[i] == args[i + 1] - 1 == args[i + 2] - 2):
            res += '-'
            n = ''
            ii = 1
            while ii < len(args[i:]):
                if (args[i:][ii] - args[i:][ii - 1]) ** 2 == 1: # is consecutive
                    n = str(args[i:][ii])
                    ii+=1
                else: break
            i+=ii # connect indexes
            res += n
        else: i +=1
        
        res += ','
    return res[:-1]


print(solution([-6,-3,-2,-1,0,1,3,4,5,7,8,9,10,11,14,15,17,18,19,20]))