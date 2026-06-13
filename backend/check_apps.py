import os
from supabase import create_client
from dotenv import load_dotenv

load_dotenv()

supabase = create_client(os.environ["SUPABASE_URL"], os.environ["SUPABASE_KEY"])

result = supabase.table("apps").select("id, name, category, source").eq("source", "playstore").execute()
print(f"Total playstore apps: {len(result.data)}")

categories = {}
for row in result.data:
    categories[row["category"]] = categories.get(row["category"], 0) + 1

for cat, count in sorted(categories.items()):
    print(f"  {cat}: {count}")