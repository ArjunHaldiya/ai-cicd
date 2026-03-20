from mcp.server.fastmcp import FastMCP
from orchestrator import orchestrator

mcp = FastMCP("Code Reviewer")

@mcp.tool()
def review_code(code: str) -> str:
    response = orchestrator(code)
    return str(response)


if __name__ == "__main__":
    mcp.run(transport="stdio")