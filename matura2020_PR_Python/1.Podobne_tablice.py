"""1.2"""


def czy_k_podobne(n, A, B, k):
    l = 0
    for i in range(k):
        if A[i] == B[i + (n - k)]:
            l += 1
    if l == k:
        return True
    return False


print(czy_k_podobne(5, [10, 9, 12, 10, 9], [10, 10, 9, 9, 12], 3))

"""1.3"""


def czy_podobne(n, A, B):
    for k in range(n - 1):
        if czy_k_podobne(n, A, B, k):
            return "PRAWDA"
    return "FAŁSZ"


print(czy_podobne(5, [4, 7, 1, 4, 5], [1, 5, 5, 4, 7]))
