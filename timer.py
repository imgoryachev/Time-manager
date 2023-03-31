import time

# Initialize the elapsed time to zero
elapsed_time = 0

# Check if there is a saved elapsed time from a previous run
try:
    with open("elapsed_time.txt", "r") as f:
        saved_time = f.read()
        try:
            elapsed_time = float(saved_time)
        except ValueError:
            print(f"Could not convert saved time '{saved_time}' to float. Setting elapsed time to zero.")

except FileNotFoundError:
    pass

# Start the stopwatch
start_time = time.time()

# Wait for user input to stop the stopwatch
input("Press Enter to stop the stopwatch...")

# Stop the stopwatch and calculate the elapsed time
elapsed_time += time.time() - start_time

# Save the elapsed time to a file
with open("elapsed_time.txt", "w") as f:
    f.write(str(elapsed_time))

# Print the elapsed time
print("Elapsed time:", elapsed_time)

