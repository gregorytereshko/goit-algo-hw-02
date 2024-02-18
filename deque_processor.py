from collections import deque

def is_palindrome(s):
    # Перетворення рядка до нижнього регістру та видалення пробілів
    s = s.lower().replace(" ", "")
    d = deque(s)

    while len(d) > 1:
        if d.popleft() != d.pop():
            return False
    return True

# Приклади використання функції
print(is_palindrome("A man a plan a canal Panama"))  # True
print(is_palindrome("Hello"))                        # False
print(is_palindrome("Helleh"))                       # True
