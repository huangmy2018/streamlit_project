import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 设置页面样式
st.set_page_config(page_title="亚马逊广告分析工具", layout="wide")
st.title("📊 亚马逊广告 & 订单数据分析工具")
st.subheader("运营日常快速统计 | ACoS、转化率、利润自动计算")

# ---------------------- 1. 广告数据输入 ----------------------
st.markdown("## 1️⃣ 广告数据录入")
col1, col2 = st.columns(2)

with col1:
    spend = st.number_input("广告花费($)", value=120.50)
    clicks = st.number_input("广告点击量", value=320)
    
with col2:
    orders = st.number_input("广告订单量", value=45)
    sales = st.number_input("广告销售额($)", value=1350.00)

# 自动计算核心指标
cpc = spend / clicks if clicks > 0 else 0
acos = spend / sales if sales > 0 else 0
cvr = orders / clicks if clicks > 0 else 0
order_value = sales / orders if orders > 0 else 0

# ---------------------- 2. 展示核心指标卡片 ----------------------
st.markdown("## 2️⃣ 核心运营指标")
col1, col2, col3, col4 = st.columns(4)

col1.metric("CPC（单次点击成本）", f"${cpc:.2f}")
col2.metric("ACoS（广告占比）", f"{acos:.1%}")
col3.metric("转化率 CVR", f"{cvr:.1%}")
col4.metric("客单价", f"${order_value:.2f}")

# ---------------------- 3. 数据趋势图表 ----------------------
st.markdown("## 3️⃣ 近7天数据趋势（模拟）")
days = ["第1天", "第2天", "第3天", "第4天", "第5天", "第6天", "第7天"]
aco_list = [0.22, 0.25, 0.19, 0.23, 0.18, 0.21, 0.17]
cvr_list = [0.12, 0.15, 0.13, 0.16, 0.14, 0.18, 0.17]

df = pd.DataFrame({
    "日期": days,
    "ACoS": aco_list,
    "转化率": cvr_list
})

# 双图表展示
fig, ax = plt.subplots(1, 2, figsize=(12, 4))
ax[0].plot(days, aco_list, marker="o", color="red", label="ACoS")
ax[0].set_title("ACoS 趋势")
ax[0].grid(True)

ax[1].plot(days, cvr_list, marker="s", color="green", label="转化率")
ax[1].set_title("转化率 趋势")
ax[1].grid(True)

st.pyplot(fig)

# ---------------------- 4. 运营建议（自动判断） ----------------------
st.markdown("## 4️⃣ 智能运营建议")
if acos < 0.2:
    st.success("✅ ACoS 表现优秀，广告健康！")
elif 0.2 <= acos < 0.3:
    st.warning("⚠️ ACoS 一般，可优化关键词、否定无效流量")
else:
    st.error("❌ ACoS 偏高，建议降低出价、排查高花费词")

if cvr >= 0.15:
    st.success("✅ 转化率优秀，Listing 表现良好")
else:
    st.info("💡 转化率偏低，可优化主图、标题、五点、评价")

st.markdown("---")
st.caption("✅ 亚马逊运营专用 Streamlit 工具 | 一键生成日报")