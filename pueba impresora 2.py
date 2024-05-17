import asyncio
import aioserial

# Replace with the actual port name (COM5)
port_name = "COM5"
baudrate = 9600
timeout = 1

async def print_ticket(ticket_content):
    """
    Asynchronously prints the provided ticket content to the serial port.
    """
    async with aioserial.open_serial_connection(
        port=port_name, baudrate=baudrate, timeout=timeout
    ) as printer:
        encoded_ticket = ticket_content.encode("ascii")
        await printer.write(encoded_ticket)

# Prepare the ticket content (replace with your actual ticket data)
ticket_content = """
  ------------------------------
    P  i  n  k  y  2  4  h  s
  ------------------------------
    nombre del local: Pinky24hs
    Order ID: #12345
    producto:
        - Product 1: $10.00
        - Product 2: $15.00
        - Product 3: $20.00
    Subtotal: $45.00
    Tax: $5.00
    Total: $50.00
    --------------------------------
    gracia por su compra !
    """

# Run the coroutine asynchronously
asyncio.run(print_ticket(ticket_content))
