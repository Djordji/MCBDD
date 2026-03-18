# Infection Probability Visualization

## Overview

A Python application that visualizes the probability of infection given a positive test result across different prevalence rates and test specificities.

## Requirements

- Python 3.10 or higher
- Packages: `numpy==2.4.3`, `matplotlib==3.10.8`

## Setup and Installation

### 1. Create a Virtual Environment

Create a `.venv` directory in your project folder:

```bash
# Navigate to your project directory
cd /path/to/your/project

# Create virtual environment
python -m venv .venv
```

### 2. Activate the Virtual Environment

**On Windows:**
```bash
.venv\Scripts\activate
```

**On macOS/Linux:**
```bash
source .venv/bin/activate
```

### 3. Install Dependencies

Install the required packages from `requirements.txt`:

```bash
pip install -r requirements.txt
```

## Running the Application

Once the environment is set up and dependencies are installed, run the visualization:

```bash
python invection_propability_visualization.py
```

The application will generate and display a plot showing:
- X-axis: Infection prevalence rate (0% to 50%)
- Y-axis: Probability of being infected given a positive test result (0% to 100%)
- Multiple curves for different test specificities (99%, 99.9%, 99.99%, 99.999%)