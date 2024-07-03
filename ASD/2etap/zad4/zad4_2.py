from zad4testy import runtests
def licznik_wywolan(func):
    def wrapper(*args, **kwargs):
        wrapper.cunter += 1
        return func(*args, **kwargs)
    wrapper.cunter = 0
    return wrapper
@licznik_wywolan

def Flight(L,x,y,t): return (Flight.cunter%2==1)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( Flight, all_tests = True )
