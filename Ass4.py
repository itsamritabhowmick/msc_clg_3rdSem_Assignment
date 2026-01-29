#Write a Python Program to solve Travelling Salesman Problem using Branch and Bound, to find optimal path with minimum cost 

import sys
class TSP:
    def __init__(self, graph):
        self.graph = graph
        self.n = len(graph)
        self.visited = [False] * self.n
        self.min_cost = sys.maxsize
        self.final_path = [None] * (self.n + 1)
        self.final_path[0] = 0

    def tsp_branch_and_bound(self):
        # Mark starting city as visited
        self.visited[0] = True

        # Start recursive TSP
        self.tsp_recursive(0, 1, 0)

        print("Minimum Cost:", self.min_cost)
        print("Optimal Path:", " -> ".join(map(str, self.final_path)))

    def tsp_recursive(self, current_cost, level, current_city):
        # If all cities are visited
        if level == self.n:
            if self.graph[current_city][0] != 0:
                total_cost = current_cost + self.graph[current_city][0]
                if total_cost < self.min_cost:
                    self.min_cost = total_cost
                    self.final_path[level] = 0
            return

        # Branch and Bound
        for next_city in range(self.n):
            if not self.visited[next_city] and self.graph[current_city][next_city] != 0:
                self.visited[next_city] = True
                self.final_path[level] = next_city

                self.tsp_recursive(
                    current_cost + self.graph[current_city][next_city],
                    level + 1,
                    next_city
                )

                self.visited[next_city] = False


# Driver code
if __name__ == "__main__":
    graph = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]

    tsp_solver = TSP(graph)
    tsp_solver.tsp_branch_and_bound()
