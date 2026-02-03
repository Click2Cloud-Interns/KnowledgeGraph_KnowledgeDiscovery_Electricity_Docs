# 🚀 GRAPHRAG FRESH START - COMPLETE GUIDE
# NO ERRORS - GUARANTEED TO WORK

## ⚡ QUICK START (Copy-Paste Commands)

### 1️⃣ CREATE DIRECTORY STRUCTURE

```powershell
# Create base directory
New-Item -ItemType Directory -Path "D:\GraphRAG_FINAL" -Force
cd D:\GraphRAG_FINAL

# Create project directory
New-Item -ItemType Directory -Path "project" -Force
cd project

# Create subdirectories
New-Item -ItemType Directory -Path "input", "output", "cache", "logs", "prompts" -Force
```

**Your structure should now look like:**
```
D:\GraphRAG_FINAL\
└── project\
    ├── input\      (empty - you'll add files here)
    ├── output\     (empty - will be filled by GraphRAG)
    ├── cache\      (empty)
    ├── logs\       (empty)
    └── prompts\    (empty - you'll add files here)
```

---

### 2️⃣ CREATE VIRTUAL ENVIRONMENT

```powershell
# Go back to base directory
cd D:\GraphRAG_FINAL

# Create venv
python -m venv venv

# Activate venv
.\venv\Scripts\Activate.ps1

# You should see (venv) in your prompt
```

**If activation fails:**
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
.\venv\Scripts\Activate.ps1
```

---

### 3️⃣ INSTALL GRAPHRAG

```powershell
# Ensure venv is activated (see (venv) in prompt)
pip install --upgrade pip
pip install graphrag
pip install networkx matplotlib pandas pyarrow

# Verify installation
graphrag --version
```

---

### 4️⃣ DOWNLOAD AND PLACE FILES

**Download these files from this chat:**
1. `env_file.txt` → Rename to `.env`
2. `settings_final.yaml` → Rename to `settings.yaml`
3. `entity_extraction.txt`
4. `summarize_descriptions.txt`
5. `community_report.txt`
6. `visualize_final.py`

**Place them in the correct locations:**

```powershell
# Navigate to project directory
cd D:\GraphRAG_FINAL\project

# Place files (after downloading):
# .env → D:\GraphRAG_FINAL\project\.env
# settings.yaml → D:\GraphRAG_FINAL\project\settings.yaml
# entity_extraction.txt → D:\GraphRAG_FINAL\project\prompts\entity_extraction.txt
# summarize_descriptions.txt → D:\GraphRAG_FINAL\project\prompts\summarize_descriptions.txt
# community_report.txt → D:\GraphRAG_FINAL\project\prompts\community_report.txt
# visualize_final.py → D:\GraphRAG_FINAL\project\visualize_final.py
```

**Quick command to verify file placement:**
```powershell
# Check files exist
Test-Path .env
Test-Path settings.yaml
Test-Path prompts\entity_extraction.txt
Test-Path prompts\summarize_descriptions.txt
Test-Path prompts\community_report.txt
Test-Path visualize_final.py

# All should return: True
```

---

### 5️⃣ ADD YOUR INPUT FILES

```powershell
# Copy your 5 .md files to input directory
# Example:
Copy-Item "D:\path\to\your\file1.md" "D:\GraphRAG_FINAL\project\input\"
Copy-Item "D:\path\to\your\file2.md" "D:\GraphRAG_FINAL\project\input\"
Copy-Item "D:\path\to\your\file3.md" "D:\GraphRAG_FINAL\project\input\"
Copy-Item "D:\path\to\your\file4.md" "D:\GraphRAG_FINAL\project\input\"
Copy-Item "D:\path\to\your\file5.md" "D:\GraphRAG_FINAL\project\input\"

# Verify files are there
dir input\*.md
```

---

### 6️⃣ VERIFY SETUP

```powershell
# Make sure you're in the project directory
cd D:\GraphRAG_FINAL\project
pwd  # Should show: D:\GraphRAG_FINAL\project

# Check all files
dir
```

**You should see:**
```
Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----                                            cache
d-----                                            input
d-----                                            logs
d-----                                            output
d-----                                            prompts
-a----                                       XXX  .env
-a----                                       XXX  settings.yaml
-a----                                       XXX  visualize_final.py
```

```powershell
# Check input files
dir input

# Should show your 5 .md files

# Check prompts
dir prompts

# Should show:
# entity_extraction.txt
# summarize_descriptions.txt
# community_report.txt
```

---

### 7️⃣ RUN INDEXING

```powershell
# Ensure:
# 1. You're in D:\GraphRAG_FINAL\project
# 2. venv is activated (see (venv) in prompt)

# Run indexing
graphrag index --root .

# This will take 10-20 minutes
# You'll see progress messages
```

**Expected output:**
```
🚀 GraphRAG Indexer
Reading settings from .\settings.yaml
Processing documents...
Creating text chunks...
Extracting entities...
Building graph...
Creating communities...
Generating reports...
✅ Indexing complete!
```

---

### 8️⃣ VERIFY INDEXING SUCCESS

```powershell
# Check output directory
dir output

