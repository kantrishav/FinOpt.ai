import yfinance as yf
#import os
from openai import OpenAI
import streamlit as st
#import anthropic
#from st_audiorec import st_audiorec
import openai
#import tempfile 
#import matplotlib.pyplot as plt
#import plotly.express as px
import warnings
#from config import OPENAI_API_KEY
st.set_page_config(layout="wide")


warnings.filterwarnings('ignore')


st.markdown("""
        <style>
               .block-container {
                    padding-top: 1rem;
                    padding-bottom: 0rem;
                    padding-left: 5rem;
                    padding-right: 5rem;
                }
        </style>
        """, unsafe_allow_html=True)

st.markdown(
    """
    <style>
    .stApp {
        background-color: 	#000000; 
    }
    </style>
    """,
    unsafe_allow_html=True
)


st.markdown(
    """
    <h1 style='color: #FFFFFF;'>FinOpt.ai</h1>
    """, unsafe_allow_html=True
)

#st.write("""# FinStock.ai : An AI Option & Futures Analyzer 💹""")





#Dow Jones 
ticker = '^DJI'
ticker_sp500 = '^GSPC'
dow_data = yf.download(ticker, period='5d' ,  progress=False)
qqq_data  = yf.download('QQQ', period='5d' ,  progress=False)
sp500_data1  = yf.download(ticker_sp500, period='5d' , progress=False)

gold_data  = yf.download('GC=F', period='5d' , progress=False)
gold_data = gold_data.sort_index(ascending=False)

oil_data  = yf.download('CL=F', period='5d' , progress=False)
oil_data = oil_data.sort_index(ascending=False)


sp500_kpi = round(float(sp500_data1.iloc[4]["Adj Close"]), 2)
prev_day_sp500 = round(float(sp500_data1.iloc[3]["Adj Close"]), 2)
today_sp500 = round(float(sp500_data1.iloc[4]["Adj Close"]), 2)
change_sp500 = ((today_sp500-prev_day_sp500)/prev_day_sp500)*100
change_sp500 = round(float(change_sp500),2)
change_sp500 = f"{change_sp500} %"



dow_kpi = round(float(dow_data.iloc[4]["Adj Close"]), 2)
dow_prev  = round(float(dow_data.iloc[3]["Adj Close"]), 2)
dow_change =  ((dow_kpi-dow_prev)/dow_prev)*100
dow_change = round(float(dow_change),2)
dow_change = f"{dow_change} %"



qqq_kpi = round(float(qqq_data.iloc[4]["Adj Close"]), 2)
qqq_prev  = round(float(qqq_data.iloc[3]["Adj Close"]), 2)
qqq_change =  ((qqq_kpi-qqq_prev)/dow_prev)*100
qqq_change = round(float(qqq_change),2)
qqq_change = f"{qqq_change} %"


gold_kpi = round(float(gold_data.iloc[0]["Adj Close"]), 2)
gold_prev  = round(float(gold_data.iloc[1]["Adj Close"]), 2)
gold_change =  ((gold_kpi-gold_prev)/gold_prev)*100
gold_change = round(float(gold_change),2)
gold_change = f"{gold_change} %"

oil_kpi = round(float(oil_data.iloc[0]["Adj Close"]), 2)
oil_prev  = round(float(oil_data.iloc[1]["Adj Close"]), 2)
oil_change =  ((oil_kpi-oil_prev)/oil_prev)*100
oil_change = round(float(oil_change),2)
oil_change = f"{oil_change} %"



var = '#000000'



col2_html = f"""
    <style>
    .kpi-box {{
        background-color: {var};
        padding: 10px;
        border-radius: 10px;
        display: flex;
        flex-direction: column; /* Stack items vertically */
        justify-content: center;
        align-items: center;
        height: 120px;
        width: 230px;
        font-size: 1.2em;
        font-weight: bold;
        color: #0A64EE;
    }}
    .kpi-label {{
        font-size: 24px; 
        font-weight: bold; 
        color: #0ff550;
        margin-bottom: 1px; /* Space below the label */
    }}
    .kpi-value {{
        font-size: 32px;
        margin-bottom: 1px; /* Space below the value */
    }}
        .kpi-delta {{
        font-size: 20px;
        margin-bottom: 1px; /* Space below the value */
    }}
    </style>

    <div class='kpi-box'>
        <div class='kpi-label'>Dow Jones</div>
        <div class='kpi-value'>{dow_kpi}</div>
        <div class='kpi-delta'>{dow_change}</div>
    </div>
"""



