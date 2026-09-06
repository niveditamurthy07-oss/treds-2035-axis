import streamlit as st
import numpy as np
import pandas as pd

try:
    import plotly.graph_objects as go
    PLOTLY_OK = True
except Exception:
    PLOTLY_OK = False

st.set_page_config(
    page_title="TReDS 2035 | Axis Bank",
    page_icon="◈",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ---------------------------------------------------------
# Theme / CSS — Axis Bank Red & White
# ---------------------------------------------------------
st.markdown("""
<style>
:root {
    --maroon: #5C0C30;
    --red: #97144D;
    --bright-red: #D71920;
    --red-light: #FBEAF0;
    --white: #FFFFFF;
    --bg: #FDFAFA;
    --text: #2B0714;
    --muted: #7A5464;
    --border: #ECD3DB;
}

html, body, [class*="css"], .stApp, .stMarkdown, p, div, span,
h1, h2, h3, h4, label, input, textarea, select, button {
    font-family: "Times New Roman", Times, Georgia, serif !important;
}

html { font-size: 18px; }

.stApp {
    background-color: var(--bg);
    background-image: radial-gradient(circle at 100% 0%, rgba(151,20,77,0.05), transparent 40%);
    color: var(--text);
}

.block-container {
    max-width: 1400px;
    padding: 26px 40px 46px 40px;
}

[data-testid="stHeader"] { background: transparent; }
[data-testid="stToolbar"] { visibility: hidden; height: 0; }

.hero {
    background: var(--maroon);
    color: white;
    border-radius: 12px;
    padding: 34px 40px;
    margin-bottom: 16px;
    box-shadow: 0 10px 26px rgba(92,12,48,.28);
    border-left: 8px solid var(--bright-red);
}

.hero .eyebrow {
    font-size: 13px;
    letter-spacing: 3px;
    font-weight: 700;
    opacity: .82;
}

.hero h1 {
    font-size: 54px;
    line-height: 1.05;
    margin: 10px 0 8px;
    font-weight: 700;
    letter-spacing: -.5px;
}

.hero p {
    margin: 0;
    opacity: .92;
    font-size: 20px;
}

.demo-note {
    color: var(--muted);
    font-size: 14px;
    margin: 10px 0 20px 2px;
    font-style: italic;
}

.stat-strip {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 14px;
    margin: 0 0 20px;
}

.stat-box {
    background: var(--white);
    border: 1px solid var(--border);
    border-left: 4px solid var(--red);
    border-radius: 8px;
    padding: 16px 18px;
    text-align: center;
}

.stat-box .n {
    font-size: 28px;
    font-weight: 700;
    color: var(--red);
}

.stat-box .l {
    font-size: 13px;
    color: var(--muted);
    letter-spacing: .4px;
    margin-top: 4px;
}

.section {
    font-size: 28px;
    font-weight: 700;
    margin: 30px 0 14px;
    color: var(--maroon);
    letter-spacing: -.2px;
    border-left: 5px solid var(--bright-red);
    padding-left: 14px;
}

.section-sub {
    color: var(--muted);
    font-size: 16px;
    margin: -8px 0 16px 2px;
}

.card, .signal, .bank, .kpi-card {
    background: #fff;
    border: 1px solid var(--border);
    border-radius: 10px;
}

.card {
    padding: 20px 22px;
    min-height: 128px;
}

.signal {
    padding: 18px 20px;
    min-height: 130px;
    border-left: 4px solid var(--red);
}

.bank {
    padding: 24px;
    min-height: 275px;
}

.bank.best {
    border: 2px solid var(--bright-red);
    box-shadow: 0 8px 22px rgba(215,25,32,.16);
}

.kpi-card {
    padding: 20px 22px;
    min-height: 118px;
}

.label {
    font-size: 13px;
    color: var(--muted);
    text-transform: uppercase;
    letter-spacing: 1px;
    font-weight: 700;
}

.value {
    font-size: 27px;
    line-height: 1.2;
    font-weight: 700;
    margin-top: 8px;
    color: var(--text);
}

.muted {
    color: var(--muted);
    font-size: 15px;
    line-height: 1.5;
}

.tag {
    display: inline-block;
    border-radius: 5px;
    padding: 5px 11px;
    font-size: 12.5px;
    font-weight: 700;
    letter-spacing: .4px;
    background: var(--red-light);
    color: var(--red);
    text-transform: uppercase;
}

.tag.strong {
    background: var(--bright-red);
    color: white;
}

.big {
    font-size: 38px;
    line-height: 1;
    font-weight: 700;
    color: var(--bright-red);
    margin: 16px 0 8px;
}

.ai {
    background: var(--red-light);
    border: 1px solid var(--border);
    border-left: 4px solid var(--bright-red);
    border-radius: 10px;
    padding: 22px 26px;
    margin-top: 14px;
}

.ai h3 {
    color: var(--maroon);
    margin: 10px 0 10px;
    font-size: 27px;
}

.ai p {
    color: #6E4655;
    margin: 0 0 12px;
    font-size: 17px;
    line-height: 1.6;
}

.finale {
    background: var(--maroon);
    color: white;
    border-radius: 12px;
    padding: 34px 40px;
    text-align: center;
    margin-top: 16px;
    border-left: 8px solid var(--bright-red);
}

.finale h2 {
    font-size: 32px;
    margin: 0 0 10px;
    font-weight: 700;
}

.finale p {
    font-size: 18px;
    opacity: .92;
    margin: 0;
}

.signal-chip {
    display: inline-block;
    background: white;
    border: 1px solid var(--border);
    border-radius: 6px;
    padding: 9px 14px;
    margin: 4px 6px 4px 0;
    font-size: 15px;
    color: var(--text);
}

.bar-row {
    display: flex;
    align-items: center;
    margin: 10px 0;
}

.bar-label {
    width: 270px;
    font-size: 15px;
    color: var(--text);
    font-weight: 600;
}

.bar-wrap {
    flex: 1;
    background: var(--red-light);
    border-radius: 5px;
    height: 15px;
    overflow: hidden;
    margin: 0 12px;
}

.bar-fill {
    height: 100%;
    background: var(--red);
    border-radius: 5px;
}

.bar-fill.alt {
    background: var(--bright-red);
}

.bar-pct {
    width: 46px;
    font-size: 14px;
    color: var(--muted);
    font-weight: 700;
    text-align: right;
}

.gauge-wrap {
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
    padding: 6px 0 4px;
}

.gauge {
    width: 176px;
    height: 176px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
}

.gauge .inner {
    width: 132px;
    height: 132px;
    border-radius: 50%;
    background: white;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
    box-shadow: inset 0 0 0 1px var(--border);
}

.gauge .inner .pct {
    font-size: 32px;
    font-weight: 700;
    color: var(--red);
}

.gauge .inner .sub {
    font-size: 12px;
    color: var(--muted);
    letter-spacing: .4px;
    text-align: center;
}

.gauge-caption {
    color: var(--muted);
    font-size: 13.5px;
    text-align: center;
    margin-top: 12px;
    line-height: 1.5;
}

.chart-caption {
    color: var(--muted);
    font-size: 15px;
    font-style: italic;
    margin-top: 8px;
}

.footer {
    color: var(--muted);
    font-size: 13px;
    text-align: center;
    margin-top: 32px;
}

div[data-testid="stMetric"] {
    background: white;
    border: 1px solid var(--border);
    border-left: 4px solid var(--red);
    padding: 18px 20px;
    border-radius: 10px;
    min-height: 112px;
}

/* ---------------------------------
   METRIC CARDS
   Chrome-safe typography
--------------------------------- */

div[data-testid="stMetric"] {
    background: white !important;
    border: 1px solid var(--border) !important;
    border-left: 4px solid var(--red) !important;
    padding: 18px 20px !important;
    border-radius: 10px !important;
    min-height: 112px !important;
}

/* Metric label */
div[data-testid="stMetricLabel"],
div[data-testid="stMetricLabel"] p,
div[data-testid="stMetricLabel"] span,
div[data-testid="stMetricLabel"] div {
    color: #6E4655 !important;
    font-size: 16px !important;
    font-weight: 600 !important;
    opacity: 1 !important;
}

/* Metric value */
div[data-testid="stMetricValue"],
div[data-testid="stMetricValue"] div,
div[data-testid="stMetricValue"] span {
    color: #2B0714 !important;
    font-size: 30px !important;
    font-weight: 500 !important;
    opacity: 1 !important;

}

input[type="radio"] { accent-color: var(--red) !important; }

section[data-testid="stSidebar"] { background: #FFF3F6; }

.stSelectbox label {
    font-size: 16px !important;
    color: var(--maroon) !important;
    font-weight: 700 !important;
}

@media (max-width: 900px) {
    .block-container { padding: 20px 18px 30px; }
    .hero h1 { font-size: 38px; }
    .section { font-size: 22px; }
    .stat-strip { grid-template-columns: repeat(2, 1fr); }
}
.outcome-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 24px;
    width: 100%;
    margin: 8px 0 24px 0;
}

.outcome-card {
    background: #FFFFFF !important;
    border: 1px solid #ECD3DB !important;
    border-left: 5px solid #97144D !important;
    border-radius: 10px;
    padding: 26px 24px;
    min-height: 112px;
    box-sizing: border-box;
}

.outcome-label {
    color: #6E4655 !important;
    font-family: "Times New Roman", Times, Georgia, serif !important;
    font-size: 16px !important;
    font-weight: 600 !important;
    line-height: 1.3 !important;
    opacity: 1 !important;
    margin: 0 0 12px 0 !important;
}

.outcome-value {
    color: #2B0714 !important;
    font-family: "Times New Roman", Times, Georgia, serif !important;
    font-size: 31px !important;
    font-weight: 500 !important;
    line-height: 1.15 !important;
    opacity: 1 !important;
    margin: 0 !important;
}

@media (max-width: 900px) {
    .outcome-grid {
        grid-template-columns: 1fr;
    }
}
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# Scenario
# ---------------------------------------------------------
scenario = st.session_state.get("scenario", "Base Case")

_, control_b = st.columns([3.2, 1.2])
with control_b:
    scenario = st.selectbox(
        "Scenario",
        ["Base Case", "Healthy Liquidity", "High Risk"],
        index=["Base Case", "Healthy Liquidity", "High Risk"].index(scenario),
    )

st.session_state["scenario"] = scenario

if scenario == "Healthy Liquidity":
    score, need, delay, risk, confidence = 34, 2.5, 3, "Low", 88
    cash_end_no_fin, cash_end_fin = 16.0, 18.7
elif scenario == "High Risk":
    score, need, delay, risk, confidence = 87, 11.5, 19, "High", 94
    cash_end_no_fin, cash_end_fin = 9.0, 21.1
else:
    score, need, delay, risk, confidence = 78, 7.5, 10, "Low–Medium", 91
    cash_end_no_fin, cash_end_fin = 12.0, 20.0

scenario_weights = {
    "Base Case": [("Cost fit", 40), ("Risk fit", 25), ("Speed", 20), ("Supplier preference", 15)],
    "Healthy Liquidity": [("Cost fit", 45), ("Risk fit", 20), ("Speed", 15), ("Supplier preference", 20)],
    "High Risk": [("Speed", 40), ("Cost fit", 20), ("Risk fit", 20), ("Supplier preference", 20)],
}

scenario_bids = {
    "Base Case": [
        ("Bank A", "8.70%", "28 min", 88, "Cost + speed"),
        ("Bank B", "8.50%", "41 min", 92, "Best overall"),
        ("Bank C", "8.90%", "18 min", 84, "Fastest"),
    ],
    "Healthy Liquidity": [
        ("Bank A", "8.60%", "30 min", 90, "Cost efficient"),
        ("Bank B", "8.45%", "44 min", 93, "Best overall"),
        ("Bank C", "8.85%", "17 min", 82, "Fastest"),
    ],
    "High Risk": [
        ("Bank A", "8.75%", "30 min", 80, "Cost + speed"),
        ("Bank B", "8.55%", "40 min", 85, "Balanced"),
        ("Bank C", "8.95%", "16 min", 91, "Fastest execution"),
    ],
}

recommended_bank = {
    "Base Case": "Bank B",
    "Healthy Liquidity": "Bank B",
    "High Risk": "Bank C",
}

recommendation_text = {
    "Base Case": "Bank B is the strongest overall fit when cost, execution speed, risk fit and supplier preference are considered together.",
    "Healthy Liquidity": "Because liquidity pressure is low, the recommendation gives more weight to financing cost while maintaining acceptable risk fit.",
    "High Risk": "When liquidity pressure is high, faster execution becomes more important, making Bank C the strongest fit despite its higher rate.",
}

# ---------------------------------------------------------
# Header
# ---------------------------------------------------------
st.markdown("""
<div class="hero">
  <div class="eyebrow">AXIS BANK MOVES 2026 &nbsp;·&nbsp; WORKING-CAPITAL INTELLIGENCE ENGINE</div>
  <h1>TReDS 2035</h1>
  <p>From Invoice Discounting to Working Capital Intelligence</p>
</div>
<div class="demo-note">
LIVE PROTOTYPE · Fictional MSME scenario · Illustrative AI simulation, not a real Axis Bank product
</div>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# Top KPIs — make the meanings explicit
# ---------------------------------------------------------
best_bank = recommended_bank[scenario]
best_score = next(ai for name, rate, tm, ai, why in scenario_bids[scenario] if name == best_bank)

st.markdown(f"""
<div class="stat-strip">
  <div class="stat-box"><div class="n">4</div><div class="l">DATA SIGNALS</div></div>
  <div class="stat-box"><div class="n">₹{need}L</div><div class="l">PREDICTED FUNDING NEED</div></div>
  <div class="stat-box"><div class="n">{confidence}%</div><div class="l">AI PREDICTION CONFIDENCE</div></div>
  <div class="stat-box"><div class="n">{best_score}/100</div><div class="l">RECOMMENDED BANK FIT</div></div>
</div>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# 01 MSME Context
# ---------------------------------------------------------
st.markdown('<div class="section">01 · MSME Context</div>', unsafe_allow_html=True)

row1 = st.columns(3)
row2 = st.columns(3)

items = [
    ("SUPPLIER", "ABC Components Pvt. Ltd.", "Registered MSME supplier"),
    ("INDUSTRY", "Auto Components", "Tier-2 automotive supply chain"),
    ("BUYER", "Apex Motors Ltd.", "Corporate anchor buyer"),
    ("MONTHLY SALES", "₹42L", "ERP-reported average"),
    ("RECEIVABLES", "₹18L", "Cash conversion slowing"),
    ("CREDIT VINTAGE", "6.5 yrs", "TReDS + banking history"),
]

for c, (a, b, d) in zip(row1 + row2, items):
    with c:
        st.markdown(
            f'<div class="card"><div class="label">{a}</div>'
            f'<div class="value">{b}</div><div class="muted">{d}</div></div>',
            unsafe_allow_html=True,
        )

# ---------------------------------------------------------
# 02 AI Working Capital Intelligence — deliberately simple
# ---------------------------------------------------------
st.markdown('<div class="section">02 · AI Working Capital Intelligence</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="section-sub">Three simple steps: read the signals → predict the cash gap → recommend an action.</div>',
    unsafe_allow_html=True
)

ai_cols = st.columns(3, gap="medium")
ai_steps = [
    ("01 · READ", "Combine business signals",
     "ERP sales, GST activity, banking cash flows and TReDS invoice history."),
    ("02 · PREDICT", f"Flag a ₹{need}L cash gap",
     "Detect weakening receivables, buyer delays and upcoming obligations."),
    ("03 · ACT", f"Prepare financing with {best_bank}",
     "Match the predicted requirement to the best available financing option."),
]

for c, (tag, title, desc) in zip(ai_cols, ai_steps):
    with c:
        st.markdown(
            f'<div class="signal"><span class="tag">{tag}</span>'
            f'<div style="font-size:21px;font-weight:700;color:#5C0C30;margin-top:12px">{title}</div>'
            f'<div class="muted" style="margin-top:8px">{desc}</div></div>',
            unsafe_allow_html=True,
        )

chips = [
    "↓ Cash balance 22%",
    "↑ Receivable days 11",
    "⚠ Buyer delay risk",
    f"₹{need}L obligations",
    "✓ GST consistency",
]
st.markdown(
    "<div style='margin:16px 0 10px'>" +
    "".join(f'<span class="signal-chip">{x}</span>' for x in chips) +
    "</div>",
    unsafe_allow_html=True
)

a, b, c, d = st.columns(4, gap="medium")
with a:
    st.metric("Liquidity Stress", f"{score}/100")
with b:
    st.metric("Predicted Funding Need", f"₹{need}L")
with c:
    st.metric("Expected Buyer Delay", f"{delay} days")
with d:
    st.metric("Supplier Risk", risk)

st.markdown(f"""
<div class="ai">
  <span class="tag strong">AI SIGNAL</span>
  <h3>Potential liquidity requirement: ₹{need}L</h3>
  <p>The simulation detects a potential working-capital gap early enough for the bank to prepare a financing response before the MSME makes an urgent request.</p>
  <b>Action:</b> prepare eligible invoices and financing options proactively.
</div>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# 03 Cash-flow impact
# ---------------------------------------------------------
st.markdown('<div class="section">03 · Cash-Flow Impact</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="section-sub">What happens to the MSME’s projected cash balance if the identified funding gap is addressed early?</div>',
    unsafe_allow_html=True
)

chart_col, gauge_col = st.columns([2.7, 1], gap="large")

# Deterministic illustrative forecast — no random noise
weeks = [f"Wk {i}" for i in range(1, 13)]
without_fin = np.linspace(18.0, cash_end_no_fin, 12)

# Financing is introduced at the point where the gap is identified.
alert_idx = 3
with_fin = without_fin.copy()
with_fin[alert_idx:] = np.linspace(
    without_fin[alert_idx] + need,
    cash_end_fin,
    12 - alert_idx
)

with chart_col:
    if PLOTLY_OK:
        fig = go.Figure()

        fig.add_trace(go.Scatter(
            x=weeks,
            y=without_fin,
            mode="lines+markers",
            name="Without proactive financing",
            line=dict(color="#97144D", width=3, dash="dot"),
            marker=dict(size=6),
        ))

        fig.add_trace(go.Scatter(
            x=weeks,
            y=with_fin,
            mode="lines+markers",
            name=f"After ₹{need}L funding",
            line=dict(color="#D71920", width=4),
            marker=dict(size=6),
        ))

        fig.add_vline(
            x=weeks[alert_idx],
            line_width=1.5,
            line_dash="dash",
            line_color="#D71920",
            annotation_text="Funding triggered",
            annotation_position="top",
            annotation_font=dict(color="#D71920", size=13),
        )

        fig.update_layout(
            height=410,
            margin=dict(l=10, r=10, t=40, b=10),
            paper_bgcolor="white",
            plot_bgcolor="white",
            font=dict(family="Times New Roman, Times, serif", size=15, color="#2B0714"),
            legend=dict(orientation="h", yanchor="bottom", y=1.06, x=0),
            xaxis=dict(gridcolor="#ECD3DB", title="Forecast period"),
            yaxis=dict(gridcolor="#ECD3DB", title="Projected Cash Balance (₹L)"),
        )
        st.plotly_chart(fig, use_container_width=True)
    else:
        chart_df = pd.DataFrame(
            {"Without financing": without_fin, "After financing": with_fin},
            index=weeks
        )
        st.line_chart(chart_df)

    st.markdown(
        '<div class="chart-caption">Illustrative scenario: the financing intervention is shown at the point where the AI flags the projected liquidity gap.</div>',
        unsafe_allow_html=True
    )

with gauge_col:
    deg = int(confidence / 100 * 360)
    st.markdown(
        f'<div class="gauge-wrap">'
        f'<div class="gauge" style="background: conic-gradient(#D71920 {deg}deg, #FBEAF0 0deg);">'
        f'<div class="inner"><div class="pct">{confidence}%</div>'
        f'<div class="sub">AI PREDICTION<br>CONFIDENCE</div></div></div>'
        f'<div class="gauge-caption">Confidence in the simulated prediction that a funding requirement will emerge within the forecast window.</div>'
        f'</div>',
        unsafe_allow_html=True
    )

# ---------------------------------------------------------
# 04 Financing Marketplace
# ---------------------------------------------------------
st.markdown('<div class="section">04 · Dynamic Financing Marketplace</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="section-sub">The recommendation is based on fit — not simply the lowest interest rate.</div>',
    unsafe_allow_html=True
)

bankcols = st.columns(3, gap="medium")

for c, (name, rate, tm, ai, why) in zip(bankcols, scenario_bids[scenario]):
    with c:
        cls = "bank best" if name == best_bank else "bank"
        badge = (
            '<span class="tag strong">★ AI RECOMMENDED</span>'
            if name == best_bank
            else '<span class="tag">INDICATIVE BID</span>'
        )

        st.markdown(
            f'<div class="{cls}">{badge}'
            f'<h3 style="margin:14px 0 0;color:#2B0714;font-size:22px">{name}</h3>'
            f'<div class="big">{rate}</div>'
            f'<div class="muted">Indicative financing rate</div>'
            f'<div style="height:1px;background:#ECD3DB;margin:18px 0"></div>'
            f'<div style="font-size:16px;line-height:1.9">'
            f'<b>Funding time:</b> {tm}<br>'
            f'<b>Bank fit score:</b> {ai}/100</div>'
            f'<div class="muted" style="margin-top:14px">{why}</div></div>',
            unsafe_allow_html=True,
        )

st.markdown("<div style='height:8px'></div>", unsafe_allow_html=True)

wcol, bcol = st.columns([1.6, 1], gap="large")

with wcol:
    st.markdown(
        '<div class="muted" style="margin-bottom:6px">'
        '<b style="color:#5C0C30">Illustrative decision weights</b></div>',
        unsafe_allow_html=True
    )

    w_html = "".join(
        f'<div class="bar-row"><div class="bar-label">{name}</div>'
        f'<div class="bar-wrap"><div class="bar-fill" style="width:{pct}%"></div></div>'
        f'<div class="bar-pct">{pct}%</div></div>'
        for name, pct in scenario_weights[scenario]
    )
    st.markdown(w_html, unsafe_allow_html=True)

with bcol:
    st.markdown(
        f'<div class="card" style="text-align:center;border:2px solid var(--bright-red);min-height:auto;padding:18px">'
        f'<div class="label">{best_bank}</div>'
        f'<div class="big" style="margin:8px 0">{best_score}/100</div>'
        f'<div class="tag strong">BEST OVERALL FIT</div></div>',
        unsafe_allow_html=True,
    )

st.markdown(f"""
<div class="ai">
  <b style="font-size:19px">AI Recommendation: {best_bank}</b><br>
  <span class="muted">{recommendation_text[scenario]}</span>
  <br><br>
  <b>Prediction confidence:</b> {confidence}%
</div>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# 05 Funding Outcome
# ---------------------------------------------------------
st.markdown('<div class="section">05 · Funding Outcome</div>', unsafe_allow_html=True)

st.markdown(f"""
<div class="outcome-grid">

    <div class="outcome-card">
        <div class="outcome-label">FUNDING OPPORTUNITY</div>
        <div class="outcome-value">₹{need}L</div>
    </div>

    <div class="outcome-card">
        <div class="outcome-label">TIME-TO-BID</div>
        <div class="outcome-value">&lt;30 min</div>
    </div>

    <div class="outcome-card">
        <div class="outcome-label">RISK MONITORING</div>
        <div class="outcome-value">Continuous</div>
    </div>

</div>
""", unsafe_allow_html=True)

st.markdown(f"""
<div class="finale">
  <h2>₹{need}L PROACTIVE FUNDING OPPORTUNITY IDENTIFIED</h2>
  <p>The bank moves from reacting to a funding request to anticipating a working-capital need.</p>
</div>
""", unsafe_allow_html=True)

st.markdown(
    '<div class="footer">'
    'Prototype for Axis Bank Moves 2026 · Fictional data · Indicative financing bids · '
    'Illustrative AI simulation, not a production model · Actual implementation subject to '
    'technology, consent, credit policy and regulatory approvals.'
    '</div>',
    unsafe_allow_html=True
)
