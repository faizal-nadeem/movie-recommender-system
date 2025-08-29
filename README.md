🎬 Movie Recommender System

A Content-Based Movie Recommender System that suggests similar movies based on their overview, genres, keywords, cast, and crew using NLP techniques and cosine similarity.

This project is implemented in Python and deployed as an interactive Streamlit web app.

---

🚀 Features

Recommends top 5 similar movies for any selected movie

Uses CountVectorizer + Cosine Similarity

Preprocessing includes cleaning, stemming, and combining metadata (overview, genres, cast, crew)

Saved trained data with Pickle for deployment

Interactive Streamlit Web App with movie posters

---

🛠️ Tech Stack

Python

Pandas, NumPy

Scikit-learn (Cosine Similarity)

nltk (NLP)

Pickle (for model saving)

Streamlit (for web app UI)

TMDb API (for fetching movie posters)

---

📂 Project Structure

📦 movie-recommender-system
 ┣ 📜 app.py                # Streamlit app
 ┣ 📜 Movie_Recommender_System.ipynb   # Jupyter Notebook (explaining project)
 ┣ 📜 movies_dict.pkl       # Movies data pickle
 ┣ 📜 similarity.pkl        # Similarity matrix pickle
 ┣ 📜 requirements.txt      # Python dependencies
 ┣ 📜 README.md             # Project documentation
 ┗ 📂 dataset
    ┣ 📜 movies.csv
    ┗ 📜 credits.csv

---

⚙️ Installation & Setup

1. Clone this repository
    git clone https://github.com/faizal-nadeem/movie-recommender-system.git
    cd movie-recommender-system

2. Install dependencies

    pip install -r requirements.txt

3. Run the Jupyter Notebook (optional, to see project explanation)

    jupyter notebook Movie_Recommender_System.ipynb

4. Run the Streamlit app

    streamlit run app.py

---

🌐 Deployment

This project is deployed on Streamlit Cloud.
👉 Live Demo Link

---

📊 Example Output

If you search for "Avatar", the recommender will suggest:

John Carter

Guardians of the Galaxy

The Helix …

[etc.]

---

🏆 Key Learnings

How to preprocess text data for NLP

How to create a content-based recommender system

Saving models with Pickle

Deploying ML projects with Streamlit Cloud

---

✨ Author

👤 Md Faizal Khan
📧 Email: your-email@example.com
💼 LinkedIn

---