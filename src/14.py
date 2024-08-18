from tqdm import tqdm
import time
def cal_len(start:int)-> int:
    sequence_len=0
    while start != 1:
        if(start %2 == 0):
            start //= 2
            # print(start)
        else:
            start = (3 * start) + 1
            # print(start)
        sequence_len += 1
    return sequence_len

def solve() -> int:
    result =0 
    max_sequence_len = 0
    for start in tqdm(range(1,1_000_000)):
        # print(start)
        sequence_len = cal_len(start)
        # print(sequence_len)
        if sequence_len > max_sequence_len:
            max_sequence_len = sequence_len
            result = start
    return result

current_time = time.time()
print(solve())
print("Time taken:", time.time()-current_time)
