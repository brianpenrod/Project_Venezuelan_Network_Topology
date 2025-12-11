# Project_Venezuelan_Network_Topology
Quantifying the Venezuelan 'Shadow State': A Python-based forensic audit applying Graph Theory (NetworkX) and Benford's Law to model regime command authority and detect electoral anomalies
# Venezuelan State Architecture: Network Topology & Forensic Audit (2025)

## 1. Executive Summary
This project applies **Graph Theory (NetworkX)** and **Forensic Data Analysis (Benford's Law)** to validate open-source intelligence regarding the command structure of the Venezuelan regime. 

Using the December 2025 testimony of Clíver Alcalá Cordones (Ret. Major General) as the primary dataset[cite: 128], this analysis quantifies "Command Authority" and tests for statistical anomalies in electoral data mechanisms.

## 2. Strategic Objectives
* **Quantify Influence:** Move beyond static organizational charts to measure dynamic power using centrality algorithms.
* **Detect Fraud:** Apply digital frequency analysis to identify manual manipulation in reported data.
* **Demonstrate Capability:** Showcase the application of Python in National Security and Strategic Risk context.

## 3. Methodology

### A. Network Topology (The "Shadow Directorate")
* **Algorithm:** Inverted PageRank (Reverse Centrality).
* **Goal:** Measure the "Source of Orders" rather than "Degree of Connection."
* **Finding:** The "Shadow Directorate" (Rodríguez Clan) holds **2.1x** the structural authority (Score: 0.20) of the Executive Branch (Score: 0.09).

### B. Forensic Audit (Benford's Law)
* **Algorithm:** First-Digit Frequency Analysis (Benford's Law).
* **Target:** Simulated "Totalization" data representing manual interference.
* **Finding:** * *Natural Baseline:* 0.31% Deviation (Clean).
    * *Target Data:* 5.19% Deviation (Significant Anomaly).

## 4. Visual Assets
![Network Graph](images/network_graph.png)
*Figure 1: Network Topology identifying the primary command node.*

![Benford Analysis](images/benford_chart.png)
*Figure 2: Forensic analysis detecting statistical engineering in data distributions.*

## 5. Tools Used
* **Language:** Python 3.10+
* **Libraries:** `NetworkX`, `Pandas`, `Matplotlib`, `NumPy`, `SciPy`
* **Concept:** Open Source Intelligence (OSINT) Analysis

---
*Disclaimer: This analysis is based on open-source datasets and public testimony. It is intended for educational and portfolio demonstration purposes only.*
