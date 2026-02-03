 # ⚡ Power Knowledge Graph Assistant  

AI-Powered GraphRAG System for Energy & Invoice Intelligence  

---

## 📌 Overview

This project implements a **GraphRAG-based Knowledge Graph System** for analyzing:

- Power Schedules  
- Peak Hour Data  
- Energy Trading Documents  
- Invoice Documents  

It converts structured and semi-structured documents into a **knowledge graph**, enabling:

- Graph-based reasoning  
- Local & global querying  
- Entity relationship discovery  
- Interactive visualization via Streamlit  

---

## 🧠 What This Project Does

- Converts `.xlsx` / `.pdf` → Markdown  
- Indexes documents using **GraphRAG**  
- Extracts:
  - Entities (organization, geo, event, etc.)
  - Relationships
  - Communities
- Builds a structured Knowledge Graph  
- Enables:
  - Global reasoning queries  
  - Local entity-level queries  
- Displays graph & top connected entities  

---


## 📂 Project Structure

```
KNOWLEDGEGRAPH_KNOWLEDGE_ASSISTANT/
│
├── app.py                        #Streamlit
├── MASTER_GUIDE.md
├── .env
│
├── venv/                         # Virtual environment (root)
│
├── logs/                         # Root logs
├── output/                       # Root-level outputs (all 5 docs combined knowledge graph)
│
└── project/
    │
    ├── doc_invoice/
    │   ├── .env
    │   ├── settings.yaml
    │   ├── visualize_final.py
    │   │
    │   ├── input/                # Invoice markdown files
    │   ├── prompts/              # GraphRAG prompt templates
    │   ├── output/               # Generated graph + CSV
    │   ├── logs/
    │   └── cache/
    │
    ├── doc_invoice_schedule/     #Document Invoice + power schedule 
    │   ├── .env
    │   ├── settings.yaml
    │   ├── visualize_final.py
    │   │
    │   ├── input/
    │   ├── prompts/
    │   ├── output/
    │   ├── logs/
    │   └── cache/
    │
    ├── doc_power_schedule/
    │   ├── .env
    │   ├── settings.yaml
    │   ├── visualize_final.py
    │   │
    │   ├── input/
    │   ├── prompts/
    │   ├── output/
    │   ├── logs/
    │   └── cache/
    │
    └── prompts/                  # Shared prompt templates (optional)

```
## 🔧 Tech Stack

- **Python 3.10**
- **GraphRAG** - Knowledge graph construction and querying
- **Azure OpenAI (GPT-4.1)** - Natural language processing
- **Azure Embeddings (text-embedding-3-large)** - Semantic embeddings
- **NetworkX** - Graph analysis and manipulation
- **Pandas** - Data processing
- **Matplotlib** - Graph visualization
- **Streamlit** - Interactive web interface

---

## 🚀 Setup Instructions

### 1️⃣ Create Virtual Environment

```bash
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 2️⃣ Install Dependencies

```bash
pip install graphrag
pip install streamlit pandas matplotlib networkx
```

### 3️⃣ Configure Environment Variables

Create a `.env` file in the project root with the following:

```env
GRAPHRAG_API_KEY=your_key_here
AZURE_OPENAI_ENDPOINT=https://your-endpoint.openai.azure.com/
AZURE_OPENAI_CHAT_DEPLOYMENT=gpt-4.1
AZURE_OPENAI_EMBEDDING_DEPLOYMENT=text-embedding-3-large
```

### 4️⃣ Index Documents

Navigate to each document folder and run the indexing command:

```bash
cd project/doc_invoice
graphrag index --root .
```

Repeat for other folders (e.g., `doc_schedule`, `doc_reports`, etc.)

---

## 🔍 Query the Knowledge Graph

### Global Reasoning Query

```bash
graphrag query --root . --method global --query "Summarize this invoice"
```

### Local Entity-Level Query

```bash
graphrag query --root . --method local --query "What were the peak hours?"
```

---

## 📊 Visualization

Generate knowledge graph visualizations:

```bash
python visualize_final.py
```

**Generated files:**
- `knowledge_graph_FINAL.png` - Visual representation of the knowledge graph
- `top_entities.csv` - List of most connected entities

---

## 🖥️ Streamlit Interface

Launch the interactive web interface:

```bash
streamlit run app.py
```

### Features:
- ✅ Select document (invoice, schedule, reports, etc.)
- ✅ Choose global or local search mode
- ✅ Ask natural language questions
- ✅ View Knowledge Graph visualization
- ✅ Explore Top Connected Entities

---

## 🧩 How GraphRAG Works

```
Document → Chunking → Entity Extraction → Relationship Building → Community Formation → Graph Storage
                           ↓
                    Query Processing (Graph-based, not raw text)
