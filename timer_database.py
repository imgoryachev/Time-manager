import psycopg2
import time

# Connect to the PostgreSQL database
conn = psycopg2.connect(
    host="your_host_name",
    database="your_database_name",
    user="your_username",
    password="your_password"
)
cur = conn.cursor()

# Create the stopwatch table if it doesn't exist
cur.execute("""
    CREATE TABLE IF NOT EXISTS stopwatch (
        id SERIAL PRIMARY KEY,
        elapsed_time FLOAT NOT NULL
    );
""")
conn.commit()

# Get the previously saved elapsed time from the database
cur.execute("SELECT elapsed_time FROM stopwatch ORDER BY id DESC LIMIT 1;")
result = cur.fetchone()
if result is not None:
    elapsed_time = float(result[0])
else:
    elapsed_time = 0

# Start the stopwatch
start_time = time.time()

# Wait for user input to stop the stopwatch
input("Press Enter to stop the stopwatch...")

# Stop the stopwatch and calculate the elapsed time
elapsed_time += time.time() - start_time

# Save the elapsed time to the database
cur.execute("INSERT INTO stopwatch (elapsed_time) VALUES (%s);", (elapsed_time,))
conn.commit()

# Print the elapsed time
print("Elapsed time:", elapsed_time)

# Close the database connection
cur.close()
conn.close()