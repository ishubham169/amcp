# app.py
from cypher_generator import generate_cypher, sanitize_cypher, ensure_valid_cypher
from graph import run_query

def main():
    print("Welcome to CodeGraph AI 🔍")
    while True:
        print("\n")
        question = input("Ask a question about your codebase: ")

        print("\n🧠 Generating Cypher query...")
        cypher = sanitize_cypher(generate_cypher(question))
        cypher = ensure_valid_cypher(cypher)

        if cypher.endswith("}"):
            cypher = cypher[:-1].strip()

        print(f"\n🔁 Generated Cypher:\n{cypher}")
        print("\n📡 Querying Neo4j...")
        results = run_query(cypher)
        for row in results:
            print(row)

if __name__ == "__main__":
    main()
