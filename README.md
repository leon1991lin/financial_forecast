# 財務檢看聽 - 公司獲利趨勢預測模型

<h3>簡報影片連結: https://youtu.be/Gwv5ZpQTaO0</h3>

<h3>簡報資料：https://drive.google.com/file/d/1QM4oGZF-HkpaKRn3lyxbQBpI4vwWcJdu/view?usp=sharing</h3>

本研究是針對台灣半導體業中長期價值投資者，以財務、股權、貿易、原物料、疫情與輿情影響等建立獲利趨勢預測模型。

透過網頁爬蟲及開源資料庫取得財務報表、股東及董監事股權資訊、新冠肺炎疫情統計、國際原物料行情、商品價格、能源指數、貿易統計、匯率等特徵。

預測標的為股東權益報酬率(ROE)，預測下一紀錄 ROE 表現是否會高於過去三年的產業平均。

透過特徵工程、選擇與模型評估分析，最終完成羅吉斯回歸模型、隨機森林模型與 DNN神經網路模型的建立。
其中以隨機森林模型表現最佳，針對真實數據的預測準確度可達 0.88，F1 Score 達 0.92。
