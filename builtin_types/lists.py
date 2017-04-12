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
    pass

def square_each(L):
    return [n ** 2 for n in L]
