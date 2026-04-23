
def isPalindrome(s: str) -> bool:
    

    left, right = 0, len(s)-1

    while right > left:

        # check if any of them are not alphanumeric so we sikp them
        while left < right and not s[left].isalnum():
            left += 1
        
        while left < right and not s[right].isalnum():
            right -= 1

        if left < right and s[left].lower() != s[right].lower():
            return False
        
        left += 1
        right -= 1

    return True

print(isPalindrome("A man, a plan, a canal: Panama"))
    
