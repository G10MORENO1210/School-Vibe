import streamlit as st
import time

# --- 页面基础设置 ---
st.set_page_config(
    page_title="国际高中神仙指数鉴定",
    page_icon="🏫",
    layout="centered"
)

# ===========================
# 👉 新增：侧边栏个人名片
# ===========================
with st.sidebar:
    st.image("kim.jpg", use_container_width=True) # 这里读取你的图片
    st.markdown("### 👨‍🏫 Kim | 国际教育")
    st.info("👆 扫码或搜索小红书号：**1040163221**\n\n获取更多国际教育干货！")
    st.markdown("---")
    st.caption("已辅导 5000+ hrs")

# ===========================
#         主页面内容
# ===========================

# --- 样式优化 ---
st.markdown("""
    <style>
    .stButton>button { width: 100%; background-color: #FF4B4B; color: white; height: 50px; border-radius: 10px; font-weight: bold;}
    .result-card { background-color: white; padding: 20px; border-radius: 15px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); text-align: center; margin-top: 20px; }
    .big-score { font-size: 60px; font-weight: bold; color: #FF4B4B; }
    </style>
""", unsafe_allow_html=True)

st.title("🏫 国际高中“神仙指数”鉴定")
st.markdown("---")

# --- Step 1: 生存状态 ---
st.subheader("📝 Step 1: 生存状态")
col1, col2 = st.columns(2)

with col1:
    sleep = st.slider("😴 睡眠时长", 3.0, 12.0, 7.0, 0.5, help="包含晚上睡觉、午休以及课上补觉的总时间")
    if sleep < 5.0: st.caption("💀 你的肝还好吗？")
    elif sleep > 9.0: st.caption("🐨 你是考拉转世吗？")
    else: st.caption("✅ 正常的碳基生物作息")

    chill = st.slider("📱 摸鱼时长", 0.0, 10.0, 2.0, 0.5, help="除去吃饭睡觉，纯玩手机/发呆的时间")
    if chill > 4.0: st.caption("🎮 看来作业还是太少了")
    else: st.caption("⏳ 时间管理大师")

    food = st.slider("🍱 食堂评分", 1, 5, 3, help="1分=维持生命，5分=舌尖上的中国")
    if food == 1: st.caption("🤢 活着就好...")
    elif food == 5: st.caption("🤤 羡慕哭了")

with col2:
    homework = st.slider("📚 作业时长", 0.0, 10.0, 3.0, 0.5, help="包含写文书、做Project、赶Due的时间")
    if homework > 5.0: st.caption("👴 头发还在吗？")
    elif homework < 1.0: st.caption("🤔 学神还是学渣？")
    else: st.caption("📝 痛并快乐着")

    commute = st.slider("🚌 通勤时长", 0.0, 6.0, 1.0, 0.5, help="单程还是往返？反正就是堵在路上的时间")
    if commute > 2.0: st.caption("🗺️ 你这是跨省上学？")
    else: st.caption("🚗 稍微有点堵")

# --- Step 2: 氛围 ---
st.markdown("---")
st.subheader("🎛️ Step 2: 学校氛围")

st.markdown("##### 1. 📱 电子产品")
tech_map = {
    "进校门没收 | 仿佛回到诺基亚时代": 0.8,
    "仅特定时段可用 | 勉强维持现代生活": 1.0,
    "全天自由 | 对高中生起码的信任": 1.1,
    "电子化教学 (iPad/Mac) | 书包轻得像郊游": 1.2
}
tech_key = st.selectbox("电子产品政策", list(tech_map.keys()), index=1)
tech_score = tech_map[tech_key]

st.markdown("##### 2. 🎉 校园活动")
event_map = {
    "只有学习 | 运动会都要缩减": 0.85,
    "常规配置 | 四大节中规中矩": 1.0,
    "社团极丰富 | 马术/电竞都有": 1.1,
    "经常外出 | 博物馆/露营/Field Trip": 1.15
}
event_key = st.selectbox("活动丰富度", list(event_map.keys()), index=1)
event_score = event_map[event_key]

st.markdown("##### 3. 🤝 同学氛围")
peer_map = {
    "极度高压 | 笔记不共享，火药味重": 0.9,
    "两极分化 | 学霸刷题，气氛组搞事": 1.0,
    "良性竞争 | 考前互划重点": 1.1,
    "神仙队友 | 全员大佬，随便组队拿奖": 1.2
}
peer_key = st.selectbox("同学关系", list(peer_map.keys()), index=2)
peer_score = peer_map[peer_key]

st.markdown("##### 4. 🏟️ 硬件设施")
facility_map = {
    "复古风 | 冬冷夏热，全靠一身正气": 0.95,
    "标准现代化 | 无功无过": 1.0,
    "网红打卡级 | 落地窗/咖啡厅": 1.1,
    "开放式/大学城 | 外卖自由，奶茶自由": 1.15
}
facility_key = st.selectbox("校园环境", list(facility_map.keys()), index=1)
facility_score = facility_map[facility_key]

st.markdown("##### 5. 👕 着装要求")
style_map = {
    "严格统一 | 每天检查拉链，像当兵": 0.9,
    "周五便服日 | 一周就盼这一天": 1.0,
    "适度自由 | 可染发/戴首饰": 1.05,
    "完全自由 | 学校简直是T台": 1.1
}
style_key = st.selectbox("着装规定", list(style_map.keys()), index=1)
style_score = style_map[style_key]

# --- 计算与结果 ---
if st.button("🔥 开始鉴定 🔥"):
    with st.spinner('计算中...'):
        time.sleep(1)
        
    total_multiplier = tech_score * event_score * peer_score * facility_score * style_score
    base_score = (sleep + chill + food*0.6) / (homework + commute + 4.0)
    final_score = base_score * total_multiplier

    if final_score < 0.8:
        title, color, desc = "🧘 硬核求学者", "#8B0000", "天将降大任于斯人也！抗压能力满级！"
    elif final_score < 1.2:
        title, color, desc = "🏃 全能平衡手", "#1E90FF", "在赶Due和摸鱼之间找到了完美平衡。"
    elif final_score < 1.6:
        title, color, desc = "✨ 凡尔赛原住民", "#9370DB", "这种神仙日子，且行且珍惜。"
    else:
        title, color, desc = "👑 天选之子", "#FFD700", "贵校还缺吉祥物吗？这是学术界的五星级酒店！"

    st.markdown(f"""
        <div class="result-card">
            <div style="color:#888;">你的国际学校神仙指数</div>
            <div class="big-score" style="color:{color}">{final_score:.2f}</div>
            <div style="font-size:24px; font-weight:bold; color:{color}; margin:10px 0;">{title}</div>
            <p>{desc}</p>
        </div>
    """, unsafe_allow_html=True)
    st.balloons()
