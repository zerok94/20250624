import streamlit as st

# MBTI 직업 추천 사전
mbti_jobs = {
    "INTJ": ["전략 컨설턴트", "데이터 과학자", "정책 분석가"],
    "INTP": ["연구원", "프로그래머", "이론 물리학자"],
    "ENTJ": ["경영 컨설턴트", "CEO", "프로젝트 매니저"],
    "ENTP": ["창업가", "마케팅 전략가", "기술 혁신가"],
    "INFJ": ["상담사", "작가", "인문학 교수"],
    "INFP": ["시인", "예술가", "심리치료사"],
    "ENFJ": ["교사", "정치가", "사회운동가"],
    "ENFP": ["홍보 담당자", "크리에이티브 디렉터", "여행 작가"],
    "ISTJ": ["회계사", "판사", "군 장교"],
    "ISFJ": ["간호사", "초등 교사", "사회복지사"],
    "ESTJ": ["경영자", "행정 공무원", "현장 관리자"],
    "ESFJ": ["고객 서비스 매니저", "인사 담당자", "학교 행정가"],
    "ISTP": ["기계공", "파일럿", "응급 구조사"],
    "ISFP": ["그래픽 디자이너", "셰프", "플로리스트"],
    "ESTP": ["세일즈 전문가", "기업인", "이벤트 기획자"],
    "ESFP": ["배우", "MC", "엔터테이너"]
}

# 제목
st.title("🌟 MBTI 기반 직업 추천기")

# 사용자 MBTI 입력
selected_mbti = st.selectbox("당신의 MBTI를 선택하세요", list(mbti_jobs.keys()))

# 추천 직업 출력
if selected_mbti:
    st.subheader(f"💼 {selected_mbti} 유형에게 추천하는 직업들:")
    for job in mbti_jobs[selected_mbti]:
        st.markdown(f"- {job}")
