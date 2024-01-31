from intersections import count_intersection

if __name__ == "__main__":
    
    input_list = [(1, 1.2, 2.0, 2.5, 3.0, 3.5, 3.6, 4.0, 4.5, 5.0, 5.5, 6.0),
                  ('s1', 's2', 's3', 'e1', 's4', 'e2', 's5', 'e5', 's6', 'e3', 'e4', 'e6')]
    
    count = count_intersection(input_list, draw=True)
    print('Number of Intersections = {}'.format(count))