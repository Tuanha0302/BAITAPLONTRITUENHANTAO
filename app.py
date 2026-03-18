import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
import os
import hashlib

# ========================
# CONFIG
# ========================
IMG_SIZE = 224
CONFIDENCE_THRESHOLD = 0.7

CLASS_INFO = [
    ("Chó", "Chihuahua"),
    ("Chó", "American Bulldog"),
    ("Chó", "Beagle"),
    ("Chó", "Shiba Inu"),
    ("Chó", "Pug"),
    ("Mèo", "Persian"),
    ("Mèo", "Maine Coon"),
    ("Mèo", "Bengal"),
    ("Mèo", "Siamese"),
    ("Mèo", "British Shorthair")
]

# ========================
# LOAD MODEL
# ========================
MODEL_NAME = "pet_breed_model_final.h5"

@st.cache_resource
def load_model(path):
    return tf.keras.models.load_model(path)

if not os.path.exists(MODEL_NAME):
    st.error("❌ Không tìm thấy model.")
    st.stop()

model = load_model(MODEL_NAME)

# ========================
# PAGE CONFIG
# ========================
st.set_page_config(page_title="Pet Breed AI", page_icon="🐾", layout="wide")

st.markdown("""
    <style>
    .stApp {
        background-color: #dbefff;
    }
    </style>
""", unsafe_allow_html=True)

# ========================
# SESSION STATE
# ========================
if "history" not in st.session_state:
    st.session_state.history = []

if "current_image" not in st.session_state:
    st.session_state.current_image = None

if "last_hash" not in st.session_state:
    st.session_state.last_hash = None

if "camera_on" not in st.session_state:
    st.session_state.camera_on = False

# ========================
# HEADER
# ========================
st.title("🐾 Hệ thống phân loại giống chó & mèo")
st.markdown("---")

# ========================
# SIDEBAR
# ========================
st.sidebar.title("🕘 Lịch sử nhận diện")

if st.sidebar.button("🗑 Xóa tất cả lịch sử"):
    st.session_state.history = []
    st.rerun()

for idx, img in enumerate(st.session_state.history):
    st.sidebar.image(img, width=120)
    if st.sidebar.button(f"❌ Xóa ảnh {idx+1}", key=f"del_{idx}"):
        st.session_state.history.pop(idx)
        st.rerun()

# ========================
# LAYOUT
# ========================
col1, col2 = st.columns([1, 1])

# ========================
# INPUT
# ========================
with col1:

    uploaded_file = st.file_uploader("📤 Tải ảnh lên", type=["jpg","png","jpeg"])

    # =====================
    # UPLOAD LOGIC
    # =====================
    if uploaded_file is not None:
        image = Image.open(uploaded_file).convert("RGB")
        st.session_state.current_image = image

        img_hash = hashlib.md5(uploaded_file.getvalue()).hexdigest()

        if img_hash != st.session_state.last_hash:
            st.session_state.history.append(image)
            st.session_state.last_hash = img_hash

    # Nếu upload bị clear và camera đang tắt → reset ảnh
    if uploaded_file is None and not st.session_state.camera_on:
        st.session_state.current_image = None
        st.session_state.last_hash = None

    # =====================
    # CAMERA BUTTON
    # =====================
    if st.button("📷 Bật / Tắt Camera"):
        st.session_state.camera_on = not st.session_state.camera_on

    # =====================
    # CAMERA LOGIC
    # =====================
    if st.session_state.camera_on:

        camera_image = st.camera_input("Chụp ảnh")

        # Nếu bấm Clear Photo
        if camera_image is None:
            st.session_state.current_image = None
            st.session_state.last_hash = None

        else:
            image = Image.open(camera_image).convert("RGB")
            st.session_state.current_image = image

            img_hash = hashlib.md5(camera_image.getvalue()).hexdigest()

            if img_hash != st.session_state.last_hash:
                st.session_state.history.append(image)
                st.session_state.last_hash = img_hash

    # =====================
    # HIỂN THỊ ẢNH
    # =====================
    if st.session_state.current_image is not None:
        st.image(
            st.session_state.current_image,
            caption="Ảnh hiện tại",
            use_container_width=True
        )

# ========================
# PREDICT
# ========================
with col2:

    if st.session_state.current_image is not None:

        img = st.session_state.current_image.resize((IMG_SIZE, IMG_SIZE))
        img_array = np.array(img) / 255.0
        img_array = np.expand_dims(img_array, axis=0)

        if st.button("🚀 Dự đoán", use_container_width=True):

            prediction = model.predict(img_array)
            probs = prediction[0]

            top3_indices = np.argsort(probs)[-3:][::-1]
            max_confidence = probs[top3_indices[0]]

            if max_confidence < CONFIDENCE_THRESHOLD:
                st.warning("⚠️ Ảnh không thuộc 10 giống đã huấn luyện.")
            else:
                main_type, main_breed = CLASS_INFO[top3_indices[0]]
                st.success(
                    f"Kết quả chính: {main_type} - {main_breed} "
                    f"({max_confidence*100:.2f}%)"
                )

                st.write("### 🔎 Top 3 dự đoán")

                for i in top3_indices:
                    animal_type, breed_name = CLASS_INFO[i]
                    confidence = float(probs[i])

                    colA, colB = st.columns([4,1])
                    with colA:
                        st.write(f"{animal_type} - {breed_name}")
                        st.progress(confidence)
                    with colB:
                        st.write(f"{confidence*100:.2f}%")