#---------------------- Column Test ----------


# Create the first row with 3 columns
col1, col2, col3 , col4 , col5 = st.columns(5)

# Add content to each column in the first row
with col1:
    
        st.markdown(
        f"""
        <div class='kpi-box'>
        <div style="color: #0ff550; font-size: 24px; font-weight: bold;">SPY 500</div>
            <div class='kpi-value'>{sp500_kpi}</div>
            <div class='kpi-delta'>{change_sp500}</div>
        </div>
        """, 
        unsafe_allow_html=True
    )
    


with col2:
    #st.markdown("<h2 style='text-align: center;'>🎈</h2>", unsafe_allow_html=True)
    st.write(col2_html, unsafe_allow_html=True)


# Render the custom-styled version (if needed)




with col3:
        st.markdown(
        f"""
        <div class='kpi-box'>
        <div style="color: #0ff550; font-size: 24px; font-weight: bold;">QQQ</div>
            <div class='kpi-value'>{qqq_kpi}</div>
            <div class='kpi-delta'>{qqq_change}</div>
        </div>
        """, 
        unsafe_allow_html=True
    )

with col4:
        st.markdown(
        f"""
        <div class='kpi-box'>
        <div style="color: #0ff550; font-size: 24px; font-weight: bold;">Gold</div>
            <div class='kpi-value'>{gold_kpi}</div>
            <div class='kpi-delta'>{gold_change}</div>
        </div>
        """, 
        unsafe_allow_html=True
    )


with col5:
        st.markdown(
        f"""
        <div class='kpi-box'>
        <div style="color: #0ff550; font-size: 24px; font-weight: bold;">Crude Oil</div>
            <div class='kpi-value'>{oil_kpi}</div>
            <div class='kpi-delta'>{oil_change}</div>
        </div>
        """, 
        unsafe_allow_html=True
    )




#--------------------------------





#----------------------------------


st.write("   ")
st.write("   ")
st.write("   ")
st.write("   ")

client = OpenAI(
    # This is the default and can be omitted
    api_key= st.secrets["OPEN_AI_KEY"],
)

st.markdown(
    """
    <div style='text-align: center;'>
        <h1 style='color: #FFFFFF;'> Do You Want To Analyze Stock Options Using AI ? </h1>
    </div>
    """,
    unsafe_allow_html=True
)



st.markdown(
    """
    <div style='text-align: center;'>
        <h1 style='color: #8c8c8c; font-size: 20px;'>Choose the best option strategy for you. Just paste your option chain data.</h1>
    </div>
    """,
    unsafe_allow_html=True
)


st.markdown(
    """
    <div style='text-align: center;'>
        <h1 style='color: #0ff550; font-size: 20px;'>Drop Your Option Chain in the Box and hit Submit !</h1>
    </div>
    """,
    unsafe_allow_html=True
)



#-------

st.markdown(
    """
    <style>
    /* Center the text area by setting its container's max-width and using margin auto */
    div[data-testid="stTextArea"] {
        max-width: 950px; /* Adjust as needed to control the width */
        margin: 0 auto; /* Centers the container horizontally */
        padding: 10px; /* Optional padding for additional space */
        position: relative; /* Enable positioning for child elements */
    }
    div[data-testid="stTextArea"] textarea {
        background-color: #f0f0f5; /* Light gray background */
        color: #333333; /* Dark text color */
        border: 2px solid #3498db; /* Blue border */
        border-radius: 10px;
        padding: 10px;
        width: 100%; /* Ensure the textarea fills its container */
    }
    .icon-container {
        position: absolute; /* Position the icons relative to the text area */
        top: -310px; /* Adjust this value to position icons above the textarea */
        left: 50%; /* Center the icons horizontally */
        transform: translateX(-50%); /* Center alignment adjustment */      
    }
    .icon-container img {
        width: 100px; /* Adjust icon size */
        height: 45px; /* Adjust icon size */
        margin-left: 30px; /* Space between icons */
    }
    </style>
    """,
    unsafe_allow_html=True
)



