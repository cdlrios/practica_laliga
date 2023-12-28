# streamlit/Dockerfile
FROM python:3.8-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Make port 8501 available to the world outside this container
EXPOSE 8501

# Copy the data directory into the container at /app/data
#COPY data /app/data

# Define environment variable
ENV NAME World

# Run main.py when the container launches
CMD ["streamlit", "run", "main.py"]
