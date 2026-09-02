# ============================================================
# GENERIC AI DIAGRAM GENERATOR
# Snowflake Cortex + Mistral Large 2 + Graphviz
# ============================================================

import re
import time
from pathlib import Path

from snowflake.snowpark.context import get_active_session
from snowflake.cortex import complete, CompleteOptions

from graphviz import Source
from IPython.display import Image, display


# ============================================================
# 1. CONFIGURATION
# ============================================================

MODEL_NAME = "mistral-large2"

MAX_TOKENS = 2500
TEMPERATURE = 0.0

OUTPUT_DIR = Path("generated_diagrams")
OUTPUT_DIR.mkdir(exist_ok=True)

session = get_active_session()


# ============================================================
# 2. SYSTEM PROMPT
# ============================================================

SYSTEM_PROMPT = """
You are an expert system architect and technical diagram generator.

Your task is to convert a user's natural-language requirement into
a clear and accurate Graphviz DOT diagram.

IMPORTANT RULES:

1. Return ONLY valid Graphviz DOT code.
2. Do NOT return Markdown.
3. Do NOT use ```dot or ``` blocks.
4. Do NOT provide explanations before or after the DOT code.
5. Always start with:

   digraph G {

6. Always close the graph with:

   }

7. Use:

   rankdir=LR;

8. Create meaningful node IDs without spaces.
9. Use human-readable labels for nodes.
10. Clearly represent the flow using arrows.
11. Preserve important terminology from the user's requirement.
12. Do not invent unnecessary components.
13. If the requirement contains decisions, represent them using
    diamond-shaped nodes.
14. Clearly label decision branches such as:
       Yes / No
       Pass / Fail
       Low Risk / High Risk
       Success / Failure
15. Use appropriate shapes:

    - User / Actor      -> ellipse
    - API / Service     -> box
    - Database          -> cylinder
    - Queue / Kafka     -> box3d
    - Decision          -> diamond
    - External System   -> component
    - Agent / AI        -> box

16. Keep the diagram readable and avoid unnecessary complexity.
17. If the user describes a sequence, preserve the sequence.
18. If the user describes an architecture, show major components
    and their interactions.
19. If the user describes a pipeline, show the pipeline stages.
20. If the user describes a workflow, show the workflow and decisions.

Example:

digraph G {
    rankdir=LR;

    User [
        label="User"
        shape=ellipse
    ];

    API [
        label="API Gateway"
        shape=box
    ];

    Database [
        label="Database"
        shape=cylinder
    ];

    User -> API [
        label="Request"
    ];

    API -> Database [
        label="Read / Write"
    ];
}

Generate only the DOT diagram.
"""


# ============================================================
# 3. BUILD MISTRAL PROMPT
# ============================================================

def build_prompt(user_requirement: str) -> str:
    """
    Build the final prompt sent to Mistral.

    Parameters:
        user_requirement: Any natural-language diagram requirement.

    Returns:
        Prompt string.
    """

    return f"""
{SYSTEM_PROMPT}

USER REQUIREMENT
----------------
{user_requirement}

TASK
----
Convert the above requirement into a clear Graphviz DOT diagram.

Remember:
- Return ONLY DOT code.
- No Markdown.
- No explanation.
- No ``` blocks.
- Start with "digraph G {{"
- End with "}}"
"""


# ============================================================
# 4. CALL MISTRAL
# ============================================================

def call_mistral(user_requirement: str):
    """
    Send the user's requirement to Mistral Large 2.

    Returns:
        response, latency
    """

    prompt = build_prompt(user_requirement)

    start_time = time.time()

    response = complete(
        MODEL_NAME,
        prompt,
        options=CompleteOptions({
            "temperature": TEMPERATURE,
            "max_tokens": MAX_TOKENS
        }),
        session=session
    )

    latency = round(time.time() - start_time, 2)

    return response, latency


# ============================================================
# 5. CLEAN MISTRAL OUTPUT
# ============================================================

def clean_dot(response: str) -> str:
    """
    Clean the model response and extract only Graphviz DOT code.
    """

    if response is None:
        raise ValueError("Mistral returned an empty response.")

    response = str(response).strip()

    # Remove Markdown code fences if model accidentally adds them
    response = re.sub(r"```(?:dot|graphviz)?", "", response, flags=re.IGNORECASE)
    response = response.replace("```", "")

    response = response.strip()

    # Find the beginning of digraph
    start = response.find("digraph")

    if start == -1:
        raise ValueError(
            "Mistral response does not contain valid Graphviz DOT code."
        )

    response = response[start:]

    # Try to cut anything after the final closing brace
    end = response.rfind("}")

    if end != -1:
        response = response[:end + 1]

    return response.strip()


# ============================================================
# 6. VALIDATE DOT
# ============================================================

def validate_dot(dot_code: str):
    """
    Basic validation for generated DOT code.
    """

    if not dot_code:
        raise ValueError("DOT code is empty.")

    if not dot_code.strip().startswith("digraph"):
        raise ValueError(
            "Invalid DOT: graph must start with 'digraph'."
        )

    if "{" not in dot_code:
        raise ValueError(
            "Invalid DOT: opening '{' not found."
        )

    if "}" not in dot_code:
        raise ValueError(
            "Invalid DOT: closing '}' not found."
        )

    # Basic brace balance check
    if dot_code.count("{") != dot_code.count("}"):
        raise ValueError(
            "Invalid DOT: braces are not balanced."
        )

    return True


