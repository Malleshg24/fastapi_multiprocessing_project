from multiprocessing import Pool

def sum_list(input_list):
    return sum(input_list)

def add_lists(lists):
    with Pool() as pool:
        results = pool.map(sum_list, lists)
    return results
