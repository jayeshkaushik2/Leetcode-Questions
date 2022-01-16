# 5194. Minimum Moves to Reach Target Score

# time comp --> O(N) space comp --> O(1)
def minMoves(target: int, maxDoubles: int) -> int:
    ans = 0
    
    while target > 1:
        if target % 2 == 0 and maxDoubles > 0:
            target //= 2
            maxDoubles -= 1
            ans += 1
        elif target % 2 == 1:
            target -= 1
            ans += 1
        
        if maxDoubles == 0:
            break
    
    ans += target - 1

    return ans


if __name__ == '__main__':
    target = 19
    maxDoubles = 2
    # ans is 7
    ans = minMoves(target, maxDoubles)
    print(ans)