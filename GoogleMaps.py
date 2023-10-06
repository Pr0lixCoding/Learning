import webbrowser
import pyperclip

# paste what is on clipboard and stores it in a variable
address = pyperclip.paste()

# opens default web browser and searches the address on Google Maps.
webbrowser.open('https://www.google.com/maps/place/' + address)