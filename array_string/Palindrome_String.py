# https://www.interviewbit.com/problems/palindrome-string/?study_plan=study-plan-3-months&/

def isPalindrome(A: str) -> int:
    arr = [x.lower() for x in A if x.isalnum()]
    i, j = 0, len(arr) - 1
    while i <= j:
        if arr[i] != arr[j]:
            return False
        i += 1
        j -= 1
    return True


A = "A man, a plan, a canal: Panama"
# A = "Nas"
print(isPalindrome(A))
