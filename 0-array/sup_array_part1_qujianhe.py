import sys
input = sys.stdin.read

def main():
    data = input().split()
    n = int(data[0])
    nums = [0] * n
    intervals = []

    for i in range(1, len(data)+1):
        if i <= n:
            nums[i-1] = int(data[i])
        else:
            a, b = map(int, data[i].split())
            intervals.append([a, b])

    print(n)
    print(nums)
    print(intervals)

if __name__ == '__main__':
    main()