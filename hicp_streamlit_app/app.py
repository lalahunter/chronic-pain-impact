from pathlib import Path
import base64
import html
import textwrap
import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="It's All in Your Head · HICP",
    layout="wide",
    initial_sidebar_state="collapsed",
)

BASE = Path(__file__).resolve().parent
ASSETS = BASE / "assets"
TOTAL_SCENES = 13

# -----------------------------
# State
# -----------------------------
if "scene" not in st.session_state:
    st.session_state.scene = 1
if "reveal" not in st.session_state:
    st.session_state.reveal = 0

REVEAL_MAX = {7: 4, 8: 2, 9: 3, 10: 3, 11: 2}


def go_next():
    s = st.session_state.scene
    max_r = REVEAL_MAX.get(s, 0)
    if st.session_state.reveal < max_r:
        st.session_state.reveal += 1
    elif s < TOTAL_SCENES:
        st.session_state.scene += 1
        st.session_state.reveal = 0


def go_back():
    s = st.session_state.scene
    if st.session_state.reveal > 0:
        st.session_state.reveal -= 1
    elif s > 1:
        st.session_state.scene -= 1
        st.session_state.reveal = REVEAL_MAX.get(st.session_state.scene, 0)


@st.cache_data(show_spinner=False)
def img_uri(filename: str) -> str:
    p = ASSETS / filename
    data = base64.b64encode(p.read_bytes()).decode("ascii")
    return f"data:image/png;base64,{data}"


def html_block(markup: str):
    """Render generated HTML without Markdown treating indented lines as code blocks."""
    cleaned = "\n".join(line.lstrip() for line in textwrap.dedent(markup).strip().splitlines())
    st.markdown(cleaned, unsafe_allow_html=True)


