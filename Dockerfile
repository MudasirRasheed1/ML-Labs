# Use an official Python runtime as base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy all files from the current directory to the container
COPY . .

# Install dependencies
RUN pip install -r requirements.txt

# Define the command to run your app
CMD ["python", "test_script.py"]
