import json
import re

def generate_diagram_spec(business_prompt):

    prompt = f"""
You are a senior software architect.

Your task is to convert a business/system description into
a precise architecture or flow diagram specification.

Business/System Description:
{business_prompt}

Return ONLY valid JSON.

Use exactly this structure:

{{
  "title": "Short diagram title",
  "nodes": [
    {{
      "id": "unique_id",
      "label": "Component name",
      "type": "user|service|database|queue|external|llm"
    }}
  ],
  "edges": [
    {{
      "source": "source_node_id",
      "target": "target_node_id",
      "label": "relationship or action"
    }}
  ]
}}

Rules:
1. Identify all important components.
2. Represent the actual flow between components.
3. Do not invent unnecessary components.
4. Node IDs must be unique.
5. Keep node labels short.
6. Preserve important business terminology.
7. Every edge source and target must exist in nodes.
8. Return JSON only.
"""

    messages = [
        {
            "role": "user",
            "content": prompt
        }
    ]

    inputs = tokenizer.apply_chat_template(
        messages,
        return_tensors="pt",
        add_generation_prompt=True
    ).to("cuda")

    with torch.no_grad():

        outputs = model.generate(
            inputs,
            max_new_tokens=1200,
            temperature=0.1,
            do_sample=False
        )

    response = tokenizer.decode(
        outputs[0][inputs.shape[-1]:],
        skip_special_tokens=True
    )

    return response