# -----------------------------
# Global CSS
# -----------------------------
st.markdown(
    """
<style>
:root {
    --bg: #0B0C0F;
    --ivory: #F1EEE8;
    --soft: #D5D1C9;
    --slate: #9BA3B0;
    --dim: #747C88;
    --gold: #C8AC7A;
    --violet: #8E88BE;
    --panel: #12161C;
    --panel2: #0F1217;
    --line: #30343C;
}
html, body, [data-testid="stAppViewContainer"], .stApp {
    background: var(--bg) !important;
    color: var(--ivory) !important;
}
[data-testid="stHeader"], [data-testid="stToolbar"], footer { display:none !important; }
#MainMenu {visibility:hidden;}
.block-container {
    padding: 0 !important;
    max-width: 100% !important;
}
[data-testid="stVerticalBlock"] { gap: 0 !important; }

.slide {
    min-height: calc(100vh - 56px);
    width: 100%;
    box-sizing: border-box;
    position: relative;
    overflow: hidden;
    background: var(--bg);
}
.slide-inner {
    width: min(1440px, 92vw);
    margin: 0 auto;
    padding: 3.2vh 0 7.5vh 0;
    box-sizing: border-box;
}
.bg-slide {
    min-height: calc(100vh - 56px);
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    position: relative;
}
.serif { font-family: Georgia, 'Times New Roman', serif; }
.sans { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Arial, sans-serif; }
.kicker {
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Arial, sans-serif;
    color: var(--slate); font-size: clamp(14px,1.05vw,19px);
    letter-spacing: .08em; text-transform: uppercase; font-weight: 600;
}
.title {
    font-family: Georgia, 'Times New Roman', serif;
    color: var(--ivory); font-size: clamp(40px, 4vw, 66px);
    line-height: 1.05; margin: .55rem 0 .45rem;
}
.subtitle {
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Arial, sans-serif;
    color: var(--soft); font-size: clamp(17px,1.35vw,23px); line-height:1.5;
}
.rule { border-top:1px solid var(--line); margin: 1.5rem 0; }
.gold { color: var(--gold); }
.violet { color: var(--violet); }
.muted { color: var(--slate); }
.fade-in { animation: fadein .55s ease both; }
.fade-in-slow { animation: fadein 1.1s ease both; }
@keyframes fadein { from {opacity:0; transform:translateY(5px);} to {opacity:1; transform:none;} }

/* Global presentation shell */
.shell-left, .shell-right {
    position:absolute; bottom:18px; z-index:30;
    font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Arial,sans-serif;
    color:var(--slate); font-size:13px; letter-spacing:.11em;
}
.shell-left { left:4.5vw; text-transform:uppercase; }
.shell-right { right:4.5vw; display:flex; align-items:center; gap:13px; }
.dots { display:flex; gap:7px; align-items:center; }
.dot { width:7px; height:7px; border-radius:50%; background:#484D57; display:inline-block; }
.dot.active { background:var(--gold); width:8px; height:8px; }
.page-num { letter-spacing:.04em; color:#AAB1BC; }

/* Navigation */
.nav-wrap { padding: 7px 0 8px; background:#0B0C0F; border-top:1px solid #1D2026; }
.nav-wrap div[data-testid="stHorizontalBlock"] { width:220px; margin:auto; }
.nav-wrap .stButton > button {
    min-height:38px; height:38px; width:100%;
    border:1px solid #343942 !important; border-radius:999px !important;
    background:#11141A !important; color:#D7D3CC !important;
    font-size:18px !important; padding:0 !important;
}
.nav-wrap .stButton > button:hover { border-color:#C8AC7A !important; color:#F1EEE8 !important; }

/* Analytical rows/cards */
.rq { font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Arial,sans-serif; font-weight:700;
      font-size:clamp(18px,1.5vw,25px); color:var(--ivory); line-height:1.35; margin-top:1.2rem; }
.model-row {
    display:grid; grid-template-columns: 145px 1fr 155px 150px;
    align-items:center; min-height:112px; border-top:1px solid var(--line);
    font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Arial,sans-serif;
    position:relative;
}
.model-row:last-of-type { border-bottom:1px solid var(--line); }
.model-label { color:var(--slate); font-size:15px; letter-spacing:.06em; font-weight:700; }
.model-name { color:var(--ivory); font-size:clamp(20px,1.65vw,28px); font-weight:700; }
.model-desc { color:var(--slate); font-size:clamp(15px,1.05vw,18px); margin-top:4px; }
.auc-label { color:var(--slate); font-size:14px; text-transform:uppercase; }
.auc { font-family:Georgia,'Times New Roman',serif; color:var(--ivory); font-size:clamp(36px,3vw,49px); }
.auc.gold { color: var(--gold) !important; }
.delta { color:var(--violet); font-size:clamp(17px,1.25vw,22px); font-weight:700; text-align:right; }
.delta.base { color:#747C88; font-weight:500; }
.model-track {
    position:absolute; left:145px; right:305px; bottom:13px;
    height:3px; background:#242830; overflow:hidden;
}
.model-fill { height:3px; }
.model-fill.context { background:linear-gradient(90deg, rgba(142,136,190,.92), rgba(200,172,122,.98)); }
.model-fill.goldbar { background:#C8AC7A; }
.model-fill.violetbar { background:#8E88BE; }
.takeaway {
    font-family:Georgia,'Times New Roman',serif; color:var(--ivory);
    font-size:clamp(30px,2.5vw,42px); line-height:1.25; margin-top:1.35rem;
}

.scene7 .model-row { min-height:128px; }
.scene7 .model-track { bottom:16px; }
.scene7 .takeaway { margin-top:1.6rem; }

.metric-grid { display:grid; grid-template-columns:repeat(4,1fr); gap:16px; margin-top:1rem; }
.metric-card { background:var(--panel); border:1px solid var(--line); border-radius:14px; padding:18px 20px; }
.metric-label { color:var(--slate); font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Arial,sans-serif; font-weight:700; font-size:18px; }
.metric-value { font-family:Georgia,'Times New Roman',serif; font-size:38px; color:var(--ivory); margin-top:5px; }
.metric-desc { color:var(--soft); font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Arial,sans-serif; font-size:16px; margin-top:5px; }

/* Streamlit expander / slider tuning */
[data-testid="stExpander"] { border-color:#30343C !important; background:#101319 !important; }
[data-testid="stExpander"] summary { color:#C9C5BD !important; font-size:15px !important; }
[data-testid="stSlider"] { padding-top:.2rem; }
[data-testid="stSlider"] [role="slider"] { background:var(--gold) !important; border-color:var(--gold) !important; }

/* Scene 9 */
.two-col { display:grid; grid-template-columns: 1.2fr .8fr; gap:5vw; align-items:start; }
.strategy { margin:18px 0; }
.strategy-head { display:grid; grid-template-columns:1fr auto auto; gap:12px; align-items:baseline; }
.strategy-name { color:var(--soft); font:600 clamp(17px,1.2vw,21px)/1.2 -apple-system,BlinkMacSystemFont,'Segoe UI',Arial,sans-serif; }
.strategy-pct { color:var(--ivory); font:clamp(24px,1.8vw,31px)/1 Georgia,'Times New Roman',serif; }
.strategy-n { color:var(--slate); font:15px/1.2 -apple-system,BlinkMacSystemFont,'Segoe UI',Arial,sans-serif; }
.bar-track { height:8px; background:#242830; margin-top:9px; }
.bar-fill { height:8px; }
.legend { display:flex; gap:9px; margin:12px 0 18px; }
.tag { padding:5px 11px; border-radius:8px; font:700 12px -apple-system,BlinkMacSystemFont,'Segoe UI',Arial,sans-serif; }
.hero65 { font-family:Georgia,'Times New Roman',serif; font-size:clamp(58px,5vw,82px); line-height:1; font-weight:400;
          background:linear-gradient(90deg,var(--violet),var(--gold)); -webkit-background-clip:text; color:transparent; }

/* Scene 10 */
.rq3-layout { display:grid; grid-template-columns:1fr 1fr; gap:38px; margin-top:1.2rem; align-items:start; }
.rq3-col { display:grid; gap:22px; align-content:start; }
.rq3-block { border-top:1px solid var(--line); padding-top:16px; }
.rq3-head { color:var(--slate); font:700 18px -apple-system,BlinkMacSystemFont,'Segoe UI',Arial,sans-serif; letter-spacing:.05em; }
.pp-gap { font-family:Georgia,'Times New Roman',serif; font-size:clamp(45px,3.8vw,65px); line-height:1.1; margin:8px 0 14px; }
.range-row { display:grid; grid-template-columns:132px 1fr 72px; gap:14px; align-items:center; margin:12px 0; }
.range-label,.range-val { color:var(--soft); font:17px -apple-system,BlinkMacSystemFont,'Segoe UI',Arial,sans-serif; }
.range-val { text-align:right; color:var(--ivory); font-family:Georgia,'Times New Roman',serif; font-size:20px; }
.range-track { height:9px; background:#242830; overflow:hidden; }
.range-fill { height:9px; }
.access-card,.key-card { background:var(--panel); border:1px solid var(--line); border-radius:14px; padding:20px 24px; }


/* Threshold scene: keep Streamlit slider aligned with the analytical canvas */
[data-testid="stSlider"] {
    width: min(1440px, 92vw) !important;
    margin: -2px auto 0 auto !important;
    padding: 0 !important;
}
[data-testid="stSlider"] > div { padding-top: 0 !important; }
.threshold-metrics { margin-top: 8px; }
.threshold-cm { margin-top: 10px; }
.threshold-cm .cm-cell { min-height: 88px; padding: 12px 16px; }
.threshold-cm .cm-val { font-size: 31px; }
.threshold-cm .cm-caption { font-size: 15px; }
.threshold-shell-left, .threshold-shell-right {
    position: fixed; bottom: 58px; z-index: 60;
    font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Arial,sans-serif;
    color:var(--slate); font-size:13px; letter-spacing:.11em;
    pointer-events:none;
}
.threshold-shell-left { left:4.5vw; text-transform:uppercase; }
.threshold-shell-right { right:4.5vw; display:flex; align-items:center; gap:13px; }

/* Confusion matrix */
.cm-wrap { margin-top:1rem; display:grid; grid-template-columns:170px 1fr 1fr; gap:10px; align-items:stretch; }
.cm-axis { display:flex; align-items:center; justify-content:center; color:var(--slate); font:700 17px -apple-system,BlinkMacSystemFont,'Segoe UI',Arial,sans-serif; text-align:center; }
.cm-cell { background:var(--panel2); border:1px solid var(--line); border-radius:13px; padding:15px 18px; min-height:105px; }
.cm-kicker { color:var(--slate); font:700 15px -apple-system,BlinkMacSystemFont,'Segoe UI',Arial,sans-serif; letter-spacing:.05em; }
.cm-val { color:var(--ivory); font:34px Georgia,'Times New Roman',serif; margin-top:5px; }
.cm-caption { color:var(--soft); font:16px -apple-system,BlinkMacSystemFont,'Segoe UI',Arial,sans-serif; margin-top:4px; }

@media (max-width: 1050px) {
  .model-row { grid-template-columns:120px 1fr 130px 100px; }
  .metric-grid { gap:9px; }
  .two-col { gap:3vw; }
  .rq3-layout { gap:24px; }
  .range-row { grid-template-columns:115px 1fr 66px; gap:10px; }
}
</style>
""",
    unsafe_allow_html=True,
)


