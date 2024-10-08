def decode_message( s: str, p: str) -> bool:

# write your code here
    dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
    
    # Base case: An empty pattern matches an empty string
    dp[0][0] = True
    
    # Handle cases where the pattern starts with '*'
    for j in range(1, len(p) + 1):
        if p[j - 1] == '*':
            dp[0][j] = dp[0][j - 1]
    
    # Fill in the DP table
    for i in range(1, len(s) + 1):
        for j in range(1, len(p) + 1):
            if p[j - 1] == s[i - 1] or p[j - 1] == '?':
                # Match a single character (or a '?')
                dp[i][j] = dp[i - 1][j - 1]
            elif p[j - 1] == '*':
                # '*' can match zero characters (dp[i][j - 1]) or any sequence (dp[i - 1][j])
                dp[i][j] = dp[i][j - 1] or dp[i - 1][j]

    # The result is whether the entire string matches the entire pattern
    return dp[len(s)][len(p)]

  
        