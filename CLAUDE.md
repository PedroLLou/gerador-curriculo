# CLAUDE.md

Instruções para o assistente de IA ao gerar currículos neste repositório.
Instructions for the AI assistant when generating resumes in this repository.

> Este arquivo e o `AGENTS.md` têm o **mesmo conteúdo**. Use o que sua ferramenta de IA lê (Claude
> Code lê `CLAUDE.md`; Cursor/Codex e outros leem `AGENTS.md`). Mantenha os dois em sincronia.
> This file and `AGENTS.md` have the **same content**. Use whichever your AI tool reads (Claude Code
> reads `CLAUDE.md`; Cursor/Codex and others read `AGENTS.md`). Keep both in sync.

---

## 🚀 Como começar / Getting started

**Gatilho / Trigger:** quando o usuário disser **"começar"** (ou **"start"**), conduza o onboarding
abaixo. / when the user says **"start"** (or **"começar"**), run the onboarding below.

**🇧🇷 Passo a passo (a IA conduz, uma seção por vez, e preenche os arquivos):**
1. Dê as boas-vindas e explique em 1-2 linhas o que este kit faz.
2. Verifique quais arquivos ainda têm `<preencher>`. Se já estiverem preenchidos, pule direto para o
   passo 4.
3. **Entreviste o usuário, uma seção por vez** (não peça tudo de uma vez; confirme antes de salvar) e
   preencha:
   - `dados-pessoais/perfil.md` (nome, contato, links, localização, objetivo, pretensão)
   - `experiencia-profissional/` (cada experiência: cargo, empresa, período, o que fez, tech, resultados)
   - `formacao-academica/`, `habilidades/stack-tecnico.md` (com níveis), `idiomas/`, `certificacoes/`
   - `projetos-github/` (se houver integração com GitHub/MCP, ofereça mapear os repos
     automaticamente; senão, peça os links dos repositórios relevantes)
4. Ao terminar, diga: **"Pronto! Agora me envie a descrição de uma vaga e eu monto seu currículo."**
5. Quando o usuário enviar a vaga, siga o **Fluxo** abaixo. Lembre os requisitos de geração
   (Python + `python-docx`, navegador) só na hora de gerar os arquivos.

**🇺🇸 Step by step (the AI leads, one section at a time, and fills the files):**
1. Welcome the user and explain in 1-2 lines what this kit does.
2. Check which files still contain `<fill in>`. If already filled, skip to step 4.
3. **Interview the user, one section at a time** (do not ask for everything at once; confirm before
   saving) and fill in: `dados-pessoais/perfil.md`, `experiencia-profissional/`,
   `formacao-academica/`, `habilidades/stack-tecnico.md` (with levels), `idiomas/`, `certificacoes/`,
   and `projetos-github/` (offer to map repos automatically if a GitHub/MCP integration exists;
   otherwise ask for the relevant repo links).
4. When done, say: **"All set! Now send me a job description and I'll build your resume."**
5. When the user sends a job, follow the **Workflow** below. Mention the generation requirements
   (Python + `python-docx`, a browser) only when it is time to generate the files.

---

## ✍️ Escopo: carta e perguntas / Scope: cover letter and application questions

Além do currículo, o assistente também ajuda com / Besides the resume, the assistant also helps with:

- **Carta de apresentação / Cover letter:** se a vaga pedir, gere `carta.md` (e `carta.pdf` opcional)
  a partir de `templates/carta.*`. Curta (3-4 parágrafos), específica, **não repetir o currículo**,
  gancho de fit no início, sem clichês, sem travessão. / if requested, generate `carta.md` (and an
  optional `carta.pdf`) from `templates/carta.*`. Short, specific, do not restate the resume.
- **Perguntas de candidatura / Application questions** ("por que aqui?", "quantos anos com X?",
  "descreva seu fluxo"): responder com fatos da base, calibrado por senioridade, **sem inventar**.
  Se houver teste técnico adiante, não exagerar o que não dá para defender. / answer from the data
  base, calibrated to seniority, never fabricating; if a tech test is coming, do not overclaim.

