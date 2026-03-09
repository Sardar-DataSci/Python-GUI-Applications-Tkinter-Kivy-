import time # pip install time
import os # pip install os
# Water Drinking Reminder App
while True:
    print("Please sip some water!")
    # For MacOS
    os.system("""
    osascript -e 'display notification "Water is essential for your health. Stay hydrated!" with title "Please Drink Water 💧"'
    """)
    time.sleep(60)
    # Reminder every 60 seconds (1 minute)
  

