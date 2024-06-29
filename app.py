import streamlit as st
import datetime
import time

# Data alvo: 05/07/2024 07:30
target_date = datetime.datetime(2024, 7, 5, 7, 30)
start_date = datetime.datetime.now()

st.markdown(
    """
    <style>
    .timer { font-size: 50px; font-weight: bold; text-align: center; }
    .progress-bar-container { width: 80%; height: 30px; background-color: #e0e0e0; border-radius: 15px; margin-top: 20px; text-align: center; }
    .progress-bar { height: 100%; background-color: #76c7c0; border-radius: 15px; color: white; font-weight: bold; text-align: center; }
    </style>
    """, unsafe_allow_html=True
)

while True:
    now = datetime.datetime.now()
    diff = target_date - now
    days, seconds = diff.days, diff.seconds
    hours, minutes, seconds = seconds // 3600, (seconds % 3600) // 60, seconds % 60

    total_seconds = (target_date - start_date).total_seconds()
    elapsed_seconds = (now - start_date).total_seconds()
    progress = (elapsed_seconds / total_seconds) * 100

    st.markdown(f'<div class="timer">{days}d {hours}h {minutes}m {seconds}s</div>', unsafe_allow_html=True)

    time.sleep(1)
    st.experimental_rerun()
