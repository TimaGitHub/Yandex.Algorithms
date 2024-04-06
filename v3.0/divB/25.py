class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        if pu == pv:
            return False
        if self.rank[pu] > self.rank[pv]:
            self.parent[pv] = pu
        elif self.rank[pv] > self.rank[pu]:
            self.parent[pu] = pv
        else:
            self.parent[pv] = pu
            self.rank[pu] += 1
        return True


def kruskal(n, edges):
    disjoint_set = DisjointSet(n)
    edges.sort(key=lambda x: x[2])
    min_cost = 0
    for u, v, weight in edges:
        if disjoint_set.union(u, v):
            min_cost += weight
    return min_cost


# считываем данные
n = int(input())
coords = list(map(int, input().split()))

# строим список всех возможных ребер
edges = []
for i in range(n):
    for j in range(i + 1, n):
        weight = abs(coords[i] - coords[j])
        edges.append((i, j, weight))

# запускаем алгоритм Краскала
min_cost = kruskal(n, edges)

# выводим результат
print(min_cost)
