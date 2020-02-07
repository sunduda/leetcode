def isPalindrome(self, x: int) -> bool:
    ans = True
    # Attempt 2:
    # Reverse half of the number
    if x < 0 or (x % 10 == 0 and x != 0):
        ans = False
    rev = 0
    while x > rev:
        rev = rev * 10 + x % 10
        x = x // 10
    if x != rev and x != rev // 10:
        ans = False

    # Attempt 1:
    # Split and determine
    # digits = []
    # #   Append each digit to array successively
    # while x > 0:
    #     digits.append(x % 10)
    #     x = x // 10
    # ndigits = len(digits)
    # if ndigits == 0 and x != 0:
    #     # If x < 0 then it mustn't be a palindrome number
    #     ans = False
    # else:
    #     # Check symmetry
    #     for i in range(ndigits // 2):
    #         if digits[i] != digits[ndigits-1-i]:
    #             ans = False
    #             break

    return ans
