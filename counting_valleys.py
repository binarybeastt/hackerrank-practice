def countingValleys(steps, path):
    sea_level = 0
    valley_count = 0
    in_valley = False
    
    for step in path:
        if step == 'U':
            sea_level += 1
        elif step == 'D':
            sea_level -= 1
        
        # Check if we are exiting a valley
        if sea_level == 0 and step == 'U':
            valley_count += 1
    
    return valley_count