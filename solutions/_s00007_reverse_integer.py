def reverse(self, x: int) -> int:
    if (x < -1 * (2 ** 31)) or (x > 2 ** 31 - 1):
        x = 0
    ans = 0

    # Attempt 2:
    # On the go
    # while x != 0:
    #     if (int(2 ** 31 / -10) < ans < int((2 ** 31 - 1) / 10)
    #             or (ans == int(2 ** 31 / -10) and x % 10 >= -8)
    #             or (ans == int((2 ** 31 - 1) / 10) and x % 10 <= 7)):
    #         digit = x % -10 if x < 0 else x % 10
    #         ans = ans * 10 + digit
    #         x = int(x / 10)
    #     else:
    #         ans = 0
    #         break

    # Attempt 1:
    # Store and reverse
    digits = [1, 0]
    #   Write sign of x
    if x < 0:
        digits[0] = -1
        x = -1 * x
    #   Append each digit to array successively
    while x != 0:
        digits.append(x % 10)
        x = x // 10
    ndigits = len(digits) - 2
    for i in range(2, ndigits + 2):
        ans += digits[i] * (10 ** (ndigits - i + 1))
    ans *= digits[0]
    if (ans < -1 * (2 ** 31)) or (ans > 2 ** 31 - 1):
        ans = 0

    return ans
