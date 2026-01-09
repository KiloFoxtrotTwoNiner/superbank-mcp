from pathlib import Path
import tools    
from mcp.server.fastmcp import FastMCP
from mcp.server.fastmcp.resources import FileResource, TextResource, DirectoryResource
# from mcp.server.fastmcp.prompts.prompt import Message, PromptMessage, TextContent

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

data_dir_path = Path("./transcriptions").resolve()
if data_dir_path.is_dir():
    data_listing_resource = DirectoryResource(
        uri = "resource://data-files",
        path = data_dir_path, 
        name = "Data Directory Listing",
        description = "Lists files available in the data directory.",
        recursive = False 
    )
    mcp.add_resource(data_listing_resource) 

@mcp.prompt()
def support_investment(type_of_investment):
    """
    Support user with prompt of investment proposal
    """
    prompt = f"Create an {type_of_investment} investemnt proposal with risk warning."
    match type_of_investment:
        case "ore":
            prompt += " Include current prices of most popular ores and display how they changed in last 6 months."
        case "deposit":
            prompt += " Search for best deposit offers from Polish banks. Include only ones for new funds."
        case "real_estate":
            prompt += " Search for current average prices of square meter in Wrocław. List average square meter price in different districts of Wrocław."
        case _:
            return "Incorrect type of investment"
    return prompt