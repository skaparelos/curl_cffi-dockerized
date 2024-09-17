FROM lwthiker/curl-impersonate:0.6-chrome

# Set the working directory in the container
WORKDIR /

# Install Python using apk (for Alpine-based images)
RUN apk update && apk add --no-cache python3 py3-pip build-base python3-dev curl-dev

# Copy the requirements file into the container
COPY requirements.txt .

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code into the container
COPY main.py .

# Expose the port the app runs on
EXPOSE 8080

# Run the application
CMD ["python3", "main.py"]