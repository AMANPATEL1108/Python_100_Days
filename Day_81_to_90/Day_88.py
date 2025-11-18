# write a program to pronounce list of names using win32 Api
# if you are givem a list l as follows:
# l=["pen","jen","dan"]

# your program should pronounce:

# shoutout to pen
# shoutout to jen
# shoutout to den


# text to speeach using python code write a list of that 


import win32com.client  # Import win32com for text-to-speech functionality

def pronounce_names(names_list):
    # Create a speech engine object
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    
    # Loop through the list of names and pronounce each one
    for name in names_list:
        shoutout = f"shoutout to {name}"  # Format the shoutout message
        print(shoutout)  # Optionally print it to the console
        speaker.Speak(shoutout)  # Speak the shoutout message

# List of names to shout out
names = ["pen", "jen", "dan"]

# Call the function to pronounce the names
pronounce_names(names)
