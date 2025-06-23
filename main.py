from data.generate_data import generate_temperature_data
from src.anomaly_detection import detect_anomalies
from src.visualize import plot_temperature, plot_anomalies

def main():
    df = generate_temperature_data()
    plot_temperature(df)
    df = detect_anomalies(df)
    plot_anomalies(df)
    df.to_csv("output/temperature_anomalies.csv")

if __name__ == "__main__":
    main()
