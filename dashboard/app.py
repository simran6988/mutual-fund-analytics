from utils.database import run_query
from utils.queries import KPI_QUERY, HOME_INSIGHT_QUERY
from utils.charts import top_fund_house_chart
import streamlit as st

kpi = run_query(KPI_QUERY)
best_fund = run_query(HOME_INSIGHT_QUERY)

fund_houses = int(kpi.loc[0, "fund_houses"])
schemes = int(kpi.loc[0, "schemes"])
investors = int(kpi.loc[0, "investors"])
sip = int(kpi.loc[0, "sip_inflow"])

st.set_page_config(
    page_title="Mutual Fund Analytics",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>

.main > div{
    padding-top:20px;
}

.block-container{
    padding-top:2rem;
    padding-bottom:2rem;
}

div[data-testid="metric-container"]{
    background:#F8FAFC;
    border:1px solid #E5E7EB;
    border-radius:12px;
    padding:18px;
    box-shadow:0 2px 6px rgba(0,0,0,0.08);
}

h1{
    color:#1F3A8A;
}

</style>
""", unsafe_allow_html=True)

st.title("📊 Mutual Fund Analytics Dashboard")

st.caption("Interactive dashboard for Mutual Fund performance and investor analytics.")

st.sidebar.title("📊 Dashboard Menu")

st.sidebar.markdown("---")

st.sidebar.subheader("Project")

st.sidebar.write("Mutual Fund Analytics")

st.sidebar.markdown("---")

st.sidebar.subheader("Datasets")

st.sidebar.write("• Fund Performance")

st.sidebar.write("• Investor Transactions")

st.sidebar.write("• SIP Analysis")

st.sidebar.write("• Portfolio Holdings")

st.sidebar.markdown("---")

st.sidebar.subheader("Database")

st.sidebar.success("SQLite Connected")

st.sidebar.markdown("---")

st.sidebar.caption("Developed using Python, SQLite, Plotly and Streamlit")
st.markdown("""
<style>

div[data-testid="metric-container"] {
    background-color: white;
    border: 1px solid #dddddd;
    padding: 18px;
    border-radius: 12px;
    box-shadow: 2px 2px 8px rgba(0,0,0,0.08);
}

div[data-testid="metric-container"] label {
    font-size:16px;
}

div[data-testid="metric-container"] div {
    font-size:28px;
    font-weight:bold;
}

</style>
""", unsafe_allow_html=True)

st.divider()

st.info("🚀 Dashboard development is in progress.")

col1, col2, col3, col4 = st.columns(4)

col1.metric("🏦 Fund Houses", f"{fund_houses:,}")
col2.metric("📑 Schemes", f"{schemes:,}")
col3.metric("👥 Investors", f"{investors:,}")
col4.metric("💰 SIP Inflow", f"{sip:,} Cr")

st.divider()

left, right = st.columns([2, 1])

with left:
    st.subheader("Top Fund Houses by AUM")

    st.plotly_chart(
        top_fund_house_chart(),
        use_container_width=True
    )

with right:
    st.subheader("Quick Insights")

    st.success("🏆 Best Performing Scheme (5 Years)")

    st.write(best_fund.loc[0, "scheme_name"])

    st.metric(
        "5-Year Return",
        f"{best_fund.loc[0, 'return_5yr_pct']}%"
    )

st.divider()

st.subheader("Dashboard Modules")

col1, col2 = st.columns(2)

with col1:

    st.info(
        """
### 📈 Fund Analysis

- Top performing schemes
- Fund house comparison
- Expense ratio analysis
- Risk vs Return
"""
    )

    st.info(
        """
### 👥 Investor Analysis

- State-wise investment
- Payment mode analysis
- Investor trends
"""
    )

with col2:

    st.info(
        """
### 💰 SIP Analysis

- Monthly SIP inflow
- Category-wise inflow
- Industry trends
"""
    )

    st.info(
        """
### 🔍 Fund Explorer

- Search any scheme
- View detailed metrics
- Compare fund performance
"""
    )

st.divider()

st.success(
    "Use the navigation menu on the left to explore each analytics module."
)