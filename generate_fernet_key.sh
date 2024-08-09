#!/bin/bash

# Generate a new Fernet key
FERNET_KEY=$(python -c "from cryptography.fernet import Fernet; print(Fernet.generate_key().decode())")

# Define the placeholder to be replaced
PLACEHOLDER="your_fernet_key_here"

# Replace the placeholder in docker-compose.yml with the generated Fernet key
sed -i "s|$PLACEHOLDER|$FERNET_KEY|g" docker-compose.yml

# Output the new Fernet key for reference
echo "New Fernet key: $FERNET_KEY"

