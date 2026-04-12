import sys
import pypdf

def extract_text(file_path):
    """Extracts all text from a PDF file."""
    try:
        reader = pypdf.PdfReader(file_path)
        text = []
        for i, page in enumerate(reader.pages):
            page_text = page.extract_text()
            if page_text:
                text.append(f"--- Page {i+1} ---\n{page_text}")
        
        if not text:
            print("No text found in the PDF (it might be scanned).", file=sys.stderr)
            return

        print("\n\n".join(text))
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error reading PDF: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 read_pdf.py <file_path>", file=sys.stderr)
        sys.exit(1)
    
    extract_text(sys.argv[1])
