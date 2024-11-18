FROM python:3.9-slim

# Set the working directory inside the Docker container
WORKDIR /app

# Copy the src directory into /app in the container
COPY ./src /app

# Install Poetry
RUN pip install poetry

# Install dependencies specified in pyproject.toml
RUN poetry install

# Set the default command to run your application
CMD ["python", "main.py"]
