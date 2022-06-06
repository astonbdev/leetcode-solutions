def isPalindrome(self, x: int) -> bool:
    num_str = str(x)
    rev_str = num_str[::-1]

    if num_str == rev_str:
        return True
    else:
        return False