# Use the official Python 3.11 image as the base image
FROM python:3.11-slim

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Flask application code into the container
COPY . .

# Set the environment variable for the database URL
ENV DATABASE_URL=postgresql://postgres:password@db/accountancy_data

# Expose port 5000 for the Flask application
EXPOSE 5000

# Set the entrypoint to run the Flask application
ENTRYPOINT ["python", "app.py"]
