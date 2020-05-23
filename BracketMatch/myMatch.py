

result = []
def generateParenthesis(left,right,n,res):
    if left == n and right ==n:
        result.append(res)
        return
    if left < n:
        generateParenthesis(left+1,right,n,res+"{")
    if left > right and right < n:
        generateParenthesis(left,right+1,n,res+"}")
    # write code here
n=3

generateParenthesis(0,0,n,"")
print(result)