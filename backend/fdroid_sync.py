"""
fdroid_sync.py
Fetches the F-Droid app index and populates the Supabase 'apps' table
with source='fdroid'.
Run manually: python fdroid_sync.py
"""

import os
import httpx
from supabase import create_client
from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL = os.environ["SUPABASE_URL"]
SUPABASE_KEY = os.environ["SUPABASE_KEY"]

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

FDROID_INDEX_URL = "https://f-droid.org/repo/index-v1.json"
ICON_BASE_URL = "https://f-droid.org/repo/icons-640/"
APK_BASE_URL = "https://f-droid.org/repo/"


def fetch_fdroid_index():
    print("Fetching F-Droid index... (large file, may take a minute)")
    with httpx.Client(timeout=120) as client:
        resp = client.get(FDROID_INDEX_URL)
        resp.raise_for_status()
        return resp.json()


def get_localized(field, fallback=""):
    """F-Droid index fields can be plain strings or {'en-US': '...'} dicts."""
    if isinstance(field, dict):
        return field.get("en-US") or next(iter(field.values()), fallback)
    if isinstance(field, str):
        return field
    return fallback


def build_app_rows(data):
    apps = data.get("apps", [])
    packages = data.get("packages", {})

    rows = []
    for app in apps:
        package_name = app.get("packageName")
        if not package_name:
            continue

        versions = packages.get(package_name, [])
        latest_apk = versions[0] if versions else {}

        apk_filename = latest_apk.get("apkName")
        apk_url = f"{APK_BASE_URL}{apk_filename}" if apk_filename else None

        icon = app.get("icon")
        icon_url = f"{ICON_BASE_URL}{icon}" if icon else None

        categories = app.get("categories", [])
        category = categories[0] if categories else "Other"

        name = get_localized(app.get("name"), package_name)
        summary = get_localized(app.get("summary"), "")
        description = get_localized(app.get("description"), "")

        row = {
            "id": package_name,
            "name": name,
            "summary": summary,
            "description": description,
            "icon_url": icon_url,
            "category": category,
            "source": "fdroid",
            "license": app.get("license", ""),
            "apk_url": apk_url,
            "play_store_url": None,
            "version": latest_apk.get("versionName", ""),
        }
        rows.append(row)

    return rows


def upload_to_supabase(rows):
    print(f"Uploading {len(rows)} apps to Supabase...")
    batch_size = 50
    for i in range(0, len(rows), batch_size):
        batch = rows[i:i + batch_size]
        supabase.table("apps").upsert(batch).execute()
        print(f"  Uploaded batch {i // batch_size + 1} ({len(batch)} apps)")
    print("Done!")


if __name__ == "__main__":
    data = fetch_fdroid_index()
    rows = build_app_rows(data)
    upload_to_supabase(rows)