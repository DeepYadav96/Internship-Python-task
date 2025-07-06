import os
import subprocess

menu = '''
-----------------------------------------
          Python Menu Based Project
---------------------------------
          1. Send Whatsapp Message
          2. Send Email
          3. Send SMS
          4. Voice Call
          5. Post on Instagram
          6. Post on Linkedin
          0. Exit
-----------------------------------------
'''

while True:
    print(menu)
    choice = input("Enter your choice (0-6): ").strip()
    if choice == '1':
        subprocess.run(["streamlit", "run", "WA_Message.py"])
    elif choice == '2':
        subprocess.run(["streamlit", "run", "python_email.py"])
    elif choice == '3':
        subprocess.run(["streamlit", "run", "text.py"])
    elif choice == '4':
        subprocess.run(["streamlit", "run", "voice.py"])
    elif choice == '5':
        subprocess.run(["streamlit", "run", "insta.py"])
    elif choice == '6':
        subprocess.run(["streamlit", "run", "post.py"])
    elif choice == '0':
        print("Exiting. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number from 0 to 6.")
