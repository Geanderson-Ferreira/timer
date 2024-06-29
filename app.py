import streamlit as st
import datetime
import time

# Data alvo: 05/07/2024 07:30
target_date = datetime.datetime(2024, 7, 5, 7, 30)

def time_left(target):
    now = datetime.datetime.now()
    diff = target - now
    return diff

st.markdown(
    """
    <style>
    .timer {
        font-size: 50px;
        font-weight: bold;
        text-align: center;
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
    }
    </style>
    """,
    unsafe_allow_html=True,
)

while True:
    time_remaining = time_left(target_date)
    days, seconds = time_remaining.days, time_remaining.seconds
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60

    st.markdown(f'<div class="timer">0{days}:{hours}:{minutes}:{seconds}s</div>', unsafe_allow_html=True)
    time.sleep(1)
    st.experimental_rerun()
