import statistics as stats

def display_stats(res):
    # Frequency of each rating
    freq = {i: res.count(i) for i in range(1, 6)}
    
    # Calculate statistics using the statistics module
    min_val = min(res)
    max_val = max(res)
    rng = max_val - min_val
    mean = stats.mean(res)
    median = stats.median(res)
    mode = stats.mode(res)
    var = stats.variance(res)
    std_dev = stats.stdev(res)
    
    # Display the statistics
    print("Rating Frequency:")
    for r, count in freq.items():
        print(f"Rating {r}: {count} times")
    
    print("\nStatistics:")
    print(f"Min: {min_val}")
    print(f"Max: {max_val}")
    print(f"Range: {rng}")
    print(f"Mean: {mean:.2f}")
    print(f"Median: {median}")
    print(f"Mode: {mode}")
    print(f"Variance: {var:.2f}")
    print(f"Standard Deviation: {std_dev:.2f}")

# List of responses from 20 students
res = [1, 2, 5, 4, 3, 5, 2, 1, 3, 3, 1, 4, 3, 3, 3, 2, 3, 3, 2, 5]

# Display the statistics
display_stats(res)
