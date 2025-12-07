import marimo

__generated_with = "0.8.0"
app = marimo.App(width="medium")


@app.cell
def _(mo):
    # Email: 24f3004072@ds.study.iitm.ac.in
    # This cell imports necessary libraries for data analysis and visualization
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns

    # Set up plotting style
    plt.style.use('seaborn-v0_8')
    sns.set_palette("husl")

    return np, pd, plt, sns


@app.cell
def _(np, pd):
    # Data Generation Cell
    # This cell creates synthetic data with relationships between variables
    # The data will be used in subsequent cells for analysis

    np.random.seed(42)  # For reproducible results
    n_samples = 200

    # Create correlated variables
    x1 = np.random.normal(50, 10, n_samples)
    x2 = x1 * 0.8 + np.random.normal(0, 5, n_samples)  # Correlated with x1
    x3 = x1 * 0.3 + x2 * 0.5 + np.random.normal(0, 3, n_samples)  # Depends on both x1 and x2

    # Create target variable with non-linear relationship
    y = 2 * x1 + 0.5 * x2**2 + np.random.normal(0, 2, n_samples)

    # Create DataFrame
    df = pd.DataFrame({
        'feature_1': x1,
        'feature_2': x2,
        'feature_3': x3,
        'target': y
    })

    # Data flow: This cell generates the dataset that will be used in visualization cells below
    return df, n_samples


@app.cell
def _(df):
    # Data Summary Cell
    # This cell depends on the df variable from the data generation cell above
    # It provides summary statistics for the dataset

    data_summary = df.describe()
    correlation_matrix = df.corr()

    # Data flow: Summary statistics and correlations calculated here will be displayed in markdown below
    return correlation_matrix, data_summary


@app.cell
def _(mo):
    # Interactive Widget Cell
    # This cell creates an interactive slider widget
    # The slider value will control filtering and visualization parameters

    sample_size_slider = mo.ui.slider(
        start=50,
        stop=200,
        step=10,
        value=100,
        label="Sample Size for Analysis"
    )

    # Data flow: The slider value will be used in the filtering cell below
    return sample_size_slider,


@app.cell
def _(df, sample_size_slider):
    # Data Filtering Cell
    # This cell depends on both the df from data generation and sample_size_slider from widget cell
    # It filters the dataset based on the interactive slider value

    filtered_df = df.sample(n=sample_size_slider.value, random_state=42)

    # Data flow: Filtered data will be used in the visualization and dynamic markdown cells
    return filtered_df,


@app.cell
def _(filtered_df, plt, sns):
    # Visualization Cell
    # This cell depends on the filtered_df from the filtering cell above
    # It creates scatter plots showing relationships between variables

    fig, axes = plt.subplots(2, 2, figsize=(12, 10))

    # Scatter plot: feature_1 vs target
    axes[0,0].scatter(filtered_df['feature_1'], filtered_df['target'], alpha=0.6)
    axes[0,0].set_xlabel('Feature 1')
    axes[0,0].set_ylabel('Target')
    axes[0,0].set_title('Feature 1 vs Target Relationship')
    axes[0,0].grid(True, alpha=0.3)

    # Scatter plot: feature_2 vs target
    axes[0,1].scatter(filtered_df['feature_2'], filtered_df['target'], alpha=0.6, color='orange')
    axes[0,1].set_xlabel('Feature 2')
    axes[0,1].set_ylabel('Target')
    axes[0,1].set_title('Feature 2 vs Target Relationship')
    axes[0,1].grid(True, alpha=0.3)

    # Scatter plot: feature_1 vs feature_2
    axes[1,0].scatter(filtered_df['feature_1'], filtered_df['feature_2'], alpha=0.6, color='green')
    axes[1,0].set_xlabel('Feature 1')
    axes[1,0].set_ylabel('Feature 2')
    axes[1,0].set_title('Feature 1 vs Feature 2 Correlation')
    axes[1,0].grid(True, alpha=0.3)

    # Histogram of target variable
    axes[1,1].hist(filtered_df['target'], bins=20, alpha=0.7, color='purple', edgecolor='black')
    axes[1,1].set_xlabel('Target Value')
    axes[1,1].set_ylabel('Frequency')
    axes[1,1].set_title('Target Variable Distribution')
    axes[1,1].grid(True, alpha=0.3)

    plt.tight_layout()

    # Data flow: This visualization will be displayed and depends on the filtered dataset
    return fig,


@app.cell
def _(filtered_df, sample_size_slider):
    # Dynamic Markdown Cell
    # This cell depends on both filtered_df and sample_size_slider
    # It generates dynamic markdown content based on the current widget state

    correlation_f1_target = filtered_df['feature_1'].corr(filtered_df['target'])
    correlation_f2_target = filtered_df['feature_2'].corr(filtered_df['target'])
    correlation_f1_f2 = filtered_df['feature_1'].corr(filtered_df['feature_2'])

    mean_target = filtered_df['target'].mean()
    std_target = filtered_df['target'].std()

    # Create dynamic markdown content
    markdown_content = f"""
    ## Interactive Data Analysis Results

    **Current Sample Size:** {sample_size_slider.value} observations

    ### Correlation Analysis
    - **Feature 1 vs Target:** {correlation_f1_target:.3f}
    - **Feature 2 vs Target:** {correlation_f2_target:.3f}
    - **Feature 1 vs Feature 2:** {correlation_f1_f2:.3f}

    ### Target Variable Statistics
    - **Mean:** {mean_target:.2f}
    - **Standard Deviation:** {std_target:.2f}

    ### Key Insights
    {'Feature 1 shows a strong positive correlation with the target variable.' if abs(correlation_f1_target) > 0.5 else 'Feature 1 has a moderate correlation with the target.'}
    {'Feature 2 shows a strong positive correlation with the target variable.' if abs(correlation_f2_target) > 0.5 else 'Feature 2 has a moderate correlation with the target.'}
    {'Features 1 and 2 are highly correlated.' if abs(correlation_f1_f2) > 0.7 else 'Features 1 and 2 show moderate correlation.'}
    """

    # Data flow: This dynamic markdown depends on the filtered dataset and updates when slider changes
    return markdown_content,


@app.cell
def _(mo, data_summary, correlation_matrix, sample_size_slider, fig, markdown_content):
    # Final Output Cell
    # This cell combines all outputs and displays them
    # It depends on multiple variables from different cells throughout the notebook

    mo.vstack([
        mo.md("# Interactive Data Analysis Notebook"),
        mo.md("## Dataset Summary"),
        mo.md("### Descriptive Statistics"),
        data_summary,
        mo.md("### Correlation Matrix"),
        correlation_matrix,
        mo.md("## Interactive Analysis"),
        sample_size_slider,
        mo.md("### Visualizations"),
        fig,
        mo.md(markdown_content)
    ])

    # Data flow: This cell aggregates outputs from all previous cells
    return


if __name__ == "__main__":
    app.run()
