#A simple program to search address in Google Maps from clip board or from command line
import webbrowser, sys, pyperclip
if len(sys.argv) > 1:                   #checks if Address passed as an argument from command prompt
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()        #Address is taken from clipboard 

webbrowser.open('https://www.google.com/maps/place/' + address)
