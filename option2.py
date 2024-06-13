import pandas as pd
from db.config import engine, db

# SQL query to select data from the table

tables = []
for table in tables:
    tables.append(table["tables"])

try:  
  

    # Establish connection
    connection = engine.connect()
    i = 0
    while len(tables) > i:
        query = f"SELECT * FROM {tables[i]}"
        # Read data from the database into a pandas DataFrame
        df = pd.read_sql(query, connection)
        # Export the DataFrame to a CSV file
        output_file = f"./{db}.{tables[i]}.csv"
        df.to_csv(output_file, index=False)
        print(f"Data has been exported to {output_file}")
        i += 1




except IndexError as e:
    print(f"Error: {e}")
    print("Please provide a table name as an argument.")
    print("Usage: python3 index.py <tablename>")
    sys.exit(1)

finally:
    # Close connection
    connection.close()
