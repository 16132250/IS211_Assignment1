
class ListDivideException(Exception):
    pass
def list_divide(numbers, divide=2):
    """
    The function returns the number of elements in the numbers list that are divisibleby divide
    """
    try:
        divide_count = 0
        for item in numbers:
            if item % divide == 0:
                divide_count += 1
                # print(divide_count)
        return divide_count

    except ListDivideException:
        print('there\'s a problem!')

def test_list_divide():
    """
    Test listDivide
    """
    assert list_divide([1,2,3,4,5]) == 2
    # print(f"1 Done!")
    assert list_divide([2,4,6,8,10]) == 5
    # print("2 Done!")
    assert list_divide([30, 54, 63,98, 100], divide=10) == 2
    # print("3 Done!")
    assert list_divide([]) == 0
    # print("4 Done!")
    assert list_divide([1,2,3,4,5], 1) == 5
    # print("5 Done!")

if __name__ == "__main__":
    test_list_divide()
