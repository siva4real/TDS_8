"""
Quarterly Performance Analysis and Predictive Maintenance Recommendation
Author: 24f3004072@ds.study.iitm.ac.in
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from datetime import datetime

# Set style for better visualizations
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)

# Generate quarterly data
quarters = ['Q1 2023', 'Q2 2023', 'Q3 2023', 'Q4 2023', 
            'Q1 2024', 'Q2 2024', 'Q3 2024', 'Q4 2024']

# Performance scores (average should be 73.35)
# Total needed: 73.35 * 8 = 586.8
performance_scores = [78.5, 75.2, 72.1, 68.3, 76.4, 74.1, 70.8, 71.4]

# Verify the average
average_score = np.mean(performance_scores)
print(f"Average Performance Score: {average_score:.2f}")

# Create DataFrame
df = pd.DataFrame({
    'Quarter': quarters,
    'Performance_Score': performance_scores,
    'Target': [90] * len(quarters),
    'Industry_Benchmark': [82] * len(quarters)
})

# Add quarter number for trend analysis
df['Quarter_Num'] = range(1, len(quarters) + 1)

# Calculate key statistics
print("\n=== Key Statistics ===")
print(f"Mean: {df['Performance_Score'].mean():.2f}")
print(f"Median: {df['Performance_Score'].median():.2f}")
print(f"Std Dev: {df['Performance_Score'].std():.2f}")
print(f"Min: {df['Performance_Score'].min():.2f}")
print(f"Max: {df['Performance_Score'].max():.2f}")
print(f"Gap to Target: {90 - df['Performance_Score'].mean():.2f} points")
print(f"Gap to Benchmark: {82 - df['Performance_Score'].mean():.2f} points")

# Perform linear regression for trend analysis
slope, intercept, r_value, p_value, std_err = stats.linregress(
    df['Quarter_Num'], df['Performance_Score']
)
print(f"\n=== Trend Analysis ===")
print(f"Slope: {slope:.3f} (points per quarter)")
print(f"R-squared: {r_value**2:.3f}")
print(f"P-value: {p_value:.4f}")

# Predict future quarters if current trend continues
future_quarters = ['Q1 2025', 'Q2 2025', 'Q3 2025', 'Q4 2025']
future_quarter_nums = range(len(quarters) + 1, len(quarters) + 5)
predicted_scores = [slope * q + intercept for q in future_quarter_nums]

print(f"\n=== Predictions (Current Trend) ===")
for q, score in zip(future_quarters, predicted_scores):
    print(f"{q}: {score:.2f}")

# Calculate improvement needed
print(f"\n=== Improvement Analysis ===")
current_avg = df['Performance_Score'].mean()
improvement_needed = 90 - current_avg
print(f"Current Average: {current_avg:.2f}")
print(f"Target: 90")
print(f"Improvement Needed: {improvement_needed:.2f} points ({improvement_needed/current_avg*100:.1f}%)")

# Visualization 1: Trend Analysis with Forecast
plt.figure(figsize=(14, 7))
plt.plot(df['Quarter_Num'], df['Performance_Score'], 
         marker='o', linewidth=2, markersize=10, label='Actual Performance', color='#2E86AB')
plt.plot(df['Quarter_Num'], df['Target'], 
         '--', linewidth=2, label='Target (90)', color='#06A77D')
plt.plot(df['Quarter_Num'], df['Industry_Benchmark'], 
         '--', linewidth=2, label='Industry Benchmark (82)', color='#F77F00')

# Add trend line
trend_line = [slope * q + intercept for q in df['Quarter_Num']]
plt.plot(df['Quarter_Num'], trend_line, 
         ':', linewidth=2, label='Current Trend', color='#D62828', alpha=0.7)

# Add future predictions
plt.plot(future_quarter_nums, predicted_scores, 
         's--', linewidth=2, markersize=8, label='Forecast (No Intervention)', 
         color='#D62828', alpha=0.5)

plt.xlabel('Quarter', fontsize=12, fontweight='bold')
plt.ylabel('Performance Score', fontsize=12, fontweight='bold')
plt.title('Quarterly Performance Trend & Benchmark Comparison\nAverage: 73.35', 
          fontsize=14, fontweight='bold', pad=20)
plt.xticks(list(df['Quarter_Num']) + list(future_quarter_nums), 
           quarters + future_quarters, rotation=45, ha='right')
plt.legend(loc='best', fontsize=10)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('performance_trend.png', dpi=300, bbox_inches='tight')
print("\n✓ Saved: performance_trend.png")

# Visualization 2: Gap Analysis
plt.figure(figsize=(12, 7))
categories = ['Current\nPerformance', 'Industry\nBenchmark', 'Target']
values = [current_avg, 82, 90]
colors = ['#E63946', '#F77F00', '#06A77D']

bars = plt.bar(categories, values, color=colors, alpha=0.7, edgecolor='black', linewidth=2)
plt.axhline(y=current_avg, color='gray', linestyle='--', alpha=0.5)

# Add value labels on bars
for bar, val in zip(bars, values):
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height,
             f'{val:.2f}',
             ha='center', va='bottom', fontsize=14, fontweight='bold')

# Add gap annotations
plt.annotate('', xy=(0, 82), xytext=(0, current_avg),
            arrowprops=dict(arrowstyle='<->', color='red', lw=2))
plt.text(-0.3, (current_avg + 82)/2, f'Gap: {82-current_avg:.2f}\npoints',
         fontsize=10, color='red', fontweight='bold')

plt.annotate('', xy=(1, 90), xytext=(1, 82),
            arrowprops=dict(arrowstyle='<->', color='orange', lw=2))
plt.text(0.7, (82 + 90)/2, f'Gap: {90-82:.0f}\npoints',
         fontsize=10, color='orange', fontweight='bold')

plt.ylabel('Performance Score', fontsize=12, fontweight='bold')
plt.title('Performance Gap Analysis\nCurrent vs Benchmark vs Target', 
          fontsize=14, fontweight='bold', pad=20)
plt.ylim(0, 100)
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig('gap_analysis.png', dpi=300, bbox_inches='tight')
print("✓ Saved: gap_analysis.png")

# Visualization 3: Quarterly Performance Breakdown
plt.figure(figsize=(14, 6))
x = np.arange(len(quarters))
width = 0.25

plt.bar(x - width, df['Performance_Score'], width, 
        label='Performance', color='#2E86AB', alpha=0.8)
plt.bar(x, df['Industry_Benchmark'], width, 
        label='Benchmark', color='#F77F00', alpha=0.8)
plt.bar(x + width, df['Target'], width, 
        label='Target', color='#06A77D', alpha=0.8)

plt.xlabel('Quarter', fontsize=12, fontweight='bold')
plt.ylabel('Score', fontsize=12, fontweight='bold')
plt.title('Quarterly Performance vs Benchmark vs Target', 
          fontsize=14, fontweight='bold', pad=20)
plt.xticks(x, quarters, rotation=45, ha='right')
plt.legend(fontsize=11)
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig('quarterly_comparison.png', dpi=300, bbox_inches='tight')
print("✓ Saved: quarterly_comparison.png")

# Save data to CSV
df.to_csv('quarterly_data.csv', index=False)
print("✓ Saved: quarterly_data.csv")

# Generate summary report
summary_report = f"""
QUARTERLY PERFORMANCE ANALYSIS SUMMARY
Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
Analyst: 24f3004072@ds.study.iitm.ac.in

KEY METRICS:
- Average Performance Score: {current_avg:.2f}
- Target: 90.00
- Industry Benchmark: 82.00
- Gap to Target: {90 - current_avg:.2f} points
- Gap to Benchmark: {82 - current_avg:.2f} points

TREND ANALYSIS:
- Slope: {slope:.3f} points per quarter
- Trend Direction: {'Declining' if slope < 0 else 'Improving'}
- R-squared: {r_value**2:.3f}

FINDINGS:
1. Performance is consistently below both target and benchmark
2. {'Negative trend observed - performance declining over time' if slope < 0 else 'Slight improvement trend'}
3. Gap of {improvement_needed:.2f} points needs to be addressed
4. Without intervention, target unlikely to be reached

RECOMMENDATIONS:
Implement Predictive Maintenance Program to:
- Reduce downtime and improve operational efficiency
- Prevent performance degradation
- Close the {improvement_needed:.2f}-point gap to target
- Achieve industry-leading performance of 90+
"""

with open('analysis_summary.txt', 'w') as f:
    f.write(summary_report)

print("\n✓ Saved: analysis_summary.txt")
print("\n" + "="*60)
print("ANALYSIS COMPLETE")
print("="*60)
print(summary_report)

