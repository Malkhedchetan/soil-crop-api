import pandas as pd
import numpy as np
from co import get_connection

conn = get_connection()

# Fetch crop and soil data
query = """
SELECT 
    s.soil_name AS soil_type,
    c.crop_name,
    MAX(CASE WHEN cn.nutrient = 'Nitrogen'   THEN cn.ideal_value END) AS N,
    MAX(CASE WHEN cn.nutrient = 'Phosphorus' THEN cn.ideal_value END) AS P,
    MAX(CASE WHEN cn.nutrient = 'Potassium'  THEN cn.ideal_value END) AS K
FROM crops c
JOIN soiltypes s       ON c.soil_id = s.id
JOIN crop_nutrients cn ON c.id = cn.crop_id
GROUP BY s.soil_name, c.crop_name
ORDER BY s.soil_name, c.crop_name;
"""
df_crops_full = pd.read_sql(query, conn)
fertilizers_df = pd.read_sql("SELECT * FROM fertilizers;", conn)

# Function to recommend the best crop based on soil NPK
def recommend_best_crop(soil_type: str, n: float, p: float, k: float, top_k: int = 1):
    FEATURES = ['N','P','K']
    
    subset = df_crops_full[df_crops_full['soil_type'].str.strip().str.lower() == soil_type.strip().lower()]
    if subset.empty:
        subset = df_crops_full.copy()
    
    mean = subset[FEATURES].mean().values
    std = subset[FEATURES].std().replace(0,1).values
    X = (subset[FEATURES].to_numpy(dtype=float) - mean) / std
    target = (np.array([n,p,k], dtype=float) - mean) / std
    
    weights = np.array([0.33,0.33,0.34])
    diffs = (X - target) * weights
    dists = np.linalg.norm(diffs, axis=1)
    
    subset = subset.copy()
    subset['distance'] = dists
    subset = subset.sort_values(by='distance').head(top_k)
    
    results = []
    for _, row in subset.iterrows():
        results.append({
            "soil_type": row['soil_type'],
            "recommended_crop": row['crop_name'],
            "ideal_NPK": {"N": float(row['N']), "P": float(row['P']), "K": float(row['K'])},
            "distance": float(row['distance'])
        })
    
    return results[0] if top_k == 1 else results

# Function to check nutrient excess for a specific crop
def recommend_fertilizer_for_other_crop(target_crop: str, soil_type: str, n: float, p: float, k: float):
    target = df_crops_full[(df_crops_full['crop_name'].str.lower() == target_crop.lower()) &
                        (df_crops_full['soil_type'].str.lower() == soil_type.strip().lower())]
    if target.empty:
        target = df_crops_full[df_crops_full['crop_name'].str.lower() == target_crop.strip().lower()]
    if target.empty:
        raise ValueError(f"Crop '{target_crop}' not found.")

    row = target.iloc[0]
    ideal = {"Nitrogen": row['N'], "Phosphorus": row['P'], "Potassium": row['K']}
    current = {"Nitrogen": n, "Phosphorus": p, "Potassium": k}

    messages = []
    for nutrient in ["Nitrogen", "Phosphorus", "Potassium"]:
        excess = current[nutrient] - ideal[nutrient]
        if excess > 0:
            messages.append(f"{nutrient} is {excess} above the ideal value.")

    greeting = f"👋 Hello! Here's your soil nutrient update for {target_crop.title()} on {soil_type.title()}:\n"
    if not messages:
        return greeting + "All nutrients are within ideal range. Great job! 😊"
    return greeting + "\n".join(messages)

user_soil = "BLACK Soil"
user_N, user_P, user_K = 55, 60, 30


rec = recommend_best_crop(user_soil, user_N, user_P, user_K)

print("\n🌱 Based on your soil test results:")
print("------------------------------------------------------")
print(f"   🌾 Soil Type       : {rec['soil_type'].title()}")
print(f"   🥬 Recommended Crop: {rec['recommended_crop'].title()}")
print(f"   💧 Ideal NPK Values: N={rec['ideal_NPK']['N']}, P={rec['ideal_NPK']['P']}, K={rec['ideal_NPK']['K']}")

target_crop = "ragi"
user_soil = 'red soil'
fert_plan = recommend_fertilizer_for_other_crop(target_crop, user_soil, user_N, user_P, user_K)

print(f"\n💡 Fertilizer plan if you want to grow {target_crop.title()}:")
print("------------------------------------------------------")
print(f"{fert_plan}")

