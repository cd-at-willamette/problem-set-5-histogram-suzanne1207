##################################################
# Name: Suzanne Gunderson
# Collaborators: N/A
# Estimate of time spent (hr): 1
##################################################

def is_magic_square(array:list[list[int]]) -> bool:
    sumlist1 = small[0][0] + small[0][1] + small[0][2] # sum of list 1
    sumlist2 = small[1][0] + small[1][1] + small[1][2] # sum of list 2
    sumlist3 = small[2][0] + small[2][1] + small[2][2] # sum of list 3
    sumcolumn1 = small[0][0] + small[1][0] + small[2][0] # sum of column 1
    sumcolumn2 = small[0][1] + small[1][1] + small[2][1] # sum of column 2
    sumcolumn3 = small[0][2] + small[1][2] + small[2][2] # sum of column 3
    if sumlist1 == sumlist2 == sumlist3: # if each list sum is equal to each other
        if sumcolumn1 == sumcolumn2 == sumcolumn3: # if each column sum is equal to each other
            if small[0][0] + small[1][1] + small[2][2] == small[0][2] + small[1][1] + small[2][0]: # if each diagonal sum is equal to each other
                return True # is a magic square
    else:
        return False # is not a magic square

small = [[8,1,6],[3,5,7],[4,9,2]]
print(is_magic_square(small))
