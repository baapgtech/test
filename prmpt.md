Act as a Principal AI Architect, Staff AI Engineer, and Solution Architect.

Analyze the entire repository and reverse engineer the complete AI/RAG system.

Do not provide generic explanations.

Only explain what is actually implemented in the codebase.

For every statement provide:
- File name
- Class name
- Function name
- Code location

I want to understand the complete system from document upload to final answer generation.

====================================
SECTION 1 : PROJECT OVERVIEW
====================================

Explain:

1. What business problem is being solved?

2. Who are the end users?

3. What is the expected input?

4. What is the expected output?

5. Draw complete architecture diagram in text format.

6. Explain request lifecycle from start to end.

7. Identify all AI components.

8. Identify all external services.

9. Identify all databases.

10. Identify all queues/events.

====================================
SECTION 2 : DOCUMENT INGESTION PIPELINE
====================================

Trace document ingestion completely.

Explain:

1. How document enters system

2. Supported document formats

3. PDF processing library

4. OCR library

5. Image processing

6. Data cleaning

7. Duplicate detection

8. Versioning strategy

9. Metadata extraction

10. Validation checks

11. Error handling

12. Async processing

13. Queue usage

For every step explain:

- What happens
- Why it happens
- Which file implements it

Create sequence diagram.

====================================
SECTION 3 : CHUNKING PIPELINE
====================================

Find chunking implementation.

Explain:

1. Chunking strategy

2. Recursive chunking

3. Semantic chunking

4. Fixed chunking

5. Sliding window

6. Parent child chunking

7. Chunk size

8. Chunk overlap

9. Why chosen

10. Pros and cons

11. Configuration parameters

12. Failure scenarios

Show actual values from code.

Explain interview answer.

====================================
SECTION 4 : EMBEDDING PIPELINE
====================================

Identify all embedding models.

For each model explain:

1. Exact model name

2. Vendor

3. Embedding dimension

4. Input token limit

5. Cost considerations

6. Why selected

7. Alternative options

8. Where called in code

9. Parameters passed

10. Batch strategy

11. Caching strategy

12. Failure handling

Create table:

| Model | Dimension | Purpose | Location |

====================================
SECTION 5 : VECTOR DATABASE
====================================

Identify vector storage.

Explain:

1. Technology used

2. Schema

3. Index type

4. HNSW

5. IVF

6. Flat Index

7. Similarity metric

8. Cosine similarity

9. Euclidean distance

10. Metadata filtering

11. Partitioning

12. Performance optimization

13. Scaling strategy

14. Retrieval latency optimization

Show actual implementation.

====================================
SECTION 6 : QUERY UNDERSTANDING
====================================

Trace user question flow.

Explain:

1. Query preprocessing

2. Query classification

3. Intent detection

4. Query rewriting

5. Query expansion

6. Multi-query retrieval

7. HyDE

8. Self-query retrieval

9. Guardrails

10. Safety checks

11. Prompt injection protection

Explain actual implementation.

====================================
SECTION 7 : RETRIEVAL PIPELINE
====================================

Explain retrieval in detail.

For every step explain:

1. Query embedding generation

2. Similarity search

3. Hybrid search

4. BM25

5. Keyword search

6. Metadata filtering

7. Top-K retrieval

8. Candidate generation

9. Candidate filtering

10. Context ranking

11. Retrieval optimization

12. Recall optimization

13. Precision optimization

Show actual K values.

Show actual thresholds.

Create flow diagram.

====================================
SECTION 8 : RE-RANKING
====================================

Find re-ranking implementation.

Explain:

1. Cross Encoder usage

2. BGE Reranker

3. Cohere Reranker

4. LLM reranking

5. Score threshold

6. Candidate pruning

7. Latency tradeoffs

If reranking not implemented explain why.

====================================
SECTION 9 : CONTEXT CONSTRUCTION
====================================

Explain:

1. How retrieved chunks are selected

2. How many chunks used

3. Context ordering strategy

4. Metadata inclusion

5. Citation generation

6. Token budgeting

7. Context window optimization

8. Prompt assembly

9. Conversation history handling

10. Memory implementation

Show actual prompt templates.

====================================
SECTION 10 : LLM PIPELINE
====================================

Identify all LLMs.

For each LLM explain:

1. Model name

2. Provider

3. Context length

4. Temperature

5. Top P

6. Max Tokens

7. Frequency penalty

8. Presence penalty

9. Streaming

10. Function calling

11. Structured output

12. JSON mode

13. Why selected

14. Cost optimization

15. Fallback strategy

Create table:

| Model | Purpose | Parameters | Location |

====================================
SECTION 11 : ANSWER GENERATION
====================================

Explain:

1. How prompt is created

2. System prompt

3. User prompt

4. Retrieved context injection

5. Citation generation

6. Hallucination prevention

7. Grounding strategy

8. Output formatting

9. Confidence score generation

10. Post processing

Show actual implementation.

====================================
SECTION 12 : EVALUATION PIPELINE
====================================

Identify answer evaluation.

Explain:

1. Faithfulness evaluation

2. Groundedness

3. Relevancy

4. Context precision

5. Context recall

6. Toxicity

7. Bias checks

8. Hallucination detection

9. Human feedback

10. LLM-as-Judge

11. RAGAS

12. DeepEval

13. TruLens

14. Custom evaluation

Show actual metrics.

Show actual thresholds.

====================================
SECTION 13 : OBSERVABILITY
====================================

Explain:

1. LangSmith

2. Phoenix

3. Weights and Biases

4. OpenTelemetry

5. Monitoring

6. Tracing

7. Logging

8. Alerting

9. Cost tracking

10. Token tracking

11. Latency tracking

====================================
SECTION 14 : PRODUCTION READINESS
====================================

Explain:

1. Caching

2. Redis usage

3. Async processing

4. RabbitMQ

5. Kafka

6. Retries

7. Circuit breaker

8. Rate limiting

9. Load balancing

10. Kubernetes

11. Autoscaling

12. Disaster recovery

13. High availability

14. Cost optimization

15. Security

====================================
SECTION 15 : INTERVIEW MODE
====================================

Generate:

1. 2 minute project explanation

2. 5 minute architecture explanation

3. 10 minute deep dive

4. Complete RAG explanation

5. Why each model was selected

6. Tradeoffs made

7. Challenges faced

8. Production incidents possible

9. Scaling discussion

10. 50 interview questions

11. 50 follow-up questions

12. STAR format answers

13. Architecture discussion for Staff Engineer interview

14. Principal Engineer level critique

15. Improvements that can be made in current system

Be extremely detailed.
