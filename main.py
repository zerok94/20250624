import streamlit as st
import pandas as pd

st.title("2022년 시도별 미세먼지 배출량 시각화")

# 파일 업로드
uploaded_file = st.file_uploader("2022년 시도별 배출량 파일을 업로드해주세요.", type=["xlsx"])
if uploaded_file is not None:
    # 엑셀 파일 읽기
    df = pd.read_excel(uploaded_file)

    # 원본 데이터 보여주기
    st.subheader("📄 원본 데이터")
    st.dataframe(df)

    # 데이터 전처리: 행정구역을 기준으로 미세먼지 종류별로 피벗 변환
    df_melted = df.melt(id_vars=["행정구역"], var_name="미세먼지 종류", value_name="배출량")
    df_pivot = df_melted.pivot(index="미세먼지 종류", columns="행정구역", values="배출량")

    # 시각화
    st.subheader("📈 시도별 미세먼지 배출량 (선 그래프)")
    st.line_chart(df_pivot)

else:
    st.warning("📁 좌측 사이드바 또는 위의 영역에서 Excel 파일을 업로드해주세요.")
