# Importing Libraries for the code

# Import module for text-to-speech synthesis
 import pyttsx3

# Import module for opening web browsers
 import webbrowser

# Import module for generating random numbers or selecting random items
 import random 
 
# Import module for speech recognition
 import speech_recognition as sr  
 
# Import module for accessing Wikipedia articles
 import wikipedia                                  

 # Import module for working with dates and times
 import datetime  
 
 # Import module for querying the Wolfram Alpha computational knowledge engine
 import wolframalpha                                 
 
 # Import module for interacting with the operating system
 import os      
 
 # Import module for system-specific parameters and functions
 import sys   
 
 # Import module for sending emails using Gmail
 import yagmail                                     

 #Import module for creating games and multimedia applications
 import pygame   
 
 #Import module for accessing the system keyring services
 import keyring        

# Initialize the text-to-speech engine using the 'sapi5' speech API
engine = pyttsx3.init('sapi5')    
# Create a client object for accessing the Wolfram Alpha API with your client ID
client = wolframalpha.Client('YOUR_CLIENT_ID')
# Get the available voices for the text-to-speech engine
voices = engine.getProperty('voices')   
# Set the voice property of the engine to the last available voice
engine.setProperty('voice', voices[len(voices)-1].id)           

