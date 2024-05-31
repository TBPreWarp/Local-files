import requests
import pandas as pd
from sqlalchemy import create_engine

# Example data ingestion
response = requests.get('https://api.example.com/data')
data = response.json()
df = pd.DataFrame(data)

# Load data into PostgreSQL (replace with your connection details)
# engine = create_engine('postgresql://user:password@localhost:5432/mydatabase')
# df.to_sql('table_name', engine, if_exists='replace', index=False)

# Cleaning example
df.dropna(inplace=True)
df['column'] = df['column'].apply(lambda x: x.strip().lower())


# Transformation example
df['new_column'] = df['existing_column'] / df['another_column']
