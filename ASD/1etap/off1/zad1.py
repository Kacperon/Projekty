from zad1testy import Node, runtests
#Kacper Feliks
#Z racji że lista jest k elementowa to z k pierwszych elementów wybieram najmniejszy.
#następnie przepinam go na początek i przechodzę dalej skoro lista jest n elementowa
#to tą operację wykonuję n razy więc złożoność mojego algorytmu to Θ(n*k)

def SortH(head,k):
    if k==0:
        return head
    start=Node()
    start.next=head
    head=start      # Dodanie wartownika
    current = head
    while current.next:
        min_node= current
        runner = current.next
        i=0
        while runner.next and i<k:  # Przezeszukanie pierwsze k elementów listy
            if runner.next.val < min_node.next.val:
                min_node = runner
            runner = runner.next
            i+=1
        
        mem=min_node.next
        min_node.next=min_node.next.next
        mem.next=current.next
        current.next=mem
        current = current.next
        # Przepięcie najmniejszego elementu na początek
    return head.next

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( SortH, all_tests = True )
