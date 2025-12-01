# 🎤 IVE AI PK Demo

這是一個使用 **Streamlit** 架設的互動式 Demo，透過 **InsightFace** 模型辨識韓國女團 **IVE** 成員，並提供 AI PK 遊戲互動功能。

---

## 功能介紹

1. **團員介紹區**  
   - 顯示 IVE 全員的代表照片與名字，讓使用者快速認識團員。

2. **即時辨識區**  
   - 上傳一張圖片後，系統自動偵測臉部，並使用 AI 預測這位團員是誰。

3. **AI PK 遊戲區**  
   - 系統隨機抽取一張團員照片，使用者需從下拉選單中選擇猜測團員名字。
   - 提交後會顯示：
     - 使用者猜測結果
     - AI 預測結果
     - 正確答案
   - 即時互動，增加趣味性。

4. **Jupyter Notebook 示範 (`IVE_AI_PK.ipynb`)**  
   - 提供完整程式碼範例與教學，包含：
     - 團員照片資料準備
     - InsightFace 模型初始化
     - 臉部特徵向量建立
     - 成員辨識流程
     - 遊戲互動邏輯
   - 適合想了解程式細節或自行修改的使用者。

---

## 使用方式

1. **訪問 Demo**  
   - 點擊以下連結即可直接體驗：  
   [IVE AI PK Demo]([https://ai-pk-recognition-k-pop-member-9g9nbw9uu5ngnmdp6objcg.streamlit.app/](https://ai-pk-recognition-k-pop-member-56szmhdqpdtztcpssy92xg.streamlit.app/))

2. **上傳照片辨識**  
   - 點擊「選擇一張圖片」上傳圖片（jpg/jpeg/png）。
   - 系統將自動分析圖片並預測該團員。

3. **AI PK 遊戲**  
   - 在遊戲區從下拉選單選擇你猜的團員名字。
   - 點擊「提交猜測」後，系統會顯示結果及 AI 預測。

4. **使用 Notebook (`IVE_AI_PK.ipynb`)**  
   - 開啟 Notebook，可在本地運行，學習或修改辨識邏輯。
   - 適合對程式細節或 AI 模型使用有興趣的使用者。

---

## 環境需求

- Python 3.10+
- 套件：
```txt
streamlit
insightface
numpy
opencv-python
requests
beautifulsoup4
Pillow
```

- 建議先在本地準備好各團員照片於 `ive_members` 資料夾，以避免部署時網路下載造成錯誤。

---

## 專案結構

```
AI-PK-recognition-k-pop-member/
│
├─ app.py              # Streamlit 主程式
├─ IVE_AI_PK.ipynb     # Jupyter Notebook 示範
├─ requirements.txt    # 環境需求
└─ ive_members/        # 團員照片資料夾 (Yujin, Wonyoung, Rei, Liz, Leeseo)
```

---

## 注意事項

- 初次啟動 App 時，若需要下載 InsightFace 模型，可能需稍等。
- 避免在 Streamlit Cloud 部署時使用即時爬取 Google 圖片，建議先將照片準備好放在 `ive_members`。
- 系統主要使用 CPU 模式運行 InsightFace，可透過 `ctx_id=-1` 設定。

---

## Demo 連結

[https://ai-pk-recognition-k-pop-member-9g9nbw9uu5ngnmdp6objcg.streamlit.app/](https://ai-pk-recognition-k-pop-member-9g9nbw9uu5ngnmdp6objcg.streamlit.app/)