def shell(scene: int, analytical: bool = False):
    if scene == 1 or scene == 13:
        return ""
    dots = "".join(
        f'<span class="dot {"active" if i == scene else ""}"></span>'
        for i in range(1, TOTAL_SCENES + 1)
    )
    left = '<div class="shell-left">HIGH-IMPACT CHRONIC PAIN</div>' if analytical else ""
    return f"{left}<div class='shell-right'><div class='dots'>{dots}</div><div class='page-num'>{scene} / {TOTAL_SCENES}</div></div>"


def static_bg(filename: str, scene: int, analytical=False, extra=""):
    uri = img_uri(filename)
    html_block(f"""
        <div class="slide bg-slide" style="background-image:url('{uri}');">
            {extra}
            {shell(scene, analytical)}
        </div>
    """)


# -----------------------------
# Scenes 1–6
# -----------------------------
def scene_1():
    uri = img_uri("scene01.png")
    html_block(f"""
        <div class="slide bg-slide" style="background-image:url('{uri}');">
          <div style="position:absolute;right:4.5vw;bottom:3.5vh;color:#B8B1A7;
                      font:14px Georgia,'Times New Roman',serif;letter-spacing:.035em;
                      opacity:0;animation:fadein 1s ease 1.2s forwards;">
            Lara Caçador · Data Analytics · Ironhack · 2026
          </div>
        </div>
        """)


