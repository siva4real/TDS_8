# Customer Analytics: Response Time Distribution by Support Channel

## Project Overview

This project provides a professional data visualization analyzing customer support response times across different communication channels. Created for Hickle Wolf and Hilpert's client analysis, this visualization helps executives understand support efficiency patterns and make data-driven decisions.

## Business Context

The visualization demonstrates the distribution and density of customer support response times across four key channels:
- **Email**: Traditional email support
- **Phone**: Direct phone assistance
- **Chat**: Live chat support
- **Social Media**: Social platform engagement

## Files

- `chart.py` - Python script that generates the Seaborn violinplot visualization
- `chart.png` - Generated chart image (512x512 pixels)
- `README.md` - Project documentation

## Technical Details

### Technologies Used
- Python 3.x
- Seaborn - Statistical data visualization
- Matplotlib - Plotting library
- Pandas - Data manipulation
- NumPy - Numerical computing

### Chart Specifications
- **Type**: Violinplot with quartile markers
- **Dimensions**: 512x512 pixels
- **Style**: Professional whitegrid with Set2 color palette
- **Data**: Synthetic data representing 1,150 customer support interactions

## How to Run

1. Install required dependencies:
```bash
pip install seaborn matplotlib pandas numpy
```

2. Run the script:
```bash
python chart.py
```

3. The chart will be saved as `chart.png` in the current directory

## Key Insights

The violinplot reveals:
- **Phone support** shows the fastest and most consistent response times
- **Email support** exhibits higher variability in response times
- **Chat support** demonstrates moderate speed with good consistency
- **Social Media** shows high variability in response patterns

The width of each violin indicates the density of data points at different response time values, while the inner quartile lines show the statistical distribution.

## Contact

Email: 24f3004072@ds.study.iitm.ac.in

## License

This project is created for educational and business analytics purposes.

