import serial

# Replace with the actual port name (COM5)
port_name = "COM5"

# Open the serial port for communication
try:
    printer = serial.Serial(port_name, baudrate=9600, timeout=1)
except serial.SerialException as e:
    print(f"Error opening serial port: {e}")
    exit()

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

# Encode the ticket content to bytes
encoded_ticket = ticket_content.encode("ascii")

# Send the ticket data to the printer
printer.write(encoded_ticket)

# Close the serial port
printer.close()
