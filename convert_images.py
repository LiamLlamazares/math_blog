import os
try:
    import fitz  # PyMuPDF
except ImportError:
    print("ERROR: PyMuPDF not found. Please run: py -m pip install pymupdf")
    exit(1)

def convert_pdfs_to_pngs(root_dir):
    """
    Scans the directory for .pdf files and converts them to .png 
    using PyMuPDF (fitz), which is self-contained.
    """
    print(f"Searching for PDFs in {os.path.abspath(root_dir)}...")
    pdf_count = 0
    success_count = 0

    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.lower().endswith('.pdf'):
                # Ignore the main post PDF (e.g., if there's a file called 'Parabolic.pdf' next to 'Parabolic.tex')
                # Usually figures don't have a matching .tex file with the exact same name
                if file.lower().replace('.pdf', '.tex') in files:
                    continue
                    
                pdf_path = os.path.join(root, file)
                png_path = os.path.join(root, file[:-4] + '.png')
                
                pdf_count += 1
                print(f"[{pdf_count}] Converting: {file} ...")
                try:
                    doc = fitz.open(pdf_path)
                    # We assume these are 1-page figure PDFs
                    page = doc.load_page(0)
                    
                    # 300 DPI calculation: 300 / 72 = 4.1666...
                    zoom = 300 / 72
                    mat = fitz.Matrix(zoom, zoom)
                    
                    pix = page.get_pixmap(matrix=mat, alpha=False)
                    pix.save(png_path)
                    doc.close()
                    print(f"    SUCCESS -> {os.path.basename(png_path)}")
                    success_count += 1
                except Exception as e:
                    print(f"    FAILED: {e}")

    print("\n" + "="*30)
    print(f"Finished. Successfully converted {success_count} of {pdf_count} PDFs.")
    print("="*30)

if __name__ == "__main__":
    convert_pdfs_to_pngs('posts')
