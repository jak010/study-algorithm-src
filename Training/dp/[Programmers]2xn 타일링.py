# https://www.youtube.com/watch?v=v_x3JJzaqnc
def tile(n):
    dp = [-1 for _ in range(1001)]
    dp[0] = 0
    dp[1] = 1
    dp[2] = 2

    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n] % 10007


# Prgorammers
def solution(n):
    dp = [0 for _ in range(n)]
    dp[0] = 1
    dp[1] = 2

    for i in range(2, n):
        dp[i] = (dp[i - 2] + dp[i - 2]) % 1000000007

    return dp[n - 1]
