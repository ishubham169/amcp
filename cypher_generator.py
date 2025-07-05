import openai
import os

def generate_cypher(user_question: str) -> str:
    prompt = f"""
You are an expert in converting English to Cypher queries for a Neo4j graph database representing Python source code structure.

The graph uses these node types:
- File
- PythonClass
- PythonFunction
- PythonMethod
- PythonParameter
- PythonVariable
- PythonModule

And these relationship types:
- PYTHON_DEFINES_CLASS (File → PythonClass)
- PYTHON_DEFINES_FUNCTION (File → PythonFunction)
- PYTHON_HAS_METHOD (PythonClass → PythonMethod)
- PYTHON_HAS_PARAMETER (PythonFunction/PythonMethod → PythonParameter)
- PYTHON_IMPORTS (File → PythonModule)
- PYTHON_CALLS (PythonFunction/PythonMethod/File → PythonFunction)

Write a Cypher query that answers the following question:
\"\"\"{user_question}\"\"\"

Only return the Cypher query. Do not include any explanation or formatting like ```cypher.
"""

    openai.api_base = "https://api.together.xyz/v1"
    openai.api_key = 'c23cc4fa5200f6a935a430bc2dcb37833388de5068cea5259a5966da3bd57d0f'

    response = openai.ChatCompletion.create(
        model="mistralai/Mixtral-8x7B-Instruct-v0.1",
        messages=[{"role": "user", "content": prompt}]
    )
    return response["choices"][0]["message"]["content"].strip()


def ensure_valid_cypher(query: str) -> str:
    """Ensure the query has a RETURN clause, otherwise add a fallback."""
    if "RETURN" not in query.upper():
        query += "\nRETURN *"
    return query.strip()

def sanitize_cypher(query: str) -> str:
    """Remove markdown formatting or trailing junk like ``` or explanations."""
    lines = query.strip().splitlines()
    clean_lines = [line for line in lines if not line.strip().startswith("```") and not line.strip().startswith("#")]
    return "\n".join(clean_lines).strip()
