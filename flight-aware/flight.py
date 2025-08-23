from mcp.server.fastmcp import FastMCP
import aiohttp

mcp = FastMCP("FlightAware Server")

FLIGHTAWARE_API_URL = "https://aeroapi.flightaware.com/aeroapi/flights"
FLIGHTAWARE_API_KEY = "dummy"

@mcp.tool()
async def get_flight_info(flight_number: str) -> dict:
    """
    Fetches flight information from FlightAware API.

    Args:
        flight_number (str): The flight number to look up.

    Returns:
        dict: A dictionary containing flight information.
    """
    headers = {
        "x-apikey": FLIGHTAWARE_API_KEY
    }
    async with aiohttp.ClientSession() as session:
        async with session.get(f"{FLIGHTAWARE_API_URL}/{flight_number}", headers=headers) as response:
            if response.status == 200:
                return await response.json()
            return {"error": f"API request failed with status {response.status}"}

if __name__ == "__main__":
    mcp.run()
