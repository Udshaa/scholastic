import telnetlib

host = 'smtp.office365.com'
port = 587

try:
    # Connect to the SMTP server
    tn = telnetlib.Telnet(host, port)
    print('Connection successful.')
    tn.close()
except Exception as e:
    print(f'Error connecting to SMTP server: {e}')