option_text_input = st.text_area('', height=310)

option_prompt = "You are an AI Option trader. Below is the text format of Option Chain of an asset. Analyze and share top 3 strategies using option chain data uploaded and share how can we build that strategies with the data shared.  Here is the option chain text : "

option_final_prompt = option_prompt + option_text_input


with st.container():
    a, b, c = st.columns([0.49, 1, 1])  # Adjust the width ratios as needed
    with b:  # This places it in the center column
        st.button("Submit",key="submit_button_1")




# Add the icons in the bottom right corner
st.markdown(
    """
    <div class="icon-container">
        <img src="https://thevyatergroup.com/wp-content/uploads/2021/03/logo-amazon-404px-grey.png" alt="Icon 1">
        <img src="https://www.krenerbookkeeping.com/wp-content/uploads/2018/07/logo-microsoft-404px-grey.png" alt="Icon 2">
        <img src="https://mohamadfaizal.com/wp-content/uploads/2017/05/logo-google-404px-grey.png" alt="Icon 3">

        
    </div>
    """,
    unsafe_allow_html=True
)






if len(option_final_prompt) > 500:
    chat_completion = client.chat.completions.create( messages=[{"role": "user","content": option_final_prompt,}],model="gpt-3.5-turbo",)
    op = chat_completion.choices[0].message.content
    op = op.replace('\n', '<br>')
    st.markdown(f'<p style="color:white;">{op}</p>', unsafe_allow_html=True)
    #st.markdown(f'<p style="color:white;">{op}</p>', unsafe_allow_html=True)
    #st.write(op)
else:
    st.write('')


#---------Betting App------------------------------------------------------


curve_kpi = f"""
    <style>
    .kpi-box-curve {{
        background-color: {var};
        padding: 10px;
        border-radius: 10px;
        display: flex;
        flex-direction: column; /* Stack items vertically */
        justify-content: center;
        align-items: center;
        height: 120px;
        width: 500px;
        font-size: 1.2em;
        font-weight: bold;
        color: #0A64EE;
    }}
    .kpi-label-curve {{
        font-size: 24px; 
        font-weight: bold; 
        color: #0ff550;
        margin-bottom: 1px; /* Space below the label */
    }}
    .kpi-value-curve {{
        font-size: 32px;
        margin-bottom: 1px; /* Space below the value */
    }}
    </style>
"""




st.markdown(
    """
    <h1 style='color: #FFFFFF;'>Option Probablity Simulator</h1>
    """, unsafe_allow_html=True
)


import random

def simulate_betting(initial_portfolio, risk_reward_ratio, win_probability,
                     frequency_of_trade, num_bets_at_once, bet_percentage):
  """
  Simulates a betting strategy over a year.

  Args:
    initial_portfolio: Starting amount of money.
    risk_reward_ratio: Ratio of potential loss to potential win (e.g., 1:1).
    win_probability: Probability of winning a single bet (between 0 and 1).
    frequency_of_trade: Number of days between bets.
    num_bets_at_once: Number of bets placed simultaneously.
    bet_percentage: Percentage of the portfolio to use for each bet.

  Returns:
    A tuple containing:
      - final_portfolio_value: Portfolio value at the end of the year.
      - max_drawdown: Maximum percentage decline from a peak value.
      - wins: Number of winning bets.
      - losses: Number of losing bets.
  """

  portfolio_value = initial_portfolio
  max_portfolio_value = initial_portfolio
  max_drawdown = 0
  wins = 0
  losses = 0

  for day in range(0, 365, frequency_of_trade):
    bet_amount = portfolio_value * (bet_percentage / 100)

    for _ in range(num_bets_at_once):
      if random.random() < win_probability:
        portfolio_value += bet_amount
        wins += 1
      else:
        portfolio_value -= bet_amount
        losses += 1

    max_portfolio_value = max(max_portfolio_value, portfolio_value)
    drawdown = (max_portfolio_value - portfolio_value) / max_portfolio_value
    max_drawdown = max(max_drawdown, drawdown)

  return portfolio_value, max_drawdown, wins, losses

