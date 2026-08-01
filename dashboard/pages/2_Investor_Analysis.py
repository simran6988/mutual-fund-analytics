import streamlit as st

from utils.database import run_query
from utils.queries import TOP_STATES_QUERY, PAYMENT_MODE_QUERY


st.set_page_config(page_title="Investor Analysis", layout="wide")

st.title("👥 Investor Analysis")

st.caption("Investment distribution and investor behavior.")

st.divider()

left, right = st.columns(2)

with left:
    st.subheader("Top States by Investment")

    states = run_query(TOP_STATES_QUERY)

    st.bar_chart(
        states,
        x="state",
        y="investment_crore",
        use_container_width=True,
    )

with right:
    st.subheader("Payment Mode Distribution")

    payment = run_query(PAYMENT_MODE_QUERY)

    st.dataframe(
        payment,
        use_container_width=True,
        hide_index=True,
    )