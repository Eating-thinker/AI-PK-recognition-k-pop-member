import streamlit as st #
import os
import random
import numpy as np
from numpy.linalg import norm
from PIL import Image
from insightface.app import FaceAnalysis
import cv2
import requests
from bs4 import BeautifulSoup

# ------------------------------
# Streamlit 頁面設定
# ------------------------------
st.set_page_config(page_title="IVE AI PK Demo", layout="wide")
st.title("🎤 IVE AI PK Demo")
st.write("使用 InsightFace 辨識 IVE 成員並進行 PK 遊戲")

# ------------------------------
# 成員列表與資料夾設定
# ------------------------------
members = ["Yujin", "Wonyoung", "Rei", "Liz", "Leeseo"]
base_dir = "./ive_members"

# ------------------------------
# 自動建立資料夾
# ------------------------------
for member in members:
    folder = os.path.join(base_dir, member)
    if not os.path.exists(folder):
        os.makedirs(folder)

# ------------------------------
# 爬蟲抓照片 (最多2張)
# ------------------------------
def fetch_images_google(member, limit=2):
    headers = {"User-Agent": "Mozilla/5.0"}
    query = f"IVE {member} site:twitter.com OR site:instagram.com OR site:google.com"
    search_url = f"https://www.google.com/search?tbm=isch&q={query}"
    try:
        res = requests.get(search_url, headers=headers, timeout=10)
        soup = BeautifulSoup(res.text, "html.parser")
        imgs = soup.find_all("img")
        urls = [img['src'] for img in imgs if img.get('src')][:limit]
        return urls
    except:
        return []

def download_images(member, limit=2):
    folder = os.path.join(base_dir, member)
    existing = len(os.listdir(folder))
    if existing >= limit:
        return
    urls = fetch_images_google(member, limit)
    for i, url in enumerate(urls):
        try:
            img_data = requests.get(url, timeout=5).content
            with open(os.path.join(folder, f"{member}_{i}.jpg"), "wb") as f:
                f.write(img_data)
        except:
            continue

# ------------------------------
# 第一次使用按鈕抓照片
# ------------------------------
st.header("📥 第一次使用請按下按鈕抓取 IVE 成員照片")
if st.button("開始抓取所有成員照片"):
    with st.spinner("正在抓取照片，請稍等 10~20 秒..."):
        for member in members:
            download_images(member, limit=2)
    st.success("🎉 成員照片下載完成！")

# ------------------------------
# 初始化 InsightFace（CPU模式）
# ------------------------------
app = FaceAnalysis(name="buffalo_l")
app.prepare(ctx_id=-1, det_size=(640, 640))

# ------------------------------
# 建立 face_db
# ------------------------------
@st.cache_data(show_spinner=False)
def build_face_db():
    face_db = {}
    for member in members:
        folder = os.path.join(base_dir, member)
        embeddings = []
        for img_name in os.listdir(folder):
            img_path = os.path.join(folder, img_name)
            img = cv2.imread(img_path)
            if img is None:
                continue
            faces = app.get(img)
            if len(faces) == 0:
                continue
            embeddings.append(faces[0].embedding)
        face_db[member] = embeddings
    return face_db

face_db = build_face_db()

# ------------------------------
# 預測成員
# ------------------------------
def predict_member(img):
    faces = app.get(img)
    if len(faces) == 0:
        return "無法偵測到臉"
    query_emb = faces[0].embedding
    scores = {}
    for member, embs in face_db.items():
        if len(embs) == 0:
            continue
        sims = [np.dot(query_emb, e)/(norm(query_emb)*norm(e)) for e in embs]
        scores[member] = np.mean(sims)
    return max(scores, key=scores.get)

# ------------------------------
# 1️⃣ 團員介紹區
# ------------------------------
st.header("🎶 團員介紹")
cols = st.columns(len(members))
for i, member in enumerate(members):
    folder = os.path.join(base_dir, member)
    imgs = os.listdir(folder)
    if len(imgs) > 0:
        img_path = os.path.join(folder, imgs[0])
        cols[i].image(img_path, caption=member, use_column_width=True)
    else:
        cols[i].write(f"{member}（無照片，請先抓取）")

# ------------------------------
# 2️⃣ 即時辨識區
# ------------------------------
st.header("📸 上傳照片進行辨識")
uploaded_file = st.file_uploader("選擇一張圖片", type=["jpg","jpeg","png"])
if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    img_cv = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    pred = predict_member(img_cv)
    st.image(image, caption=f"AI 預測：{pred}", use_column_width=True)

# ------------------------------
# 3️⃣ 遊戲互動區
# ------------------------------
st.header("🎮 AI PK 遊戲")
st.write("系統隨機抽一張團員照片，猜這是誰！")

valid_members = [m for m in members if len(os.listdir(os.path.join(base_dir, m))) > 0]

if valid_members:
    if "game_member" not in st.session_state:
        st.session_state.game_member = random.choice(valid_members)

    game_member = st.session_state.game_member
    member_imgs = os.listdir(os.path.join(base_dir, game_member))
    game_img_name = random.choice(member_imgs)
    game_img_path = os.path.join(base_dir, game_member, game_img_name)
    game_image = Image.open(game_img_path).convert("RGB")
    st.image(game_image, caption="猜猜這是誰？", use_column_width=True)

    # 下拉選單
    user_guess = st.selectbox("選擇你認為這是哪位成員：", members)

    if st.button("提交猜測"):
        ai_pred = predict_member(cv2.cvtColor(np.array(game_image), cv2.COLOR_RGB2BGR))
        st.write(f"使用者猜測：{user_guess}")
        st.write(f"AI 預測：{ai_pred}")
        st.write(f"正確答案：{game_member}")

        if user_guess == game_member:
            st.success("🎉 你猜對了！")
        else:
            st.error("❌ 你猜錯了")

        if ai_pred.lower() == game_member.lower():
            st.info("AI 預測正確 ✅")
        else:
            st.warning("AI 預測錯誤 ⚠️")

        # 重新選擇下一張遊戲圖片
        st.session_state.game_member = random.choice(valid_members)
else:
    st.warning("目前沒有任何團員照片，請先按上方按鈕下載照片。")
