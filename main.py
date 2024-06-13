import pandas as pd
import sys
from db.config import engine, db


# SQL query to select data from the table
try:
    if len(sys.argv) < 2:
        raise IndexError("Insufficient arguments provided")

    table = sys.argv[1] 

    query = f"SELECT * FROM {table}"

    # Establish connection
    connection = engine.connect()



# Read data from the database into a pandas DataFrame
    df = pd.read_sql(query, connection)

except IndexError as e:
    print(f"Error: {e}")
    print("Please provide a table name as an argument.")
    print("Usage: python3 main.py <tablename>")
    sys.exit(1)

finally:
    # Close connection
    connection.close()

# Export the DataFrame to a CSV file
    output_file = f"./{db}.{table}.csv"
    df.to_csv(output_file, index=False)

    print(f"Data has been exported to {output_file}")



