Code Storage Calculator

A Flask-based web application to calculate the storage size of uploaded programming code files, displaying results in bits. The application features a user-friendly HTML/CSS interface, allowing users to upload multiple code files, view total storage size, and optionally see a detailed list of processed files.
Features

File Upload: Upload multiple code files (e.g., .py, .java, .js, .cpp) via a web interface.

Storage Calculation: Computes total storage size in bits, with human-readable formatting (bits, kb, Mb).

Verbose Mode: Shows a detailed list of processed files with individual sizes in bits.

Error Handling: Validates file extensions and handles errors (e.g., invalid files, no files uploaded).

Responsive Design: Modern, mobile-friendly interface using HTML and CSS.

Secure File Handling: Temporarily stores uploaded files and clears them after processing.


Prerequisites:

Python 3.6 or higher

Flask (pip install flask)

Installation:

Clone the Repository:
git clone https://github.com/Ayushi10-kumari/Code_Storage_Calculator.git

cd code-storage-calculator


Set Up a Virtual Environment (optional but recommended):

python -m venv venv

source venv/bin/activate  # On Windows: venv\Scripts\activate


Install Dependencies:

pip install flask


Ensure Project Structure:The project should have the following structure:
code_storage_calculator/
├── app.py                  # Flask backend
├── templates/
│   └── index.html         # HTML frontend
├── static/
│   └── style.css          # CSS for styling
├── uploads/               # Temporary folder for uploaded files (created automatically)
├── README.md              # This file



Usage

Run the Application:

python app.py


Access the Web Interface:

Open a browser and navigate to http://127.0.0.1:5000.

Upload one or more code files (e.g., .py, .js, .cpp).

Check "Show detailed file list" to see individual file sizes in bits.

Click "Calculate" to view results.


Example Output:
Results

Total Storage: 1.25 Mb

Number of Code Files: 3

Processed Files:

- main.py (125.60 kb)
- 
- utils.js (80.00 kb)
- 
- style.css (50.40 kb)


Error Handling:

1.Non-code files trigger: "Some files were skipped (invalid or non-code file extension)".

2.No files uploaded shows: "No files uploaded or invalid files selected".



Project Structure

1.app.py: Flask backend handling file uploads, storage calculations, and result rendering.

2.templates/index.html: HTML frontend with file upload form and result display.

3.static/style.css: CSS for responsive, modern styling.

4.uploads/: Temporary folder for storing uploaded files during processing.

Contributing
Contributions are welcome! To contribute:

1.Fork the repository.

2.Create a new branch (git checkout -b feature/your-feature).

3.Make your changes and commit (git commit -m 'Add your feature').

4.Push to the branch (git push origin feature/your-feature).

5.Open a Pull Request.

Please ensure your code follows the project's coding style and includes relevant tests.

License:

This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgments:

Built with Flask for the backend.

Styled with custom CSS for a responsive user interface.

Inspired by the need to analyze code file storage efficiently.

