# Methodology

This document summarizes the approach followed to complete the Redis Movie & Actor data exploration project.


## 1. Environment Setup

- **Docker Compose** was used to launch:
  - A Redis server (`redis:latest`)
  - RedisInsight GUI (`redis/redisinsight:latest`) for visual inspection
- Two `.redis` files (`actors.redis` and `movies.redis`) were placed in a mounted `data/` folder.

---

## 2. Data Loading

- Data insertion was done using the Redis CLI:
  ```bash
  docker exec -i redis-server redis-cli < data/actors.redis
  docker exec -i redis-server redis-cli < data/movies.redis

    This created HSET entries in Redis for actors and movies using keys like actor:<id> and movie:<id>.

## 3. Data Exploration (Python)

    A Jupyter notebook was used to connect to Redis using the redis Python client.

    Key patterns (actor:*, movie:*) were used to scan and interact with hash entries.

Queries performed:

    Counted actors and movies

    Filtered actors by birth year

    Retrieved movie details by title

    Ranked top-rated movies

    Updated and deleted specific records

    Inserted a new actor entry

## 4. Results and Documentation

    All outputs were documented in the Jupyter notebook.

    The notebook was exported as a PDF for submission.

    This README and the notebook describe how to run and reproduce the work.

✅ Tools Used

    Redis

    Docker & Docker Compose

    RedisInsight

    Python (Jupyter Notebook)

    Redis Python client (redis-py)