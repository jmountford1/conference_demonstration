
# Method Conference Chatbot Demo

This project is a chatbot application that integrates with the OpenAI API. Follow the instructions below to set up the project using Docker and get started.

## Prerequisites

Before you can run the project, you'll need to have the following installed on your machine:

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)
- An OpenAI account with a funded API key

## OpenAI Setup

1. **Sign Up for an OpenAI Account:**
   If you don’t already have an account, you can sign up for one here: [OpenAI Sign Up](https://beta.openai.com/signup/).

2. **Load Your OpenAI Account with Funds:**
   Ensure that your account is funded to use the API.

3. **Generate an API Key:**
   - After signing in to your OpenAI account, navigate to the API section.
   - Generate a new API key that will be used to access the GPT model.
   - Make sure to save this API key, as you will need it for the configuration file.

## Project Setup

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/your-username/your-repository-name.git
   cd your-repository-name
   ```

2. **Add Your OpenAI API Key to `config.py`:**
   The `config.py` file is located in the `chatbot_backend` directory. Open the file in a text editor and add your OpenAI API key:

   ```python
   OPENAI_KEY = 'your-openai-api-key'
   ```

3. **Run the Application with Docker Compose:**

   To build and start the application, run:

   ```bash
   docker-compose up --build
   ```

   This command will build the Docker images and start the containers for the application.

## Usage

Once the containers are up and running, the chatbot will be accessible at the following URL:

```
http://localhost:5173
```

You can start interacting with the chatbot through the frontend interface, which communicates with the backend to send and receive chat messages using OpenAI's API.

## Troubleshooting

If you encounter any issues, make sure to:

- Check that your OpenAI API key is valid and has sufficient funds.
- Review the Docker logs for any errors using the command:
  ```bash
  docker-compose logs
  ```

## License

This project is licensed under the MIT License.
