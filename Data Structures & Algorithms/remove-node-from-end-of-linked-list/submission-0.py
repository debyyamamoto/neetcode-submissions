# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        atual = head 
        tam = 0
        while atual:
            tam += 1
            atual = atual.next
        
        alvo = tam - n 
        dummy = ListNode()
        dummy.next = head


        atual = dummy
        for i in range(alvo):
            atual = atual.next
            print(atual.val)
            
        atual.next = atual.next.next

        return dummy.next 