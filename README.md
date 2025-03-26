![Screenshot_26-3-2025_233742_localhost](https://github.com/user-attachments/assets/7643e557-fa6f-4425-b2f4-8305e818b4b2)
# IPL Win Predictor

A Streamlit-based web application that predicts the winning probability of IPL (Indian Premier League) cricket matches in real-time based on current match situations.

## Features

- Real-time win probability prediction for IPL matches
- Interactive user interface built with Streamlit
- Support for all IPL teams and major cricket venues
- Instant probability calculations based on multiple match parameters

## Prerequisites

- Python 3.x
- pip (Python package installer)

## Required Libraries

```bash
streamlit
pandas
pickle
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/rohitbansal2005/IPL-Win-Predictor
cd ipl-win-predictor
```

2. Install the required packages:
```bash
pip install -r requirements.txt
```

3. Ensure the trained model file (`pipe.pkl`) is present in the root directory.

## Usage

1. Run the Streamlit application:
```bash
streamlit run app.py
```

2. Input the following match parameters:
   - Batting team
   - Bowling team
   - Host city
   - Target score
   - Current score
   - Overs completed
   - Wickets fallen

3. Click on "Predict Probability" to see the winning chances for both teams

## Input Validation

The application includes several validation checks:
- Overs cannot be zero
- Overs completed cannot exceed 20
- Current score cannot exceed the target

## Supported Teams

- Sunrisers Hyderabad
- Mumbai Indians
- Royal Challengers Bangalore
- Kolkata Knight Riders
- Kings XI Punjab
- Chennai Super Kings
- Rajasthan Royals
- Delhi Capitals

## Supported Cities

The application supports multiple cricket venues across:
- India (e.g., Mumbai, Delhi, Chennai, etc.)
- South Africa (e.g., Cape Town, Durban, etc.)
- UAE (Abu Dhabi, Sharjah)

## Model Information

The prediction is based on a machine learning model (stored in `pipe.pkl`) that takes into account various match parameters including:
- Current run rate (CRR)
- Required run rate (RRR)
- Wickets remaining
- Balls remaining
- Runs left to win

## Contributing

Feel free to fork the repository and submit pull requests for any improvements.
