from flask import Flask, render_template, request
from flask import send_from_directory
from pathlib import Path
import os
import shutil

app = Flask(__name__)

# Common programming file extensions
CODE_EXTENSIONS = {
    '.py', '.java', '.cpp', '.c', '.h', '.js', '.ts', '.html', '.css',
    '.rb', '.php', '.go', '.rs', '.kt', '.swift', '.cs', '.sh', '.sql'
}

# Temporary upload folder
UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def get_file_size(file_path: Path) -> int:
    """Return the size of a file in bytes."""
    try:
        return file_path.stat().st_size
    except (OSError, PermissionError):
        return 0

def is_code_file(file_path: Path) -> bool:
    """Check if the file has a programming-related extension."""
    return file_path.suffix.lower() in CODE_EXTENSIONS

def calculate_storage(uploaded_files) -> tuple[int, list[dict], str]:
    """
    Calculate total storage of uploaded code files.
    Returns total size in bits, list of processed files with sizes, and error message (if any).
    """
    total_size_bytes = 0
    processed_files = []
    error_message = ""

    if not uploaded_files:
        return 0, [], "No files uploaded"

    # Clear upload folder before processing
    shutil.rmtree(UPLOAD_FOLDER, ignore_errors=True)
    os.makedirs(UPLOAD_FOLDER)

    for file in uploaded_files:
        if file and is_code_file(Path(file.filename)):
            # Save file temporarily
            file_path = Path(UPLOAD_FOLDER) / file.filename
            file.save(file_path)
            size_bytes = get_file_size(file_path)
            total_size_bytes += size_bytes
            processed_files.append({
                'name': file.filename,
                'size_bits': size_bytes * 8
            })
        else:
            error_message = "Some files were skipped (invalid code file extension)"

    total_size_bits = total_size_bytes * 8
    return total_size_bits, processed_files, error_message

def format_size_bits(size_bits: int) -> str:
    """Convert bits to human-readable format (bits, kb, Mb)."""
    if size_bits < 1000:
        return f"{size_bits} bits"
    elif size_bits < 1000 * 1000:
        return f"{size_bits / 1000:.2f} kb"
    else:
        return f"{size_bits / (1000 * 1000):.2f} Mb"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        uploaded_files = request.files.getlist('files')
        verbose = request.form.get('verbose') == 'on'

        total_size_bits, processed_files, error_message = calculate_storage(uploaded_files)
        
        if error_message and not processed_files:
            return render_template('index.html', error=error_message)

        result = {
            'total_size': format_size_bits(total_size_bits),
            'file_count': len(processed_files),
            'files': [
                {'name': f['name'], 'size': format_size_bits(f['size_bits'])}
                for f in processed_files
            ] if verbose else []
        }
        return render_template('index.html', result=result, error=error_message if error_message else None)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)