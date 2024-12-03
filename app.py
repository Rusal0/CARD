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

# Title and styling with a wedding-themed background and font styles
st.markdown(
    """
    <style>
    body {
        background-image: url('https://www.example.com/wedding_rings_background.jpg'); /* Replace with actual image URL */
        background-size: cover;
        background-position: center;
        color: #333333;  /* Changed font color to improve readability */
        font-family: 'Georgia', serif;
    }
    .wedding-header {
        font-family: "Brush Script MT", cursive;
        font-size: 48px;
        text-align: center;
        color: #FFF;
        margin-top: 20px;
        text-shadow: 2px 2px 10px rgba(0, 0, 0, 0.5);
    }
    .sub-header {
        text-align: center;
        font-family: "Georgia", serif;
        font-size: 24px;
        color: #FFF;  /* Updated text color for better contrast */
        margin-top: 10px;
        text-shadow: 1px 1px 5px rgba(0, 0, 0, 0.3);
    }
    .dedication {
        text-align: center;
        font-family: "Georgia", serif;
        font-size: 20px;
        color: #FFF;  /* Updated text color */
        margin-top: 20px;
        font-style: italic;
        text-shadow: 1px 1px 5px rgba(0, 0, 0, 0.5);
    }
    .message {
        font-family: "Georgia", serif;
        font-size: 24px;
        text-align: center;
        color: #5A189A;
        background: rgba(244, 225, 247, 0.9);
        border-radius: 10px;
        padding: 20px;
        margin-top: 20px;
        box-shadow: 2px 2px 15px rgba(0, 0, 0, 0.3);
        border: 3px solid #5A189A;
    }
    .comment-section {
        font-family: "Arial", sans-serif;
        margin-top: 20px;
        padding: 15px;
        border-radius: 8px;
        background: rgba(255, 255, 255, 0.8);
        color: #5A189A;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
    }
    .footer {
        text-align: center;
        font-family: "Georgia", serif;
        color: #5A189A;
        margin-top: 30px;
    }
    .input-section {
        background-color: rgba(244, 225, 247, 0.8);
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
    }
    .input-field {
        background-color: rgba(255, 255, 255, 0.7);
        border-radius: 8px;
        padding: 10px;
        font-size: 16px;
        border: none;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }
    .submit-btn {
        background-color: #5A189A;
        color: white;
        padding: 10px 20px;
        font-size: 16px;
        border-radius: 8px;
        border: none;
        cursor: pointer;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
    }
    .submit-btn:hover {
        background-color: #9B4D96;
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
st.markdown("<div class='input-section'>", unsafe_allow_html=True)
name = st.text_input("Your Name", placeholder="Enter your name here", key="name", label_visibility="collapsed", help="Enter your name here", max_chars=50)
wish = st.text_area("Your Wedding Wish", placeholder="Enter your wedding wish here", key="wish", label_visibility="collapsed", height=150, max_chars=500)

submit_button = st.button("Submit Wish", key="submit-btn", help="Click to submit your wedding wish")

st.markdown("</div>", unsafe_allow_html=True)

if submit_button:
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
