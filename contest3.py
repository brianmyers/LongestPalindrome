##############################################################################
def contest3(arg1):
    length = len(arg1)
    #print arg1, length

    # Make a list of all index-numbers where index and index+1 are the same
    # (2-letter palindrome seeds).
    seeds2 = []
    for k in range(0,length - 1):
        if arg1[k] == arg1[k + 1]:
            seeds2.append(k)
    #print seeds2

    # Make a list of all index-numbers where index-1 and index+1 are the same
    # (3-letter palindrome seeds).
    seeds3 = []
    for k in range(1,length - 1):
        if arg1[k - 1] == arg1[k + 1]:
            seeds3.append(k)
    #print seeds3

    expanded_seeds2 = []
    for s2 in seeds2:
        n = 1
        while ((s2 - n) > 0) and ((s2 + (n + 1)) < length) and \
              (arg1[s2 - n] == arg1[s2 + (n + 1)]):
            n = n + 1
        expanded_seeds2.append( (s2, n ) )
    #print expanded_seeds2

    expanded_seeds3 = []
    for s3 in seeds3:
        n = 1
        while ((s3 - (n + 1)) > 0) and ((s3 + (n + 1)) < length) and \
              (arg1[s3 - (n + 1)] == arg1[s3 + (n + 1)]):
            n = n + 1
        expanded_seeds3.append( (s3, n ) )
    #print expanded_seeds3

    longest = 0
    longest_seed2 = None
    for s2 in expanded_seeds2:
        if s2[1] > longest:
            longest = s2[1]
            longest_seed2 = s2

    longest = 0
    longest_seed3 = None
    for s3 in expanded_seeds3:
        if s3[1] > longest:
            longest = s3[1]
            longest_seed3 = s3

    solution = None
    if longest_seed2 == None:
        if longest_seed3 != None:
            solution = arg1[longest_seed3[0] - longest_seed3[1] - 1 :
                            longest_seed3[0] + longest_seed3[1] + 2]
    else:
        if longest_seed3 == None:
            solution = arg1[longest_seed2[0] - longest_seed2[1] + 1 :
                            longest_seed2[0] + longest_seed2[1] + 1]
        else:
            if longest_seed2[1] > longest_seed3[1]:
                solution = arg1[longest_seed2[0] - longest_seed2[1] + 1 :
                                longest_seed2[0] + longest_seed2[1] + 1]
            else:
                solution = arg1[longest_seed3[0] - longest_seed3[1] - 1 :
                                longest_seed3[0] + longest_seed3[1] + 2]

    #print "\nSolution:\n"
    print solution

##############################################################################
