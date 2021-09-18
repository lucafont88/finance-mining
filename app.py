from finance_mining_service import FinanceMiningService
import streamlit as st

st.title('FinFetch Analyzer')

PROMPT_DEBUG = False
finance_mining_service = FinanceMiningService(PROMPT_DEBUG)
stats, rel_freq_result, cum_freq_result, model_info, poly_models, plot_model = finance_mining_service.run()

# st.write(stats)

# st.write(rel_freq_result)

# st.write(cum_freq_result)

st.write(model_info)

# st.write(poly_models)

# st.write(plot_model)