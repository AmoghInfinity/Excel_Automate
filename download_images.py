import pandas as pd
import requests
import os
from concurrent.futures import ThreadPoolExecutor, as_completed

EXCEL_FILE = r"C:\Users\LENOVO\excel_automate\TSECL_1001101_F004_202506.xlsx"
OUTPUT_FILE = r"C:\Users\LENOVO\excel_automate\TSECL_1001101_F004_202506_LOCAL.xlsx"

IMAGES_FOLDER = r"C:\Users\LENOVO\excel_automate\images"

os.makedirs(IMAGES_FOLDER, exist_ok=True)

df = pd.read_excel(
    EXCEL_FILE,
    engine="openpyxl"
)

if "local_image" not in df.columns:
    df["local_image"] = ""


def download_image(idx, url):

    try:

        filepath = os.path.join(
            IMAGES_FOLDER,
            f"{idx}.png"
        )

        if not os.path.exists(filepath):

            response = requests.get(
                url,
                timeout=30
            )

            response.raise_for_status()

            with open(filepath, "wb") as f:
                f.write(response.content)

        return idx, filepath, None

    except Exception as e:

        return idx, "", str(e)


futures = []

with ThreadPoolExecutor(max_workers=30) as executor:

    for idx, row in df.iterrows():

        futures.append(
            executor.submit(
                download_image,
                idx,
                row["rating"]
            )
        )

    completed = 0

    for future in as_completed(futures):

        idx, path, error = future.result()

        if path:
            df.at[idx, "local_image"] = path

        completed += 1

        if completed % 50 == 0:
            print(
                f"{completed}/{len(df)} downloaded"
            )

df.to_excel(
    OUTPUT_FILE,
    index=False,
    engine="openpyxl"
)

print("\nDone!")
print(f"Saved: {OUTPUT_FILE}")