# ============================================================
# 7. RENDER DIAGRAM
# ============================================================

def render_diagram(dot_code: str, diagram_name: str = "diagram"):
    """
    Convert DOT code into PNG using Graphviz.

    Returns:
        PNG file path
    """

    safe_name = re.sub(
        r"[^a-zA-Z0-9_-]",
        "_",
        diagram_name
    )

    output_path = OUTPUT_DIR / safe_name

    graph = Source(dot_code)

    rendered_path = graph.render(
        filename=str(output_path),
        format="png",
        cleanup=True
    )

    return rendered_path


# ============================================================
# 8. GENERIC DIAGRAM GENERATOR
# ============================================================

def generate_diagram(
    user_requirement: str,
    diagram_name: str = "diagram",
    display_image: bool = True
):
    """
    Generate a diagram from ANY natural-language requirement.

    Parameters
    ----------
    user_requirement : str
        Natural-language description of the diagram.

    diagram_name : str
        Name of the generated diagram file.

    display_image : bool
        Whether to display the generated PNG in the notebook.

    Returns
    -------
    dict
        Contains:
        - input
        - dot_code
        - output_path
        - latency_seconds
    """

    # --------------------------------------------------------
    # Input validation
    # --------------------------------------------------------

    if not user_requirement:
        raise ValueError(
            "user_requirement cannot be empty."
        )

    user_requirement = user_requirement.strip()

    print("=" * 70)
    print("AI DIAGRAM GENERATOR")
    print("=" * 70)

    print("\nUser Requirement:")
    print(user_requirement)

    # --------------------------------------------------------
    # Step 1: Mistral generation
    # --------------------------------------------------------

    print("\n[1/4] Calling Mistral...")

    response, latency = call_mistral(
        user_requirement
    )

    print(f"Mistral response generated in {latency} seconds.")

    # --------------------------------------------------------
    # Step 2: Clean DOT
    # --------------------------------------------------------

    print("\n[2/4] Cleaning DOT...")

    dot_code = clean_dot(response)

    # --------------------------------------------------------
    # Step 3: Validate DOT
    # --------------------------------------------------------

    print("\n[3/4] Validating DOT...")

    validate_dot(dot_code)

    print("DOT validation successful.")

    # --------------------------------------------------------
    # Step 4: Render PNG
    # --------------------------------------------------------

    print("\n[4/4] Rendering diagram...")

    output_path = render_diagram(
        dot_code,
        diagram_name
    )

    print(f"Diagram generated: {output_path}")

    # --------------------------------------------------------
    # Display
    # --------------------------------------------------------

    if display_image:
        display(
            Image(
                filename=output_path
            )
        )

    print("\n" + "=" * 70)
    print("DIAGRAM GENERATION COMPLETED")
    print("=" * 70)

    return {
        "input": user_requirement,
        "dot_code": dot_code,
        "output_path": output_path,
        "latency_seconds": latency
    }


# ============================================================
# 9. EXAMPLE 1 - DIGITAL CLAIM EXAMINER
# ============================================================

claim_requirement = """
Create a healthcare Digital Claim Examiner workflow.

A provider submits a healthcare claim through the Claims Intake API.
The Digital Claim Examiner Agent receives the claim and validates
required fields, member eligibility, provider information, service
dates, procedure codes, diagnosis codes, and duplicate indicators.

If validation fails, reject the claim and provide the rejection reason.

If validation passes, perform business rule checks and AI-based
analysis.

The system checks for duplicate services, unusual procedure and
diagnosis combinations, incorrect coding, out-of-network providers,
and suspicious claim patterns.

Calculate a risk score.

If the risk is low, automatically approve the claim and send it to
downstream claim processing.

If the risk is high, send the claim to a human claim examiner for
manual review.

Store the claim, validation results, analysis results, risk score,
and final decision in the Claims Database.

Clearly show Validation Pass/Fail and Low Risk/High Risk branches.
"""


result = generate_diagram(
    user_requirement=claim_requirement,
    diagram_name="digital_claim_examiner"
)


# ============================================================
# 10. PRINT GENERATED DOT
# ============================================================

print("\nGenerated DOT:")
print("-" * 70)
print(result["dot_code"])
print("-" * 70)


# ============================================================
# 11. MORE GENERIC EXAMPLES
# ============================================================

# Example 2: Microservice architecture
#
# result = generate_diagram(
#     """
#     Create a microservice architecture where a user sends requests
#     through an API Gateway. The gateway routes requests to Order
#     Service and Payment Service. Both services use PostgreSQL.
#     Payment Service publishes events to Kafka.
#     """,
#     diagram_name="microservice_architecture"
# )


# Example 3: Data pipeline
#
# result = generate_diagram(
#     """
#     Create a data pipeline where files are uploaded to Amazon S3.
#     Airflow orchestrates an ETL process. The ETL service extracts
#     and transforms the data and loads it into Snowflake. A machine
#     learning service reads processed data from Snowflake and
#     generates predictions.
#     """,
#     diagram_name="data_pipeline"
# )


# Example 4: Generic approval workflow
#
# result = generate_diagram(
#     """
#     Create an employee expense approval workflow.
#     An employee submits an expense. The system validates the
#     expense amount and required documents. If validation fails,
#     return the expense to the employee. If validation passes,
#     check whether the amount is above 5000. Expenses above 5000
#     require manager approval. Expenses below 5000 are automatically
#     approved and sent to finance for payment.
#     """,
#     diagram_name="expense_approval"
# )
