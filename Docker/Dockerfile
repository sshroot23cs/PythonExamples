# Use an official Python runtime as the base image
FROM python:3.8

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install -r app/requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 8090

# Define environment variable
ENV NAME World
# Use the argument to set an environment variable
ENV MY_ENV_VAR=$MY_ARG
# ENV: Use for configuration settings, database connection strings, or any values needed at runtime.

# Define an argument during image build
ARG MY_ARG=my_value
# ARG: Useful for dynamic values during the build process (e.g., version numbers, paths, etc.).
# only available during the build process and not at runtime.

# Run app.py when the container launches
CMD ["python", "app/app.py"]