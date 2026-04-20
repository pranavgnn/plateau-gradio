from ultralytics import YOLO
import gradio as gr
from PIL import Image
import os
from dotenv import load_dotenv

def predict_image(model: YOLO, image: Image.Image) -> Image.Image:
    results = model.predict(image)
    plotted = results[0].plot()
    return Image.fromarray(plotted[:, :, ::-1])

def main():
    load_dotenv()

    model = YOLO("weights.pt")


    description = (
        "<b>Plateau</b> is our ML & DL Lab Endsem Project.<br><br>"
        "<b>Submitted by:</b><br>"
        "1. Pranav G Nayak - 230958011<br>"
        "2. Aprameya Srinivasan Tatachari - 230958006<br>"
        "3. Roselin Maria T J - 230958032<br>"
        "4. Dhruva Deepak - 230958048<br><br>"
        "<b>Submitted to:</b><br>"
        "Prof. Dr. Srikanth Prabhu<br>"
        "Professor of Machine Learning and Deep Learning<br><br>"
        "Upload an image to detect license plates using the YOLOv8 model."
    )

    demo = gr.Interface(
        fn=lambda image: predict_image(model, image),
        inputs=gr.Image(type="pil", height=512, label="Upload an Image"),
        outputs=gr.Image(type="pil", height=512, label="Detected License Plates"),
        title="Plateau - License Plate Detection",
        description=description,
    )

    demo.launch(share=os.environ.get("GRADIO_SHARE", "false").lower() == "true")


if __name__ == "__main__":
    main()
