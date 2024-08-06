class Solution(object):
    def networkDelayTime(self, times, n, k):
        pathTo = {node: None for node in range(1,n+1)}
        pathTo[k] = 0

        from queue import PriorityQueue
        pri_q = PriorityQueue()
        pri_q.put((0, k))

        visited = set()

        while not pri_q.empty():
            cost, node = pri_q.get()
            if node in visited: continue
            visited.add(node)

            for time in times:
                if time[0] == node and time[1] not in visited:
                    if pathTo[time[1]] is None or pathTo[time[1]] > cost+time[2]:
                        pathTo[time[1]] = cost + time[2] 
                        pri_q.put((pathTo[time[1]], time[1]))

        maxCost = 0
        for node, cost in pathTo.items():
            if cost is None: return -1
            maxCost = max(maxCost, cost)
        return maxCost

