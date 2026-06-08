# Repository Architecture Deep Dive

Analyze the entire repository as a Principal Software Architect and AI Engineer.

Do not just explain files. Reverse engineer the complete system and explain it from an interview perspective.

Provide:

1. Business problem being solved
2. High-level architecture diagram (Mermaid)
3. End-to-end request flow from user request to final response
4. Layer-by-layer explanation:
   - UI/Client Layer
   - API Layer
   - Authentication Layer
   - Service Layer
   - Business Logic Layer
   - Database Layer
   - Cache Layer
   - Queue/Event Layer
   - AI/RAG/LLM Layer (if applicable)
   - Monitoring Layer
   - Deployment Layer
5. For each layer explain:
   - Purpose
   - Components involved
   - Source code locations
   - Technologies used
   - Why that technology was chosen
6. Explain all major classes, services, models, and their relationships.
7. Identify design patterns used (Repository, Factory, Dependency Injection, Strategy, etc.).
8. Explain database schema, table relationships, indexes, and query flow.
9. Explain security, authentication, authorization, and secret management.
10. Explain scalability, fault tolerance, retry mechanisms, and bottlenecks.
11. Explain logging, monitoring, tracing, and observability.
12. Explain deployment architecture (Docker, Kubernetes, Cloud Services, CI/CD).
13. Generate a 5-minute and 10-minute interview-ready architecture explanation.
14. Generate the top 30 interview questions and answers that can be asked from this repository.

Important:
- Explain everything as a connected architecture, not file-by-file.
- Show how each component interacts with other components.
- Assume I need to explain this project to a Hiring Manager, Tech Lead, Architect, and AI Engineer interviewer.
- Be extremely detailed and use evidence from the codebase.