## 🔎 QA antes de finalizar / QA before finalizing

Rode o lint no `curriculo.md` e corrija os alertas antes de gerar o PDF/DOCX.
Run the lint on `curriculo.md` and fix the warnings before generating the PDF/DOCX:

```bash
python scripts/lint.py curriculos-gerados/<pasta>/curriculo.md curriculos-gerados/<pasta>/vaga.md
```

Verifica / Checks: travessão "—", buzzwords, bullets longos, aberturas repetidas e palavras-chave da
vaga ausentes. / em dash, buzzwords, long bullets, repeated openings and missing job keywords.

---

## 🇧🇷 Português

### Propósito
Base de dados pessoal para gerar currículos sob medida por vaga. Não é código: é matéria-prima
(dados, experiências, projetos, habilidades) selecionada e adaptada para cada vaga.

### Fluxo (cada vaga vira uma subpasta `curriculos-gerados/<empresa>-<cargo>-AAAA-MM-DD/`)
1. O usuário envia a **descrição de uma vaga**.
2. **Sincronizar GitHub (se disponível):** se houver um MCP/integração de GitHub, verifique repos
   novos/atualizados e atualize `projetos-github/` antes de montar.
3. **Analisar a vaga (obrigatório):** salve `vaga.md` com empresa, cargo, senioridade, requisitos
   obrigatórios, diferenciais, palavras-chave (na redação exata), idioma e riscos.
4. **Scorecard (obrigatório):** salve `scorecard.md` classificando cada requisito como
   **forte / médio / ausente**, listando diferenciais não cobertos e riscos.
5. **Montar o currículo** seguindo as Regras de redação abaixo (selecione só o que é aderente).
6. **Gerar duas versões** (mesmo conteúdo): humana (`curriculo.md` → `.html` → `.pdf`) e ATS-limpa
   (`curriculo-ats.docx`).
7. Atualizar `curriculos-gerados/README.md` e o rastreador `candidaturas.md`.

### Regras de redação (obrigatórias)
1. **Fatos acima de adjetivos.** Sem clichês (ver lista negra).
2. **Quantificar com contexto** (número + "onde"), nunca número solto.
3. **Nunca inventar.** Não declarar tecnologia/experiência sem evidência. Verifique no GitHub
   quando possível. Se faltar evidência de um requisito-core, **avise o usuário** (fit fraco) em vez
   de fabricar.
4. **1 página** por padrão para estágio/júnior.
5. **Bullets no formato XYZ:** verbo de ação + o que foi feito + tecnologia + resultado/evidência.
6. **Quebrar a simetria:** nunca dois bullets seguidos com a mesma abertura ou o mesmo tamanho;
   ao menos um detalhe concreto por função. (Evita "cara de IA".)
7. **Terço superior:** a conquista mais relevante para a vaga aparece no topo (resumo ou 1º bullet).
8. **Calibrar o tom pela senioridade:** estágio = aprendiz forte; júnior = autonomia parcial;
   pleno/sênior = decisões/arquitetura/mentoria. Não inflar.
9. **Espelhar a linguagem da vaga só onde a experiência real sustenta** (matchers semânticos punem
   keyword-stuffing). Usar a redação exata em skills quando for honesto.
10. **Controle de repetição:** não repetir a mesma prova de valor mais de ~2x.
11. **Habilidades em tiers** (Core / Web / Banco de dados / Ferramentas / Idiomas), não checklist
    gigante; diferencie domínio de familiaridade.
12. **Projetos como prova:** stack + resultado + link ao vivo (quando houver) + GitHub.
13. **Sem foto, sem dados sensíveis** (CPF/RG/idade/estado civil); apenas cidade + estado/país.
14. **Não anunciar a vaga dentro do currículo** (nada de selo "Vaga: X"). O alvo vai no nome do
    arquivo e na mensagem de candidatura.
