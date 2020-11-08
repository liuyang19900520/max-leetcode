# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from No0560_Subarray_Sum_Equals_K import subarraySum2


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


def test(num):
    for i in range(num):
        print(i)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    nums = [1, 2, 3, 1, 0, 3, 4, 2];
    k = 6
    result = subarraySum2(nums, k)
    print_hi(result)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
