import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Generate realistic synthetic data for customer support response times
# Different channels with different response time distributions
channels = []
response_times = []

# Email: slower, more variable (mean ~45 min, wider distribution)
email_times = np.random.gamma(shape=3, scale=15, size=300)
channels.extend(['Email'] * 300)
response_times.extend(email_times)

# Phone: fast, consistent (mean ~8 min, narrow distribution)
phone_times = np.random.gamma(shape=4, scale=2, size=280)
channels.extend(['Phone'] * 280)
response_times.extend(phone_times)

# Chat: moderate speed (mean ~15 min, moderate distribution)
chat_times = np.random.gamma(shape=3, scale=5, size=320)
channels.extend(['Chat'] * 320)
response_times.extend(chat_times)

# Social Media: highly variable (mean ~30 min, very wide distribution)
social_times = np.random.gamma(shape=2, scale=15, size=250)
channels.extend(['Social Media'] * 250)
response_times.extend(social_times)

# Create DataFrame
df = pd.DataFrame({
    'Support Channel': channels,
    'Response Time (minutes)': response_times
})

# Set Seaborn style and context for professional appearance
sns.set_style("whitegrid")
sns.set_context("talk", font_scale=0.9)

# Create figure with exact dimensions for 512x512 output
plt.figure(figsize=(8, 8))

# Create violinplot with professional styling
ax = sns.violinplot(
    data=df,
    x='Support Channel',
    y='Response Time (minutes)',
    palette='Set2',
    inner='quartile',
    linewidth=1.5,
    saturation=0.8
)

# Customize the plot
plt.title('Customer Support Response Time Distribution\nby Support Channel', 
          fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Support Channel', fontsize=13, fontweight='bold')
plt.ylabel('Response Time (minutes)', fontsize=13, fontweight='bold')

# Rotate x-axis labels for better readability
plt.xticks(rotation=0, ha='center')

# Add grid for better readability
ax.yaxis.grid(True, alpha=0.3)
ax.set_axisbelow(True)

# Adjust layout to prevent label cutoff
plt.tight_layout()

# Save the chart as PNG with exactly 512x512 pixels
plt.savefig('chart.png', dpi=64, bbox_inches='tight')

print("Chart generated successfully!")
print(f"Total records analyzed: {len(df)}")
print(f"\nSummary Statistics by Channel:")
print(df.groupby('Support Channel')['Response Time (minutes)'].describe().round(2))

