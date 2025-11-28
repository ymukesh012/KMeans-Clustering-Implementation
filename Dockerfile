
# Use Python slim image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy all files into the container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose container port
EXPOSE 8051

# Run Streamlit on container port 8051
CMD ["streamlit", "run", "app.py", "--server.port=8051", "--server.address=0.0.0.0"]
