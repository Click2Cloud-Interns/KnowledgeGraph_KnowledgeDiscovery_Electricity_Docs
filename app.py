import streamlit as st
import subprocess
import os
import pandas as pd

# ---------------------------
# PAGE CONFIG
# ---------------------------
st.set_page_config(
    page_title="Power Knowledge Assistant",
    layout="wide"
)

st.title("GraphRAG Knowledge Assistant")
st.markdown("AI-powered reasoning over structured knowledge graphs")

# ---------------------------
# BASE DIRECTORY
# ---------------------------
BASE_DIR = "project"

if not os.path.exists(BASE_DIR):
    st.error("❌ 'project' folder not found.")
    st.stop()

# ---------------------------
# ONLY SHOW THESE DOCUMENTS
# ---------------------------
ALLOWED_DOCS = [
    "doc_invoice",
    "doc_power_schedule",
    "doc_invoice_schedule",
    "doc_peak_compensation",
    "doc_rsopl_schedule",
    "all_docs"
]

documents = [
    doc for doc in ALLOWED_DOCS
    if os.path.isdir(os.path.join(BASE_DIR, doc))
]

if not documents:
    st.error("❌ None of the required document folders were found.")
    st.stop()

# ---------------------------
# SIDEBAR
# ---------------------------
st.sidebar.header("📂 Select Document")
selected_doc = st.sidebar.selectbox("Choose document", documents)

st.sidebar.header("⚙ Query Settings")
method = st.sidebar.radio(
    "Search Method",
    ["global", "local"],
    help="Global = reasoning across graph | Local = deep entity-level search"
)

project_path = os.path.join(BASE_DIR, selected_doc)

# ---------------------------
# MAIN QUERY INPUT
# ---------------------------
st.subheader("❓ Ask a Question")

question = st.text_input(
    "Enter your question:",
    placeholder="Example: Explain how peak energy affects billing amount."
)

col1, col2 = st.columns(2)

with col1:
    run_query = st.button("🚀 Get Answer")

with col2:
    show_graph = st.button("📊 Show Knowledge Graph")

# ---------------------------
# QUERY EXECUTION
# ---------------------------
if run_query:
    if question.strip() == "":
        st.warning("Please enter a question.")
    else:
        with st.spinner("Thinking... Please wait..."):
            command = [
                "graphrag",
                "query",
                "--root",
                project_path,
                "--method",
                method,
                "--query",
                question,
            ]

            result = subprocess.run(command, capture_output=True, text=True)

            if result.returncode == 0:
                st.success("✅ Answer")
                st.write(result.stdout)
            else:
                st.error("❌ Error occurred")
                st.write(result.stderr)

# ---------------------------
# SHOW KNOWLEDGE GRAPH
# ---------------------------
if show_graph:
    st.subheader(f"📊 Knowledge Graph: {selected_doc}")

    # If ALL_DOCS → use project/output
    if selected_doc == "all_docs":
        image_path = os.path.join(
            BASE_DIR,
            "output",
            "knowledge_graph_FINAL.png"
        )
    else:
        image_path = os.path.join(
            project_path,
            "output",
            "knowledge_graph_FINAL.png"
        )

    if os.path.exists(image_path):
        st.image(image_path, use_container_width=True)
    else:
        st.warning("Knowledge graph image not found.")
