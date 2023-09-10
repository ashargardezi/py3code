import math

def find_top_3_horses(num_horses, track_capacity):
    races = math.ceil((num_horses - 2) / (track_capacity - 1))  # Calculate the number of races required
    
    return races

# Example usage
num_horses = 25
track_capacity = 5

num_races = find_top_3_horses(num_horses, track_capacity)
print(f"Number of races required: {num_races}")
