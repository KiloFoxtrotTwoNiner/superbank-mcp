import bank

def main():
    # Initialize and run the server
    bank.mcp.run(transport="stdio")

if __name__ == "__main__":
    main()
