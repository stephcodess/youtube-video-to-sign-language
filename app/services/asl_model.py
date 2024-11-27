import torch
from app.services.models import LargeModel, TransformerModel 

LARGE_MODEL_PATH = "./models/text_to_motion_transformer.pth"
TRANSFORMER_MODEL_PATH = "./models/text_to_motion_transformer.pth"

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

large_model = None
transformer_model = None

def load_models():
    global large_model, transformer_model
    print("Loading models...")

    large_model = LargeModel()
    transformer_model = TransformerModel()

    large_model.load_state_dict(torch.load(LARGE_MODEL_PATH, map_location=device))
    transformer_model.load_state_dict(torch.load(TRANSFORMER_MODEL_PATH, map_location=device))

    large_model.to(device).eval()
    transformer_model.to(device).eval()


load_models()


def map_text_to_asl(text: str):
    """
    Convert text to ASL gestures using the loaded models.
    """

    input_tensor = preprocess_text(text)

    with torch.no_grad():
        large_model_output = large_model(input_tensor)


    with torch.no_grad():
        transformer_output = transformer_model(large_model_output)

    gestures = postprocess_output(transformer_output)
    return gestures

def preprocess_text(text: str):
    """
    Preprocess text into model-compatible format.
    """
    words = text.split()
    tokenized = [len(word) for word in words]
    input_tensor = torch.tensor([tokenized], dtype=torch.float32).to(device)
    return input_tensor

def postprocess_output(output):
    """
    Postprocess model output into gesture frames.
    """

    gestures = []
    for frame_idx, frame_data in enumerate(output):
        frame = {
            "frame": frame_idx + 1,
            "timestamp": frame_idx * 0.033,
            "joints": [
                {"name": "head", "position": [0.1, 0.5, 0.2], "rotation": [0, 0, 0, 1]},
                {"name": "left_hand", "position": [-0.2, 0.4, 0.1], "rotation": [0.5, 0, 0, 0.8]},
                {"name": "right_hand", "position": [0.3, 0.4, 0.1], "rotation": [0.7, 0, 0, 0.7]},
            ],
        }
        gestures.append(frame)
    return gestures
