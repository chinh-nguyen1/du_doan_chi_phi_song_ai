import streamlit as st
from utils.inference import predict_total, split_expense

st.set_page_config(page_title="Dự đoán chi phí sống", layout="centered")

st.title("💡 AI Dự đoán Chi phí Sống tại Việt Nam")
st.markdown("---")

# Nhập thông tin
khu_vuc = st.selectbox("🌍 Khu vực sinh sống", ["Hà Nội", "TP.HCM", "Đà Nẵng", "Huế", "Cần Thơ", "Khác"])
muc_song = st.radio("🎯 Mức sống mong muốn", ["Tiết kiệm", "Vừa đủ", "Dư giả"])
so_tien = st.number_input("💵 Số tiền bạn có thể chi mỗi tháng (VND)", min_value=1000000, max_value=100000000, step=500000)

mo_ta = st.text_area("📝 Mô tả ngắn tình hình thế giới ảnh hưởng tới chi phí", height=150,
                     placeholder="Ví dụ: Lạm phát tăng cao, giá xăng dầu tăng, khủng hoảng năng lượng...")

if st.button("📊 Dự đoán chi phí & phân bổ"):
    with st.spinner("Đang phân tích..."):
        total_pred = predict_total(mo_ta)
        detail = split_expense(total_pred, muc_song)

    st.success(f"✅ Chi phí sống dự đoán: **{round(total_pred):,} VND/tháng**")
    st.markdown("### 📦 Chi tiết phân bổ:")
    st.table(detail)

    # Biểu đồ
    try:
        import matplotlib.pyplot as plt

        fig, ax = plt.subplots()
        ax.pie(detail.values(), labels=detail.keys(), autopct='%1.1f%%', startangle=90)
        ax.axis('equal')
        st.pyplot(fig)
    except:
        st.warning("Không thể hiển thị biểu đồ (thiếu thư viện matplotlib)")