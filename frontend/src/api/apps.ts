const API_URL = "http://127.0.0.1:8002";

export interface App {
  id: string;
  name: string;
  summary: string;
  description: string;
  icon_url: string | null;
  category: string;
  source: "fdroid" | "playstore";
  license: string;
  apk_url: string | null;
  play_store_url: string | null;
  version: string;
  last_updated: string;
}

export async function fetchApps(params?: {
  category?: string;
  search?: string;
  source?: string;
  limit?: number;
  offset?: number;
}): Promise<App[]> {
  const query = new URLSearchParams();
  if (params?.category) query.set("category", params.category);
  if (params?.search) query.set("search", params.search);
  if (params?.source) query.set("source", params.source);
  if (params?.limit) query.set("limit", String(params.limit));
  if (params?.offset) query.set("offset", String(params.offset));

  const res = await fetch(`${API_URL}/api/apps?${query.toString()}`);
  if (!res.ok) throw new Error("Failed to fetch apps");
  return res.json();
}

export async function fetchApp(id: string): Promise<App> {
  const res = await fetch(`${API_URL}/api/apps/${id}`);
  if (!res.ok) throw new Error("Failed to fetch app");
  return res.json();
}

export async function fetchCategories(source?: string): Promise<string[]> {
  const query = new URLSearchParams();
  if (source) query.set("source", source);
  const res = await fetch(`${API_URL}/api/categories?${query.toString()}`);
  if (!res.ok) throw new Error("Failed to fetch categories");
  return res.json();
}