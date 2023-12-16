import streamlit as st

# タイトルの表示
st.title('確率の計算')

# 数値の入力
input_number = st.number_input('数値を入力してください', min_value=0)

# 確率の計算
probability = input_number / 100  # 仮の確率計算例

# 結果の表示
st.write(f"入力した数値に対応する確率は {probability} です。")