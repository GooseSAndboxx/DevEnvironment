# DevEnvironment Setup Guide with ngrok Integration

## Prerequisites

- [Git](https://git-scm.com/downloads)
- [Docker](https://www.docker.com/get-started)
- [ngrok](https://ngrok.com/download) (for secure tunneling to localhost)

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/GooseSAndboxx/DevEnvironment.git
   cd DevEnvironment
   ```

2. **Build the Docker Image:**
   ```bash
   docker build -t dev-environment .
   ```

3. **Run the Docker Container:**
   ```bash
   docker run -p 5000:5000 -p 6000:6000 -p 7000:7000 -p 8080:8080 -p 9000:9000 flask-webhook
   ```

## Setting up ngrok

1. **Install ngrok:**
   Follow the instructions on the ngrok website to install it on your system.

2. **Start ngrok:**
   To create a secure tunnel to your localhost, run:
   ```bash
   ngrok http 5000
   ```
   This will expose your local server (running inside the Docker container) to the internet.

3. **Copy the ngrok URL:**
   ngrok will provide an HTTPS URL (e.g., `https://1234abcd.ngrok.io`). Copy this URL.

4. **Update the Action Configuration:**
   In your custom GPT's edit form, edit the action listed in the GPT
   Replace the existing URL with the ngrok URL. For example, change:
   ```json
   "servers": [
       {
           "url": "https://7c6d-105-242-65-118.ngrok-free.app"
       }
   ]
   ```
   to:
   ```json
   "servers": [
       {
           "url": "https://1234abcd.ngrok.io"  // Your ngrok URL
       }
   ]
   ```

## Usage

- Access the application via the ngrok URL in your browser or API client.
- The development environment is now accessible over the internet via the ngrok URL.

## Troubleshooting

- Ensure Docker and ngrok are running without errors.
- Check if the ngrok URL is correctly updated in the action configuration.
- Verify that the port numbers match between Docker, ngrok, and your application settings.

For further assistance, refer to the [ngrok documentation](https://ngrok.com/docs) or raise an issue in the repository.

---

This guide now includes the necessary steps to set up ngrok and integrate it with your development environment, making it accessible over the internet. The steps are simplified for beginners, with clear instructions and commands.
