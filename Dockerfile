# Use the official Python image as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /src

# Copy the requirements file to the working directory
COPY src/requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the source code to the working directory
COPY src .

# Expose the port on which the Flask app will run
EXPOSE 5000

# Run the Flask app
CMD ["flask", "run", "--host=0.0.0.0"]
