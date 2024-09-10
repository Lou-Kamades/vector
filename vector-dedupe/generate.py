import random
import time

def generate_random_numbers(num_lines, num_chars):
    # Generate a list of random numbers, each with a specified number of characters
    return [str(random.randint(10**(num_chars-1), 10**num_chars-1)) for _ in range(num_lines)]

def write_to_file(file_path, lines):
    # Write the lines to the file, overwriting any existing content
    with open(file_path, 'w') as f:
        for line in lines:
            f.write(line + '\n')

# The number of lines in each batch
num_lines = 100000
# The number of characters in each random number
num_chars = 17
# The path to the file
file_path = './log/test.log'
# The amount of time to pause after writing each batch (in seconds)
pause_time = 5

while True:
    # Generate a batch of random numbers
    lines = generate_random_numbers(num_lines, num_chars)
    # Write the batch to the file
    write_to_file(file_path, lines)
    # Pause before writing the next batch
    time.sleep(pause_time)
