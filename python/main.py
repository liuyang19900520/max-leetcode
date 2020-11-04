# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from No0053_Maximum_Subarray import maxSubArray


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


def test(num):
    for i in range(num):
        print(i)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    test(10)
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    result = maxSubArray(nums)
    print_hi(result)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
