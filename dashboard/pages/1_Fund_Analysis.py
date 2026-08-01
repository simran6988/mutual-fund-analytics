import streamlit as st

from utils.database import run_query
from utils.charts import top_fund_house_chart
from utils.queries import TOP_FUNDS_QUERY


st.set_page_config(page_title="Fund Analysis", layout="wide")

st.title("📈 Fund Analysis")

st.caption("Performance analysis of mutual fund schemes.")

st.divider()

left, right = st.columns([2, 1])

with left:
    st.plotly_chart(
        top_fund_house_chart(),
        use_container_width=True
    )

with right:
    st.subheader("Top Performing Funds")

    top_funds = run_query(TOP_FUNDS_QUERY)

    st.dataframe(
        top_funds,
        use_container_width=True,
        hide_index=True
    )