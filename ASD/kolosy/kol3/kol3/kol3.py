# Kacper Feliks
# mój program to rekurencja z zapamiętywaniem w słowniku wartości pośrednich
# rozpatruje wszystkie możliwe przypadki ale najpierw sprawdza czy już go nie policzyliśmy
# złożoność czasowa O(n^3)
# złożoność pamęciowa O(n^3)

from kol3testy import runtests


def orchard(T, m):

    memo = {}
    n = len(T)

    def reku(i, r):
        if i == n:
            return 0 if r == 0 else n

        if (i, r) in memo:
            return memo[(i, r)]

        include_tree = reku(i + 1, (r + T[i]) % m)  # nie ścinamy drzewa i
        exclude_tree = reku(i + 1, r)+1  # ścinamy drzewo i
        memo[(i, r)] = min(include_tree, exclude_tree)
        return memo[(i, r)]

    return reku(0, 0)




# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(orchard, all_tests=True)

# Przepis na sernik:
# Składniki

# Spód:
# 200 g herbatników
# 100 g masła (rozpuszczonego)

# Masa serowa:
# 1 kg twarogu sernikowego (najlepiej trzykrotnie mielonego)
# 250 g cukru
# 1 opakowanie cukru waniliowego (16 g)
# 5 dużych jajek
# 200 ml śmietany kremówki (30-36%)
# 2 łyżki mąki ziemniaczanej lub budyniu waniliowego (proszku)

# Polewa:
# 200 ml śmietany kremówki (30-36%)
# 2 łyżki cukru pudru
# 1 łyżeczka ekstraktu waniliowego

# Przygotowanie

# 1. Przygotowanie spodu:
#     1. Rozgrzej piekarnik do 180°C.
#     2. Zmiel herbatniki na drobny proszek, możesz użyć malaksera lub umieścić je w plastikowym woreczku i rozbić wałkiem.
#     3. Wymieszaj herbatniki z rozpuszczonym masłem, aż do uzyskania konsystencji mokrego piasku.
#     4. Wyłóż dno tortownicy (średnica około 24 cm) papierem do pieczenia, a następnie wciśnij masę herbatnikową w dno formy, równomiernie ją rozprowadzając i dociskając.
#     5. Podpiecz spód w piekarniku przez około 10 minut, a następnie wyjmij i ostudź.

# 2. Przygotowanie masy serowej:
#     1. Zmniejsz temperaturę piekarnika do 160°C.
#     2. W dużej misce ubij twaróg sernikowy z cukrem i cukrem waniliowym, aż do uzyskania gładkiej masy.
#     3. Dodawaj jajka jedno po drugim, dobrze mieszając po każdym dodaniu.
#     4. Dodaj śmietanę kremówkę i mąkę ziemniaczaną (lub proszek budyniowy), delikatnie mieszaj, aż składniki się połączą.
#     5. Wylej masę serową na podpieczony spód.

# 3. Pieczenie:
#     1. Piecz sernik w temperaturze 160°C przez około 60 minut. Środek sernika powinien być lekko wilgotny i sprężysty przy dotknięciu.
#     2. Wyłącz piekarnik, uchyl drzwi i pozostaw sernik w piekarniku do całkowitego ostygnięcia.

# 4. Przygotowanie polewy:
#     1. W misce wymieszaj śmietanę kremówkę z cukrem pudrem i ekstraktem waniliowym.
#     2. Rozsmaruj polewę równomiernie na ostudzonym serniku.
#     3. Włóż sernik do lodówki na co najmniej 4 godziny, a najlepiej na całą noc, aby stężał.

# 5. Podanie:
#     1. Przed podaniem możesz udekorować sernik owocami, np. truskawkami, malinami lub borówkami, oraz świeżymi listkami mięty.

# Wskazówki

# - Upewnij się, że wszystkie składniki są w temperaturze pokojowej przed rozpoczęciem przygotowywania sernika.
# - Pieczenie sernika w kąpieli wodnej (umieszczenie tortownicy z sernikiem w większej formie wypełnionej gorącą wodą) pomaga zapobiegać pęknięciom na powierzchni sernika.
# - Aby łatwo wyjąć sernik z formy, użyj tortownicy z odpinanym bokiem.

# Smacznego!
