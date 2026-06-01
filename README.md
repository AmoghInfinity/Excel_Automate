# Meter Image Review Tool

A Streamlit-based application for reviewing electricity meter images and recording manual remarks against each entry in an Excel sheet.

## Features

- Review meter images one by one
- Enter free-text remarks
- Press **Enter** to save and move to the next entry
- Resume from the last reviewed entry
- Jump to a specific entry
- Progress tracking
- Local image storage for fast image loading
- Automatic saving of remarks to Excel

---

## Project Structure

```text
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
```

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/AmoghInfinity/Excel_Automate.git
cd Excel_Automate
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / macOS

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Usage

### Step 1: Place the Source Excel File

Copy the source Excel file into the project directory.

### Step 2: Download All Images Locally

```bash
python download_images.py
```

This script:
- Downloads all meter images
- Creates the `images/` folder
- Generates a new Excel file with local image paths

### Step 3: Launch the Application

```bash
streamlit run meter_review_app.py
```

### Step 4: Review Entries

1. View the meter image.
2. Enter a remark.
3. Press **Enter** to save and automatically move to the next entry.

All remarks are saved automatically.

---

## Output Files

### Local Image Mapping File

```text
TSECL_1001101_F004_202506_LOCAL.xlsx
```

### Reviewed Output File

```text
TSECL_1001101_F004_202506_REVIEWED.xlsx
```

Contains all entered remarks and can be shared directly after review.

---

## Required Python Packages

```bash
pip install streamlit pandas openpyxl pillow requests
```

---

## Workflow Summary

```text
Excel File
    ↓
Download Images
    ↓
Store Images Locally
    ↓
Launch Streamlit App
    ↓
Review Images
    ↓
Enter Remarks
    ↓
Generate Reviewed Excel File
```
