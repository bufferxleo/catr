import gradio as gr
import cv2
import torch
import sys
import os

# Add the path to the script directory to sys.path to ensure it can be imported
script_dir = "/content/drive/MyDrive/catr"
sys.path.append(script_dir)

# Import the predict module
import predict

# Define Gradio interface
iface = gr.Interface(
    fn=predict.outputs, 
    inputs=[gr.Textbox(lines=3, label="Enter Text"), "image"],
    outputs=["text", "image"],
    title="Image Captioning",
    description="Enter the path to an image to generate a caption.",
    examples=[
        ["/content/drive/MyDrive/catr/img/sample1.jpg"],
        ["/content/drive/MyDrive/catr/img/sample2.jpg"]
    ]
)

# Launch the interface
iface.launch(share=True)
