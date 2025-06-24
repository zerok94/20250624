aimport streamlit as st
import pandas as pd

# CSV 파일 불러오기 (EUC-KR 인코딩)
df = pd.read_csv("202505_202505_연령별인구현황_월간.csv", encoding="euc-kr")

# 총인구수 숫자형으로 변환
df['총인구수'] = df['2025년05월_계_총인구수'].str.replace(',', '').astype(int)

# 연령별 인구 컬럼 전처리
age_columns = [col for col in df.columns if col.startswith('2025년05월_계_') and '총인구수' not in col and '연령구간' not in col]
age_labels = [col.replace('2025년05월_계_', '') for col in age_columns]

# 상위 5개 행정구역 선택
df_top5 = df.sort_values(by='총인구수', ascending=False).head(5).copy()
for col in age_columns:
    df_top5[col] = df_top5[col].astype(str).str.replace(',', '').astype(int)

# 연령별 인구 데이터 재구성
age_df = pd.DataFrame({'연령': age_labels})
for idx, row in df_top5.iterrows():
    age_df[row['행정구역']] = row[age_columns].values

# Streamlit 앱 구성
st.title("2025년 5월 기준 연령별 인구 현황 (상위 5개 행정구역)")
st.write("※ 모든 데이터는 행정안전부 통계를 기반으로 하며, 단위는 명입니다.")

st.subheader("원본 데이터 미리보기")
st.dataframe(df_top5)

st.subheader("연령별 인구 변화 (선 그래프)")
st.line_chart(data=age_df.set_index("연령"))