def scene_2(): static_bg("scene02.png", 2)
def scene_3(): static_bg("scene03.png", 3)


def scene_4():
    # The artwork itself carries the copy; only the date label was changed to "17th century".
    static_bg("scene04.png", 4)


def scene_5(): static_bg("scene05.png", 5)
def scene_6(): static_bg("scene06.png", 6)


# -----------------------------
# Scene 7 — information ladder
# -----------------------------
FULL_METRICS_MODELS = pd.DataFrame(
    {
        "Metric": ["Accuracy","Balanced accuracy","Sensitivity","Specificity","Precision","F1","ROC-AUC"],
        "Model 0": [.698,.660,.531,.788,.573,.552,.694],
        "Model A": [.713,.656,.469,.844,.617,.533,.746],
        "Model B": [.718,.667,.497,.837,.621,.552,.761],
    }
)


def scene_7():
    r = st.session_state.reveal
    rows = []
    if r >= 1:
        rows.append(("MODEL 0", "Pain intensity only", "1 feature", "0.694", "baseline"))
    if r >= 2:
        rows.append(("MODEL A", "+ age · sex · pain location", "9 features total · 6 pain-location variables", "0.746", "+0.052"))
    if r >= 3:
        rows.append(("MODEL B", "+ biopsychosocial context", "17 features total · +8 biopsychosocial variables", "0.761", "+0.015"))
    rows_html = ""
    for label,name,desc,auc,delta in rows:
        width = float(auc) * 100
        delta_cls = "delta base" if delta == "baseline" else "delta"
        rows_html += f"""
        <div class="model-row fade-in">
          <div class="model-label">{label}</div>
          <div><div class="model-name">{name}</div><div class="model-desc">{desc}</div></div>
          <div><div class="auc-label">ROC-AUC</div><div class="auc gold">{auc}</div></div>
          <div class="{delta_cls}">{delta}</div>
          <div class="model-track"><div class="model-fill context" style="width:{width:.1f}%"></div></div>
        </div>"""
    takeaway = "" if r < 4 else "<div class='takeaway fade-in'>Adding more information <span class='gold' style='font-style:italic;'>improved discrimination.</span></div>"
    html_block(f"""
        <div class="slide scene7"><div class="slide-inner">
          <div class="kicker">RQ1 · SAME COHORT. SAME SPLIT. MORE INFORMATION.</div>
          <div class="title">What does the model know?</div>
          <div class="rq">Among adults with chronic pain, what distinguishes HICP, and is pain intensity alone enough?</div>
          <div style="margin-top:20px;">{rows_html}</div>
          {takeaway}
          <div class="sans muted" style="font-size:15px;margin-top:16px;">Logistic Regression · same 5,465 respondents · same stratified 80/20 split · held-out test set</div>
          <div class="sans muted" style="font-size:14px;margin-top:6px;">AUC changes are descriptive; differences were not formally tested.</div>
        </div>{shell(7, True)}</div>
        """)
    if r >= 3:
        with st.expander("Model details"):
            st.dataframe(FULL_METRICS_MODELS.style.format(precision=3), use_container_width=True, hide_index=True)


# -----------------------------
# Scene 8 — algorithms
# -----------------------------
ALGO_METRICS = pd.DataFrame(
    {
        "Metric": ["Accuracy","Balanced accuracy","Sensitivity","Specificity","Precision","F1","ROC-AUC"],
        "Logistic Regression": [.718,.667,.497,.837,.621,.552,.761],
        "Random Forest": [.718,.666,.492,.840,.623,.550,.750],
        "Gradient Boosting": [.727,.681,.529,.834,.631,.575,.758],
        "XGBoost": [.686,.645,.508,.782,.556,.531,.719],
    }
)


def algo_row(name, auc, delta, reference=False):
    label = "MODEL B · LR" if reference else "ALTERNATIVE"
    width = float(auc) * 100
    bar_cls = "goldbar" if reference else "violetbar"
    delta_cls = "delta base" if reference else "delta"
    auc_cls = "auc gold" if reference else "auc"
    return f"""
      <div class="model-row fade-in">
        <div class="model-label">{label}</div>
        <div><div class="model-name">{name}</div></div>
        <div><div class="auc-label">ROC-AUC</div><div class="{auc_cls}">{auc}</div></div>
        <div class="{delta_cls}">{delta}</div>
        <div class="model-track"><div class="model-fill {bar_cls}" style="width:{width:.1f}%"></div></div>
      </div>"""


