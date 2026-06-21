import streamlit as st
import pandas as pd
import os

# configure the page, must run first
st.set_page_config(
    page_title="ExpenseLens",
    page_icon="🔍",
    layout="centered",
    initial_sidebar_state="expanded"
)
LOGO_PATH = "/content/drive/MyDrive/ExpenseLensDatasets/logo.png"
col1, col2 = st.columns([1, 4])
with col1:
    if os.path.exists(LOGO_PATH):
        st.image(LOGO_PATH, width=80)
    else:
        st.markdown("# 🔍")
with col2:
    st.title("ExpenseLens")
    st.caption("Precision Expense Tracking & Receipt Analysis")
st.markdown("""
### Welcome to ExpenseLens

ExpenseLens helps you organize and manage your expenses by extracting information from receipt images.
Upload a receipt, review the extracted information, make any necessary edits, and save it for future reference.
""")

# instructions and descriptions
with st.expander("How It Works"):
    st.write("""
    1. Upload a receipt image.
    2. ExpenseLens extracts receipt information.
    3. Review and edit extracted data.
    4. Save the receipt to your expense database.
    """)

with st.expander("Supported Information"):
    st.write("""
    - Store name
    - Date
    - Total amount
    - Individual items (when available)
    - Notes
    """)

# user can upload a file
uploaded_file = st.file_uploader(
    "Upload a receipt image",
    type=["png", "jpg", "jpeg"],
    help="Upload a clear image of a receipt for automatic information extraction."
)



if uploaded_file:
  st.success("Receipt uploaded successfully!")
  st.image(uploaded_file, caption="Uploaded Receipt", width=300)

  # SAVE
  st.session_state["uploaded_image"] = uploaded_file

  # fake extracted data for now
  st.session_state["receipt_data"] = {
      "store": "Target",
      "date": "2026-06-10",
      "total": "42.87",
      "items": "Printer Paper x2\nInk Cartridge x1",
      "notes": "Office supplies order"

  }

# add page here
if st.button("View Receipts"):
    st.switch_page("pages/summary.py")

if st.button("View Receipt Details"):
    st.switch_page("pages/details.py")

# rate activities here
st.divider()
st.subheader("Feedback")

with st.form("feedback_form"):
    rating = st.slider(
        "Rate your experience",
        min_value=1,
        max_value=5,
        value=3
    )

    submitted = st.form_submit_button("Submit Feedback")

    if submitted:
        st.success("Thank you for your feedback!")
        st.write("Your rating:", "⭐" * rating)
    # we will need to store all the ratings...
