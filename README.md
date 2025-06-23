# 🌡️ Temperature Sensor Anomaly Detection (Time-Series)

An end-to-end machine learning project to simulate IoT temperature sensor data, detect anomalies using Isolation Forest, and visualize results. This is a practical use-case for industrial IoT (IIoT) systems such as predictive maintenance, HVAC monitoring, or factory temperature control.

---

## 📌 Features

- Simulated time-series temperature data
- Injected realistic anomalies (spikes and drops)
- Anomaly detection using Isolation Forest
- Time-series data visualization with anomaly markers
- Modular codebase for easy scaling and real sensor integration

---

## 🚀 Tech Stack

| Type        | Tools/Libraries                   |
|-------------|-----------------------------------|
| Language    | Python 3.x                        |
| Libraries   | pandas, numpy, matplotlib, scikit-learn |
| ML Model    | Isolation Forest (Unsupervised)   |
| Output      | CSV file with anomaly labels      |

---

## 📂 Project Structure

temperature-anomaly-detector/
│
├── data/
│ └── generate_data.py # Simulates temperature data
│
├── src/
│ ├── anomaly_detection.py # Isolation Forest anomaly detection
│ └── visualize.py # Graph plotting functions
│
├── output/
│ └── temperature_anomalies.csv # Final output with anomaly labels
│
├── main.py # Main runner script
├── requirements.txt # Python dependencies
└── README.md # Project documentation

---

## 🔧 How to Run

1. **Clone the repository:**
   ```bash
   git clone https://github.com/A-ditya-Keshri/temperature-anomaly-detector.git
   cd temperature-anomaly-detector

2. Install dependencies:
   pip install -r requirements.txt

3. Run the project:
   python main.py

4. Output:
   Plots showing temperature trends and detected anomalies.
   A CSV file: output/temperature_anomalies.csv with labels.

👨‍💻 Author
Aditya Keshri

B.Tech CSE (AI), JECRC Foundation
