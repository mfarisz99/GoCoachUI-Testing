import streamlit as st
from datetime import datetime

# --- Coach Login ---
st.title("Coach Session Booking Platform")
coach_name = st.text_input("Enter your name:", key="coach_name")

# --- Display Schedule ---
if coach_name:
    st.success(f"Welcome, Coach {coach_name}!")

    # Mock schedule data (this can later come from a database)
    sessions = [
        {"title": "Online Coaching - Fitness", "time": "10:00 AM", "type": "Online"},
        {"title": "Personal Training - Gym", "time": "2:00 PM", "type": "Physical"},
    ]

    st.subheader("Today's Sessions:")
    for idx, session in enumerate(sessions):
        st.write(f"**{session['title']}** at {session['time']} ({session['type']})")

        # --- Punch In / Out Buttons ---
        if st.button(f"✅ Start Session {idx+1}", key=f"start_{idx}"):
            st.session_state[f"start_time_{idx}"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            st.success(f"Session Started at {st.session_state[f'start_time_{idx}']}")

        if st.button(f"🛑 End Session {idx+1}", key=f"end_{idx}"):
            if f"start_time_{idx}" in st.session_state:
                end_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                st.success(f"Session Ended at {end_time}")

                # Calculate duration
                start = datetime.strptime(st.session_state[f"start_time_{idx}"], "%Y-%m-%d %H:%M:%S")
                end = datetime.strptime(end_time, "%Y-%m-%d %H:%M:%S")
                duration = round((end - start).total_seconds() / 60, 2)

                st.write(f"✅ **Duration:** {duration} minutes")
            else:
                st.warning("You need to start the session first!")

    # --- Attendance Summary ---
    st.subheader("📋 Attendance Summary")
    for idx, session in enumerate(sessions):
        if f"start_time_{idx}" in st.session_state:
            st.write(f"**{session['title']}** - {st.session_state[f'start_time_{idx}']} ✅")
