# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        lista = []
        inicio = head
        while head:
            prox = head.next
            lista.append(head)
            head = prox
        l = 0
        r = len(lista)-1
        while l < r:
            lista[l].next = lista[r]
            l+=1
            if l == r:
                break
            lista[r].next = lista[l]
            r -= 1
        lista[l].next = None