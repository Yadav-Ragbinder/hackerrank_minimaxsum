import math
import os
import random
import re
import sys

def miniMaxSum(arr):
    mini = min(arr)
    maxi = max(arr)
    mini_sum = sum(arr) - maxi
    maxi_sum = sum(arr) - mini
    print(mini_sum,maxi_sum)

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
