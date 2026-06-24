from flask import Flask, request, send_file
import fitz
import requests
import io
import os

app = Flask(**name**)

@app.route("/watermark")
def watermark():

```
pdf_url = request.args.get("url")

if not pdf_url:
    return "PDF URL Missing", 400

pdf_data = requests.get(pdf_url).content

pdf = fitz.open(stream=pdf_data, filetype="pdf")

logo_path = "po.jpg"   # apna logo isi naam se repo me upload karo

for page in pdf:

    rect = page.rect

    # Footer Line
    page.draw_line(
        (40, rect.height - 35),
        (rect.width - 40, rect.height - 35),
        color=(0.15, 0.35, 0.85),
        width=1
    )

    # Logo
    if os.path.exists(logo_path):
        page.insert_image(
            fitz.Rect(
                45,
                rect.height - 30,
                65,
                rect.height - 10
            ),
            filename=logo_path
        )

    # Verified Badge
    page.insert_text(
        (75, rect.height - 18),
        "✓ VERIFIED",
        fontsize=10,
        color=(0.0, 0.6, 0.2)
    )

    # Portal Name
    page.insert_text(
        (150, rect.height - 18),
        "CBPG RESULT PORTAL",
        fontsize=11,
        color=(0.1, 0.1, 0.1)
    )

    # Website
    page.insert_text(
        (320, rect.height - 18),
        "cbpgresult-com.github.io",
        fontsize=9,
        color=(0.45, 0.45, 0.45)
    )

output = io.BytesIO()

pdf.save(output)
output.seek(0)

return send_file(
    output,
    mimetype="application/pdf",
    download_name="CBPG_Result.pdf"
)
```

if **name** == "**main**":
app.run(host="0.0.0.0", port=5000)
