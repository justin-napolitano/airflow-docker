from cryptography.fernet import Fernet
fernet_key = Fernet.generate_key().decode()  # Generate a new Fernet key
print(fernet_key)  # Print the Fernet key to use in your configuration

