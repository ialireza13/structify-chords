import matplotlib.pyplot as plt
import re
import math

def bisect_left(arr, x):
    '''
        Find the location to insert x in arr to maintain sorted order
        (assumes arr is sorted in ascending order)
    '''
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < x:
            left = mid + 1
        else:
            right = mid
    return left


def count_intersection(input_list, draw=True):
    
    i = 0
    intersection_count = 0
    opens = []
    seen = [False for _ in range(len(input_list[0]) // 2)]
    ends = [None for _ in range(len(input_list[0]) // 2)]
    
    labels = [int(re.sub('\D', '', label))-1 for label in input_list[1]]
    
    for i, label in enumerate(labels):
        if seen[label] == False:
            seen[label] = True
            ends[label] = input_list[0][i]
            opens.append(label)
        else:
            opens.remove(label)
            intersection_count += len(opens) - bisect_left(opens, ends[label])
                
    if draw:
        plot_circle(input_list, title='Number of Intersections = {}'.format(intersection_count))
        
    return intersection_count


def plot_circle(input_list, title=''):
    
    chords = [[None, None] for _ in range(int(len(input_list[0])/2))]
    
    for chord in zip(input_list[0], input_list[1]):
        chord_id = int(re.sub('\D', '', chord[1]))
        end_type = 1 if re.sub(r'[0-9]', '', chord[1])=='s' else 0
        chords[chord_id-1][end_type] = chord[0]
    
    fig, ax = plt.subplots(1, 1, figsize=(5, 5))
    
    ax.add_patch(plt.Circle((0, 0), 1, color='black', fill=False, lw=1))
    
    for chord in chords:
        ax.plot([math.cos(chord[0]), math.cos(chord[1])], [math.sin(chord[0]), math.sin(chord[1])], '-o', lw=2.5)
        
    ax.set_xlim(-1.3, 1.3)
    ax.set_ylim(-1.3, 1.3)
    ax.set_axis_off()
    
    ax.set_title(title)
    
    fig.tight_layout()
    
    plt.show()