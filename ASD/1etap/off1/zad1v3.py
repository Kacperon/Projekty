def SortH(p,k):
    start=Node()
    start.next=p
    p=start
    for _ in range(k):
        p=start
        while p.next.next!=None:
            if p.next.val>p.next.next.val:
                zap=p.next
                p.next=p.next.next
                zap.next=p.next.next
                p.next.next=zap
            p=p.next
    # tu prosze wpisac wlasna implementacje
    return start.next