def list_of_range(start, stop):
    return list(range(start,stop))

def list_of_chars(string):
    return list(string)

def list_extend(L, to_extend):
    return L.extend(to_extend)

def list_length(L):
    return len(L)

def positive_number_count(L):
    return len([n for n in L if n > 0])

def most_frequent_element(L):
    return max((L.count(c), c) for c in L)[1]

def square_each(L):
    return [n ** 2 for n in L]

def slice_last_n(L, n):
    return L[-n:]

def slice_from_to(L, to, f):
    return L[to:f]

def slice_every_third_element(L):
    return L[::3]

def if_even_square_each(L):
    return [n ** 2 for n in L if n % 2 == 0]

def get_second_to_last_item(L):
    return L[-2]

def get_item_at(L, i):
    return L[i]

def copy_of_list(L):
    return L.copy() #can also do L[:]
