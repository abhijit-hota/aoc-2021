with open("../inputs/1_sonar_sweep.txt", "r") as f:
    depths = list(map(int, f.read().splitlines()))

    # Part 1
    increases = 0
    for i in range(1, len(depths)):
        if depths[i] > depths[i - 1]:
            increases += 1

    print(increases)
    
    # Part 2
    window_sum = sum(depths[:3])
    window_increases = 0
    
    for i in range(3, len(depths)):
        new_sum = window_sum + depths[i] - depths[i - 3]
        
        if(new_sum > window_sum):
            window_increases += 1
            
        window_sum = new_sum
        
    print(window_increases)