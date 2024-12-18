# unlike 3.12-slim, 3.11 has no vulnerabilities according to docker-hub
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy application files
COPY . .

# Install dependencies
RUN pip install -r requirements.txt

# Expose port and run the app
EXPOSE 5000
CMD ["python", "catfact.py"]
