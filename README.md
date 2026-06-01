Meter Image Review Tool

A lightweight Streamlit application for reviewing electricity meter images and recording manual remarks against each entry in an Excel sheet.

Features
Review meter images one by one
Enter free-text remarks
Press Enter to save and move to the next entry
Progress tracking
Resume from the last reviewed entry
Jump to a specific entry
Local image storage for fast navigation
Automatic saving to Excel
Project Structure
project/
│
├── meter_review_app.py
├── download_images.py
├── requirements.txt
├── .gitignore
│
├── TSECL_1001101_F004_202506.xlsx
│
├── images/
│   ├── 0.png
│   ├── 1.png
│   └── ...
│
├── TSECL_1001101_F004_202506_LOCAL.xlsx
└── TSECL_1001101_F004_202506_REVIEWED.xlsx
Installation
1. Clone the Repository
git clone <repository-url>
cd <repository-folder>
2. Create Virtual Environment
python -m venv venv
3. Activate Virtual Environment

Windows

venv\Scripts\activate

Linux / Mac

source venv/bin/activate
4. Install Dependencies
pip install -r requirements.txt
Usage
Step 1: Place Excel File

Copy the source Excel file into the project directory.

Step 2: Download Images Locally
python download_images.py

This will:

Download all meter images
Create the images/ folder
Generate *_LOCAL.xlsx with local image paths
Step 3: Launch Application
streamlit run meter_review_app.py
Step 4: Review Entries
View meter image
Enter remark
Press Enter to save and move to the next entry

All remarks are automatically saved to:

TSECL_1001101_F004_202506_REVIEWED.xlsx
Dependencies
Streamlit
Pandas
OpenPyXL
Pillow

Install manually:

pip install streamlit pandas openpyxl pillow
Output

The application creates:

Local image repository (images/)
Excel file with image mappings (*_LOCAL.xlsx)
Reviewed Excel file with remarks (*_REVIEWED.xlsx)
