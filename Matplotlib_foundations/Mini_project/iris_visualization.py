import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from mpl_toolkits.mplot3d import Axes3D

# ---------------------------
# 1. Setup & Load Dataset
# ---------------------------
SAVE_DIR = "Project_output"
os.makedirs(SAVE_DIR, exist_ok=True)  # Folder to save plots

columns = ["sepal_length", "sepal_width", "petal_length", "petal_width", "species"]

# Load dataset
df = pd.read_csv("Project_data/iris.csv", header=None, names=columns)

print("✅ Dataset Loaded Successfully!")
print(df.head(), "\n")

# ---------------------------
# 2. Basic Info
# ---------------------------
print("📊 Dataset Info:")
print(df.describe(), "\n")

# ---------------------------
# 3. Feature Distributions
# ---------------------------
plt.figure(figsize=(12, 8))
plt.suptitle("Iris Dataset - Feature Distributions", fontsize=16, fontweight="bold")

features = ["sepal_length", "sepal_width", "petal_length", "petal_width"]

for i, col in enumerate(features):
    plt.subplot(2, 2, i + 1)
    plt.hist(df[col], bins=20, color="#66b3ff", edgecolor="black", alpha=0.75)
    plt.title(col.replace("_", " ").title())
    plt.xlabel(col)
    plt.ylabel("Frequency")

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.savefig(f"{SAVE_DIR}/1_feature_distributions.png", dpi=300)
plt.close()

# ---------------------------
# 4. Boxplots for Feature Comparison
# ---------------------------
plt.figure(figsize=(10, 6))
plt.boxplot([df["sepal_length"], df["sepal_width"], df["petal_length"], df["petal_width"]],
            labels=features, patch_artist=True,
            boxprops=dict(facecolor="#ffcc99", color="black"),
            medianprops=dict(color="red"))
plt.title("Feature Comparison via Boxplots")
plt.ylabel("cm")
plt.grid(True, linestyle="--", alpha=0.6)
plt.savefig(f"{SAVE_DIR}/2_boxplots.png", dpi=300)
plt.close()

# ---------------------------
# 5. Scatter Plots (Species-wise)
# ---------------------------
plt.figure(figsize=(10, 6))
species_list = df["species"].unique()
colors = ["#ff9999", "#99ff99", "#9999ff"]

for i, species in enumerate(species_list):
    subset = df[df["species"] == species]
    plt.scatter(subset["sepal_length"], subset["petal_length"],
                label=species, color=colors[i], alpha=0.7, edgecolor="black")

plt.title("Sepal Length vs Petal Length by Species")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.5)
plt.savefig(f"{SAVE_DIR}/3_scatter_species.png", dpi=300)
plt.close()

# ---------------------------
# 6. Correlation Heatmap
# ---------------------------
corr = df.iloc[:, 0:4].corr()

plt.figure(figsize=(6, 5))
plt.imshow(corr, cmap="coolwarm", interpolation="nearest")
plt.colorbar(label="Correlation")
plt.title("Correlation Heatmap of Iris Features")
plt.xticks(range(len(corr.columns)), corr.columns, rotation=45)
plt.yticks(range(len(corr.index)), corr.index)
plt.tight_layout()
plt.savefig(f"{SAVE_DIR}/4_correlation_heatmap.png", dpi=300)
plt.close()

# ---------------------------
# 7. 3D Visualization
# ---------------------------
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection="3d")

for i, species in enumerate(species_list):
    subset = df[df["species"] == species]
    ax.scatter(subset["sepal_length"], subset["sepal_width"], subset["petal_length"],
               color=colors[i], label=species, s=50, edgecolor="black")

ax.set_title("3D Plot: Sepal Length vs Width vs Petal Length")
ax.set_xlabel("Sepal Length (cm)")
ax.set_ylabel("Sepal Width (cm)")
ax.set_zlabel("Petal Length (cm)")
ax.legend()
plt.savefig(f"{SAVE_DIR}/5_3d_visualization.png", dpi=300)
plt.close()

# ---------------------------
# 8. Scatter Matrix (No seaborn)
# ---------------------------
plt.figure(figsize=(10, 10))
plt.suptitle("Scatter Matrix of Features", fontsize=16, fontweight="bold")

for i, col1 in enumerate(features):
    for j, col2 in enumerate(features):
        plt.subplot(len(features), len(features), i * len(features) + j + 1)
        if i == j:
            plt.hist(df[col1], bins=15, color="#b3d9ff", edgecolor="black")
        else:
            plt.scatter(df[col2], df[col1], s=10, alpha=0.6, color="#66cc99")
        if i == len(features) - 1:
            plt.xlabel(col2, fontsize=8)
        if j == 0:
            plt.ylabel(col1, fontsize=8)
        plt.xticks(fontsize=6)
        plt.yticks(fontsize=6)

plt.tight_layout(rect=[0, 0, 1, 0.97])
plt.savefig(f"{SAVE_DIR}/6_scatter_matrix.png", dpi=300)
plt.close()

# ---------------------------
# 9. Save Summary Report
# ---------------------------
summary_text = f"""
📈 IRIS VISUALIZATION PROJECT SUMMARY
------------------------------------
Total Samples: {len(df)}
Number of Species: {df['species'].nunique()}
Species List: {', '.join(species_list)}

Observations:
1. Setosa species are clearly separable in scatter plots.
2. Petal length and petal width show strong correlation (~0.96).
3. Boxplots reveal Setosa has much smaller petal dimensions.
4. Feature distributions are mostly normal, except for petal width skew.
5. 3D and scatter matrix visuals highlight clear clustering between species.

All plots have been saved in the folder: {SAVE_DIR}/
"""

with open(f"{SAVE_DIR}/visualization_summary.txt", "w", encoding="utf-8") as f:
    f.write(summary_text)

print(summary_text)
print("All graphs and summary saved successfully!")