from libs.plotting.plot_model import PlotModel
from typing import Any, Dict
from scipy.stats.stats import CumfreqResult, DescribeResult, RelfreqResult
from sklearn.pipeline import Pipeline
from finance_mining_service import FinanceMiningService
import streamlit as st

st.title('FinFetch Analyzer')

PROMPT_DEBUG = False
finance_mining_service = FinanceMiningService(PROMPT_DEBUG)
stats: DescribeResult = None
rel_freq_result: RelfreqResult = None
cum_freq_result: CumfreqResult = None
model_info: Dict[str, Any] = {}
poly_models: Dict[int, Pipeline] = {}
plot_model: PlotModel = None
stats, rel_freq_result, cum_freq_result, model_info, poly_models, plot_model = finance_mining_service.run()

st.write(str(stats))

st.write(str(rel_freq_result))

st.write(str(cum_freq_result))

st.write(model_info)

# st.write(poly_models)

# st.write(plot_model)