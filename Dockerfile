# Use the Python 3 slim official image
# https://hub.docker.com/_/python
FROM python:3-slim

# Create and change to the app directory.
WORKDIR /app

# Copy requirements first for better caching
COPY requirements.txt .

# Install project dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy local code to the container image.
COPY . .

# Expose port for Railway
EXPOSE 8000

# Run the web service on container startup.
CMD ["hypercorn", "main:app", "--bind", "0.0.0.0:8000"]