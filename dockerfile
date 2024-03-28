# Use a base image with Python installed
FROM python:3.9

# Install Telnet
RUN apt-get update && apt-get install -y telnet

# Set the working directory in the container
WORKDIR /app

# Copy the Python server script into the container
COPY server.py /app/

# Copy the shell scripts into the container
COPY telnet_attack.sh totally_not_bitcoin_miner.sh /app/

# Expose the telnet server
EXPOSE 23
# Expose port 8000 for the Python server
EXPOSE 8000

# Run the Python server script when the container starts
CMD ["python", "server.py"]
