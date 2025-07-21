
# 🎬 Redis Movies & Actors Data Exploration

This project explores a dataset of over 1,300 actors and 900 movies using **Redis**, a high-performance NoSQL in-memory data store. It showcases how to use **Docker**, **RedisInsight**, and **Python (Jupyter Notebook)** for real-world data querying and manipulation.

---

## 📚 Project Objectives

- Set up Redis and RedisInsight using Docker Compose
- Load actor and movie datasets using `HSET` commands
- Query the Redis database using Python
- Perform common data operations: filtering, updating, and deleting records
- Present results clearly in a notebook and final PDF report

---

## 🧠 Skills Demonstrated

✅ Redis CLI & Hashes  
✅ Docker Compose  
✅ Python Redis Client (`redis-py`)  
✅ Jupyter Notebook for Data Exploration  
✅ RedisInsight GUI  
✅ Git & GitHub Version Control  

---

## 🗂️ Project Structure

```
redis-movie-actors-project/
├── data/
│   ├── actors.redis
│   ├── movies.redis
│   └── dump.rdb                  # Redis database dump
├── notebooks/
│   └── results_notebook.ipynb    # This notebook
├── docker-compose.yml            # Redis + RedisInsight setup
├── py_script.py                  # Python script for data operations
├── README.md                     # Project overview & instructions
├── requirements.txt              # Python dependencies
└── results_PDF.pdf               # Exported notebook results as PDF
```

---

## ⚙️ Environment Setup

Using Docker Compose to launch:

- **Redis server** (`redis:latest`) on port 6379
- **RedisInsight GUI** (`redis/redisinsight:latest`) on port 5540

```bash
docker-compose up -d
```

> RedisInsight UI available at [http://localhost:5540](http://localhost:5540)

---

## 📥 Data Loading

Insert actor and movie data into Redis using:

```bash
docker exec -i redis-server redis-cli < data/actors.redis
docker exec -i redis-server redis-cli < data/movies.redis
```

This stores each actor and movie as a Redis hash under keys like:
- `actor:<id>`
- `movie:<id>`

---

## 🧪 Data Exploration in Python

Data exploration was done in `redis_data_exploration.ipynb` using the `redis` Python client.

Queries and operations included:

- 📊 Count: number of actors and movies
- 👤 Filter: actors born before 1980
- 🎞️ Lookup: genre and rating of "The Imitation Game"
- 🏆 Ranking: top 5 highest-rated movies
- 🎯 Filter: movies rated above 7.5
- 🔧 Update: modify movie rating
- ➕ Insert: new actor (Zendaya, 1996)
- 🗑️ Delete: movie titled "The Room"

Each query is explained and documented in the notebook.

---

## 📝 Documentation

- **Notebook**: `redis_data_exploration.ipynb` includes all logic, queries, and outputs
- **PDF Report**: `queries_results.pdf` is a clean export of the notebook
- **Methodology**: See [`methodology.md`](./methodology.md) for the implementation breakdown

---

## 🚀 How to Run the Project

1. Clone the repository:

```bash
git clone https://github.com/yacine-ammi/redis-movie-actors-project.git
cd redis-movie-actors-project
```

2. Start Redis + RedisInsight:

```bash
docker-compose up -d
```

3. Load the data:

```bash
docker exec -i redis-server redis-cli < data/actors.redis
docker exec -i redis-server redis-cli < data/movies.redis
```

4. Open the notebook (`redis_data_exploration.ipynb`) in **VS Code**, **Jupyter**, or **JupyterLab** and run all cells.

---

## 📌 Final Deliverables

- ✅ Redis database with data loaded
- ✅ Fully working Docker Compose environment
- ✅ Python-based exploration notebook
- ✅ PDF with documented results
- ✅ GitHub repository for sharing and versioning

---

## 🙋 About Me

This project was developed as part of a NoSQL/Redis course and reflects my hands-on skills with Dockerized environments, NoSQL data stores, and Python-based data processing.

Feel free to explore or contact me if you'd like to collaborate or give feedback!