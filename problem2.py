class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA is None and headB is None:
            return None
        if headA is None and headB is not None:
            return None
        if headB is None and headA is not None:
            return None

        A = headA
        B = headB
    
        count = 0

        sizeA = Solution.size_of(headA)
        sizeB = Solution.size_of(headB)

        while (A is not None or B is not None) and count <= (sizeA + sizeB):
            print(count)
            if A.val == B.val:
                print(A.val)
                return A
            else:
                A = A.next
                B = B.next

                if A is None:
                    A = headB
                if B is None:
                    B = headA

                count += 1
                
        return None
    
    @staticmethod
    def size_of(node):
        c = 0
        while node is not None:
            c += 1
            if node.next is None:
                return c
            node = node.next
        return c
        
s = Solution()

B = ListNode('b1')
B.next = ListNode('b2')
B.next.next = ListNode('b3')

A = ListNode('a1')
A.next = ListNode('a2')

C = ListNode('c1')
C.next = ListNode('c2')
C.next.next = ListNode('c3')

A.next.next = C
B.next.next.next = C

print(s.getIntersectionNode(A, B))
