from pathlib import Path

path = Path("index.html")
text = path.read_text(encoding="utf-8")

insert_code = '''
    async function loadGeneratedData() {
      try {
        const papersRes = await fetch("./data/papers.json");
        const generatedPapers = await papersRes.json();

        if (generatedPapers && generatedPapers.length) {
          state.papers = generatedPapers;
          state.selectedPaperId = generatedPapers[0].id;
        }
      } catch (e) {
        console.error("Failed to load generated data:", e);
      }
    }

'''

old = '''document.addEventListener("DOMContentLoaded", () => {
      renderAll();'''

new = '''document.addEventListener("DOMContentLoaded", async () => {
      await loadGeneratedData();
      renderAll();'''

if "async function loadGeneratedData()" not in text:
    text = text.replace(old, insert_code + new)

path.write_text(text, encoding="utf-8")

print("index.html updated")
