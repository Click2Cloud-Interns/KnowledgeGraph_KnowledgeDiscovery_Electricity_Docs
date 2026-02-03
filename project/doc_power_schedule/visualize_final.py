"""
GraphRAG Knowledge Graph Visualizer - FINAL VERSION
Run this after indexing completes to create your knowledge graph visualization
"""

import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from pathlib import Path
import sys

print("="*70)
print("GRAPHRAG KNOWLEDGE GRAPH VISUALIZER")
print("="*70)

# Check if output files exist
output_dir = Path("output")
entities_file = output_dir / "create_final_entities.parquet"
relationships_file = output_dir / "create_final_relationships.parquet"

# Try alternative file names
if not entities_file.exists():
    entities_file = output_dir / "entities.parquet"
if not relationships_file.exists():
    relationships_file = output_dir / "relationships.parquet"

if not entities_file.exists():
    print("\n❌ ERROR: Entity file not found!")
    print("Looking for files in output directory...")
    if output_dir.exists():
        parquet_files = list(output_dir.glob("*.parquet"))
        if parquet_files:
            print("\nFound these parquet files:")
            for f in parquet_files:
                print(f"  - {f.name}")
        else:
            print("No parquet files found in output directory")
    sys.exit(1)

print(f"\n✓ Loading entities from: {entities_file.name}")
print(f"✓ Loading relationships from: {relationships_file.name}")

# Load data
entities = pd.read_parquet(entities_file)
relationships = pd.read_parquet(relationships_file)

print(f"\n📊 Data Summary:")
print(f"   Total Entities: {len(entities)}")
print(f"   Total Relationships: {len(relationships)}")

# Show entity types
if 'type' in entities.columns:
    print(f"\n📋 Entity Types:")
    for etype, count in entities['type'].value_counts().items():
        print(f"   {etype}: {count}")

# Create graph
print(f"\n🔨 Building network graph...")
G = nx.Graph()

# Add nodes
title_col = 'title' if 'title' in entities.columns else 'name'
for _, entity in entities.iterrows():
    node_name = entity[title_col]
    G.add_node(node_name, 
               type=entity.get('type', 'unknown'),
               description=entity.get('description', ''))

# Add edges
source_col = 'source' if 'source' in relationships.columns else 'src'
target_col = 'target' if 'target' in relationships.columns else 'tgt'

for _, rel in relationships.iterrows():
    source = rel[source_col]
    target = rel[target_col]
    if source in G.nodes and target in G.nodes:
        G.add_edge(source, target,
                   description=rel.get('description', ''),
                   weight=rel.get('weight', 1.0))

print(f"✓ Graph created: {G.number_of_nodes()} nodes, {G.number_of_edges()} edges")

# Calculate statistics
print(f"\n📈 Network Statistics:")
print(f"   Density: {nx.density(G):.4f}")
print(f"   Connected components: {nx.number_connected_components(G)}")

# Create visualization
print(f"\n🎨 Creating visualization...")
fig, ax = plt.subplots(figsize=(24, 24))

# Layout
print("   Computing layout...")
pos = nx.spring_layout(G, k=1.5, iterations=50, seed=42)

# Node colors by type
entity_types = entities['type'].unique() if 'type' in entities.columns else ['unknown']
colors = plt.cm.Set3(range(len(entity_types)))
type_to_color = dict(zip(entity_types, colors))

node_colors = []
for node in G.nodes():
    node_type = G.nodes[node].get('type', 'unknown')
    node_colors.append(type_to_color.get(node_type, 'gray'))

# Node sizes based on degree
degrees = dict(G.degree())
node_sizes = [500 + degrees[node] * 100 for node in G.nodes()]

# Draw
print("   Drawing graph...")
nx.draw_networkx_edges(G, pos, alpha=0.2, width=1, edge_color='gray', ax=ax)
nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=node_sizes,
                       alpha=0.8, edgecolors='black', linewidths=1.5, ax=ax)

# Labels for high-degree nodes
high_degree_threshold = sorted(degrees.values(), reverse=True)[:min(30, len(degrees))]
min_degree = min(high_degree_threshold) if high_degree_threshold else 0
labels = {node: node for node in G.nodes() if degrees[node] >= min_degree}
nx.draw_networkx_labels(G, pos, labels, font_size=10, font_weight='bold', ax=ax)

# Title
ax.set_title(f"Knowledge Graph - Power Trading Documents\n{G.number_of_nodes()} Entities | {G.number_of_edges()} Relationships",
            fontsize=22, fontweight='bold', pad=20)

# Legend
from matplotlib.patches import Patch
legend_elements = [Patch(facecolor=type_to_color[t], label=t.upper()) 
                   for t in entity_types]
ax.legend(handles=legend_elements, loc='upper left', fontsize=12,
         title='Entity Types', title_fontsize=14)

ax.axis('off')
plt.tight_layout()

# Save
output_file = "output/knowledge_graph_FINAL.png"
plt.savefig(output_file, dpi=300, bbox_inches='tight', facecolor='white')
print(f"\n✅ Visualization saved: {output_file}")

output_file_hires = "output/knowledge_graph_FINAL_hires.png"
plt.savefig(output_file_hires, dpi=600, bbox_inches='tight', facecolor='white')
print(f"✅ High-res saved: {output_file_hires}")

# Export top entities
print(f"\n💾 Exporting data summaries...")
entity_connections = pd.concat([
    relationships[source_col],
    relationships[target_col]
]).value_counts()

top_entities_df = pd.DataFrame({
    'Entity': entity_connections.index[:20],
    'Connections': entity_connections.values[:20]
})
top_entities_df.to_csv('output/top_entities.csv', index=False)
print(f"✓ Top entities: output/top_entities.csv")

# Show the graph
print(f"\n👁️  Displaying graph window...")
plt.show()

print(f"\n{'='*70}")
print("✅ COMPLETE!")
print("="*70)
print("\nGenerated files:")
print("  • output/knowledge_graph_FINAL.png")
print("  • output/knowledge_graph_FINAL_hires.png")
print("  • output/top_entities.csv")
print("\n" + "="*70 + "\n")
