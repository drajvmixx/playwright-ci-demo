from mcp.server.fastmcp import FastMCP
import subprocess
import os

mcp = FastMCP("QA Server")

@mcp.tool()
def run_tests() -> str:
    """Runs all pytest tests and returns the results"""
    result = subprocess.run(
        ["python", "-m", "pytest", "tests/", "-v"],
        capture_output=True,
        text=True,
    )
    return result.stdout + result.stderr

@mcp.tool()
def list_test_files() -> list:
    """Lists all test files in the tests folder"""
    test_files = []
    for file in os.listdir("tests"):
        if file.startswith("test_") and file.endswith(".py"):
            test_files.append(file)
    return test_files

if __name__ == "__main__":
    mcp.run(transport="stdio")
