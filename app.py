import streamlit as st
import re

# -----------------------
# Password strength logic
# -----------------------
def calculate_strength(password):
    score = 0
    feedback = []

    # Length check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Use at least 8 characters")

    # Uppercase check
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add uppercase letters")

    # Lowercase check
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add lowercase letters")

    # Number check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Include numbers")

    # Symbol check
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Include special characters")

    return score, feedback


# ------------------
# Streamlit UI setup
# ------------------
st.set_page_config(page_title="🔐 Password Strength Meter", layout="centered")

st.markdown("<h2 style='text-align: center;'>🔐 Password Strength Meter</h2>", unsafe_allow_html=True)
st.markdown("Enter your password to check its strength and get improvement tips.")

# User input
password = st.text_input("Enter Password", type="password")

if password:
    strength, suggestions = calculate_strength(password)

    # Display strength bar
    strength_labels = {
        0: ("Very Weak", "red"),
        1: ("Weak", "orange"),
        2: ("Fair", "gold"),
        3: ("Good", "lightgreen"),
        4: ("Strong", "green"),
        5: ("Very Strong", "darkgreen")
    }

    label, color = strength_labels.get(strength, ("Unknown", "gray"))
    
    # Style bar using markdown
    st.markdown(f"**Strength:** {label}")
    st.markdown(
        f"""
        <div style='height: 20px; width: 100%; background-color: lightgray; border-radius: 10px;'>
            <div style='height: 100%; width: {strength * 20}%; background-color: {color}; border-radius: 10px;'></div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Show improvement suggestions if needed
    if strength < 5:
        st.warning("Suggestions to improve your password:")
        for item in suggestions:
            st.markdown(f"- {item}")
    else:
        st.success("Great job! Your password is very strong. ✅")
else:
    st.info("👈 Type a password in the box above to test its strength.")

# Footer
st.markdown("<hr><p style='text-align: center;'>Made with ❤️ using Streamlit</p>", unsafe_allow_html=True)
