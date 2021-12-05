#https://leetcode.com/problems/reverse-linked-list/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def createList(arr):
    head = ListNode(arr[0])
    current = head
    for i in range(1, len(arr)):
        current.next = ListNode(arr[i])
        current = current.next
    return head

def main():
    arr = [1,2,3,4,5]
    head = createList(arr)
    auxList = []
    current = head
    while current:
        auxList.append(current.val)
        current = current.next
    auxList = list(reversed(auxList))
    ind = 0
    newCurrent = head
    while newCurrent:
        newCurrent.val = auxList[ind]
        ind += 1
        newCurrent = newCurrent.next
    return head

print(main())