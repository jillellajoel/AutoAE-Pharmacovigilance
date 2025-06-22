import spacy
import pandas as pd

nlp = spacy.load("en_core_web_sm")

DRUG_KEYWORDS = ["paracetamol", "ibuprofen", "aspirin", "ranitidine", "metformin"]
AE_KEYWORDS = ["nausea", "vomiting", "rash", "cancer", "headache", "hepatotoxicity", "renal failure"]
SERIOUSNESS_KEYWORDS = ["hospitalized", "death", "disability", "life-threatening"]

def extract_ae_data(text):
    doc = nlp(text)
    records = []

    for sent in doc.sents:
        sentence = sent.text.lower()
        found_drugs = [drug for drug in DRUG_KEYWORDS if drug in sentence]
        found_ae = [ae for ae in AE_KEYWORDS if ae in sentence]
        seriousness = [s for s in SERIOUSNESS_KEYWORDS if s in sentence]

        for drug in found_drugs:
            for ae in found_ae:
                records.append({
                    "Drug": drug,
                    "Adverse Event": ae,
                    "Seriousness": ", ".join(seriousness) if seriousness else "Not serious",
                    "Sentence": sent.text.strip()
                })

    return pd.DataFrame(records)
