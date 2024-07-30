import streamlit as st
from datetime import datetime, timedelta

# Function to calculate the countdown
def calculate_countdown(birthday_date):
    now = datetime.now()
    # If the birthday has already passed this year, set it to next year
    if now > birthday_date:
        birthday_date = birthday_date.replace(year=now.year + 1)
    countdown = birthday_date - now
    return countdown

# Set the date of the birthday
birthday_date = datetime(2024, 8, 15)  # Change this to your friend's birthday

# Calculate the countdown
countdown = calculate_countdown(birthday_date)

# Streamlit app
st.title("Birthday Countdown")

col1, col2 = st.columns(2)


col1.write("Counting down to Tina's birthday on August 15, 2024!")

# Display the countdown
col1.metric(label="Days", value=countdown.days)
col1.metric(label="Hours", value=countdown.seconds // 3600)
col1.metric(label="Minutes", value=(countdown.seconds // 60) % 60)
col1.metric(label="Seconds", value=countdown.seconds % 60)

# Add a happy birthday message if today is the birthday
if countdown.days == 0 and countdown.seconds <= 86400:
    st.balloons()
    st.write("🎉 Happy Birthday! 🎉")

# HTML and CSS to position the image and icons


# Display image and icons
col2.image( image='Tina.jpg')



# Optionally, you can add a button to refresh the countdown
if st.button("Refresh Countdown"):
    st.experimental_rerun()