```

1. **Document Processing**: Documents are chunked into manageable segments
2. **Entity Extraction**: LLM identifies key entities from text
3. **Relationship Mapping**: Connections between entities are established
4. **Community Detection**: Related entities are grouped into communities
5. **Graph Storage**: Complete knowledge graph is persisted
6. **Intelligent Querying**: Queries run over structured graph, not raw files

---

## 🧠 Why Knowledge Graph Instead of Normal RAG?

| Feature | Normal RAG | GraphRAG |
|---------|-----------|----------|
| **Search Method** | Text similarity | Structured entity reasoning |
| **Retrieval** | Chunk retrieval | Relationship-aware querying |
| **Context** | Limited context window | Multi-hop reasoning |
| **Structure** | No graph structure | Full entity relationship network |
| **Understanding** | Surface-level matching | Deep semantic connections |
| **Accuracy** | May miss relationships | Captures entity interactions |

---

## ❌ WHAT YOU DO NOT NEED TO DO AGAIN

You **DO NOT** need to:
- ❌ Reinstall Python
- ❌ Reinstall graphrag
- ❌ Recreate venv
- ❌ Reconfigure `.env` or `settings.yaml`
- ❌ Run `graphrag init`
- ❌ Download configuration files again

**Unless something breaks badly.**

---

## 🔍 COMMON TASKS

### View Your Current Data

```powershell
# See your input files
dir input

# See generated outputs
dir output

# View top entities
Import-Csv output\top_entities.csv | Format-Table

# View stats
Get-Content output\stats.json
```

### Add New Documents

```powershell
# Copy new .md file to input directory
Copy-Item "path\to\new_file.md" "input\"

# Re-index
graphrag index --root .

# Wait for completion, then query or visualize
```

### Clear Everything and Start Fresh

```powershell
# Clear output and cache
Remove-Item -Recurse -Force output\*, cache\* -ErrorAction SilentlyContinue

# Re-index from scratch
graphrag index --root .
```

---

## 🟡 TROUBLESHOOTING

### Problem: `graphrag: command not found`

**Solution:**
```powershell
# Make sure venv is activated
# You should see (venv) in your prompt

# If not:
deactivate
.\venv\Scripts\Activate.ps1

# Verify
graphrag --version
```

---

### Problem: Virtual environment won't activate

**Solution:**
```powershell
# Enable script execution
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Try activating again
.\venv\Scripts\Activate.ps1
```

---

### Problem: API errors during indexing

**Check your `.env` file:**
```powershell
Get-Content .env
```

**Should contain (no extra spaces):**
```
GRAPHRAG_API_KEY=your_key_here
AZURE_OPENAI_ENDPOINT=https://your-endpoint.openai.azure.com/
AZURE_OPENAI_CHAT_DEPLOYMENT=gpt-4.1
AZURE_OPENAI_EMBEDDING_DEPLOYMENT=text-embedding-3-large
```

**Verify API is working:**
```powershell
# If you have test_api.py
python test_api.py
```

---

### Problem: "No such file or directory"

**Check you're in the right place:**
```powershell
# Where am I?
pwd

# Should show: D:\GraphRAG_FINAL\project

