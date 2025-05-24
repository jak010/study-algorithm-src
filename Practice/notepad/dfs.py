def dfs(node):
    Visited[node] = True
    print(node, end=" ")

    for next in range(N):
        if not Visited[next] and Graph[node][next]:  # 아직 방문하지 않고 인접한 노드인지 체크
            dfs(next)


if __name__ == '__main__':
    """Input
    https://www.youtube.com/watch?v=Cm3-AxNsQWg
    : DFS - 재귀호출
    : 방향성이 없다고 가정함
    5 6
    0 1 0 2 1 3 1 4 2 4 3 4

    """

    N, E = map(int, input().split())  # 노드와 간선의 개수를 입력받음

    Visited = [False for _ in range(N)]  # 방문 갯수 초기화
    Graph = [[0 for _ in range(N)] for _ in range(N)]  # N by N의 행렬로 그래프 초기화

    values = list(map(int, input().split()))
    for i in range(E):
        u, v = values[i * 2], values[i * 2 + 1]
        Graph[u][v] = Graph[v][u] = 1

    dfs(0)

