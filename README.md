# 🧰 Gerador de Currículos para Devs (com IA)

> Kit reutilizável para montar uma **base de dados pessoal** e gerar **currículos sob medida por
> vaga**, com a ajuda de um assistente de IA (ex.: Claude Code). Bilíngue (PT/EN).
>
> Reusable kit to keep a **personal data base** and generate **job-tailored resumes** with an AI
> assistant (e.g. Claude Code). Bilingual (PT/EN).

---

## 🇧🇷 Português

### O que é
Em vez de manter um único currículo genérico, você guarda suas informações em blocos
(dados pessoais, experiências, projetos, habilidades, formação) e, para cada vaga, o assistente
**seleciona, prioriza e adapta** esses blocos em um currículo focado, gerando PDF (humano) e DOCX
(para sistemas ATS).

### Como usar
1. **Abra a pasta com um assistente de IA** (Claude Code lê `CLAUDE.md`; Cursor/Codex e outros leem
   `AGENTS.md`, que tem o mesmo conteúdo).
2. **Digite `começar`.** O assistente conduz o preenchimento dos seus dados passo a passo,
   perguntando uma seção por vez. (Ou preencha você mesmo os `<preencher>` nas pastas.)
3. **Envie a descrição de uma vaga.** O assistente cria a subpasta da vaga em `curriculos-gerados/`
   com: análise (`vaga.md`), aderência (`scorecard.md`), currículo (`.md`/`.html`/`.pdf`) e a
   versão ATS (`.docx`).
4. **Registre no rastreador** `candidaturas.md`.

### Requisitos
- Um assistente de IA que leia arquivos de contexto (`CLAUDE.md`).
- **Python 3** + `python-docx` (`pip install python-docx`) para a versão `.docx`.
- Um navegador **Chrome/Edge/Chromium** instalado para gerar o PDF.

### Gerar os arquivos
```bash
# PDF (a partir do HTML): detecta o navegador automaticamente
python scripts/gerar_pdf.py caminho/curriculo.html caminho/curriculo.pdf

# DOCX (ATS): edite o conteúdo no script e rode
python scripts/gerar_docx.py
```

---

## 🇺🇸 English

### What it is
Instead of one generic resume, you keep your information in blocks (personal data, experience,
projects, skills, education) and, for each job, the assistant **selects, prioritizes and adapts**
them into a focused resume, producing a PDF (for humans) and a DOCX (for ATS).

### How to use
1. **Open the folder with an AI assistant** (Claude Code reads `CLAUDE.md`; Cursor/Codex and others
   read `AGENTS.md`, which has the same content).
2. **Type `start`.** The assistant walks you through filling in your data step by step, one section
   at a time. (Or fill the `<fill in>` placeholders yourself.)
3. **Send a job description.** The assistant creates the job subfolder in `curriculos-gerados/`
   with: analysis (`vaga.md`), fit scorecard (`scorecard.md`), resume (`.md`/`.html`/`.pdf`) and
   the ATS version (`.docx`).
4. **Log it** in the `candidaturas.md` tracker.

### Requirements
- An AI assistant that reads context files (`CLAUDE.md`).
- **Python 3** + `python-docx` (`pip install python-docx`) for the `.docx` version.
- A **Chrome/Edge/Chromium** browser installed to render the PDF.

### Generate the files
```bash
# PDF (from HTML): auto-detects the browser
python scripts/gerar_pdf.py path/curriculo.html path/curriculo.pdf

# DOCX (ATS): edit the content in the script and run it
python scripts/gerar_docx.py
```

---

## 📁 Estrutura / Structure

| Pasta / Folder | Conteúdo / Contents |
| --- | --- |
| `dados-pessoais/` | Identificação, contato, resumo / Identity, contact, summary |
| `experiencia-profissional/` | Empregos, freelas, voluntariado / Jobs, freelance, volunteering |
| `formacao-academica/` | Formação / Education |
| `habilidades/` | Stack técnica + soft skills / Tech stack + soft skills |
| `idiomas/` | Idiomas / Languages |
| `certificacoes/` | Certificados e cursos / Certs and courses |
| `projetos-github/` | Um `.md` por repositório / One `.md` per repo |
| `templates/` | Modelos de currículo (html/md) + vaga/scorecard |
| `scripts/` | `gerar_pdf.py`, `gerar_docx.py` |
| `curriculos-gerados/` | Saída por vaga / Output per job |
| `candidaturas.md` | Rastreador / Application tracker |
| `CLAUDE.md` | Regras do assistente (Claude Code) / Assistant rules (Claude Code) |
| `AGENTS.md` | Mesmas regras para outras IAs / Same rules for other AI tools |
