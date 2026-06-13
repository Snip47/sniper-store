import os
from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from supabase import create_client
from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL = os.environ["SUPABASE_URL"]
SUPABASE_KEY = os.environ["SUPABASE_KEY"]

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

app = FastAPI(title="Sniper Store API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://sniper-store-two.vercel.app", "http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {"message": "Sniper Store API is running"}


@app.get("/api/apps")
def get_apps(
    category: str | None = Query(None),
    search: str | None = Query(None),
    source: str | None = Query(None, description="'fdroid' or 'playstore'"),
    limit: int = Query(50, le=200),
    offset: int = Query(0, ge=0),
):
    query = supabase.table("apps").select("*")

    if category:
        query = query.eq("category", category)
    if search:
        query = query.ilike("name", f"%{search}%")
    if source:
        query = query.eq("source", source)

    query = query.range(offset, offset + limit - 1)
    result = query.execute()
    return result.data


@app.get("/api/apps/{app_id}")
def get_app(app_id: str):
    result = supabase.table("apps").select("*").eq("id", app_id).execute()
    if not result.data:
        raise HTTPException(status_code=404, detail="App not found")
    return result.data[0]


@app.get("/api/categories")
def get_categories(source: str | None = Query(None)):
    query = supabase.table("apps").select("category")
    if source:
        query = query.eq("source", source)
    result = query.execute()
    categories = sorted(set(row["category"] for row in result.data if row["category"]))
    return categories