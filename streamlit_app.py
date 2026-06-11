import os
import streamlit as st

st.set_page_config(page_title="Hotel Booking Dashboard", layout="wide")
st.title("Hotel Booking Dashboard")

conn = st.connection("snowflake", ttl=os.getenv("SNOWFLAKE_CONNECTION_TTL"))


@st.cache_data
def load_data():
    return conn.query(
        """
        SELECT
            booking_id,
            hotel_id,
            hotel_city,
            customer_name,
            check_in_date,
            check_out_date,
            room_type,
            num_guests,
            total_amount,
            currency,
            booking_status
        FROM HOTEL_DB.PUBLIC.SILVER_HOTEL_BOOKING
        """
    )


with st.spinner("Loading booking data..."):
    df = load_data()

# Sidebar filters
with st.sidebar:
    st.header("Filters")

    cities = sorted(df["HOTEL_CITY"].dropna().unique().tolist())
    selected_cities = st.multiselect("City", cities, default=cities)

    statuses = sorted(df["BOOKING_STATUS"].dropna().unique().tolist())
    selected_statuses = st.multiselect("Booking Status", statuses, default=statuses)

    room_types = sorted(df["ROOM_TYPE"].dropna().unique().tolist())
    selected_rooms = st.multiselect("Room Type", room_types, default=room_types)

    if st.button("Refresh Data"):
        load_data.clear()
        st.rerun()

# Apply filters
filtered = df[
    (df["HOTEL_CITY"].isin(selected_cities))
    & (df["BOOKING_STATUS"].isin(selected_statuses))
    & (df["ROOM_TYPE"].isin(selected_rooms))
]

# KPI row
total_bookings = len(filtered)
total_revenue = filtered["TOTAL_AMOUNT"].sum()
avg_guests = filtered["NUM_GUESTS"].mean() if total_bookings > 0 else 0
confirmed_pct = (
    (filtered["BOOKING_STATUS"] == "confirmed").sum() / total_bookings * 100
    if total_bookings > 0
    else 0
)

with st.container(horizontal=True):
    st.metric("Total Bookings", f"{total_bookings:,}", border=True)
    st.metric("Total Revenue", f"${total_revenue:,.0f}", border=True)
    st.metric("Avg Guests", f"{avg_guests:.1f}", border=True)
    st.metric("Confirmed %", f"{confirmed_pct:.1f}%", border=True)

# Charts row
col1, col2 = st.columns(2)

with col1:
    with st.container(border=True):
        st.subheader("Bookings by City")
        city_counts = filtered.groupby("HOTEL_CITY").size().reset_index(name="count")
        st.bar_chart(city_counts, x="HOTEL_CITY", y="count")

with col2:
    with st.container(border=True):
        st.subheader("Revenue by Room Type")
        room_revenue = (
            filtered.groupby("ROOM_TYPE")["TOTAL_AMOUNT"]
            .sum()
            .reset_index(name="revenue")
        )
        st.bar_chart(room_revenue, x="ROOM_TYPE", y="revenue")

# Second charts row
col3, col4 = st.columns(2)

with col3:
    with st.container(border=True):
        st.subheader("Booking Status Distribution")
        status_counts = (
            filtered.groupby("BOOKING_STATUS").size().reset_index(name="count")
        )
        st.bar_chart(status_counts, x="BOOKING_STATUS", y="count")

with col4:
    with st.container(border=True):
        st.subheader("Bookings Over Time")
        if "CHECK_IN_DATE" in filtered.columns:
            time_data = filtered.copy()
            time_data["CHECK_IN_DATE"] = time_data["CHECK_IN_DATE"].astype(str)
            time_data = (
                time_data.groupby("CHECK_IN_DATE").size().reset_index(name="count")
            )
            time_data = time_data.sort_values("CHECK_IN_DATE")
            st.line_chart(time_data, x="CHECK_IN_DATE", y="count")

# Data table
with st.container(border=True):
    st.subheader("Booking Details")
    st.dataframe(filtered, hide_index=True, use_container_width=True)
