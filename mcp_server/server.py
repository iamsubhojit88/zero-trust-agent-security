from fastmcp import FastMCP

mcp = FastMCP("research-tools")


@mcp.tool()
def get_customer_profile(customer_id: str) -> dict:
    """Retrieve the profile of a customer."""
    customers = {
        "C001": {
            "customer_id": "C001",
            "name": "Alice",
            "email": "alice@example.com",
            "phone": "+91-9000000001",
            "status": "active",
        },
        "C002": {
            "customer_id": "C002",
            "name": "Bob",
            "email": "bob@example.com",
            "phone": "+91-9000000002",
            "status": "active",
        },
    }

    return customers.get(
        customer_id,
        {"error": "Customer not found"},
    )


@mcp.tool()
def search_customer_orders(customer_id: str) -> dict:
    """Retrieve recent orders placed by a customer."""
    orders = {
        "C001": [
            {
                "order_id": "ORD1001",
                "product": "Laptop",
                "status": "Delivered",
            },
            {
                "order_id": "ORD1002",
                "product": "Monitor",
                "status": "Processing",
            },
        ],
        "C002": [
            {
                "order_id": "ORD2001",
                "product": "Keyboard",
                "status": "Delivered",
            },
        ],
    }

    return {
        "customer_id": customer_id,
        "orders": orders.get(customer_id, []),
    }


@mcp.tool()
def update_customer_address(
    customer_id: str,
    address: str,
) -> dict:
    """Update the customer's delivery address."""
    return {
        "success": True,
        "customer_id": customer_id,
        "updated_address": address,
        "message": "Customer address updated successfully",
    }


@mcp.tool()
def send_email(
    recipient: str,
    subject: str,
    body: str,
) -> dict:
    """Send an email to an external recipient."""
    return {
        "success": True,
        "recipient": recipient,
        "subject": subject,
        "body": body,
        "message": "Email sent successfully",
    }


if __name__ == "__main__":
    mcp.run()