# Memory Game

This project is a Python application with Flask for the backend.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.
The following API endpoints are implemented:
- An API `GET` endpoint to fetch the leaderboard data i.e from `data/leaderboard.json` file.
- An API `POST` endpoint to the Player's score into `leaderboard.json` file.
- An API `GET` endpoint to fetch the Player's score information based on handle (Player's name), from data/`handle`.json file.
- An API `POST` endpoint to save the Player's score board or game into `data` folder as json file.

### Prerequisites

You will need the following tools:

- [Visual Studio Code](https://code.visualstudio.com/download)
- [Python](https://www.python.org/downloads/)
- [Flask](https://flask.palletsprojects.com/en/3.0.x/installation/) (This will be automatically installed when you run `pip install -r requirements.txt`)
- [Git](https://git-scm.com/downloads)

### Installing & Running

1. Clone the repo:

    ```
    git clone https://github.com/im-copilot-sandbox/python-webapi-memorygame.git
    ```

2. Navigate to the project directory:

    ```
    cd python-webapi-memorygame
    ```

3. Open the project in Visual Studio Code

    ```bash
    code .
    ```

4. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

5. Run the application:

    ```bash
    python run.py
    ```


## Documentation

| IDE | Description |
|--------|-------------|
| [Copilot for IntelliJ](copilot-IntelliJ/README.md) | Copilot installation/usage for Intellij IDE |
| [Copilot for Visual Studio](copilot-visualstudio/README.md) | Copilot installation/usage for Visual Studio IDE |
| [Copilot for VS CODE](copilot-vscode/README.md) | Copilot installation/usage for VS CODE IDE |

## Using GitHub and GitHub Copilot

GitHub is a web-based hosting service for version control. You can learn more about how to use GitHub repositories [here](https://docs.github.com/en/github).

[GitHub Copilot](https://copilot.github.com/) is your AI pair programmer. With GitHub Copilot, you can write code faster with fewer errors. It's a great tool to use during a hackathon!

## Python, Flask

This project is built with Python and Flask framework. If you're new to these technologies, here are some resources to get you started:

- [Python Documentation](https://docs.python.org/3/)
- [Flask framework Documentation](https://flask.palletsprojects.com/en/3.0.x/)


Happy coding!


