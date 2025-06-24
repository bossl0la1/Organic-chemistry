import streamlit as st
import time
from pathlib import Path
import qrcode
from io import BytesIO

st.set_page_config(page_title="Organic Chemistry Tutor", page_icon="🧪", layout="wide")

# Optional styling
style_path = Path("styles.css")
if style_path.exists():
    with open(style_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Initialize session state for splash screen visibility
if 'splash_shown' not in st.session_state:
    st.session_state.splash_shown = False

# Create a placeholder for the splash screen
splash_placeholder = st.empty()

# Function to show the splash screen
def show_splash_screen():
    splash_screen = """
    <style>
    @keyframes fadeIn {
        from {
            opacity: 0;
            transform: translateY(-20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }

    #splash {
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background-color: #007bff;  /* Change to your preferred color */
        color: white;
        display: flex;
        flex-direction: column;  /* Stack items vertically */
        justify-content: center;
        align-items: center;
        font-size: 40px;
        z-index: 9999;
        text-align: center;  /* Center text */
        animation: fadeIn 2s ease-in;  /* Apply fade-in animation */
    }
    </style>

    <div id="splash">
        Welcome to Organic Chemistry Tutor!
    </div>

    <script>
        setTimeout(function() {
            document.getElementById("splash").style.display = "none";
        }, 3000);  // Adjust time in milliseconds (3000 ms = 3 seconds)
    </script>
    """

    # Show the splash screen in the placeholder
    splash_placeholder.markdown(splash_screen, unsafe_allow_html=True)

    # Wait for 3 seconds to simulate loading
    time.sleep(3)

    # Clear the splash screen
    splash_placeholder.empty()

    # Set session state to indicate the splash has been shown
    st.session_state.splash_shown = True

# Show the splash screen only if it hasn't been shown yet
if not st.session_state.splash_shown:
    show_splash_screen()


# Sidebar
st.sidebar.image("OGT.jpg", width=100)
st.sidebar.title("🧪 Chemistry Tutor")
page = st.sidebar.selectbox("📚 Choose a topic", [
    "🏠 Home",
    "Introduction to Organic chemistry",
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
    -  Introduction to Organic chemistry
    - 🧬 Functional Groups
    - 🔤 IUPAC Naming
    - 📈 Homologous Series
    - 🧠 Practice Quiz
    - [App review](https://docs.google.com/forms/d/e/1FAIpQLSebo2O7Tv0vyihmrY4eWxTDz87H9DaWemPFJO9tZrrwWyXKWQ/viewform?usp=dialog)
    - Made by Damilola Ayo-Afolabi and Olaniyan Oladayo

    Share this app or open it on your phone by scanning the QR code below:
    """)

    # Use your actual Streamlit Cloud app link here
    url = "https://organicchemistry.streamlit.app/"
    qr = qrcode.make(url)
    buf = BytesIO()
    qr.save(buf, format="PNG")
    st.image(buf.getvalue(), width=200, caption="📱 Scan to open app")

# ---------- INTRODUCTION ----------
elif page == "Introduction to Organic chemistry":
    st.title("Introduction to Organic chemistry")
    st.write("This is a video to provide a quickstart to your journey in Organic Chemistry:")
    st.video("lesson.mp4", width=500) 
    st.image("OGT.jpg", width=100)
    

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
        {"q":"What is the IUPAC name for CH₃-CH₂-CH₂-COOH?", "a":"Butanoic acid", "opts":["Butanoic acid","Propanoic acid","Ethanoic acid"]},
        {"q":"Which of the following is a functional group present in alcohols?", "a":"-OH", "opts":["-OH","-COOH","-CHO"]},
        {"q":"What type of reaction occurs when an alkene reacts with hydrogen?", "a":"Addition", "opts":["Substitution","Addition","Elimination"]},
        {"q":"What is the primary product of the complete combustion of propane (C₃H₈)?", "a":"Carbon dioxide and water", "opts":["Carbon monoxide and water","Carbon dioxide and water","Carbon and water"]},
        {"q":"What is the primary product of the incomplete combustion of propane (C₃H₈)?", "a":"Carbon monoxide,Carbon and water", "opts":["Carbon","Carbon dioxide","Carbon monoxide, Carbon and water"]},
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
    if score < 5:
        st.write("You have not yet understood organic chemistry.")
    elif score < 10:
        st.write("You are beginning to understand organic chemistry but not yet fully.")
    elif score < 15:
        st.write("You have almost developed mastery of organic chemistry.")
    else:
        st.write("You have attained mastery of organic chemistry!")

        
   
    
