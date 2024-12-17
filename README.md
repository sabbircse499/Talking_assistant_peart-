Peart - A Personal Voice Assistant

Peart is a Python-based voice assistant designed to perform various tasks like telling the time, playing music, fetching information from Wikipedia, telling jokes, and more. This assistant uses speech recognition and text-to-speech technologies to interact with users.

Features

Tell Time: Ask "What time is it?" to get the current time.

Play Songs: Request songs by saying "Play [song name]" and Peart will play it on YouTube.

Search Wikipedia: Ask "Tell me about [topic]" to get a brief summary from Wikipedia.

Tell Jokes: Say "Tell me a joke" for a quick laugh.

Reject Dates: If you ask Peart for a date, you'll get a humorous response.

Creator Information: Ask "Who made you?" to learn about Peart's creator.

Personalized Messages: Say "What is your name?" to learn Peart's name.

Exit Program: Say "Over" to exit the assistant.

Prerequisites

To run Peart, you need the following:

Python 3.x installed on your system.

The following Python libraries:

speech_recognition

pyttsx3

datetime

pywhatkit

wikipedia

pyjokes

Installation

Clone this repository or download the script.

Install the required libraries using pip:

pip install speechrecognition pyttsx3 pywhatkit wikipedia pyjokes

Ensure your microphone is properly set up for input.

Usage

Run the script:

python peart.py

Speak your commands when prompted.

Use the following commands:

"What time is it?" - Tells the current time.

"Play [song name]" - Plays the requested song on YouTube.

"Tell me about [topic]" - Provides a brief summary of the topic from Wikipedia.

"Tell me a joke" - Shares a random joke.

"Who made you?" - Provides information about Peart's creator.

"What is your name?" - Introduces Peart.

"Over" - Exits the program.

Notes

Ensure a stable internet connection for accessing YouTube and Wikipedia.

The voice assistant will listen for the keyword peart before executing commands.

Peart uses Google’s speech recognition API for processing voice commands.

Known Issues

Background noise might affect the speech recognition accuracy.

If the command is not recognized, Peart will respond with a default message.

Credits

Creator: Engineer Sabbir Hossen

Tools and Libraries: Python, SpeechRecognition, pyttsx3, pywhatkit, Wikipedia, pyjokes


This project is licensed under the MIT License. Feel free to modify and use it as per your requirements.

