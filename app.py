from libs.plotting.plot_engine import PlotEngine
from libs.plotting.plot_model import PlotModel
from typing import Any, Dict
from scipy.stats.stats import CumfreqResult, DescribeResult, RelfreqResult
from sklearn.pipeline import Pipeline
from finance_mining_service import FinanceMiningService
import streamlit as st

PROMPT_DEBUG = False
finance_mining_service = FinanceMiningService(PROMPT_DEBUG)
stats: DescribeResult = None
rel_freq_result: RelfreqResult = None
cum_freq_result: CumfreqResult = None
model_info: Dict[str, Any] = {}
poly_models: Dict[int, Pipeline] = {}
plot_model: PlotModel = None
stats, rel_freq_result, cum_freq_result, model_info, poly_models, poly_models_figure, plot_model, figure_linear_regression = finance_mining_service.run()

plot_engine = PlotEngine()


options_sequence = ['', 'EurUsd', 'IBM', 'Gold', 'UsdJpy']
option = st.sidebar.selectbox(
    'Choose a Forex symbol',
     options_sequence)

st.title(f'FinFetch Analyzer: {option}')

if option is None or option == '':
    st.stop()

st.write(stats._asdict())

st.bar_chart(rel_freq_result.frequency)

st.bar_chart(cum_freq_result.cumcount)

st.write(model_info)

fig = plot_engine.get_figure(plot_model)
    
with st.container():
    st.pyplot(fig)

    st.pyplot(poly_models_figure)

    st.pyplot(figure_linear_regression)