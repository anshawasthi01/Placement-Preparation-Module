# https://leetcode.com/problems/merge-sorted-array/description/

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        m_ptr = m-1
        n_ptr = n-1
        idx_ptr =  m+n-1
        
        while(m_ptr> - 1 and n_ptr > -1):
            if nums1[m_ptr] >= nums2[n_ptr]:
                nums1[idx_ptr] = nums1[m_ptr]
                idx_ptr-=1
                m_ptr-=1
                
            else:
                nums1[idx_ptr] = nums2[n_ptr]
                idx_ptr-=1
                n_ptr-=1
                
        while m_ptr > -1:
            nums1[idx_ptr] = nums1[m_ptr]
            idx_ptr-=1
            m_ptr-=1
            
            
        while n_ptr > -1:
            nums1[idx_ptr] = nums2[n_ptr]
            idx_ptr-=1
            n_ptr-=1
            
        