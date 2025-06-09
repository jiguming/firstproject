import streamlit as st

# 제목 🎬
st.title("🎯 MBTI 맞춤 추천: 수학·과학 명작 영화 🎯")

# 설명 💡
st.write("당신의 MBTI를 입력하면 🔮 과학과 수학을 사랑하는 당신을 위한 🎥 명작 영화를 추천해드립니다!")

# MBTI 입력 📥
mbti = st.text_input("당신의 MBTI를 입력하세요 (예: INTP, ENFP 등)").upper()

# 추천 영화 데이터 🎞️
movie_recommendations = {
    "INTJ": ["🧠 《굿 윌 헌팅》", "🚀 《인터스텔라》"],
    "INTP": ["📐 《이미테이션 게임》", "🔬 《뷰티풀 마인드》"],
    "ENTP": ["🎯 《소셜 네트워크》", "⚛️ 《아이언맨》"],
    "ENTJ": ["💡 《스티브 잡스》", "🌌 《마션》"],
    "INFJ": ["🔭 《콘택트》", "🧬 《어라이벌》"],
    "INFP": ["🌱 《월터의 상상은 현실이 된다》", "🦋 《빅 히어로 6》"],
    "ENFP": ["🎢 《인사이드 아웃》", "🚀 《라라랜드》 (창의력 폭발!)"],
    "ENFJ": ["🌟 《숨겨진 인물들》", "💻 《트랜센던스》"],
    "ISTJ": ["⚙️ 《인셉션》", "🔬 《컨테이젼》"],
    "ISFJ": ["🎓 《맷 데이먼의 마션》", "🧪 《옥자》"],
    "ESTJ": ["🔬 《패신저스》", "🛰 《그래비티》"],
    "ESFJ": ["🌟 《드림》", "⚛️ 《앤트맨》"],
    "ISTP": ["🔩 《테넷》", "🚀 《에드 아스트라》"],
    "ISFP": ["🎶 《라라랜드》", "🌸 《월-E》"],
    "ESTP": ["💣 《테넷》", "🚗 《포드 V 페라리》"],
    "ESFP": ["🎉 《위대한 쇼맨》", "🛸 《가디언즈 오브 갤럭시》"]
}

# 입력이 들어오면 추천 💖
if mbti:
    st.balloons()  # 풍선 효과 🎈🎈🎈
    recommendations = movie_recommendations.get(mbti)
    
    if recommendations:
        st.success(f"🎊 {mbti} 유형에게 추천하는 수학·과학 명작 영화 🎊")
        for movie in recommendations:
            st.write(movie)
    else:
        st.warning("😅 죄송해요! 유효한 MBTI를 입력해주세요. 예: INTP, ENFP 등")