def scene_8():
    r = st.session_state.reveal
    body = algo_row("Logistic Regression", "0.761", "reference", True)
    if r >= 1:
        body += algo_row("Random Forest", "0.750", "−0.011")
        body += algo_row("Gradient Boosting", "0.758", "−0.003")
        body += algo_row("XGBoost", "0.719", "−0.042")
    takeaway = "" if r < 2 else "<div class='takeaway fade-in'>Changing the algorithm <span class='gold' style='font-style:italic;'>did not improve overall discrimination.</span></div>"
    note = "" if r < 2 else "<div class='sans muted fade-in' style='font-size:15px;margin-top:14px;'>In this untuned comparison, none of the alternative algorithms improved ROC-AUC over Logistic Regression.</div>"
    html_block(f"""
        <div class="slide"><div class="slide-inner">
          <div class="kicker">RQ1 · SAME INFORMATION. DIFFERENT ENGINE.</div>
          <div class="title">What if the algorithm changes?</div>
          <div class="subtitle">Model B predictors · same train/test split · untuned comparison</div>
          <div style="margin-top:18px;">{body}</div>
          {takeaway}
          {note}
        </div>{shell(8, True)}</div>
        """)
    if r >= 1:
        with st.expander("Model details"):
            st.dataframe(ALGO_METRICS.style.format(precision=3), use_container_width=True, hide_index=True)


# -----------------------------
# Scene 9 — RQ2
# -----------------------------
STRATEGIES = [
    ("Over-the-counter medication", 77.7, 1953, "PHARM"),
    ("Exercise", 53.5, 1950, "NON-PHARM"),
    ("Prescribed pain reliever", 33.8, 1935, "PHARM"),
    ("Opioids", 33.0, 1945, "PHARM"),
    ("Physical therapy", 31.8, 1951, "NON-PHARM"),
]


def scene_9():
    r = st.session_state.reveal
    strategy_html = ""
    for name,pct,n,cat in STRATEGIES:
        color = "#8E88BE" if cat == "PHARM" else "#C8AC7A"
        strategy_html += f"""
        <div class="strategy">
          <div class="strategy-head">
            <div class="strategy-name"><span style="display:inline-block;width:7px;height:25px;border-radius:4px;background:{color};margin-right:12px;vertical-align:middle;"></span>{html.escape(name)}</div>
            <div class="strategy-pct">{pct:.1f}%</div>
            <div class="strategy-n">n={n:,}</div>
          </div>
          <div class="bar-track"><div class="bar-fill" style="width:{pct}%;background:{color};"></div></div>
        </div>"""

    left = ""
    if r >= 1:
        left = f"""
        <div class="fade-in">
          <div class="sans" style="font-weight:800;font-size:25px;color:#F1EEE8;">Most commonly reported strategies</div>
          <div class="legend"><span class="tag" style="background:#28243B;color:#A9A3D4;">PHARM</span><span class="tag" style="background:#372F20;color:#D9BD82;">NON-PHARM</span></div>
          {strategy_html}
          <div class="sans muted" style="font-size:16px;line-height:1.55;margin-top:18px;"><b>Valid Yes/No responses only</b><br>denominators vary slightly across strategies<br>multiple responses allowed, so percentages do not sum to 100%</div>
        </div>"""

    right = ""
    if r >= 2:
        right = """
        <div class="fade-in" style="padding-top:2px;">
          <div class="sans" style="font-weight:800;font-size:25px;color:#F1EEE8;">Broader management pattern</div>
          <div class="sans muted" style="font-size:18px;line-height:1.55;margin-top:10px;">Among 1,926 respondents with valid data<br>on 10 classifiable strategies:</div>
          <div class="hero65" style="margin-top:22px;margin-bottom:8px;">65.4%</div>
          <div class="sans" style="font-weight:800;font-size:22px;line-height:1.38;color:#F1EEE8;">used both pharmacological<br>and non-pharmacological strategies</div>
          <div style="height:3px;width:300px;background:linear-gradient(90deg,#8E88BE 0 50%,#C8AC7A 50%);margin:16px 0 22px;"></div>
          <div class="serif" style="font-size:34px;color:#D5D1C9;line-height:1.8;">24.8% <span class="sans muted" style="font-size:19px;margin-left:18px;">pharmacological only</span><br>6.7% <span class="sans muted" style="font-size:19px;margin-left:18px;">non-pharmacological only</span><br>3.1% <span class="sans muted" style="font-size:19px;margin-left:18px;">neither</span></div>
          <div class="sans muted" style="font-size:16px;line-height:1.5;margin-top:18px;"><b>Grouping note</b><br>“Other approaches” excluded because they could not be classified.</div>
        </div>"""

    content = ""
    if r >= 1:
        content = f"""<div class="two-col"><div>{left}</div><div>{right}</div></div>"""
    takeaway = "" if r < 3 else "<div class='takeaway fade-in' style='margin-top:14px;'>Management was usually <span class='gold' style='font-style:italic;'>multimodal.</span></div>"

    html_block(f"""
        <div class="slide"><div class="slide-inner">
          <div class="kicker">RQ2 · HICP n=1,956 · REPORTED IN THE PAST 3 MONTHS</div>
          <div class="title">How are people managing high-impact pain?</div>
          <div class="rule"></div>
          {content}
          {takeaway}
        </div>{shell(9, True)}</div>
    """)


