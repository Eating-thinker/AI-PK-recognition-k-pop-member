# AI PK Recognition K-pop Member

這是一個基於 **Python、InsightFace、OpenCV、Face Recognition** 的 K-pop 成員人臉辨識專案，針對 IVE 團體成員打造。  
專案包含 **Colab Notebook** 與 **Streamlit Web App**，可以自動爬取成員照片、生成人臉 embedding，並提供 AI 與使用者 PK 的互動遊戲。

---

## 📌 專案功能

### 1️⃣ Colab Notebook - `IVE_AI_PK.ipynb`
- 自動建立 IVE 成員資料夾
- 自動爬蟲下載各成員照片（Google / DuckDuckGo）
- 使用 InsightFace 建立人臉 embedding 資料庫
- 上傳任意照片 → AI 辨識是哪位成員
- 可視覺化顯示辨識結果

### 2️⃣ Streamlit Web App - `app.py`
- 顯示所有 IVE 成員照片和姓名
- 使用者可上傳照片 → AI 預測成員
- PK 遊戲模式  
  - 隨機顯示一張成員照片  
  - 使用者輸入猜測  
  - AI 同時預測  
  - 顯示誰答對  

---

## 📦 安裝與使用

### 1️⃣ Clone 專案
```bash
git clone https://github.com/Eating-thinker/AI-PK-recognition-k-pop-member.git
cd AI-PK-recognition-k-pop-member
```

### 2️⃣ 建立虛擬環境（建議）
```bash
python -m venv venv
source venv/bin/activate   # Mac / Linux
venv\Scripts\activate      # Windows
```

### 3️⃣ 安裝必要套件
如果你有 `requirements.txt`：
```bash
pip install -r requirements.txt
```

若尚未建立 `requirements.txt`，請使用：
```bash
pip install duckduckgo_search opencv-python numpy face_recognition insightface onnxruntime streamlit pillow requests beautifulsoup4 matplotlib
```

> ⚠ 注意：InsightFace 若使用 GPU 推論，需搭配對應版本 CUDA。若無 GPU 則自動使用 CPU。

---

## ▶️ 執行方式

### 1️⃣ 在 Colab 執行 Notebook
打開 `IVE_AI_PK.ipynb`  
依序執行 Step1～Step5  
即可完成爬蟲、建立 embedding、進行辨識測試。

---

### 2️⃣ 執行 Streamlit Web Demo
```bash
streamlit run app.py
```

啟動後會看到：
- IVE 成員介紹（照片 + 名字）
- 上傳圖片讓 AI 辨識成員
- PK 遊戲模式（使用者 vs AI 猜成員）

---

## 📁 專案結構

```
AI-PK-recognition-k-pop-member/
│
├─ app.py                     # Streamlit Web App
├─ IVE_AI_PK.ipynb            # Colab Notebook
├─ README.md
├─ requirements.txt           # 套件需求 (如有)
└─ ive_members/               # 自動爬取的成員圖片
   ├─ Yujin/
   ├─ Wonyoung/
   ├─ Rei/
   ├─ Liz/
   └─ Leeseo/
```

---

## 🧠 技術使用
- **InsightFace**：人臉 embedding
- **Face Recognition**：臉部偵測
- **OpenCV**：影像處理
- **DuckDuckGo Search**：爬取圖片
- **Streamlit**：Web App 建置

---

## ⚠ 注意事項
- Colab 有時 GPU 驅動與 CUDA 版本不相容 → InsightFace 自動 fallback CPU
- 請勿將未授權的圖片用於商業用途
- 若要公開部署 Streamlit，可使用 Streamlit Cloud 或 HuggingFace Spaces

---

## 📚 參考資源
- InsightFace: https://github.com/deepinsight/insightface
- Face Recognition: https://github.com/ageitgey/face_recognition
- Streamlit: https://streamlit.io/

