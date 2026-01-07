import sqlite3
import tools    
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("SuperBankMCP")

tools.db_config()

@mcp.tool()
def get_partners():
    """
    Get list of all partners from SuperBank
    """
    return tools.get_partners()

@mcp.tool()
def create_partner(first_name, last_name, email):
    """
    Create a partner in SuperBank

    Args:
        first_name: First name of new partner, maximum 25 letters
        last_name: Last name of new partner, maximum 50 letters
        email: Email of new partner, maximum 255 letters
    """

    return tools.create_partner(first_name, last_name, email)