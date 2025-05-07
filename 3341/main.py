from typing import List


class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        # print('-------------------')
        # for x in moveTime:
        #     print('\t'.join(map(str, x)))
        # print('-------------------')

        m = len(moveTime)
        n = len(moveTime[0])

        dp = [[-1 for _ in range(n)] for _ in range(m)]
        dp[0][0] = 0# moveTime[0][0]

        q = set()
        q.add((0,0))

        while len(q) > 0:
            vx = q.pop()
            vals = []

            # print('##', vx)

            add_all = vx[0] == 0 and vx[1] == 0
            add_unvisited = dp[vx[0]][vx[1]] == -1

            if vx[0] != 0 or vx[1] != 0:
                if vx[0] - 1 >= 0 and dp[vx[0] - 1][vx[1]] != -1:
                    vals.append(1 + dp[vx[0] - 1][vx[1]])
                if vx[0] + 1 < m and dp[vx[0] + 1][vx[1]] != -1:
                    vals.append(1 + dp[vx[0] + 1][vx[1]])
                if vx[1] - 1 >= 0 and dp[vx[0]][vx[1] - 1] != -1:
                    vals.append(1 + dp[vx[0]][vx[1] - 1])
                if vx[1] + 1 < n and dp[vx[0]][vx[1] + 1] != -1:
                    vals.append(1 + dp[vx[0]][vx[1] + 1])

                # print('##', 'vals=', vals)

                mval = min(vals) if len(vals) > 0 else -1

                if dp[vx[0]][vx[1]] == -1 or dp[vx[0]][vx[1]] > mval:
                    dp[vx[0]][vx[1]] = mval if mval > moveTime[vx[0]][vx[1]] + 1 else moveTime[vx[0]][vx[1]] + 1

            if vx[0] - 1 >= 0 and (add_all or (add_unvisited and dp[vx[0] - 1][vx[1]] == -1) or (dp[vx[0] - 1][vx[1]] > dp[vx[0]][vx[1]])):
                q.add((vx[0] - 1, vx[1]))
            if vx[0] + 1 < m and (add_all or (add_unvisited and dp[vx[0] + 1][vx[1]] == -1) or (dp[vx[0] + 1][vx[1]] > dp[vx[0]][vx[1]])):
                q.add((vx[0] + 1, vx[1]))
            if vx[1] - 1 >= 0 and (add_all or (add_unvisited and dp[vx[0]][vx[1] - 1] == -1) or (dp[vx[0]][vx[1] - 1] > dp[vx[0]][vx[1]])):
                q.add((vx[0], vx[1] - 1))
            if vx[1] + 1 < n and (add_all or (add_unvisited and dp[vx[0]][vx[1] + 1] == -1) or (dp[vx[0]][vx[1] + 1] > dp[vx[0]][vx[1]])):
                q.add((vx[0], vx[1] + 1))

            # print('-------------------')
            # for x in dp:
            #     print('\t'.join(map(str, x)))
            # print('-------------------')
            # print('##', q)
            # print('-------------------')

        return dp[m - 1][n - 1]


s = Solution()
print('6', s.minTimeToReach([[0,4],[4,4]]))
print('3', s.minTimeToReach([[0,0,0],[0,0,0]]))
print('3', s.minTimeToReach([[0,1],[1,2]]))
print('81', s.minTimeToReach([[17,56],[97,80]]))
print('39', s.minTimeToReach([[56,93],[3,38]]))
