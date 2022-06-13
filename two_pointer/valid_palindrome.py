# 

def valid_palindrom(s):
    s = s.lower()
    arr = [x for x in s if x.isalnum()]
    start, end = 0, len(arr) - 1
    while start < end:
        if arr[start].isalnum() and arr[end].isalnum():
            if arr[start].lower() != arr[end].lower():
                return False
        start+=1
        end-=1
    return True

print(valid_palindrom("A man, a plan, a canal: Panama"))