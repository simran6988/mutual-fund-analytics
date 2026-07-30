import plotly.express as px

from utils.database import run_query


def top_fund_house_chart():

    query = """
    SELECT
        fund_house,
        SUM(aum_crore) AS total_aum
    FROM "03_aum_by_fund_house"
    GROUP BY fund_house
    ORDER BY total_aum DESC
    LIMIT 10
    """

    df = run_query(query)

    fig = px.bar(
        df,
        x="fund_house",
        y="total_aum",
        color="total_aum",
        text="total_aum",
        title="Top 10 Fund Houses by AUM"
    )

    fig.update_layout(
    xaxis_title="Fund House",
    yaxis_title="AUM (Crore)",
    template="plotly_white",
    height=450,
    showlegend=False,
    coloraxis_showscale=False,
    xaxis_tickangle=-30,
    margin=dict(t=70, l=40, r=20, b=60)
)

    fig.update_traces(
    texttemplate="%{y:,.0f}",
    textposition="outside"
)

    return fig