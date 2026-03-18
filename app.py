import pandas as pd
from pyproj import Transformer

INPUT_CSV = "./data/Collisions.csv"
OUTPUT_JSON = "collisions_latlon_min.json"

SOURCE_CRS = "EPSG:2286"
TARGET_CRS = "EPSG:4326"

FIELDS = [
    "lat",
    "lon",
    "CollYear",
    "NumInjuries",
    "NumFatalities",
    "LightingCond",
    "Weather",
    "MostSevereInjType",
]

df = pd.read_csv(INPUT_CSV)

df["X"] = pd.to_numeric(df["X"], errors="coerce")
df["Y"] = pd.to_numeric(df["Y"], errors="coerce")

df = df.dropna(subset=["X", "Y"])

transformer = Transformer.from_crs(SOURCE_CRS, TARGET_CRS, always_xy=True)

lonlat = df.apply(lambda r: transformer.transform(r["X"], r["Y"]), axis=1)
df["lon"] = [p[0] for p in lonlat]
df["lat"] = [p[1] for p in lonlat]

fields_present = [c for c in FIELDS if c in df.columns]
df_out = df[fields_present].copy()

df_out.to_json(OUTPUT_JSON, orient="records", indent=2)
print(f"Saved {len(df_out)} rows to {OUTPUT_JSON}")