# -----------------------------
# Scene 10 — RQ3
# -----------------------------
def range_html(label1,v1,label2,v2,color):
    return f"""
      <div class="range-row"><div class="range-label">{label1}</div><div class="range-track"><div class="range-fill" style="width:{v1:.1f}%;background:{color};"></div></div><div class="range-val">{v1:.1f}%</div></div>
      <div class="range-row"><div class="range-label">{label2}</div><div class="range-track"><div class="range-fill" style="width:{v2:.1f}%;background:{color};"></div></div><div class="range-val">{v2:.1f}%</div></div>"""


def scene_10():
    r = st.session_state.reveal
    education = """
      <div class="rq3-block fade-in">
        <div class="rq3-head">EDUCATION</div>
        <div class="pp-gap violet">25.1 pp gap</div>
        %s
        <div class="sans muted" style="font-size:18px;margin-top:13px;">Exercise use increased with higher education levels.</div>
      </div>""" % range_html("< high school",39.3,"Bachelor's+",64.4,"#8E88BE")
    income = ""
    if r >= 1:
        income = """
          <div class="rq3-block fade-in">
            <div class="rq3-head">INCOME-TO-POVERTY RATIO</div>
            <div class="pp-gap gold">14.4 pp gap</div>
            %s
            <div class="sans muted" style="font-size:18px;margin-top:13px;">Exercise use was higher in higher income groups.</div>
          </div>""" % range_html("< 1.0",47.9,"4.0+",62.3,"#C8AC7A")
    access = ""
    if r >= 2:
        access = """
          <div class="access-card fade-in">
            <div class="rq3-head">COST-RELATED ACCESS BARRIERS</div>
            <div class="sans" style="font-size:19px;color:#D5D1C9;line-height:1.5;margin:10px 0 17px;">Exercise was somewhat more often reported among people who also reported these barriers.</div>
            <div style="display:grid;grid-template-columns:1fr 1fr;gap:28px;">
              <div><div class="sans" style="font-size:17px;font-weight:800;color:#F1EEE8;">Delayed care due to cost</div><div class="serif gold" style="font-size:47px;margin-top:8px;">+7.9 pp</div><div class="sans muted" style="font-size:17px;">60.2% vs 52.3%</div></div>
              <div><div class="sans" style="font-size:17px;font-weight:800;color:#F1EEE8;">Needed care but did not get it</div><div class="serif gold" style="font-size:47px;margin-top:8px;">+6.0 pp</div><div class="sans muted" style="font-size:17px;">58.6% vs 52.6%</div></div>
            </div>
            <div class="sans muted" style="font-size:15px;margin-top:16px;">Descriptive differences, not evidence of causation.</div>
          </div>"""
    takeaway = ""
    if r >= 3:
        takeaway = """
          <div class="key-card fade-in" style="border-color:#6D5A37;">
            <div class="rq3-head">KEY TAKEAWAY</div>
            <div class="serif" style="font-size:38px;line-height:1.2;color:#F1EEE8;margin-top:10px;">Exercise use varied<br>across several groups.</div>
            <div class="serif gold" style="font-size:27px;font-style:italic;line-height:1.25;margin-top:10px;">These data show where differences appear, not why they exist.</div>
          </div>"""
    html_block(f"""
        <div class="slide"><div class="slide-inner">
          <div class="kicker">RQ3 · EXERCISE · SUBGROUP ANALYSIS</div>
          <div class="title">Who reports using exercise to manage HICP?</div>
          <div class="subtitle">Exercise use varied across socioeconomic and healthcare-access characteristics.</div>
          <div class="rq3-layout">
            <div class="rq3-col">
              {education}
              {income}
            </div>
            <div class="rq3-col">
              {access}
              {takeaway}
            </div>
          </div>
          <div class="sans muted" style="font-size:14px;margin-top:18px;">Cross-sectional, descriptive analysis. Differences show variation between groups, not causation.</div>
        </div>{shell(10, True)}</div>
        """)


