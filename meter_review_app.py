import streamlit as st
import pandas as pd
from PIL import Image
import os

# =====================================================
# CONFIG
# =====================================================

FILE_PATH = r"C:\Users\LENOVO\excel_automate\TSECL_1001101_F004_202506_LOCAL.xlsx"
SAVE_PATH = r"C:\Users\LENOVO\excel_automate\TSECL_1001101_F004_202506_REVIEWED.xlsx"

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="Meter Review Tool",
    layout="wide"
)

# =====================================================
# LOAD DATA
# =====================================================

def load_data():

    if os.path.exists(SAVE_PATH):

        try:
            df = pd.read_excel(
                SAVE_PATH,
                engine="openpyxl"
            )

        except Exception:

            df = pd.read_excel(
                FILE_PATH,
                engine="openpyxl"
            )

    else:

        df = pd.read_excel(
            FILE_PATH,
            engine="openpyxl"
        )

    # Ensure remark column exists
    if "remark" not in df.columns:
        df["remark"] = ""

    # Force text type
    df["remark"] = (
        df["remark"]
        .fillna("")
        .astype(str)
    )

    return df


df = load_data()

# Convert any "nan" strings back to blank
df["remark"] = df["remark"].replace("nan", "")

# =====================================================
# ADD REMARK COLUMN IF MISSING
# =====================================================

if "remark" not in df.columns:
    df["remark"] = ""

# =====================================================
# FIND FIRST UNREVIEWED
# =====================================================

def get_next_unreviewed():

    pending = df[
        df["remark"]
        .fillna("")
        .astype(str)
        .str.strip()
        .eq("")
    ]

    if len(pending) == 0:
        return 0

    return pending.index[0]

# =====================================================
# SESSION STATE
# =====================================================

if "current_idx" not in st.session_state:
    st.session_state.current_idx = get_next_unreviewed()

idx = st.session_state.current_idx

# Safety check
idx = max(0, min(idx, len(df) - 1))

row = df.iloc[idx]

# =====================================================
# SAVE FUNCTION
# =====================================================

def save_current_remark(remark_text):

    global df

    # Force object dtype before saving
    df["remark"] = df["remark"].astype(object)

    df.at[idx, "remark"] = str(remark_text)

    df.to_excel(
        SAVE_PATH,
        index=False,
        engine="openpyxl"
    )

# =====================================================
# PROGRESS
# =====================================================

completed = (
    df["remark"]
    .fillna("")
    .astype(str)
    .str.strip()
    .ne("")
    .sum()
)

percent = round(
    (completed / len(df)) * 100,
    2
)

# =====================================================
# HEADER
# =====================================================

st.title("⚡ Meter Image Review Tool")

st.progress(completed / len(df))

st.write(
    f"Completed: {completed}/{len(df)} ({percent}%)"
)

if completed == len(df):

    st.success(
        "🎉 All entries reviewed!"
    )

st.divider()

# =====================================================
# DETAILS
# =====================================================

col1, col2, col3 = st.columns(3)

with col1:

    st.metric(
        "KNO",
        str(row["kno"])
    )

with col2:

    st.metric(
        "Present Reading",
        str(row["present_reading"])
    )

with col3:

    ocr_value = ""

    if "present_reading_ocr" in df.columns:
        ocr_value = row["present_reading_ocr"]

    st.metric(
        "OCR Reading",
        str(ocr_value)
    )

st.write(
    f"### Entry {idx + 1} / {len(df)}"
)

# =====================================================
# IMAGE (LOCAL FILES)
# =====================================================

try:

    image_path = row["local_image"]

    image = Image.open(image_path)

    col_left, col_center, col_right = st.columns(
        [1, 2, 1]
    )

    with col_center:

        st.image(
            image,
            width=450
        )

except Exception as e:

    st.error(
        f"Unable to load image.\n\n{e}"
    )

# =====================================================
# REMARK INPUT
# ENTER = SAVE & NEXT
# =====================================================

current_remark = ""

if pd.notna(row["remark"]):
    current_remark = str(row["remark"])

with st.form(
    "remark_form",
    clear_on_submit=False
):

    remark = st.text_input(
        "Enter Remark",
        value=current_remark,
        key=f"remark_{idx}"
    )

    submitted = st.form_submit_button(
        "Save & Next (Press Enter)"
    )

if submitted:

    save_current_remark(remark)

    if idx < len(df) - 1:
        st.session_state.current_idx += 1

    st.rerun()

# =====================================================
# EXTRA BUTTONS
# =====================================================

col_prev, col_save = st.columns(2)

with col_prev:

    if st.button("⬅ Previous"):

        save_current_remark(remark)

        if idx > 0:
            st.session_state.current_idx -= 1

        st.rerun()

with col_save:

    if st.button("💾 Save"):

        save_current_remark(remark)

        st.success("Saved")

# =====================================================
# JUMP TO ENTRY
# =====================================================

st.divider()

jump_to = st.number_input(
    "Jump to Entry",
    min_value=1,
    max_value=len(df),
    value=idx + 1
)

if st.button("Go"):

    st.session_state.current_idx = jump_to - 1

    st.rerun()