# https://leetcode.com/problems/happy-number/description/
def isHappy(n: int) -> bool:
    cycle = [n]
    p = 0
    if n == 1:
        return True
    else:
        # p = 0
        while n > 0:
            p += (n % 10)**2
            n = n//10
        n = p
        if n not in cycle:
            cycle.append(n)
        else:
            return False
        print(cycle)
        return isHappy(n)
num = int(input())
print(isHappy(num))

# https://leetcode.com/problems/valid-anagram/description/

# def isAnagram(s: str, t: str) -> bool:
#     return sorted(s) == sorted(t)

# # https://leetcode.com/problems/transpose-matrix/description/
# def transpose(matrix):
#     answer = []
#     answer = [[] for _ in range(len(matrix[0]))]#[[],[],[]]
#     for j in range(len(matrix[0])): #3  0 1 2
#         for i in range(len(matrix)): #2 0 u 1
#             answer[j].append(matrix[i][j])
#     return answer
# matrix = [[1,2,3],[4,5,6]]
# print(transpose(matrix))