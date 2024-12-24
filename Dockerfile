# Dockerfile

# Use the official Python image as the base image
FROM python:3.11-slim

# Set the working directory in the container to /app/src
WORKDIR /app/src

# Copy the requirements file into the container
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project directory to /app/src
COPY . /app/src/

# Expose the port FastAPI will run on
EXPOSE 8000

# Run the application with Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