15. **NUNCA usar o caractere travessão "—" (em dash)** no currículo nem nesta documentação.

### Lista negra (buzzwords e "AI tells")
Não usar: "proativo", "apaixonado por tecnologia", "comprometido com resultados", "vasta
experiência", "liderei iniciativas", "results-driven", "passionate team player", nem o uso-muleta de
"spearheaded/orchestrated/engineered". Evitar ritmo de frase uniforme.

### Idioma do currículo
Gerar **no idioma da vaga** (PT para vagas nacionais; EN para internacional/remoto-exterior ou
vagas em inglês). Em dúvida, perguntar.

---

## 🇺🇸 English

### Purpose
A personal data base to generate job-tailored resumes. It is not code: it is raw material (data,
experience, projects, skills) selected and adapted for each job.

### Workflow (each job becomes a subfolder `curriculos-gerados/<company>-<role>-YYYY-MM-DD/`)
1. The user sends a **job description**.
2. **Sync GitHub (if available):** if a GitHub MCP/integration exists, check for new/updated repos
   and refresh `projetos-github/` before building.
3. **Analyze the job (required):** save `vaga.md` with company, role, seniority, hard requirements,
   nice-to-haves, keywords (exact wording), language and risks.
4. **Scorecard (required):** save `scorecard.md` rating each requirement as
   **strong / medium / missing**, listing uncovered nice-to-haves and risks.
5. **Build the resume** following the Writing rules below (include only what fits).
6. **Generate two versions** (same content): human (`curriculo.md` → `.html` → `.pdf`) and ATS-clean
   (`curriculo-ats.docx`).
7. Update `curriculos-gerados/README.md` and the `candidaturas.md` tracker.

### Writing rules (mandatory)
1. **Facts over adjectives.** No clichés (see blacklist).
2. **Quantify with context** (number + "where"), never a bare number.
3. **Never fabricate.** Do not claim tech/experience without evidence. Verify on GitHub when
   possible. If a core requirement has no evidence, **tell the user** (weak fit) instead of inventing.
4. **One page** by default for intern/junior roles.
5. **XYZ bullets:** action verb + what you did + technology + result/evidence.
6. **Break the symmetry:** never two consecutive bullets with the same opening or length; at least
   one concrete detail per role. (Avoids the "AI look".)
7. **Top third:** the most relevant achievement appears at the top (summary or first bullet).
8. **Calibrate tone to seniority:** intern = strong learner; junior = partial autonomy;
   mid/senior = decisions/architecture/mentoring. Do not inflate.
9. **Mirror the job's wording only where real experience supports it** (semantic matchers punish
   keyword stuffing). Use exact wording in skills when honest.
10. **Repetition control:** do not repeat the same proof of value more than ~2x.
11. **Skills in tiers** (Core / Web / Databases / Tools / Languages), not a giant checklist;
    separate mastery from familiarity.
12. **Projects as proof:** stack + outcome + live link (if any) + GitHub.
13. **No photo, no sensitive data** (national IDs/age/marital status); city + state/country only.
14. **Do not announce the job inside the resume** (no "Applying for: X" badge). The target goes in
    the file name and the application message.
15. **NEVER use the em dash "—"** in the resume or in this documentation.

### Blacklist (buzzwords and "AI tells")
Avoid: "proactive", "passionate about technology", "results-driven", "extensive experience",
"led initiatives", "passionate team player", and crutch verbs like
"spearheaded/orchestrated/engineered". Avoid uniform sentence rhythm.

### Resume language
Generate **in the job's language** (PT for local roles; EN for international/remote-abroad or
English-language postings). When unsure, ask.

---

## 🔧 Tooling

- **PDF:** `python scripts/gerar_pdf.py <input.html> <output.pdf>` (auto-detects Chrome/Edge/Chromium).
- **DOCX (ATS):** edit content in `scripts/gerar_docx.py` and run it (`pip install python-docx`).
- Templates live in `templates/` (`curriculo.html`, `curriculo.md`, `vaga.md`, `scorecard.md`).
