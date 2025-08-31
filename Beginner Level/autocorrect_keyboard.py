from spellchecker import SpellChecker

sp = SpellChecker()

while True:
    text_in = input("\nEnter a sentence to autocorrect (type 'exit' to finish): ")
    if text_in.lower() in ["exit", "quit"]:
        print("\nAutocorrect session ended.")
        break

    tokens = text_in.split()
    errors = sp.unknown(tokens)

    print("\nDetected Mistakes:", errors if errors else "None")

    for err in errors:
        fix = sp.correction(err)
        opts = sp.candidates(err)
        print(f"\nWord: {err}")
        print(f"Suggested correction: {fix}")
        print(f"Other possibilities: {opts}")

    corrected_text = " ".join([sp.correction(t) if t in errors else t for t in tokens])
    print("\nCorrected Sentence:", corrected_text)
