import streamlit as st
from pathlib import Path
import qrcode
from io import BytesIO

st.set_page_config(page_title="Organic Chemistry Tutor", page_icon="🧪", layout="wide")

# Optional styling
style_path = Path("assets/styles.css")
if style_path.exists():
    with open(style_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Sidebar
st.sidebar.image("org.png", width=100)
st.sidebar.title("🧪 Chemistry Tutor")
page = st.sidebar.selectbox("📚 Choose a topic", [
    " Introduction to Organic chemistry",
    "🏠 Home",
    "🧬 Functional Groups",
    "🔤 IUPAC Naming",
    "📈 Homologous Series",
    "🧠 Quiz"
])

# ---------- HOME ----------
if page == "🏠 Home":
    st.title("🏠 Welcome to Organic Chemistry Tutor")

    st.markdown("""
    This app is designed to help SS2 students understand key concepts in organic chemistry:
    - 🧬 Functional Groups
    - 🔤 IUPAC Naming
    - 📈 Homologous Series
    - 🧠 Practice Quiz
    - Made by Damilola Ayo-Afolabi and Olaniyan Oladayo

    Share this app or open it on your phone by scanning the QR code below:
    """)

    # Use your actual Streamlit Cloud app link here
    url = "https://organicchemistry.streamlit.app/"
    qr = qrcode.make(url)
    buf = BytesIO()
    qr.save(buf, format="PNG")
    st.image(buf.getvalue(), width=200, caption="📱 Scan to open app")

# ------- INTRODUCTION -------
elif page == "Introduction to Organic chemistry":
    st.title("Introduction to Organic chemistry")
    st.video("lesson.mp4", width=500)

# ---------- FUNCTIONAL GROUPS ----------
elif page == "🧬 Functional Groups":
    st.title("🧬 Functional Groups")

    groups = {
        "Alkane": ["C–C", "Ethane (C2H6)", "Single bonds only; saturated hydrocarbon."],
        "Alkene": ["C=C", "Ethene (C2H4)", "Double bond present; unsaturated."],
        "Alkyne": ["C≡C", "Ethyne (C2H2)", "Triple bond; highly reactive."],
        "Alcohol": ["-OH", "Ethanol (C2H5OH)", "Hydroxyl group."],
        "Aldehyde": ["-CHO", "Ethanal (CH3CHO)", "Carbonyl at end of chain."],
        "Ketone": ["C=O", "Propanone (CH3COCH3)", "Carbonyl group in chain."],
        "Carboxylic Acid": ["-COOH", "Ethanoic acid (CH3COOH)", "Acidic; forms esters."],
        "Ester": ["-COO-", "Methyl ethanoate", "Formed from acid + alcohol."],
        "Amine": ["-NH2", "Methylamine (CH3NH2)", "Basic nitrogen group."]
    }

    for name, (group, example, desc) in groups.items():
        with st.expander(name):
            st.write(f"**Functional Group:** `{group}`")
            st.write(f"**Example:** {example}")
            st.write(f"**Description:** {desc}")

# ---------- IUPAC NAMING ----------
elif page == "🔤 IUPAC Naming":
    st.title("🔤 IUPAC Naming")
    st.markdown("""
    Use this section to learn how to identify and name common organic compounds.

    **Examples:**
    - CH₄ → **Methane**
    - C₂H₆ → **Ethane**
    - C₂H₄ → **Ethene**
    - CH₃CH₂OH → **Ethanol**
    - CH₃COOH → **Ethanoic Acid**
    """)

    formula = st.text_input("Enter a chemical formula to identify (e.g. CH3CH2OH):")
    examples = {
        "CH3CH2OH": "Ethanol – A two-carbon alcohol.",
        "CH3COOH": "Ethanoic Acid – Carboxylic acid with two carbon atoms.",
        "CH4": "Methane – Simplest alkane.",
        "C2H4": "Ethene – Two-carbon alkene.",
        "C2H2": "Ethyne – Two-carbon alkyne.",
        "CH3CHO": "Ethanal – An aldehyde with two carbons."
    }

    if formula:
        result = examples.get(formula.strip(), "❌ Not found in examples. Try a common compound.")
        st.info(result)

# ---------- HOMOLOGOUS SERIES ----------
elif page == "📈 Homologous Series":
    st.title("📈 Homologous Series")

    st.markdown("""
    The **Homologous Series** is a group of organic compounds with:
    - Same functional group
    - Same general formula
    - Gradual change in physical properties

    Examples include:
    - **Alkanes** → General formula CnH2n+2
    - **Alkenes** → CnH2n
    - **Alkynes** → CnH2n−2
    - **Alcohols** → CnH2n+1OH
    """)

    n = st.slider("Select number of carbon atoms (n):", 1, 10, 1)
    st.subheader("Formulas for selected n:")
    st.markdown(f"- **Alkane:** C{n}H{2*n + 2}")
    st.markdown(f"- **Alkene:** C{n}H{2*n}")
    st.markdown(f"- **Alkyne:** {'Invalid for n<2' if n < 2 else f'C{n}H{2*n - 2}'}")
    st.markdown(f"- **Alcohol:** C{n}H{2*n + 1}OH")

# ---------- QUIZ ----------
elif page == "🧠 Quiz":
    st.title("🧠 Organic Chemistry Quiz (15 Questions)")

    questions = [
        {"q":"Formula of ethanol?", "a":"C2H5OH", "opts":["CH4","C2H5OH","C2H4"]},
        {"q":"Which group is -COOH?", "a":"Carboxylic Acid", "opts":["Alcohol","Ketone","Carboxylic Acid"]},
        {"q":"General formula for alkenes?", "a":"CnH2n", "opts":["CnH2","CnH2n","CnH2n+2"]},
        {"q":"Test for unsaturation?", "a":"Decolours Br₂", "opts":["Turns red","Decolours Br₂","Fizzes with HCl"]},
        {"q":"Functional group in propanone?", "a":"Ketone", "opts":["Alcohol","Aldehyde","Ketone"]},
        {"q":"Ethanol oxidized gives?", "a":"Ethanoic Acid", "opts":["Ethanal","Ethanoic Acid","Methanol"]},
        {"q":"Homologous difference?", "a":"CH₂ group", "opts":["OH group","CH₂ group","C=O group"]},
        {"q":"Markovnikov’s rule applies to?", "a":"Alkenes", "opts":["Alkanes","Alkenes","Amines"]},
        {"q":"Test for phenol?", "a":"FeCl₃ gives purple", "opts":["KMnO₄","FeCl₃ gives purple","None"]},
        {"q":"Esterification is?", "a":"Acid + Alcohol", "opts":["Acid + Alcohol","Base + Salt","Oil + Water"]},
        {"q":"Acids have pH?", "a":"<7", "opts":[">7","=7","<7"]},
        {"q":"Alkane general formula?", "a":"CnH2n+2", "opts":["CnH2n+2","CnH2n","CnH2n-2"]},
        {"q":"Which has a triple bond?", "a":"Alkyne", "opts":["Alkene","Alkyne","Alkane"]},
        {"q":"Aromatic ring is?", "a":"Benzene", "opts":["Cyclohexane","Benzene","Hexane"]},
        {"q":"IUPAC suffix for aldehyde?", "a":"-al", "opts":["-ol","-one","-al"]},
    ]

    score = 0
    for i, q in enumerate(questions):
        st.subheader(f"{i+1}. {q['q']}")
        response = st.radio("Choose an answer:", q["opts"], key=f"q{i}", index=None)
        if response:
            if response == q["a"]:
                st.success("✅ Correct!")
                score += 1
            else:
                st.error(f"❌ Incorrect. Correct answer: {q['a']}")

    st.markdown(f"### 🏁 Final Score: **{score}/{len(questions)}**")
