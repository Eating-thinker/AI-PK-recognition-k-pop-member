# AI PK — K-POP 成員辨識系統  
利用深度學習模型進行 K-POP 團體成員臉部辨識（IVE）。此專案包含 **Streamlit 網頁 Demo** 與 **訓練/辨識 Colab Notebook**。

---

## 🚀 Demo 連結  
直接在線上體驗 IVE 成員辨識功能：

👉 **Streamlit Demo:**  
https://ai-pk-recognition-k-pop-member-9g9nbw9uu5ngnmdp6objcg.streamlit.app/

---

## 🖥️ Streamlit App 功能介紹

Streamlit Demo 主要功能如下：

### ✅ 1. 上傳人像圖片  
使用者可上傳任意圖片，系統會自動偵測人臉。

### ✅ 2. 自動辨識 IVE 成員  
後端使用 InsightFace 進行人臉向量化，比對以下成員：  
- Yujin  
- Wonyoung  
- Rei  
- Liz  
- Leeseo  
- Gaeul  

### ✅ 3. 「輸入猜測」改為下拉選單  
選單提供 IVE 所有成員，不需手動輸入英文名字。

### ✅ 4. 顯示載入提示  
第一次運行會載入模型，需要 5–10 秒，因此頁面會提示使用者耐心等待。

### ✅ 5. 比對結果顯示  
輸出內容包含：  
- 模型辨識出的成員  
- 使用者的猜測  
- 相似度（cosine similarity）  
- 標記人臉框的圖片  

---

## 📁 專案結構

