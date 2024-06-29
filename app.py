import streamlit as st
import datetime
import time

# Data alvo: 05/07/2024 07:30
target_date = datetime.datetime(2024, 7, 5, 7, 30)

def time_left(target):
    now = datetime.datetime.now()
    diff = target - now
    return diff

st.title("Contador Regressivo")

while True:
    time_remaining = time_left(target_date)
    days, seconds = time_remaining.days, time_remaining.seconds
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60

    st.write(f"Tempo restante: {days} dias, {hours} horas, {minutes} minutos, {seconds} segundos")
    time.sleep(1)
    st.rerun()
