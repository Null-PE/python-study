def solution(nums):
    max_sum = nums[0]
    for i in range(len(nums)):
        temp = nums[i]
        max_sum = max(max_sum, temp)
        for j in range(i + 1, len(nums)):
            temp += nums[j]
            max_sum = max(max_sum, temp)
    return max_sum


def main():
    nums = [int(x) for x in input().split()]
    print(solution(nums))


if __name__ == '__main__':
    main()
