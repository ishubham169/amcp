#!/bin/bash

# Set Neo4j environment variables
export NEO4J_URI="bolt://localhost:7687"
export NEO4J_USERNAME="neo4j"
export NEO4J_PASSWORD="test1234"
export NEO4J_DATABASE="neo4j"

# Navigate to the project root (optional but safe)
cd "$(dirname "$0")"

# Run the server script (relative path)
node node_modules/@alanse/mcp-neo4j-server/build/server.js