# -----------------------------
# Scene 11 — stakeholder bridge
# -----------------------------
def scene_11():
    r = st.session_state.reveal
    uri = img_uri("scene11.png")
    bullets = ""
    if r >= 1:
        bullets = """
          <div class="fade-in" style="margin-top:30px;display:grid;gap:22px;">
            <div><div class="serif" style="font-size:29px;color:#F1EEE8;">You have a limited budget.</div><div class="sans muted" style="font-size:19px;margin-top:4px;">You can’t offer intensive support to everyone.</div></div>
            <div><div class="serif" style="font-size:29px;color:#F1EEE8;">The model gives you a probability.</div><div class="sans muted" style="font-size:19px;margin-top:4px;">But a probability still has to become a <span class='gold' style='font-style:italic;'>decision.</span></div></div>
            <div><div class="serif" style="font-size:29px;color:#F1EEE8;">Where do you set the threshold?</div><div class="sans muted" style="font-size:19px;margin-top:4px;line-height:1.45;">It depends on your goals, resources and the costs of different types of errors.</div></div>
          </div>"""
    closing = ""
    if r >= 2:
        closing = """
          <div class="fade-in serif" style="font-size:30px;line-height:1.25;color:#F1EEE8;margin-top:30px;padding-top:20px;border-top:1px solid #555B64;">
            Let’s explore how this <span class="gold" style="font-style:italic;">decision</span> changes<br>
            <span class="gold" style="font-style:italic;">the balance</span> between true and false predictions.
          </div>"""
    html_block(f"""
        <div class="slide bg-slide" style="background-image:url('{uri}');background-position:center;">
          <div style="position:absolute;left:0;top:0;bottom:0;width:59%;background:linear-gradient(90deg,rgba(11,12,15,.995) 0%,rgba(11,12,15,.97) 82%,rgba(11,12,15,.50) 100%);"></div>
          <div style="position:absolute;left:0;right:0;bottom:0;height:78px;background:#0B0C0F;z-index:2;"></div>
          <div style="position:absolute;left:5.5vw;top:5.5vh;width:47vw;z-index:4;">
            <div class="kicker">FROM PATTERNS TO PRACTICE</div>
            <div class="serif" style="font-size:clamp(46px,4.2vw,70px);line-height:1.05;color:#F1EEE8;margin-top:3.5vh;">Now imagine you’re<br>planning services<br>for <span class="gold" style="font-style:italic;">this population.</span></div>
            {bullets}
            {closing}
          </div>
          {shell(11, True)}
        </div>
        """)


# -----------------------------
# Scene 12 — threshold explorer
# -----------------------------
FALLBACK = pd.DataFrame([
    [0.30,.749,.682,905,383],
    [0.35,.691,.749,713,471],
    [0.40,.632,.790,598,561],
    [0.45,.581,.837,463,639],
    [0.50,.516,.868,377,739],
    [0.55,.476,.891,311,799],
    [0.60,.411,.914,246,899],
], columns=["threshold","sensitivity","specificity","fp","fn"])


def load_threshold_data():
    candidates = [BASE / "threshold_app_data.csv", BASE.parent / "threshold_app_data.csv", Path.cwd() / "threshold_app_data.csv"]
    for p in candidates:
        if p.exists():
            try:
                return pd.read_csv(p), p
            except Exception:
                pass
    return None, None


