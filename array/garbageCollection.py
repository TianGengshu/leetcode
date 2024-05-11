# https://leetcode.cn/problems/minimum-amount-of-time-to-collect-garbage/?envType=daily-question&envId=2024-05-11
from typing import List


class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        time = 0
        visited = set()
        while len(visited) < 3:
            for i in reversed(range(len(garbage))):
                if 'G' not in visited and 'G' in garbage[i]:
                    time += sum(travel[:i])
                    visited.add('G')

                if 'M' not in visited and 'M' in garbage[i]:
                    time += sum(travel[:i])
                    visited.add('M')

                if 'P' not in visited and 'P' in garbage[i]:
                    time += sum(travel[:i])
                    visited.add('P')

            # already at the first stop, still missing a type of garbage 
            if i == 0 and len(visited) < 3:
                break
        time += len(''.join(garbage))
        return time


if __name__ == "__main__":
    solution = Solution()
    garbage = ["G", "P", "GP", "GG"]
    travel = [2, 4, 3]
    try:
        assert solution.garbageCollection(garbage, travel) == 21
    except Exception:
        print("wrong answer, having result: ")
    print(solution.garbageCollection(garbage, travel))
