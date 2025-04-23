class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        nums = [[0 for _ in range(n)] for _ in range(n)]
        start_x, start_y = 0, 0
        loop = n // 2
        count = 1
        for offset in range(1, loop+1):
            for y in range(start_y, n - offset):
                nums[start_x][y] = count
                count += 1

            for x in range(start_x, n - offset):
                nums[x][n - offset] = count
                count += 1

            for y in range(n - offset, start_y, -1):
                nums[n - offset][y] = count
                count += 1

            for x in range(n - offset, start_x, -1):
                nums[x][start_y] = count
                count += 1

            start_x += 1
            start_y += 1

        if n % 2 == 1:
            nums[loop][loop] = count

        return nums


sol = Solution()
print(sol.generateMatrix(4))