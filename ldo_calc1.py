import streamlit as st

st.title('Tank Stock Calculation App')

col1, col2 = st.columns(2)

with col1:
    st.header('Previous Tank Levels')
    prev_A2 = st.number_input('Previous A2 (stage-1) Tank Level')
    prev_B3 = st.number_input('Previous B3 (stage-1) Tank Level')
    prev_FKL = st.number_input('Previous 40KL (stage-1) Tank Level')
    prev_SKL = st.number_input('Previous 60KL (stage-1) Tank Level')
    prev_HFON = st.number_input('Previous HFO-N (stage-2) Tank Level')
    prev_LDON = st.number_input('Previous LDO-N (stage-2) Tank Level')
    prev_LDOS = st.number_input('Previous LDO-S (stage-2) Tank Level')

with col2:
    st.header('Present Tank Levels')
    A2 = st.number_input('Present A2 (stage-1) Tank Level')
    B3 = st.number_input('Present B3 (stage-1) Tank Level')
    FKL = st.number_input('Present 40KL (stage-1) Tank Level')
    SKL = st.number_input('Present 60KL (stage-1) Tank Level')
    HFON = st.number_input('Present HFO-N (stage-2) Tank Level')
    LDON = st.number_input('Present LDO-N (stage-2) Tank Level')
    LDOS = st.number_input('Present LDO-S (stage-2) Tank Level')

if st.button('Calculate Stock'):
    # Calculate previous stock
    prev_Stock_st1 = (prev_A2 * 283) + (prev_B3 * 283) + (16 * prev_FKL) + (17.14 * prev_SKL)
    prev_Stock_st2 = (prev_HFON * 254.5) + (prev_LDON * 38.48) + (prev_LDOS * 38.48)
    prev_Total_Stock = prev_Stock_st1 + prev_Stock_st2

    # Calculate present stock
    Stock_st1 = (A2 * 283) + (B3 * 283) + (16 * FKL) + (17.14 * SKL)
    Stock_st2 = (HFON * 254.5) + (LDON * 38.48) + (LDOS * 38.48)
    Total_Stock = Stock_st1 + Stock_st2

    # Calculate difference
    stock_diff_st1= Stock_st1 - prev_Stock_st1
    stock_diff_st2= Stock_st2 - prev_Stock_st2
    stock_difference = Total_Stock - prev_Total_Stock

    # Display results side by side
    res_col1, res_col2, res_col3 = st.columns(3)

    with res_col1:
        st.subheader('Previous Stock')
        st.write(f"Stage-1: {prev_Stock_st1}")
        st.write(f"Stage-2: {prev_Stock_st2}")
        st.write(f"Total: {prev_Total_Stock}")

    with res_col2:
        st.subheader('Present Stock')
        st.write(f"Stage-1: {Stock_st1}")
        st.write(f"Stage-2: {Stock_st2}")
        st.write(f"Total: {Total_Stock}")

    with res_col3:
        st.subheader('Difference')
        st.write(f"Stage-1: {stock_diff_st1}")
        st.write(f"Stage-2: {stock_diff_st2}")
        st.write(f"Total: {stock_difference}")
