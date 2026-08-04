from app.document_loader import load_pdf
from app.text_splitter import split_text

pdf_text=load_pdf("/home/kim/Documents/Ai-pdf-rag/data/ML.pdf")
chunks=split_text(pdf_text,500)

print(f"Total chunks:" ,{len(chunks)})
print(chunks[0])
