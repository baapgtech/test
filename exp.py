business_prompt = """
Create a flow diagram for an AI document processing system.

A user uploads a document.
The document is received by an API Gateway.
The API Gateway sends the document to a Document Processing Service.
The service extracts text from the document.
The extracted text is sent to an Embedding Service.
The embeddings are stored in a Vector Database.

When the user asks a question, the system retrieves
relevant information from the Vector Database.
The retrieved information is sent to an LLM.
The LLM generates the final answer.
The answer is returned to the user.
"""

raw_response = generate_diagram_spec(business_prompt)

print(raw_response)
