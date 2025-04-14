import qrcode
from PIL import Image
import os

# Create a directory to store the QR code images
output_dir = "qr_codes"
os.makedirs(output_dir, exist_ok=True)

# LaTeX document setup
latex_doc = r"""\documentclass{article}
\usepackage{graphicx}
\usepackage[margin=1in]{geometry}
\usepackage{float}
\begin{document}
"""

# Generate QR codes with labels
for i in range(1, 101):
    serial_number = f"UTHP-R1-{i:04d}"
    
    # Generate the QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=0,
    )
    qr.add_data(serial_number)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    # Save the QR code as an image
    img_path = os.path.join(output_dir, f"{serial_number}.png")
    img.save(img_path)

    # Add the QR code and label to the LaTeX document
    latex_doc += r"""\noindent \includegraphics[width=1in]{{"""
    latex_doc +=img_path.replace("\\", "/")
    latex_doc +=r"}}\newline\large\texttt{"
    latex_doc += serial_number
    latex_doc+= r"""}
    \vspace{0.5cm}
    \newline
    """
    #\vspace{0.5cm}
# Close the LaTeX document
latex_doc += r"\end{document}"

# Save the LaTeX document to a file
with open("qr_codes.tex", "w") as f:
    f.write(latex_doc)

print("QR codes and LaTeX document generated successfully.")
