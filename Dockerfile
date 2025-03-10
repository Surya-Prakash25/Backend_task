# Use an official lightweight Python image
FROM python:3.10

# Set the working directory inside the container
WORKDIR /app

# Copy the application files into the container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the Flask port
EXPOSE 5000

# Set environment variable to avoid buffering
ENV PYTHONUNBUFFERED=1

# Run the application
CMD ["python", "sentiment.py"]
