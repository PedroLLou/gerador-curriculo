# -*- coding: utf-8 -*-
"""
QA do currículo / Resume QA.

Varre um curriculo.md e alerta sobre sinais de texto fraco ou "cara de IA":
Scans a curriculo.md and flags weak or "AI-looking" text:
  - travessão "—" / em dash
  - buzzwords da lista negra / blacklisted buzzwords
  - bullets longos (> 25 palavras) / long bullets (> 25 words)
  - duas aberturas de bullet iguais seguidas / two consecutive bullets opening the same way
  - (opcional) palavras-chave da vaga ausentes / (optional) missing job keywords

Uso / Usage:
    python scripts/lint.py <curriculo.md> [vaga.md]

Sai com código 1 se encontrar problemas (útil para gate). / Exits 1 if issues are found.
"""
import re
import sys

BUZZWORDS = [
    # PT
    "proativo", "proativa", "apaixonado", "apaixonada", "apaixonado por tecnologia",
    "comprometido com resultados", "vasta experiência", "liderei iniciativas",
    "trabalho em equipe" if False else "jogador de equipe",  # evita falso positivo comum
    # EN
    "results-driven", "dynamic professional", "passionate team player", "passionate about",
    "team player", "go-getter", "synergy", "rockstar", "ninja",
    # crutch verbs
    "spearheaded", "orchestrated", "engineered",
]

EM_DASH = "—"  # —


def is_bullet(line):
    s = line.lstrip()
    return s.startswith("- ") or s.startswith("* ")


def bullet_text(line):
    return line.lstrip()[2:].strip()


def first_word(text):
    # remove markdown/negrito e pontuação inicial / strip markdown and leading punctuation
    t = re.sub(r"[*_`>#-]", "", text).strip()
    m = re.match(r"([A-Za-zÀ-ÿ]+)", t)
    return m.group(1).lower() if m else ""


def main():
    if len(sys.argv) < 2:
        print("Uso / Usage: python scripts/lint.py <curriculo.md> [vaga.md]")
        sys.exit(2)

    path = sys.argv[1]
    with open(path, encoding="utf-8") as f:
        lines = f.read().splitlines()

    issues = []
    bullets = []  # (line_no, text)

    for i, line in enumerate(lines, 1):
        if EM_DASH in line:
            issues.append(f"[{i}] travessao '—' encontrado / em dash found")
        low = line.lower()
        for bw in BUZZWORDS:
            if bw and bw in low:
                issues.append(f"[{i}] buzzword: \"{bw}\"")
        if is_bullet(line):
            bullets.append((i, bullet_text(line)))

    # bullets longos / long bullets
    for i, txt in bullets:
        wc = len(txt.split())
        if wc > 25:
            issues.append(f"[{i}] bullet longo / long bullet ({wc} palavras/words)")

    # aberturas repetidas em bullets consecutivos / repeated openings in consecutive bullets
    for (a_no, a_txt), (b_no, b_txt) in zip(bullets, bullets[1:]):
        fa, fb = first_word(a_txt), first_word(b_txt)
        if fa and fa == fb and (b_no - a_no) <= 2:
            issues.append(f"[{b_no}] abertura repetida / repeated opening: \"{fa}\"")

    # palavras-chave da vaga (opcional) / job keywords (optional)
    if len(sys.argv) >= 3:
        with open(sys.argv[2], encoding="utf-8") as f:
            vaga = f.read()
        kws = re.findall(r"`([^`]+)`", vaga)  # termos entre crases / backticked terms
        body = "\n".join(lines).lower()
        missing = [k for k in dict.fromkeys(kws) if k.lower() not in body]
        if missing:
            issues.append("palavras-chave da vaga ausentes / missing job keywords: "
                          + ", ".join(missing))

    print(f"== Lint: {path} ==")
    if not issues:
        print("OK: nenhum problema encontrado / no issues found.")
        sys.exit(0)
    for it in issues:
        print(" -", it)
    print(f"\n{len(issues)} alerta(s) / warning(s).")
    sys.exit(1)


if __name__ == "__main__":
    main()
