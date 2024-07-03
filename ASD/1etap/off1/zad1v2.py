from zad1testy import Node, runtests
class Node:
    def __init__(self):
        self.val = None # przechowywana liczba rzeczywista
        self.next = None # odsyłacz do nastepnego elementu

def marge(p,q):
    head=Node()
    cur=head
    while p!=None and q!=None:
        if p.val < q.val:
            cur.next=p
            p=p.next
            cur=cur.next
        else:
            cur.next=q
            q=q.next
            cur=cur.next
    if p!=None:
        cur.next=p
    else:
        cur.next=q
    return head.next

def mid(p):
    if p==None:
        return p
    fast,slow=p,p
    while fast.next and fast.next.next:
        fast=fast.next.next
        slow=slow.next
    return slow


def marge_sort(p):
    if p.next==None:
        return p
    mid_p=mid(p)
    zap=mid_p.next
    mid_p.next=None
    return marge(marge_sort(p),marge_sort(zap))
def sort_k_elem(head,k):
    main_head=head

        

def SortH(head,k):
    zap=head
    head1=head
    headnietykac=head

    for _ in range(k):
        if zap:
            if zap.val<headnietykac.val:
                headnietykac=zap
                zap=zap.next
    zap=head
    prev=None
    while zap:
        
        for _ in range(k):
            if zap:
                prev=zap
                zap=zap.next
        koniec=prev
        
        if koniec: 
            head2=koniec.next
            koniec.next=None
        head1=marge_sort(head1)
        zap=prev
        for _ in range(k):
            if zap:
                prev=zap
                zap=zap.next
        koniec=prev
        
        if koniec: koniec.next=None

        head2=marge_sort(head2)
        head=marge(head1,head2)
        head1=head2
    return headnietykac


def add(head,value):
    head_copy=head
    while head.next != None:
        head=head.next
    head.next=Node()
    head.next.val=value
    return head_copy
T2=[1,3,4,7,9,20]
T=[3,2,1,6,5,4,9,8,7]
head=Node()
head2=Node()
for x in T2:
    add(head2,x)
print(head2.next)
for x in T:
    add(head,x)
print(head.next)

# SortH(head.next,3)
# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( SortH, all_tests = True )



