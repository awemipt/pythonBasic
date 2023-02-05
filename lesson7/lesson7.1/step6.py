from typing import List


def foo(nums: List[int]):
    print(f"Min = {min(nums)}, max = {max(nums)}, sum = {sum(nums)}")


numbers = list(map(int, input().split()))
foo(numbers)