st.markdown(
    """
    <style>
    /* Targeting all labels within the Streamlit app */
    .stNumberInput > label ,.stSlider > label ,.stSelectbox > label {
        color: #00FF00;  /* Set label color to green */
        font-weight: bold; /* Optionally, make the text bold */
    }

      /* Customize the slider track and thumb */
    .stSlider > div > div > div > input[type=range] {
        accent-color: #00FF00;  /* Change the slider's accent color (supported in most modern browsers) */
    }


    </style>
    """,
    unsafe_allow_html=True
)

# Create the first row with 3 columns
c1, c2, c3 , c4 , c5 , c6 , c7 ,c8= st.columns(8)

# Add content to each column in the first row
with c1:
    initial_portfolio = st.number_input("Initial Investment", value = 100000)

with c2:
    risk_reward_ratio = st.number_input("Risk Reward Ratio", value=1)    # Not directly used in the calculation, but you have it as a parameter

with c3:
    win_probability = st.number_input("Win Probablity", value=0.7)

with c4:
    frequency_of_trade = st.number_input("Frequency Trade", value=14) 


with c5:
    num_bets_at_once = st.number_input("Number of Bets", value=1)

with c6:
    bet_percentage = st.number_input("Bet Percentage", value=2)

with c7:
    #sim_count = st.slider("No. Of Simulations", value=10)
    sim_count = st.selectbox(
    "No. Of Simulations",
    (10,50,100), index = 2,
)
    #sim_count = st.number_input("No. Of Simulations", value=10)

# Run a single simulation
final_portfolio_value, max_drawdown, wins, losses = simulate_betting(
    initial_portfolio, risk_reward_ratio, win_probability, frequency_of_trade,
    num_bets_at_once, bet_percentage
)




#st.write(final_portfolio_value)
#st.write(max_drawdown)

import pandas as pd
results = []
for i in range(sim_count):
  final_portfolio_value, max_drawdown, _, _ = simulate_betting(
      initial_portfolio, risk_reward_ratio, win_probability, frequency_of_trade,
      num_bets_at_once, bet_percentage
  )
  #st.write(f"Simulation {i+1}: Final Portfolio Value = {final_portfolio_value}, Max Drawdown = {max_drawdown*100:.2f}%")
  results.append({
        "Simulation": i + 1,
        "Final Portfolio Value": final_portfolio_value,
        "Max Drawdown (%)": max_drawdown * 100
    })

# Create a DataFrame from the results
df_results = pd.DataFrame(results)

final_portfolio_value = int(final_portfolio_value)

st.markdown(
    f"""
    <div class='kpi-box' style="position: relative; left: 5px; top: 40px;">
        <div style="color: #0ff550; font-size: 30px; font-weight: bold;">Portfolio Value</div>
        <div class='kpi-value'>{final_portfolio_value}</div>
    </div>
    """, 
    unsafe_allow_html=True
)

draw_down_num = float(max_drawdown*100)
draw_down_num=f"{draw_down_num:.2f}%"

st.markdown(
    f"""
    <div class='kpi-box' style="position: relative; left: 300px; top: -75px;">
        <div style="color: #0ff550; font-size: 30px; font-weight: bold;">Max Drawdown</div>
        <div class='kpi-value'>{draw_down_num}</div>
    </div>
    """, 
    unsafe_allow_html=True
)

# You can now display or save the DataFrame
#st.write(df_results)

import plotly.express as px

fig_simulation = px.line(df_results, x="Simulation", y="Final Portfolio Value", title="",
              labels={"Simulation": "Simulation No", "Final Portfolio Value": "Final Portfolio Value"},
              markers=True)  # Add markers to the line

# Update layout for black background and no gridlines
fig_simulation.update_layout(
    paper_bgcolor='black',  # Background color of the chart
    plot_bgcolor='black',   # Background color of the plotting area
    font_color='white',      # Font color for text
    xaxis=dict(showgrid=False),  # Remove gridlines
    yaxis=dict(showgrid=False) ,  # Remove gridlines
    width=1400,  # Set width of the plot
    height=450
)

# Update line color and thickness
fig_simulation.update_traces(line=dict(color='#00FF00', width=4))
 
st.plotly_chart(fig_simulation)


#--------------------------------------------------------------------------



#-------------Volatility Surface-------------------------------
import yfinance as yf
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from scipy.interpolate import griddata
import streamlit as st

