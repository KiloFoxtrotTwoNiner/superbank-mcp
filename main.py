import bank

def main():
    # Initialize and run the server
    print("SuperBank MCP Server is running...")
    bank.mcp.run(transport="stdio")

if __name__ == "__main__":
    main()
