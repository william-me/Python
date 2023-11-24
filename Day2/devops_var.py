#configuration for a web server
server_name = "my_server"
port = 80
is_https_enabled = True
max_connections = 1000

#Print the configuration
print(f"Server Name: {server_name}")
print(f"Port: {port}")
print(f"HTTPS Enabled: {is_https_enabled}")
print(f"Max Connections: {max_connections}")

#Update the configuration values
port = 443
is_https_enabled = False

#Print the updated configuration
print(f"Updated port: {port}")
print(f"Updated HTTPS Enabled: {is_https_enabled}")