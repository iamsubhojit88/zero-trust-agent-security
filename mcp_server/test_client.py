import asyncio
from pathlib import Path

from fastmcp import Client


client = Client(Path("mcp_server/server.py"))


async def main():
    async with client:
        tools = await client.list_tools()

        print("Available tools:")
        for tool in tools:
            print(f"- {tool.name}")

        print("\nTesting get_customer_profile...")
        result = await client.call_tool(
            "get_customer_profile",
            {"customer_id": "C001"},
        )
        print(result)

        print("\nTesting search_customer_orders...")
        result = await client.call_tool(
            "search_customer_orders",
            {"customer_id": "C001"},
        )
        print(result)

        print("\nTesting update_customer_address...")
        result = await client.call_tool(
            "update_customer_address",
            {
                "customer_id": "C001",
                "address": "10 Research Street, Kolkata",
            },
        )
        print(result)

        print("\nTesting send_email...")
        result = await client.call_tool(
            "send_email",
            {
                "recipient": "test@example.com",
                "subject": "Research Test",
                "body": "This is a test email.",
            },
        )
        print(result)


if __name__ == "__main__":
    asyncio.run(main())