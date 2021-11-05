#Input: "(coder)(byte))"
#Output: 0
#Input: "(c(oder)) b(yte)"
#Output: 1

def BracketMatcher(strParam):
  global count
  if (count < 0):
    strParam = ""
  if len(strParam) > 0:
    if strParam[0] == '(':
      count += 1
    elif strParam[0] == ')':
      count -= 1
    BracketMatcher(strParam[1:])
  return count+1

count=0
print(BracketMatcher(input()))