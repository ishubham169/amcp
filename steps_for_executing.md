## 🧠 Python Code Graph Analysis with Neo4j

This tool analyzes Python source code, extracts classes, functions, method calls, and more, and stores them in a Neo4j graph database. You can then query the code using natural language!

---

### ✅ Step 1: Analyze and Push Python Code to Neo4j

Run the following command to parse your Python directory and push the results to your Neo4j database:

```bash
node dist/index.js analyze ../your_python_directory
```

### 🚀 Step 2: Run the Natural Language Query Server
Start the Python server to convert natural language questions into Cypher queries:

```bash
python app.py
```

Once the server is running, you can ask questions like:
"Which functions call pid_control?"
"List all classes that define a method named update."
"Show all files that import numpy."

