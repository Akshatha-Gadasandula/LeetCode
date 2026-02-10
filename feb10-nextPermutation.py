# Next Permutation
# Problem Number -31
class Solution:
    def nextPermutation(self, A):
        pivot = -1
        n = len(A)

        # 1st step: find pivot
        for i in range(n - 2, -1, -1):
            if A[i] < A[i + 1]:
                pivot = i
                break

        # if no pivot, reverse whole array
        if pivot == -1:
            A.reverse()
            return

        # 2nd step: find element just greater than pivot
        for i in range(n - 1, pivot, -1):
            if A[i] > A[pivot]:
                A[i], A[pivot] = A[pivot], A[i]
                break

        # 3rd step: reverse from pivot+1 to end
        A[pivot + 1:] = reversed(A[pivot + 1:])
