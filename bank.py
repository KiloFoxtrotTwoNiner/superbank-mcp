from typing import Any

import httpx
import sqlite3
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("SuperBankMCP")

try:
    # Connect to SQLite Database and create a cursor
    sqliteConnection = sqlite3.connect('bank.db')
    cursor = sqliteConnection.cursor()
    print('DB Init')

    # Execute a query to get the SQLite version
    query = 'SELECT sqlite_version();'
    cursor.execute(query)

    # Fetch and print the result
    result = cursor.fetchall()
    print('SQLite Version is {}'.format(result[0][0]))

    # Close the cursor after use
    cursor.close()

except sqlite3.Error as error:
    print('Error occurred -', error)

finally:
    # Ensure the database connection is closed
    if sqliteConnection:
        sqliteConnection.close()
        print('SQLite Connection closed')