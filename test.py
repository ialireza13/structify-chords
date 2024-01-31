from intersections import count_intersection
from tqdm import tqdm
import math

if __name__ == "__main__":
    
    for n in tqdm(range(4, 100, 2)):
        alpha = 2.0 * math.pi / n
        
        'Test 1: No intersection'
        input_list = [[], []]
        for i in range(n):
            input_list[0].append(i*alpha)
            input_list[1].append('s'+str(i//2+1) if i % 2 == 0 else 'e'+str(i//2+1))
        count = count_intersection(input_list)
        assert count == 0, f'Test failed, Expected {0} but got {count}'
        
        'Test 2: all diameters intersect'
        input_list = [[], []]
        for i in range(n):
            input_list[0].append(i*alpha)
            input_list[1].append('s'+str(i+1) if i < (n//2) else 'e'+str(i+1-n//2))
    
        count = count_intersection(input_list)
        assert count == (n//2)*(n//2-1)//2, f'Test failed, Expected {n//2*(n//2-1)//2} but got {count}'
    
    'Test 3: given example #1'
    input_list = [[0.78, 1.47, 1.77, 3.92], ['s1', 's2', 'e1', 'e2']]
    
    count = count_intersection(input_list)
    assert count == 1, f'Test failed, Expected {1} but got {count}'
    
    'Test 4: given example #2'
    input_list = [[0.9, 1.3, 1.7, 2.92], ['s1', 'e1', 's2', 'e2']]
    
    count = count_intersection(input_list)
    assert count == 0, f'Test failed, Expected {0} but got {count}'
    
    print('All test cases passed!')