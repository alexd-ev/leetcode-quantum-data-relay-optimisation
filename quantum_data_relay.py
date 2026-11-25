import heapq


def optimise_relay(streams: list[list[int]], max_boxes: int) -> int:
    # --- Transform & Conquer: Sort each stream ---
    for stream in streams:
        stream.sort()
        
    # --- Divide & Conquer: K-Way Merge using a Min-Heap ---
    heap = []
    master_stream = []
    
    for i, stream in enumerate(streams):
        if stream:
            heapq.heappush(heap, (stream[0], i, 0)) # (value, stream_idx, element_idx)
            
    while heap:
        val, s_idx, e_idx = heapq.heappop(heap)
        master_stream.append(val)
        if e_idx + 1 < len(streams[s_idx]):
            heapq.heappush(heap, (streams[s_idx][e_idx + 1], s_idx, e_idx + 1))
            
    # --- Dynamic Programming with Space-Time Tradeoffs ---
    n = len(master_stream)
    if n < 2 or max_boxes == 0:
        return 0

    # --- Space-Time Tradeoffs: Precompute segment values
    # Instead of calculating segment values on the fly inside 3 nested loops,
    # we trade O(N^2) memory to achieve O(1) runtime lookups later.
    cost = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            cost[i][j] = (master_stream[j] - master_stream[i]) * (j - i + 1)
        
    # dp[i][j]: Max value using at most 'i' boxes over prefix ending at 'j'
    dp = [[0] * n for _ in range(max_boxes + 1)]
    
    for i in range(1, max_boxes + 1):
        for j in range(1, n):
            # Option A: skip index j, or simply use fewer boxes
            best = max(dp[i][j - 1], dp[i - 1][j])
            
            # Option B: form the last box from k to j, then use at most
            # (i - 1) boxes on the prefix before it. k == 0 means the box
            # starts at the beginning, so no earlier boxes may be used.
            for k in range(j):
                prev = dp[i - 1][k - 1] if k > 0 else 0
                best = max(best, prev + cost[k][j])
            
            dp[i][j] = best
                
    return dp[max_boxes][n - 1]
