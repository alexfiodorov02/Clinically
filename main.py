from summarizer import summarize_note
from compliance import flag_compliance_issues

def load_note(path):
    with open(path, "r") as f:
        return f.read()

def main():
    note_path = "sample-notes/note-1.txt"
    note_text = load_note(note_path)

    print("\n--- ORIGINAL NOTE ---\n")
    print(note_text[:500] + "\n...")  # show snippet

    print("\n--- SUMMARY ---\n")
    summary = summarize_note(note_text)
    print(summary)

    print("\n--- COMPLIANCE FLAGS ---\n")
    issues = flag_compliance_issues(note_text)
    if issues:
        for issue in issues:
            print(f"⚠️  {issue}")
    else:
        print("No compliance issues detected.")

if __name__ == "__main__":
    main()
