import cv2
import numpy as np
from pathlib import Path


def load_image(file_name: str) -> np.ndarray:
    """
    Load image by file path
    :param file_name: file name
    :return: image
    """
    file_path = Path(file_name)

    # Load an image (you can freely choose any image you like)
    if file_path.exists():
        img_bgr = cv2.imread(str(file_path))
    else:
        raise FileNotFoundError(f"File '{file_name}' doesn't exist!")

    if img_bgr is None:
        raise ValueError("Incorrect input data! Could not decode image: '{file_name}'")

    # Convert it to RGB
    img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)

    return img_rgb


def contrast(val1: np.number, val2: np.number) -> float:
    """
    Contrast between 2 values
    :param val1: first value
    :param val2: second value
    :return: result between 0 and 1
    """
    return abs(val1 - val2) / abs(val1 + val2) if (val1 + val2) != 0 else 0
