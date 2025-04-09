import streamlit as st
import requests

st.set_page_config(page_title="SHL Test Recommender", layout="wide")
st.title("🧠 SHL Test Recommender")

# Modern CSS with animations and badges
st.markdown("""
    <style>
        .recommendation-card {
            background: linear-gradient(135deg, #fdfbfb 0%, #ebedee 100%);
            padding: 20px;
            border-radius: 20px;
            box-shadow: 0 6px 20px rgba(0, 0, 0, 0.1);
            margin-bottom: 25px;
            transition: all 0.3s ease;
            animation: fadeInUp 0.4s ease forwards;
        }
        .recommendation-card:hover {
            transform: translateY(-6px);
            background-color: #f0f4ff;
        }
        .recommendation-index {
            font-size: 18px;
            font-weight: bold;
            color: #4f46e5;
            margin-right: 8px;
        }
        .badge {
            display: inline-block;
            padding: 3px 8px;
            border-radius: 8px;
            background-color: #e0e7ff;
            color: #1e3a8a;
            font-size: 12px;
            margin-right: 6px;
            font-weight: 600;
        }
        ul {
            padding-left: 20px;
            margin-top: 8px;
        }
        a {
            color: #2563eb;
            text-decoration: none;
            font-weight: 500;
        }
        a:hover {
            text-decoration: underline;
        }
        @keyframes fadeInUp {
            from {
                opacity: 0;
                transform: translate3d(0, 20px, 0);
            }
            to {
                opacity: 1;
                transform: translate3d(0, 0, 0);
            }
        }
    </style>
""", unsafe_allow_html=True)

query = st.text_input("🔍 Enter your query:")

if query:
    try:
        response = requests.post("https://sailajap-shl-fastapi.hf.space/recommend", json={"query": query})
        results = response.json()

        st.subheader("✨ Recommended Tests")

        for i, item in enumerate(results.get("recommended_assessments", []), 1):
            try:
                test_name = item.get("description", "N/A")
                remote = item.get("remote_support", "N/A")
                adaptive = item.get("adaptive_support", "N/A")
                test_type = ", ".join(item.get("test_type", []))
                duration = item.get("duration", "N/A")
                link = item.get("url", "#")

                st.markdown(f"""
                    <div class='recommendation-card'>
                        <span class='recommendation-index'>🔹 {i}.</span> <strong style='font-size: 18px;'>{test_name}</strong><br><br>
                        <span class='badge'>🧪 Type: {test_type}</span>
                        <span class='badge'>⏱️ Duration: {duration} mins</span>
                        <span class='badge'>💻 Remote: {remote}</span>
                        <span class='badge'>🧠 Adaptive: {adaptive}</span>
                        <br><br>
                        🔗 <a href="{link}" target="_blank">View Test Details</a>
                    </div>
                """, unsafe_allow_html=True)

            except Exception as e:
                st.error(f"Error rendering recommendation #{i}: {e}")

    except Exception as e:
        st.error(f"Error fetching recommendations: {e}")