# If wrong:
cd D:\GraphRAG_FINAL\project
```

---

### Problem: Graph visualization fails

**Install missing packages:**
```powershell
pip install networkx matplotlib pandas pyarrow
```

---

### Problem: Slow indexing

**This is normal.** Indexing 5 documents typically takes:
- Small documents: 5-10 minutes
- Medium documents: 10-20 minutes
- Large documents: 20-30 minutes

**If taking over 1 hour:**
- Check your Azure OpenAI rate limits
- Check network connection
- Review logs: `Get-Content logs\indexing-engine.log`

---

## 📊 SAMPLE QUERIES

### Global Queries (High-level Overview)

```powershell
graphrag query --root . --method global --query "Summarize the main themes in these documents"

graphrag query --root . --method global --query "What are the key organizations mentioned?"

graphrag query --root . --method global --query "What are the relationships between different entities?"

graphrag query --root . --method global --query "What events are discussed across all documents?"
```

### Local Queries (Specific Details)

```powershell
graphrag query --root . --method local --query "What are the details of HPPC peak power calculations?"

graphrag query --root . --method local --query "What invoices are mentioned and what are their amounts?"

graphrag query --root . --method local --query "What compensation rates are specified?"

graphrag query --root . --method local --query "What are the specific dates mentioned?"
```

---

## 📈 VIEWING YOUR RESULTS

### Open Graph Visualization

```powershell
# Standard resolution
start output\knowledge_graph_FINAL.png

# High resolution (for presentations/printing)
start output\knowledge_graph_FINAL_hires.png
```

### View Top Entities as Table

```powershell
Import-Csv output\top_entities.csv | Format-Table -AutoSize
```

### Export Results

```powershell
# Query and save to file
graphrag query --root . --method global --query "Summarize everything" > summary.txt

# View the file
Get-Content summary.txt
```

---

### Quick Presentation Setup:

```powershell
# 1. Open high-res graph
start output\knowledge_graph_FINAL_hires.png

# 2. Show top entities table
Import-Csv output\top_entities.csv | Format-Table

# 3. Run live query
graphrag query --root . --method global --query "Summarize the most important information"
```
---

## 🔑 KEY FILES (DO NOT DELETE)

### Critical Files:
- `.env` - Your API credentials
- `settings.yaml` - Configuration
- `prompts/*.txt` - Prompt templates
- `input/*.md` - Your source documents

### Safe to Delete:
- `output/*` - Can be regenerated by re-indexing
- `cache/*` - Can be regenerated
- `logs/*` - Just log files

---

## 📞 QUICK REFERENCE COMMANDS

```powershell
# Activate venv
.\venv\Scripts\Activate.ps1

# Navigate to project
cd project

# Index
graphrag index --root .

# Query (global)
graphrag query --root . --method global --query "your question"

# Query (local)
graphrag query --root . --method local --query "your question"

# Visualize
python visualize_final.py

# Check version
graphrag --version

# View logs
Get-Content logs\indexing-engine.log -Tail 50

# List input files
dir input

# List output files
dir output

# View stats
Get-Content output\stats.json
```

---

## ⏱️ EXPECTED TIMES

- **Activation & navigation:** < 1 minute
- **Query execution:** 10-30 seconds
- **Indexing 5 documents:** 10-20 minutes
- **Visualization generation:** 1-2 minutes

---

## ✅ SUCCESS CHECKLIST

You know everything is working when:
- [ ] `(venv)` appears in your terminal prompt
- [ ] You're in `D:\GraphRAG_FINAL\project`
- [ ] `graphrag --version` shows a version number
- [ ] `dir input` shows your `.md` files
- [ ] `dir output` shows `.parquet` files after indexing
- [ ] Queries return actual responses
- [ ] `visualize_final.py` creates PNG files

---

## 🎉 YOU'RE READY!

Follow this README every time you work with GraphRAG. Bookmark it or print it for quick reference.

**Most common workflow:**
```
1. Activate venv
2. cd project  
3. Query OR Index OR Visualize
```

That's all you need! 🚀






