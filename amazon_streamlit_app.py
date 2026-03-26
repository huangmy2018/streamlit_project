# 导入库
import streamlit as st

# 运行命令： python -m streamlit run amazon_streamlit_app.py 
# 页面标题
st.title("📦 亚马逊运营小工具")
st.subheader("利润计算器 + 基础数据看板")

# -------- 1. 亚马逊利润计算功能 --------
st.markdown("## 1. 单品利润计算")

# 输入框
sell_price = st.number_input("售价（美元）", value=29.99)
cost = st.number_input("产品成本（美元）", value=8.00)
amazon_fee = st.number_input("亚马逊佣金+配送费（美元）", value=6.50)
exchange = st.number_input("汇率", value=7.2)

# 计算逻辑
profit = (sell_price - cost - amazon_fee) * exchange
profit_rate = (sell_price - cost - amazon_fee) / sell_price * 100

# 输出结果
st.success(f"✅ 单品净利润：{profit:.2f} 元")
st.info(f"📈 利润率：{profit_rate:.1f}%")

# -------- 2. 运营数据展示 --------
st.markdown("## 2. 店铺数据预览")
data = {
    "产品": ["A产品", "B产品", "C产品"],
    "日销量": [32, 18, 45],
    "销售额($)": [959.68, 539.82, 1349.55]
}
st.dataframe(data)