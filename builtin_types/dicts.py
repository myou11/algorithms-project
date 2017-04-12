def dict_length(D):
    return len(D)

def sorted_list_of_items(D):
    return sorted(list(D.items()))

def dict_from_keys_values(k, v):
    return dict(zip(k,v))

def inverted_dict(D):
    return {v:k for k, v in D.items()}

def update_key(D, k, v):
    D[k] = v

def sorted_list_of_keys(D):
    return sorted(D.keys())

def remove_key(D, k):
    del D[k]
