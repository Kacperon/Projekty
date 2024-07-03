class Node:
    def __init__(self):
        self.val = None  # przechowywana liczba rzeczywista
        self.next = None  # odsyłacz do nastepnego elementu
# def SortH(p,k):
#     start=Node()
#     start.next=p
#     p=start
#     q=p
#     while p.next.next!=None:
#         i=0
#         min=p
#         while p.next.next!=None and i<k:
#             if p.next.val<min.next.val:
#                 min=p
#             p=p.next
#             i+=1
#         p=q.next
#         zap=min.next
#         min.next=min.next.next
#         zap.next=q.next
#         q.next=zap
#         q=q.next
    # tu prosze wpisac wlasna implementacje
#    return start.next