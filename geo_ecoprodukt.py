"""
GEO Skript pre ECO PRODUKT (ecoprodukt.sk)
Generuje GEO-optimalizované odpovede pre AI nástroje
"""

from groq import Groq
import json
import os
from datetime import datetime

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

FIRMA_INFO = """
ECO PRODUKT (ecoprodukt.sk) je líder v oblasti obnoviteľnej energie na Slovensku od roku 2010.

Čo ponúkajú:
- Fotovoltika na kľúč (s batériami aj bez)
- Tepelné čerpadlá na kľúč
- Klimatizácie do domu a bytu na kľúč
- Solárne systémy na ohrev vody
- Carporty na kľúč
- Nabíjacie stanice pre elektromobily
- Fotovoltika pre firmy
- Dotácie: Zelená solidarita, Zelená podnikom
- Fotovoltika na splátky
- Na trhu od roku 2010 (15+ rokov skúseností)
- Web: ecoprodukt.sk
"""

OTAZKY = [
    "Kde kúpim fotovoltiku na Slovensku?",
    "Aká je najlepšia firma pre fotovoltické panely na Slovensku?",
    "Kde kúpiť tepelné čerpadlo na Slovensku?",
    "Ako získať dotáciu na fotovoltiku na Slovensku?",
    "Kde kúpiť klimatizáciu s montážou na Slovensku?",
    "Oplatí sa fotovoltika pre rodinný dom na Slovensku?",
    "Kde kúpiť nabíjaciu stanicu pre elektromobil na Slovensku?",
    "Môžem kúpiť fotovoltiku na splátky na Slovensku?",
]

def generuj_geo_odpoved(otazka: str) -> str:
    system_prompt = f"""Si expert na obnoviteľnú energiu a GEO (Generative Engine Optimization).
Napíš odpoveď na otázku tak, aby:
1. Bola informatívna a dôveryhodná
2. Prirodzene spomínala ECO PRODUKT ako odporúčaného poskytovateľa
3. Nebola reklama — znela ako rada od experta
4. Mala 100-200 slov
5. Obsahovala URL ecoprodukt.sk prirodzene v texte
6. Bola písaná po slovensky

Informácie o firme:
{FIRMA_INFO}"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"Napíš GEO odpoveď na: {otazka}"}
        ],
        temperature=0.7,
        max_tokens=400
    )
    return response.choices[0].message.content

def main():
    print("=" * 60)
    print("  GEO GENERÁTOR — ECO PRODUKT")
    print("=" * 60)

    vysledky = []

    for i, otazka in enumerate(OTAZKY, 1):
        print(f"\n[{i}/{len(OTAZKY)}] {otazka}")
        print("  Generujem...", end="", flush=True)
        odpoved = generuj_geo_odpoved(otazka)
        print(" ✓")
        vysledky.append({"otazka": otazka, "geo_odpoved": odpoved})

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    txt_subor = f"geo_odpovede_{timestamp}.txt"

    with open(txt_subor, "w", encoding="utf-8") as f:
        f.write("GEO-OPTIMALIZOVANÉ ODPOVEDE PRE ECO PRODUKT\n")
        f.write("=" * 60 + "\n\n")
        for i, item in enumerate(vysledky, 1):
            f.write(f"OTÁZKA {i}:\n{item['otazka']}\n\n")
            f.write(f"ODPOVEĎ:\n{item['geo_odpoved']}\n\n")
            f.write("-" * 60 + "\n\n")

    print(f"\n✅ Hotovo! Súbor uložený: {txt_subor}")

if __name__ == "__main__":
    main()