# WEATHER CLI APP

A python weather application that grabs real-time weather data using the Open-Meteo API.

This project includes both Command Line Interface(CLI) aswell as a Graphical User Interface(GUI) built with Tkinter.

## Features

- Search weather by city name
- Displays:
  - Temperatures °C
  - Weather conditions
  - Wind speeds
- Handles invalid inputs and any network issues
- CLI version for terminal use
- GUI version for desktop use
- Clean code using reusable functions

## Technologies Used 

- Python 3
- Requests (API calls)
- Tkinter (GUI)
- Open-Meteo API
- Git and GitHub
- VS Code

## Installation

#### Clone the repository:

git clone https://github.com/Hamza-Mahmood13/WeatherAPICLI
cd WeatherAPICLI

#### Create and activate a virtual environment:

python -m venv .venv
.venv\Scripts\activate

#### Install dependencies:

pip install -r requirements.txt

## How To Run

### CLI Version

python main.py

### GUI Version

python gui.py

## How it works

1. User enters a city
2. App grabs coordinates using Open-Meteo Geocoding API
3. App retrieves current weather data using longitude and latitude
4. Data is displayed to the user

## Error Handling 

- Handles invalid city names
- Handles network/API errors 
- Prevents empty input from user
- Display user friendly messages in both the CLI and GUI version

## Future Improvements

- Add more weather details
- Improve GUI styling using CustomTkinter
- Deploy as web app using Flask

## What I Learned

- Working with Real-world APIs
- Handling JSON data in Python
- Structuring codes using functions
- Building GUI apps with Tkinter
