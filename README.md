# 📊 YouTube Comment Analysis

A Streamlit-based web application that analyzes YouTube video comments and provides insightful visualizations, sentiment analysis, and NLP-based text analytics.

---

## 🚀 Live Demo

🔗 **Live Demo:** https://youtubecommentanalysis-mdklyqko75aeyyh52e3hdj.streamlit.app/

## 📌 Features

- 🎥 Analyze comments from any public YouTube video
- 📈 Comment statistics
  - Total Comments
  - Unique Users
  - Average Comment Length
  - Total Likes
- 📅 Monthly comment timeline
- 📆 Weekly activity analysis
- 👤 Top commenters
- ☁️ Word Cloud generation
- 🔤 Most common words
- ❤️ Sentiment Analysis (Positive, Neutral, Negative)
- 😊 Most positive comments
- 😠 Most negative comments
- 📝 Top Bigrams
- 💬 Top Trigrams
- 🔑 TF-IDF Keyword Extraction
- 🔥 Activity Heatmap

---

## 🛠️ Tech Stack

### Frontend
- Streamlit

### Backend
- Python

### Libraries
- Pandas
- NumPy
- Matplotlib
- Seaborn
- NLTK
- WordCloud
- Scikit-learn
- VaderSentiment
- Google API Python Client

---

## 📂 Project Structure

```
youtube_comment_analysis/
│
├── app.py
├── helper.py
├── preprocessor.py
├── youtube_api.py
├── requirements.txt
├── README.md
└── .streamlit/
```

---

## 📊 Analysis Performed

### Comment Statistics
- Total Comments
- Total Likes
- Unique Users
- Average Comment Length

### Time-Based Analysis
- Monthly Timeline
- Weekly Activity
- Activity Heatmap

### NLP Analysis
- Word Cloud
- Most Common Words
- Sentiment Analysis
- Positive Comments
- Negative Comments
- Bigrams
- Trigrams
- TF-IDF Keywords

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/your-username/youtube_comment_analysis.git
```

Go to the project directory

```bash
cd youtube_comment_analysis
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

## 🔑 API Key Setup

This project uses the **YouTube Data API v3**.

### Local Development

Create a `.env` file:

```
API_KEY=YOUR_YOUTUBE_API_KEY
```

### Streamlit Cloud

Go to

**App Settings → Secrets**

Add

```toml
API_KEY = "YOUR_YOUTUBE_API_KEY"
```

---


## 📦 Requirements

Install all dependencies using

```bash
pip install -r requirements.txt
```

---

## 🎯 Future Improvements

- Emoji Analysis
- Export Reports as PDF
- Interactive Charts
- Topic Modeling using LDA
- Multi-language Support
- AI-based Comment Summarization
- Spam Comment Detection

---

## 🤝 Contributing

Contributions are welcome.

Fork the repository and submit a Pull Request.

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Tushar Dhakrey**

GitHub: https://github.com/Tushar-Dhakrey

LinkedIn: https://www.linkedin.com/in/tushar-dhakrey-57883a332/