def scene_12():
    data, path = load_threshold_data()

    html_block("""
      <div style="width:min(1440px,92vw);margin:0 auto;padding-top:3.0vh;">
        <div class="kicker">RQ1 · THRESHOLD EXPLORATION</div>
        <div class="title" style="margin-top:.35rem;">HICP Threshold Explorer</div>
        <div class="subtitle">Move the threshold and watch the trade-off change.</div>
        <div class="sans" style="font-size:20px;font-weight:800;color:#F1EEE8;margin-top:14px;">Classification threshold</div>
      </div>
    """)

    if data is not None:
        threshold = st.slider("Classification threshold", 0.30, 0.60, 0.50, 0.01, label_visibility="collapsed")
        y_raw = data["actual_hicp"]
        if y_raw.dtype == bool:
            y_true = y_raw.astype(int)
        else:
            y_true = y_raw.astype(str).str.lower().map({"true":1,"false":0,"1":1,"0":0}).astype(int)
        y_pred = (data["probability_hicp"] >= threshold).astype(int)
        tn = int(((y_true==0)&(y_pred==0)).sum())
        fp = int(((y_true==0)&(y_pred==1)).sum())
        fn = int(((y_true==1)&(y_pred==0)).sum())
        tp = int(((y_true==1)&(y_pred==1)).sum())
        sensitivity = tp/(tp+fn)
        specificity = tn/(tn+fp)
    else:
        threshold = st.slider("Classification threshold", 0.30, 0.60, 0.50, 0.05, label_visibility="collapsed")
        row = FALLBACK.iloc[(FALLBACK["threshold"]-threshold).abs().argmin()]
        sensitivity, specificity, fp, fn = float(row.sensitivity), float(row.specificity), int(row.fp), int(row.fn)
        total_pos, total_neg = 1526, 2846
        tp, tn = total_pos-fn, total_neg-fp

    html_block(f"""
      <div style="width:min(1440px,92vw);margin:0 auto;padding-bottom:72px;">
        <div class="metric-grid threshold-metrics">
          <div class="metric-card"><div class="metric-label">Sensitivity</div><div class="metric-value">{sensitivity:.1%}</div><div class="metric-desc">HICP identified</div></div>
          <div class="metric-card"><div class="metric-label">Specificity</div><div class="metric-value">{specificity:.1%}</div><div class="metric-desc">non-HICP excluded</div></div>
          <div class="metric-card"><div class="metric-label">False negatives</div><div class="metric-value">{fn:,}</div><div class="metric-desc">HICP missed</div></div>
          <div class="metric-card"><div class="metric-label">False positives</div><div class="metric-value">{fp:,}</div><div class="metric-desc">non-HICP included</div></div>
        </div>
        <div class="sans muted" style="font-size:18px;margin-top:13px;">Lower threshold → more HICP identified, more false positives. Higher threshold → the reverse.</div>
        <div class="sans" style="font-size:23px;font-weight:800;color:#F1EEE8;margin-top:21px;">What that threshold means</div>
        <div class="cm-wrap threshold-cm">
          <div></div><div class="cm-axis">Predicted non-HICP</div><div class="cm-axis">Predicted HICP</div>
          <div class="cm-axis">Actual non-HICP</div>
          <div class="cm-cell"><div class="cm-kicker">TRUE NEGATIVE</div><div class="cm-val">{tn:,}</div><div class="cm-caption">Correctly identified as non-HICP</div></div>
          <div class="cm-cell"><div class="cm-kicker">FALSE POSITIVE</div><div class="cm-val">{fp:,}</div><div class="cm-caption">Non-HICP classified as HICP</div></div>
          <div class="cm-axis">Actual HICP</div>
          <div class="cm-cell"><div class="cm-kicker">FALSE NEGATIVE</div><div class="cm-val">{fn:,}</div><div class="cm-caption">HICP cases missed</div></div>
          <div class="cm-cell"><div class="cm-kicker">TRUE POSITIVE</div><div class="cm-val">{tp:,}</div><div class="cm-caption">Correctly identified as HICP</div></div>
        </div>
        <div class="sans muted" style="font-size:14px;margin-top:14px;padding-top:12px;border-top:1px solid #30343C;">Cross-validated Model B probabilities from the training data. This explores a decision trade-off; it does not define a universal optimal threshold.</div>
        {'' if data is not None else '<div class="sans" style="font-size:13px;color:#C8AC7A;margin-top:5px;">Preview mode: add threshold_app_data.csv beside app.py for continuous 0.01 threshold updates.</div>'}
      </div>
      <div class="threshold-shell-left">HIGH-IMPACT CHRONIC PAIN</div>
      <div class="threshold-shell-right">{''.join(f'<span class="dot {"active" if i == 12 else ""}"></span>' for i in range(1, TOTAL_SCENES + 1))}<span class="page-num">12 / 13</span></div>
    """)


# -----------------------------
# Scene 13 — ending
# -----------------------------
def scene_13():
    uri = img_uri("scene13.png")
    html_block(f"""
        <div class="slide bg-slide" style="background-image:url('{uri}');">
          <!-- Cover the baked one-line credit and replace it with the same treatment plus LinkedIn. -->
          <div style="position:absolute;right:0;bottom:0;width:44vw;height:92px;
                      background:linear-gradient(270deg,rgba(11,12,15,.995) 0%,rgba(11,12,15,.985) 72%,rgba(11,12,15,0) 100%);
                      z-index:4;"></div>
          <div style="position:absolute;right:4.5vw;bottom:22px;z-index:5;text-align:right;
                      color:#B8B1A7;font:14px Georgia,'Times New Roman',serif;
                      letter-spacing:.035em;line-height:1.45;opacity:0;
                      animation:fadein 1s ease 1.1s forwards;">
            <div>Lara Caçador · Data Analytics · Ironhack · 2026</div>
            <div><a href="https://www.linkedin.com/in/lara-ca%C3%A7ador/" target="_blank"
                    style="color:#B8B1A7;text-decoration:none;font:inherit;letter-spacing:inherit;">linkedin.com/in/lara-caçador/</a></div>
          </div>
        </div>
        """)



SCENES = {
    1: scene_1, 2: scene_2, 3: scene_3, 4: scene_4, 5: scene_5, 6: scene_6,
    7: scene_7, 8: scene_8, 9: scene_9, 10: scene_10, 11: scene_11, 12: scene_12, 13: scene_13,
}

SCENES[st.session_state.scene]()

# Navigation — one control also advances reveal states on analytical scenes.
st.markdown("<div class='nav-wrap'>", unsafe_allow_html=True)
c1, c2 = st.columns(2)
with c1:
    st.button("←", on_click=go_back, use_container_width=True, disabled=(st.session_state.scene == 1 and st.session_state.reveal == 0))
with c2:
    st.button("→", on_click=go_next, use_container_width=True, disabled=(st.session_state.scene == TOTAL_SCENES))
st.markdown("</div>", unsafe_allow_html=True)
