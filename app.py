import streamlit as st
import pandas as pd

from service import generate_events
from scenarios import SCENARIOS


st.set_page_config(
    page_title="MQTT Telemetry Simulator",
    page_icon="🔋",
    layout="wide"
)


st.title("🔋 MQTT Telemetry Simulator")
st.write("Generate and monitor simulated battery telemetry events.")


# Sidebar
st.sidebar.header("Telemetry Configuration")

battery_id = st.sidebar.text_input(
    "Battery ID",
    value="BAT001"
)

scenario = st.sidebar.selectbox(
    "Select Scenario",
    SCENARIOS
)

count = st.sidebar.number_input(
    "Number of Events",
    min_value=1,
    max_value=100,
    value=5
)

delay_seconds = st.sidebar.number_input(
    "Delay (seconds)",
    min_value=0,
    max_value=300,
    value=10
)


# Generate button
if st.sidebar.button("Generate Events"):

    try:
        events = generate_events(
            battery_id=battery_id,
            scenario=scenario,
            count=count,
            delay_seconds=delay_seconds
        )

        st.success(f"{len(events)} telemetry events generated successfully.")

        # Convert to DataFrame
        df = pd.DataFrame(events)

        st.subheader("Telemetry Event Stream")

        st.dataframe(
            df,
            use_container_width=True
        )

        # Download CSV
        csv_data = df.to_csv(index=False)

        st.download_button(
            label="Download CSV",
            data=csv_data,
            file_name="telemetry_events.csv",
            mime="text/csv"
        )

        # Statistics
        st.subheader("Event Summary")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "Total Events",
                len(events)
            )

        with col2:
            anomaly_count = sum(
                1 for event in events
                if event.get("anomaly")
            )

            st.metric(
                "Anomalies",
                anomaly_count
            )

        with col3:
            st.metric(
                "Scenario",
                scenario
            )

    except Exception as e:
        st.error(f"Error: {e}")


# Information section
st.divider()

st.subheader("Available Scenarios")

for item in SCENARIOS:
    st.write(f"• {item}")