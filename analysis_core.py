"""
PROJECT: VENEZUELAN STATE ARCHITECTURE - QUANTITATIVE ANALYSIS
AUTHOR: Dr. Brian Penrod, DBA
DATE: Dec 2025
DESCRIPTION: 
    A unified forensic audit applying Graph Theory (NetworkX) and 
    Statistical Frequency Analysis (Benford's Law) to validate 
    open-source intelligence regarding regime command structures.
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import networkx as nx
import os

# --- SETUP: INFRASTRUCTURE ---
# Create an 'images' folder if it doesn't exist to store our evidence
if not os.path.exists('images'):
    os.makedirs('images')

def run_network_topology():
    print("\n[+] INITIATING NETWORK TOPOLOGY ANALYSIS...")
    
    # 1. THE INTEL DATA (Nodes & Edges)
    relationships = [
        {"Source": "Jorge Rodríguez", "Target": "Maduro", "Type": "Puppeteer"},
        {"Source": "Jorge Rodríguez", "Target": "SEBIN (Intel)", "Type": "Control"},
        {"Source": "Delcy Rodríguez", "Target": "Financial Flows", "Type": "Control"},
        {"Source": "Delcy Rodríguez", "Target": "Gold Mining", "Type": "Control"},
        {"Source": "Diosdado Cabello", "Target": "Military (FANB)", "Type": "Control"},
        {"Source": "Diosdado Cabello", "Target": "Ports/Airports", "Type": "Logistics"},
        {"Source": "Cartel of the Suns", "Target": "FARC/ELN", "Type": "Proxy Force"},
        {"Source": "Maduro", "Target": "Tren de Aragua", "Type": "Export Strategy"},
        {"Source": "Tren de Aragua", "Target": "Migration Routes", "Type": "Extortion"},
        {"Source": "General Quintero", "Target": "Electoral Results", "Type": "Manipulation"},
        {"Source": "Jorge Rodríguez", "Target": "General Quintero", "Type": "Oversight"}
    ]

    # 2. BUILD GRAPH
    df_intel = pd.DataFrame(relationships)
    G = nx.from_pandas_edgelist(df_intel, "Source", "Target", edge_attr="Type", create_using=nx.DiGraph())

    # 3. REVERSE PAGERANK (Command Authority)
    print("    > Calculating Inverted Centrality (Source of Power)...")
    G_authority = G.reverse()
    authority_score = nx.pagerank(G_authority)

    # 4. REPORTING
    print(f"    > AUTHORITY IDENTIFIED: Jorge Rodríguez (Score: {authority_score.get('Jorge Rodríguez', 0):.4f})")
    print(f"    > EXECUTIVE IDENTIFIED: Maduro (Score: {authority_score.get('Maduro', 0):.4f})")

    # 5. VISUALIZATION (AUTO-SAVE)
    plt.figure(figsize=(12, 8))
    pos = nx.spring_layout(G, seed=42, k=0.8)
    
    # Highlight the "Bosses" (Score > 0.08)
    node_colors = ['gold' if authority_score.get(node, 0) > 0.08 else 'lightgrey' for node in G.nodes()]
    node_sizes = [v * 15000 for v in authority_score.values()]
    
    nx.draw_networkx_nodes(G, pos, node_size=node_sizes, node_color=node_colors, alpha=0.9)
    nx.draw_networkx_labels(G, pos, font_size=9, font_weight="bold")
    nx.draw_networkx_edges(G, pos, arrows=True, arrowstyle="-|>", edge_color="gray")
    
    plt.title("NETWORK TOPOLOGY: Command Authority Analysis", fontsize=14, fontweight='bold')
    plt.axis("off")
    
    # SAVE TO DISK
    plt.savefig('images/network_graph.png')
    print("    > ASSET SAVED: images/network_graph.png")
    plt.close()

def run_forensic_audit():
    print("\n[+] INITIATING FORENSIC DATA AUDIT (BENFORD'S LAW)...")
    
    # 1. SIMULATE DATA (Natural vs Engineered)
    np.random.seed(42)
    natural_votes = np.random.lognormal(mean=8, sigma=1.5, size=5000).astype(int) # Organic
    natural_votes = natural_votes[natural_votes > 0]
    rigged_votes = np.random.randint(low=1000, high=25000, size=5000) # Man-made (Uniform)

    # 2. HELPER FUNCTIONS
    def get_leading_digits(data):
        return [int(str(vote)[0]) for vote in data]

    def get_frequencies(digits):
        counts = pd.Series(digits).value_counts().sort_index()
        return (counts / len(digits)) * 100

    # 3. CALCULATE STATS
    nat_freq = get_frequencies(get_leading_digits(natural_votes))
    rig_freq = get_frequencies(get_leading_digits(rigged_votes))
    
    # Benford Theoreticals
    benford_values = {1: 30.1, 2: 17.6, 3: 12.5, 4: 9.7, 5: 7.9, 6: 6.7, 7: 5.8, 8: 5.1, 9: 4.6}
    benford_series = pd.Series(benford_values)
    
    # Calculate Deviation (Mean Absolute Error)
    rig_deviation = sum(abs(rig_freq.get(d, 0) - benford_series[d]) for d in range(1, 10)) / 9
    print(f"    > RIGGED DATA DEVIATION: {rig_deviation:.2f}% (Target > 2.0% indicates anomalies)")

    # 4. VISUALIZATION (AUTO-SAVE)
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    
    # Plot Natural
    axes[0].bar(benford_series.index, benford_series.values, color='gray', alpha=0.3, label='Expected')
    axes[0].plot(nat_freq.index, nat_freq.values, color='green', marker='o', linewidth=2, label='Actual')
    axes[0].set_title("SCENARIO A: ORGANIC (Clean)")
    
    # Plot Rigged
    axes[1].bar(benford_series.index, benford_series.values, color='gray', alpha=0.3, label='Expected')
    axes[1].plot(rig_freq.index, rig_freq.values, color='red', marker='x', linewidth=2, label='Rigged')
    axes[1].set_title("SCENARIO B: ENGINEERED (Fraud)")
    axes[1].legend()

    plt.tight_layout()
    plt.savefig('images/benford_chart.png')
    print("    > ASSET SAVED: images/benford_chart.png")
    plt.close()

if __name__ == "__main__":
    print("--- STARTING STRATEGIC INTELLIGENCE PIPELINE ---")
    run_network_topology()
    run_forensic_audit()
    print("--- MISSION COMPLETE: All assets generated in /images folder ---")
