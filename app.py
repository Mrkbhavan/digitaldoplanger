# app.py
import gradio as gr
import random
import time
from datetime import datetime

commands = ["Turn left", "Turn right", "Blink", "Smile", "Speak now"]

def generate_commands():
    return random.sample(commands, 4)

def verify_actions(user_actions, real_commands):
    if user_actions == real_commands:
        return "Verification Passed! You performed all commands."
    else:
        return "Verification Failed! Commands did not match."

def fake_profile_detector(photo, user_actions):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    gps = "Lat: 17.3850, Long: 78.4867"  # Simulated GPS
    verification_result = verify_actions(user_actions, real_commands)
    return f"Photo received at {timestamp} with GPS {gps}.\n{verification_result}"

with gr.Blocks() as demo:
    gr.Markdown("# Fake Profile Detector Demo")

    real_commands = generate_commands()
    gr.Markdown(f"Please perform these actions in order: {real_commands}")

    photo = gr.Image(label="Upload a selfie")
    user_actions = gr.Textbox(label="Type commands you performed separated by commas")
    verify_btn = gr.Button("Verify")
    output = gr.Textbox()

    verify_btn.click(fake_profile_detector, inputs=[photo, user_actions], outputs=output)

demo.launch()
