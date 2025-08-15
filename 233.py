import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.gridspec as gridspec

data = {
    "Group": [
        "Control Group", "No RAG Group", "No FT Group",
        "No Feedback Agent Group", "No Debugging Agent Group"
    ],
    "C_ContextualRelevancy": [5.0, 3.8, 5.0, 4.7, 4.6],
    "C_AnswerRelevancy": [4.8, 4.2, 4.2, 4.3, 4.2],
    "C_Correctness": [4.9, 4.3, 3.9, 4.1, 4.5],
    "U_ContextualRelevancy": [5.0, 4.0, 4.8, 4.6, 4.7],
    "U_AnswerRelevancy": [4.9, 4.1, 4.0, 4.2, 4.3],
    "U_Correctness": [5.0, 4.2, 4.0, 4.0, 4.6],
    "E_ContextualRelevancy": [5.0, 3.9, 5.0, 4.7, 4.6],
    "E_AnswerRelevancy": [4.7, 4.0, 4.1, 4.4, 4.5],
    "E_Correctness": [4.8, 4.3, 4.2, 4.2, 4.6]
}

df = pd.DataFrame(data)
COLORS = ['#4e79a7', '#f28e2c', '#76b7b2', '#e15759', '#59a14f']
attribute_groups = [
    ("Coverageability", ["C_ContextualRelevancy", "C_AnswerRelevancy", "C_Correctness"]),
    ("Understandability", ["U_ContextualRelevancy", "U_AnswerRelevancy", "U_Correctness"]),
    ("Extendability", ["E_ContextualRelevancy", "E_AnswerRelevancy", "E_Correctness"])
]


def create_comparison_chart(groups, title, filename):
    fig = plt.figure(figsize=(15, 10), dpi=100)
    gs = gridspec.GridSpec(1, 3, figure=fig, width_ratios=[1, 1, 1], wspace=0.25)
    
    df_filtered = df[df["Group"].isin(groups)].reset_index(drop=True)
    
    # Draw 3 subgraphs
    for i, (group_name, metrics) in enumerate(attribute_groups):
        ax = fig.add_subplot(gs[i])
        
        bar_width = 0.25
        index = np.arange(len(df_filtered))
        for j, metric in enumerate(metrics):
            ax.bar(index + j * bar_width, df_filtered[metric], bar_width, 
                   color=COLORS[j], alpha=0.9, edgecolor='white', linewidth=1,
                   label=metric.split('_')[1])
        
        for x in index:
            for j, metric in enumerate(metrics):
                value = df_filtered.loc[x, metric]
                ax.text(x + j * bar_width, value + 0.03, f'{value:.1f}', 
                        ha='center', va='bottom', fontsize=10, fontweight='bold')
        
        ax.set_title(group_name, fontsize=16, fontweight='bold', pad=12)
        ax.set_xlabel('Groups', fontsize=12, labelpad=10)
        ax.set_xticks(index + bar_width)
        ax.set_xticklabels(df_filtered["Group"], fontsize=11, rotation=15, ha='right')
        ax.tick_params(axis='y', labelsize=10)
        ax.set_ylim(3.0, 5.5)
        ax.yaxis.grid(True, linestyle='--', alpha=0.3)
        ax.set_axisbelow(True)
        
        for spine in ax.spines.values():
            spine.set_visible(True)
            spine.set_alpha(0.5)
        
    
    fig.suptitle(title, fontsize=20, fontweight='bold', y=0.95)
    
    plt.tight_layout(rect=[0, 0, 1, 0.95])
    
    plt.savefig(filename, dpi=300, bbox_inches='tight', metadata={'Software': None})
    plt.close()

create_comparison_chart(
    groups=["Control Group", "No RAG Group"],
    title='Comparison: Control Group vs No RAG Group',
    filename='control_vs_noRAG.png'
)

create_comparison_chart(
    groups=["Control Group", "No FT Group"],
    title='Comparison: Control Group vs No Fine-Tuning Group',
    filename='control_vs_noFT.png'
)

create_comparison_chart(
    groups=["Control Group", "No Feedback Agent Group", "No Debugging Agent Group"],
    title='Comparison: Control Group vs Single-Agent Groups',
    filename='control_vs_single_agent.png'
)