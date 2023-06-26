def isPalindrome(string):
    # My second solution for Palidrome Check
  
    lenStr = len(string)
    a = 0
    b = lenStr - 1

    while True:
        if a == b:
            return True
        else:
            if string[a] != string[b]:
                return False
            if (a+1) == b:
                return True
        a += 1
        b -= 1
    pass
