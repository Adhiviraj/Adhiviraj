import sys
import io
import cv2
import numpy as np
from PIL import Image
from rembg import remove

def prep_photo(input_path="photo.jpg", output_path="source-prepped.png"):
    try:
        # 1. Read input image bytes
        with open(input_path, "rb") as f:
            img_bytes = f.read()

        # 2. Remove background using rembg
        print("Removing background (this may take a few seconds on first run)...")
        nobg_bytes = remove(img_bytes)

        # 3. Load image with PIL & composite onto pure white background
        img = Image.open(io.BytesIO(nobg_bytes)).convert("RGBA")
        white_bg = Image.new("RGBA", img.size, (255, 255, 255, 255))
        composite = Image.alpha_composite(white_bg, img).convert("L")

        # 4. Apply CLAHE (Contrast-Limited Adaptive Histogram Equalization)
        np_img = np.array(composite, dtype=np.uint8)
        clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8, 8))
        enhanced = clahe.apply(np_img)

        # 5. Save the output prepped image
        cv2.imwrite(output_path, enhanced)
        print(f"✅ Success! Prepped photo saved to {output_path}")

    except Exception as e:
        print(f"❌ Error prepping photo: {e}")

if __name__ == "__main__":
    target_photo = sys.argv[1] if len(sys.argv) > 1 else "photo.jpg"
    prep_photo(target_photo) 