import streamlit as st
import datetime
import time

# Data alvo: 05/07/2024 07:30
target_date = datetime.datetime(2024, 7, 5, 7, 30)
start_date = datetime.datetime.now()

st.markdown(
    """
    <style>
    .container {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        height: 100vh;
        background-color: #ADD8E6;
    }
    .timer {
        font-size: 60px;
        font-weight: bold;
        color: #00008B;
        text-align: center;
    }
    .message {
        font-size: 30px;
        color: #00008B;
        text-align: center;
        margin-bottom: 20px;
    }
    .progress-bar-container {
        width: 80%;
        height: 30px;
        background-color: #ffd1d1;
        border-radius: 15px;
        margin-top: 20px;
        text-align: center;
    }
    .progress-bar {
        height: 100%;
        background-color: #ff6666;
        border-radius: 15px;
        color: white;
        font-weight: bold;
        text-align: center;
    }
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

    st.markdown(
        f"""
        <div class="container">
            <div class="message">Vamos contando juntos...</div>
            <div class="timer">{days}d {hours}h {minutes}m {seconds}s</div>
        </div>
        """, unsafe_allow_html=True
    )

    time.sleep(1)
    st.rerun()
