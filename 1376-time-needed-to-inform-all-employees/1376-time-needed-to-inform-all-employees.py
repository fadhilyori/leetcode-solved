class Solution:
    def dfs(self, manager: List[int], informTime: List[int], curr_employee: int):
        max_time = 0
        for subordinate in manager[curr_employee]:
            max_time = max(max_time, self.dfs(manager, informTime, subordinate))
        return informTime[curr_employee] + max_time

    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        # Create a list of lists to store the subordinates of each employee
        subordinates = [[] for _ in range(n)]
        
        # Populate the subordinates list based on the manager array
        for i in range(n):
            if manager[i] != -1:
                subordinates[manager[i]].append(i)
        
        # Perform DFS starting from the headID
        return self.dfs(subordinates, informTime, headID)