def plot_volatility_surface(ticker, num_expirations=10):
    # Fetch the stock object
    stock = yf.Ticker(ticker)

    # Get the available expiration dates
    expiration_dates = stock.options

    # Initialize lists to store data
    strike_prices = []
    expirations = []
    implied_vols = []

    # Loop through each expiration date and get option chain data
    for date in expiration_dates[:num_expirations]:  # Limit to the specified number of dates
        opt_chain = stock.option_chain(date)
        calls = opt_chain.calls
        puts = opt_chain.puts

        # Combine call and put data
        combined_data = pd.concat([calls[['strike', 'impliedVolatility']], puts[['strike', 'impliedVolatility']]])
        combined_data = combined_data.groupby('strike').mean().reset_index()

        # Filter out extreme or unrealistic implied volatilities
        combined_data = combined_data[(combined_data['impliedVolatility'] > 0) & (combined_data['impliedVolatility'] < 2)]

        # Store the data
        strike_prices.extend(combined_data['strike'].tolist())
        expirations.extend([date] * len(combined_data))
        implied_vols.extend(combined_data['impliedVolatility'].tolist())

    # Create a DataFrame
    data = pd.DataFrame({
        'Strike': strike_prices,
        'Expiration': expirations,
        'ImpliedVolatility': implied_vols
    })

    # Convert expiration dates to numeric values
    data['Expiration'] = pd.to_datetime(data['Expiration'])
    data['DaysToExpiration'] = (data['Expiration'] - data['Expiration'].min()).dt.days

    # Create a grid for interpolation
    strike_range = np.linspace(min(data['Strike']), max(data['Strike']), 100)
    days_range = np.linspace(min(data['DaysToExpiration']), max(data['DaysToExpiration']), 100)
    strike_grid, days_grid = np.meshgrid(strike_range, days_range)

    # Interpolate implied volatilities
    iv_values = griddata(
        (data['Strike'], data['DaysToExpiration']),
        data['ImpliedVolatility'],
        (strike_grid, days_grid),
        method='cubic'  # Use cubic interpolation for smoothness
    )

    # Plot the smoothed volatility surface using Plotly
    fig = go.Figure(data=[go.Surface(
        z=iv_values, 
        x=strike_range, 
        y=days_range, 
        colorscale=[[0, 'blue'], [1, '#00FF00']],  # Transition from blue to green
        cmin=0,
        cmax=np.nanmax(iv_values)
    )])

    # Customize the layout with a larger size and black background
    fig.update_layout(
        title=f'Smoothed Volatility Surface for {ticker} (Calls and Puts)',
        scene=dict(
            xaxis_title='Strike Price',
            yaxis_title='Days to Expiration',
            zaxis_title='Implied Volatility',
            bgcolor='black'  # Set the background color of the scene to black
        ),
        paper_bgcolor='black',  # Set the overall background color to black
        font=dict(color='white'),  # Set font color to white for better contrast
        width=1500,  # Set width of the plot
        height=1100   # Set height of the plot
    )

    return fig

# Streamlit App

st.markdown(
    """
    <h1 style='color: #FFFFFF;'>Option Volatility Surface Analyzer</h1>
    """, unsafe_allow_html=True
)

#st.title("Volatility Surface Viewer")

a,b,c,d,e,f,g = st.columns(7)

# Add content to each column in the first row
with a:
    ticker = st.text_input("Enter Ticker Symbol", "TSLA")
    


with b:
    st.markdown("""
    <style>
    /* Custom styling for all sliders */
    input[type="range"] {
        accent-color: #000000;  /* Desired color for the slider thumb and track */
    }
    </style>
""", unsafe_allow_html=True)
    num_expirations = st.slider("Number of Expiration Dates", 1, 20, 10)
    

# User Input for Ticker Symbol
#ticker = st.text_input("Enter Ticker Symbol", "TSLA")
#num_expirations = st.slider("Number of Expiration Dates to Fetch", 1, 20, 10)


# Plot the volatility surface
fig = plot_volatility_surface(ticker, num_expirations)
st.plotly_chart(fig)


#----------------------------------

st.markdown(
    """
    <h4 style='color: #FFFFFF; text-align: center;'>Developed & Designed by Rishav Kant</h4>
    """, 
    unsafe_allow_html=True
)