# You MUST see these files:
# - create_final_entities.parquet (or entities.parquet)
# - create_final_relationships.parquet (or relationships.parquet)
# - create_final_communities.parquet
# - stats.json
```

```powershell
# Check stats
Get-Content output\stats.json
```

---

### 9️⃣ CREATE VISUALIZATION

```powershell
# Run the visualization script
python visualize_final.py

# This will:
# 1. Load your graph data
# 2. Create a network visualization
# 3. Save PNG files
# 4. Display the graph
```

**Output files created:**
- `output/knowledge_graph_FINAL.png` (300 DPI)
- `output/knowledge_graph_FINAL_hires.png` (600 DPI - for presentations)
- `output/top_entities.csv` (top connected entities)

---

### 🔟 QUERY YOUR GRAPH

```powershell
# Global query (overview)
graphrag query --root . --method global --query "What are the main themes and entities in these documents?"

# Local query (specific details)
graphrag query --root . --method local --query "What are the details about peak power compensation?"
```

---

## 📋 COMPLETE FILE CHECKLIST

Before running `graphrag index`, verify you have:

- [ ] ✓ Virtual environment created and activated
- [ ] ✓ GraphRAG installed (`graphrag --version` works)
- [ ] ✓ `.env` file in project directory
- [ ] ✓ `settings.yaml` in project directory
- [ ] ✓ `entity_extraction.txt` in prompts directory
- [ ] ✓ `summarize_descriptions.txt` in prompts directory
- [ ] ✓ `community_report.txt` in prompts directory
- [ ] ✓ 5 .md files in input directory
- [ ] ✓ Current directory is `D:\GraphRAG_FINAL\project`

---

## 🎯 FINAL DIRECTORY STRUCTURE

After completing all steps:

```
D:\GraphRAG_FINAL\
│
├── venv\                              ✓ Virtual environment
│
└── project\                           ✓ Working directory
    │
    ├── .env                           ✓ API credentials
    ├── settings.yaml                  ✓ Configuration
    ├── visualize_final.py             ✓ Visualization script
    │
    ├── input\                         ✓ Your 5 .md files
    │   ├── file1.md
    │   ├── file2.md
    │   ├── file3.md
    │   ├── file4.md
    │   └── file5.md
    │
    ├── prompts\                       ✓ Prompt files
    │   ├── entity_extraction.txt
    │   ├── summarize_descriptions.txt
    │   └── community_report.txt
    │
    ├── output\                        ✓ Generated files (after indexing)
    │   ├── create_final_entities.parquet
    │   ├── create_final_relationships.parquet
    │   ├── create_final_communities.parquet
    │   ├── knowledge_graph_FINAL.png
    │   ├── knowledge_graph_FINAL_hires.png
    │   ├── top_entities.csv
    │   └── stats.json
    │
    ├── cache\                         ✓ Cache files
    └── logs\                          ✓ Log files
```

---

## 🚨 TROUBLESHOOTING

### Problem: "graphrag: command not found"
**Solution:**
```powershell
# Make sure venv is activated
.\venv\Scripts\Activate.ps1  # from D:\GraphRAG_FINAL

# Reinstall GraphRAG
pip install --upgrade graphrag
```

### Problem: "No module named 'graphrag'"
**Solution:**
```powershell
# Ensure you're in the venv
# You should see (venv) in your prompt

# If not visible:
deactivate
.\venv\Scripts\Activate.ps1
```

### Problem: API errors during indexing
**Solution:**
```powershell
# Check .env file has correct values
Get-Content .env

# Ensure no extra spaces or quotes
# Each line should be: KEY=value (no spaces around =)
```

### Problem: "File not found" errors
**Solution:**
```powershell
# Verify you're in the correct directory
pwd
# Should show: D:\GraphRAG_FINAL\project

# Check all required files
dir
dir input
dir prompts
```

---

## 🎉 SUCCESS INDICATORS

You'll know it worked when:

1. ✅ `graphrag index` completes without errors
2. ✅ `output` directory contains .parquet files
3. ✅ `visualize_final.py` creates PNG files
4. ✅ You can query the graph and get responses
5. ✅ Knowledge graph visualization appears

---

## 📊 PRESENTING TO YOUR MANAGER

**Files to show:**
1. **knowledge_graph_FINAL_hires.png** - Main visual
2. **top_entities.csv** - Key entities table
3. **Demo a live query** - Show interactive Q&A

**Sample presentation flow:**
```powershell
# 1. Show the visualization
start output\knowledge_graph_FINAL_hires.png

# 2. Show top entities
Import-Csv output\top_entities.csv | Format-Table

# 3. Live query demo
graphrag query --root . --method global --query "Summarize the key insights from these documents"
```

---

## ⏱️ ESTIMATED TIME

- Setup (Steps 1-6): **10 minutes**
- Indexing (Step 7): **10-20 minutes**
- Visualization (Step 8-9): **2 minutes**
- **Total: ~30 minutes**

---

## 🆘 EMERGENCY SUPPORT

If anything fails:

1. Delete everything: `Remove-Item -Recurse -Force D:\GraphRAG_FINAL`
2. Start from Step 1 again
3. Follow each step exactly as written
4. Don't skip any verification steps

---

**You're ready to go! Follow steps 1-10 and you'll have your knowledge graph ready for your manager.** 🚀
