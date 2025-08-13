import subprocess

def summarize_note(note_text):
    """Use ollama to summarize a clinical note."""
    prompt = f"Summarize the following clinical note in 3-4 concise bullet points:\n\n{note_text}"

    result = subprocess.run(
        ["ollama", "run", "llama3", prompt],
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        return "[Error generating summary]"
    
    return result.stdout.strip()
