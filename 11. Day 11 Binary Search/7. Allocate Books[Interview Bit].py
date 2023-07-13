# https://www.interviewbit.com/problems/allocate-books/

class Solution:
	# @param A : list of integers
	# @param B : integer
	# @return an integer
    def numberOfStudents(self, A, pages):
        count = 0
        students = 1
        for i in range(len(A)):
            count += A[i]
            if count > pages:
                count = A[i]
                students += 1
        return students

    def books(self, A, M):
        if M > len(A):
            return -1
        min_pages = max(A)
        max_pages = sum(A)
        while(min_pages < max_pages):
            mid = int((min_pages + max_pages) / 2)
            if self.numberOfStudents(A, mid) > M:
                min_pages = mid + 1
            else:
                max_pages = mid
        return min_pages

