import streamlit as st

st.title("🧾 Invoice / Receipt Detail")


# Session data
receipt_image = st.session_state.get("uploaded_image")
receipt_data = st.session_state.get("receipt_data")

# fake for now
if receipt_image is None:
    receipt_image = "https://via.placeholder.com/400x600"
if receipt_data is None:
    receipt_data = {
        "store": "Demo",
        "date": "2026-06-11",
        "total": 0,
        "items": "",
        "notes": ""
    }
col1, col2 = st.columns(2)

with col1:
    st.subheader("Receipt Image")
    st.image(receipt_image, width="stretch")

with col2:
    st.subheader("Edit Data")

    store = st.text_input("Store", receipt_data.get("store", ""))
    date = st.text_input("Date", receipt_data.get("date", ""))

    total = st.number_input(
        "Total ($)",
        value=float(receipt_data.get("total") or 0),
        step=0.01
    )

    items = st.text_area("Items", receipt_data.get("items", ""))
    notes = st.text_area("Notes", receipt_data.get("notes", ""))

    if st.button("💾 Save Changes"):
        st.session_state["receipt_data"] = {
            "store": store,
            "date": date,
            "total": total,
            "items": items,
            "notes": notes
        }

        st.success("Saved successfully!")
# Navigation Back Home
if st.button("← Back to Upload Screen"):
    st.switch_page("app.py")
