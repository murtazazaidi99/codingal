# Power set of a set
from itertools import combinations
def power_set(s):
    s=list(s)
    result=[]
    for r in range(len(s)+1):
        for combo in combinations(s,r):
            result.append(set(combo))
    return result
# Example
A={1,2,3}
ps=power_set(A)
print(ps)
print("Total subsets:", len(ps))

# # Power set of a set
# #Method 2:Bit mainpilation
#  def power_set_bits(arr):
#      n=len(arr)
#      res=[]
#      for mask in range(1<<n):
#          for i in range(n):
#              if mask&(1<<i):
#                  subset.append(arr[i])
#          res.append(subset)
#          return res
#  # print(power_set_bits([1,2,3]))

# Activity
def bits_to_change(a,b):
    x=a^b
    return bin(x).count("1")
# Example
a=29 #11101
b=15 #01111
print(bits_to_change(a,b)) #output:2