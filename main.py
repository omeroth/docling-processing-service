from fastapi import FastAPI, UploadFile, File
from docling_serve.api import process_document
from typing import Dict, Any

app = FastAPI()

@app.post("/process_pdf")
async def process_pdf_document(file: UploadFile = File(...)) -> Dict[str, Any]:
    """Endpoint to receive a PDF, process it with Docling, and return structured JSON."""

    file_content = await file.read()

    # This uses the Docling library to clean and structure the PDF
    structured_data = process_document(
        file_content,
        file.filename,
        output_format='json',
    )

    return structured_data

@app.get("/")
def read_root():
    return {"status": "Docling API is running!"}
