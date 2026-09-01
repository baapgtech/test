def extract_json(text):

    text = text.strip()

    # Remove markdown fences if model adds them
    text = re.sub(r"```json", "", text, flags=re.IGNORECASE)
    text = re.sub(r"```", "", text)

    # Find JSON object
    match = re.search(r"\{.*\}", text, re.DOTALL)

    if not match:
        raise ValueError("No JSON found in Mistral response")

    return json.loads(match.group())


diagram_spec = extract_json(raw_response)

print(json.dumps(diagram_spec, indent=2))
