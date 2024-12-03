import streamlit as st
import json
from pathlib import Path

# Path to the file that stores the comments
COMMENTS_FILE = "comments.json"

# Function to load comments from the file
def load_comments():
    if Path(COMMENTS_FILE).exists():
        with open(COMMENTS_FILE, "r") as file:
            return json.load(file)
    return []

# Function to save comments to the file
def save_comments(comments):
    with open(COMMENTS_FILE, "w") as file:
        json.dump(comments, file)

# Load comments at the start
comments = load_comments()

# Title and styling with wedding rings background
st.markdown(
    """
    <style>
    body {
        background-image: url('https://www.example.com/wedding_rings_background.jpg'); /* Replace with actual image URL */
        background-size: cover;
        background-position: center;
        color: white;
    }
    .wedding-header {
        font-family: "Brush Script MT", cursive;
        font-size: 48px;
        text-align: center;
        color: #5A189A;
        margin-bottom: -10px;
    }
    .sub-header {
        text-align: center;
        font-family: "Georgia", serif;
        color: #5A189A;
    }
    .dedication {
        text-align: center;
        font-family: "Georgia", serif;
        font-size: 20px;
        color: #1D3557;
        margin-top: 20px;
    }
    .message {
        font-family: "Georgia", serif;
        font-size: 24px;
        text-align: center;
        color: #5A189A;
        background: #F4E1F7;
        border-radius: 10px;
        padding: 20px;
        margin-top: 20px;
        box-shadow: 2px 2px 10px #E2C6EE;
    }
    .comment-section {
        font-family: "Arial", sans-serif;
        margin-top: 20px;
        padding: 10px;
        border: 1px solid #E5E5E5;
        border-radius: 5px;
        background: #FAFAFA;
    }
    .footer {
        text-align: center;
        font-family: "Georgia", serif;
        color: #5A189A;
        margin-top: 30px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Display wedding message
st.markdown('<h1 class="wedding-header">Wedding Day</h1>', unsafe_allow_html=True)
st.markdown(
    """
    <div class="sub-header">
        <p>Love celebrated.</p>
        <p>Dreams come true.</p>
        <p>Hopes realized.</p>
        <p>Happiness.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# Display main message with graphical representation
st.markdown(
    """
    <div class="message">
        <p>Wishing you joy, love, and happiness on your wedding day</p>
        <p>and as you begin your new life together.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# Dedication
st.markdown(
    """
    <div class="dedication">
        <p>For Ankita Shukla</p>
        <p>Team Life Sciences COA</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# User input for name and comment
st.write("---")
st.subheader("Leave a Wedding Wish!")
name = st.text_input("Your Name", placeholder="Enter your name here")
wish = st.text_area("Your Wedding Wish", placeholder="Enter your wedding wish here")

if st.button("Submit Wish"):
    if name.strip() and wish.strip():
        new_comment = {"name": name.strip(), "wish": wish.strip()}
        comments.append(new_comment)
        save_comments(comments)
        st.success("Your wish has been added!")
    else:
        st.error("Please fill in both fields before submitting.")

# Display all comments
st.write("---")
st.subheader("Wedding Wishes for Ankita")
if comments:
    for comment in comments:
        st.markdown(
            f"""
            <div class="comment-section">
                <strong>{comment['name']}:</strong> {comment['wish']}
            </div>
            """,
            unsafe_allow_html=True,
        )
else:
    st.info("No wishes have been added yet. Be the first to leave a wish!")

# Footer
st.write("---")
st.markdown(
    """
    <div class="footer">
        <p>Ankita Shukla</p>
        <p>Team Life Sciences COA</p>
    </div>
    """,
    unsafe_allow_html=True,
)
