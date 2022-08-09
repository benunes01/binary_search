def main():
    my_list = [1,3,5,7,8,10,11,16,20,22,40,45,60,81]
    print(binary_search(my_list, 16))

def binary_search(list, item):
    low = 0
    high = len(list) - 1
    
    while low <= high:
        medium = (low + high) / 2
        risk = list[medium]
        if risk == item:
            return medium
        if risk > item:
            high = medium - 1
        else:
            low = medium + 1
    return None


