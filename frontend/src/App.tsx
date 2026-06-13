import { useEffect, useState } from "react";
import { fetchApps, fetchCategories, type App } from "./api/apps";

export default function App() {
  const [apps, setApps] = useState<App[]>([]);
  const [categories, setCategories] = useState<string[]>([]);
  const [selectedCategory, setSelectedCategory] = useState<string>("");
  const [search, setSearch] = useState("");
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchCategories("playstore").then(setCategories).catch(console.error);
  }, []);

  useEffect(() => {
    setLoading(true);
    fetchApps({ source: "playstore", category: selectedCategory || undefined, search: search || undefined, limit: 60 })
      .then(setApps)
      .catch(console.error)
      .finally(() => setLoading(false));
  }, [selectedCategory, search]);

  return (
    <div className="min-h-screen bg-zinc-950 text-zinc-100">
      {/* Header */}
      <header className="sticky top-0 z-10 border-b border-zinc-800 bg-zinc-950/90 backdrop-blur">
        <div className="mx-auto max-w-6xl px-4 py-4 flex items-center gap-4">
          <h1 className="text-2xl font-bold">
            <span className="text-purple-400">Sniper</span>{" "}
            <span className="text-cyan-400">Store</span>
          </h1>

          <input
            type="text"
            placeholder="Search apps..."
            value={search}
            onChange={(e) => setSearch(e.target.value)}
            className="ml-auto w-full sm:w-64 rounded-lg bg-zinc-900 border border-zinc-800 px-4 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-purple-500"
          />
        </div>
      </header>

      <div className="mx-auto max-w-6xl px-4 py-6 flex gap-6">
        {/* Sidebar - categories */}
        <aside className="w-48 shrink-0 hidden md:block">
          <h2 className="text-sm font-semibold text-zinc-400 uppercase mb-3">Categories</h2>
          <ul className="space-y-1 max-h-[70vh] overflow-y-auto pr-2">
            <li>
              <button
                onClick={() => setSelectedCategory("")}
                className={`w-full text-left px-3 py-2 rounded-lg text-sm transition ${
                  selectedCategory === ""
                    ? "bg-purple-500/20 text-purple-300"
                    : "text-zinc-400 hover:bg-zinc-900 hover:text-zinc-200"
                }`}
              >
                All Apps
              </button>
            </li>
            {categories.map((cat) => (
              <li key={cat}>
                <button
                  onClick={() => setSelectedCategory(cat)}
                  className={`w-full text-left px-3 py-2 rounded-lg text-sm transition ${
                    selectedCategory === cat
                      ? "bg-purple-500/20 text-purple-300"
                      : "text-zinc-400 hover:bg-zinc-900 hover:text-zinc-200"
                  }`}
                >
                  {cat}
                </button>
              </li>
            ))}
          </ul>
        </aside>

        {/* App grid */}
        <main className="flex-1">
          {loading ? (
            <div className="text-center text-zinc-500 py-20">Loading apps...</div>
          ) : apps.length === 0 ? (
            <div className="text-center text-zinc-500 py-20">No apps found.</div>
          ) : (
            <div className="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-4 gap-4">
              {apps.map((app) => (
                <AppCard key={app.id} app={app} />
              ))}
            </div>
          )}
        </main>
      </div>
    </div>
  );
}

function AppCard({ app }: { app: App }) {
  return (
    <div className="group rounded-xl bg-zinc-900 border border-zinc-800 p-4 hover:border-cyan-500/50 hover:shadow-lg hover:shadow-cyan-500/10 transition">
      <div className="flex items-center gap-3 mb-3">
        {app.icon_url ? (
          <img
            src={app.icon_url}
            alt={app.name}
            className="w-12 h-12 rounded-lg object-cover bg-zinc-800"
            onError={(e) => (e.currentTarget.style.display = "none")}
          />
        ) : (
          <div className="w-12 h-12 rounded-lg bg-gradient-to-br from-purple-500 to-cyan-500 flex items-center justify-center text-lg font-bold shrink-0">
            {app.name.charAt(0)}
          </div>
        )}
        <div className="flex-1 min-w-0">
          <h3 className="font-semibold text-sm truncate group-hover:text-cyan-300 transition">
            {app.name}
          </h3>
          <p className="text-xs text-zinc-500 truncate">{app.category}</p>
        </div>
      </div>
      <p className="text-xs text-zinc-400 line-clamp-2 mb-3 min-h-[2.5em]">
        {app.summary || "No description available."}
      </p>
      <a
        href={app.play_store_url ?? "#"}
        target="_blank"
        rel="noopener noreferrer"
        className="block text-center text-sm font-medium rounded-lg bg-gradient-to-r from-purple-600 to-cyan-600 py-2 hover:from-purple-500 hover:to-cyan-500 transition"
      >
        Install
      </a>
    </div>
  );
}