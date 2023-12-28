my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}
print(my_dict['name']) #Output John

#modifying elements
my_dict['name'] = 'Jane'
my_dict['age'] = 30
my_dict['occupation'] = 'Engineer' #add a new key-value pair

#removing elements
del my_dict['city']
print(my_dict) #Output {'name': 'Jane', 'age': 30, 'occupation': 'Engineer'}

#checking if a key exists
if 'name' in my_dict:
    print(my_dict['name']) #Output Jane
    
#iterating over a dictionary
for key, value in my_dict.items():
    print(f"{key}: {value}") #Output name: Jane age: 30 occupation: Engineer
  

#managing  a dictionary of server configurations and optimizing retrieval

server_config = {
    'server1': {'ip': '10.0.0.1', 'port': 80, 'status': 'active'},
    'server2': {'ip': '10.0.0.2', 'port': 80, 'status': 'active'},
    'server3': {'ip': '10.0.0.3', 'port': 80, 'status': 'inactive'}
}

def get_server_status(server_name):
    return server_config.get(server_name, {}).get('status', 'server not found')

server_name = 'server3'
status = get_server_status(server_name)
print(f"{server_name} status: {status}")