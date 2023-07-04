# *****
# *****
# *****
# *****
# *****

def seq_pattern(star):
    for i in range(star):
        print('*' * star)
        
n = int(input())
seq_pattern(n)




# another approach 
# just make a different function name 
def hollow_pattern(star):  
    for i in range(0,star,1):
        print('*' * star)
        
n = int(input())
hollow_pattern(n)

