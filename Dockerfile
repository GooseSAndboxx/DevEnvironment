# Use an official Ubuntu as a base image
FROM ubuntu:latest

# Install Python
RUN apt-get update && apt-get install -y python3 python3-pip && apt-get install -y sudo && apt-get install -y curl && apt-get install -y wget
# Set Python 3 as the default
RUN ln -s /usr/bin/python3 /usr/bin/python

# Install Git, Java, and other useful tools
RUN apt-get install -y git openjdk-11-jdk

# Set Git configuration
RUN git config --global user.email "gouwslolly076@gmail.com"
RUN git config --global user.name "GooseSAndboxx"
# Set Git to store credentials and hardcode the GitHub token
RUN git config --global credential.helper store && \
    echo "https://GooseSAndboxx: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@github.com" > /root/.git-credentials


# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000
EXPOSE 6000
EXPOSE 7000
EXPOSE 8080
EXPOSE 9000
# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["python", "./app.py"]
