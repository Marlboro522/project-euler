from typing import Dict,List, Optional, Tuple
def find_paths(length: int, moves: Optional[List[int]]=None, solutions: Optional[Dict[Tuple[int,int],int]]=None) -> int:
    if moves is None:
        moves = [0, 0]  

    assert moves[0] <= length, "Crossing the Edge."
    assert moves[1] <= length, "Crossing the Edge."

    if solutions is None:
        solutions = {}  

    if moves[0] == length:
        return 1  
    elif moves[1] == length:
        return 1  
    elif tuple(moves) in solutions:
        return solutions[tuple(moves)]  
    else:
        answer0 = find_paths(length, [moves[0] + 1, moves[1]], solutions)
        solutions[(moves[0] + 1, moves[1])] = answer0
        answer1 = find_paths(length, [moves[0], moves[1] + 1], solutions)
        solutions[(moves[0], moves[1] + 1)] = answer1
        return answer0 + answer1    
    
print(find_paths(20))