
from collections import deque

def solve():
    start = (3, 3, 1)
    goal = (0, 0, 0)
    
    moves = [(1, 0), (2, 0), (0, 1),
             (0, 2), (1, 1)]
    
    queue = deque([(start, [])])
    visited = set()
    
    while queue:
        state, path = queue.popleft()
        m, c, boat = state
        
        if state == goal:
            for step in path + [state]:
                print(step)
            return
        
        if state in visited:
            continue
        visited.add(state)
        
        for dm, dc in moves:
            if boat == 1:
                new_state = (m-dm, c-dc, 0)
            else:
                new_state = (m+dm, c+dc, 1)
            
            nm, nc, nb = new_state
            
            if not (0 <= nm <= 3 and 0 <= nc <= 3):
                continue
            
            rm, rc = 3-nm, 3-nc
            
            if ((nm == 0 or nm >= nc) and
                (rm == 0 or rm >= rc)):
                queue.append((new_state, path + [state]))
    
solve()
