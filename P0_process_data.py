from pathlib import Path
from dspipe import Pipe
import bs4
import jsonlines

f_save = "EuroParliamentProceedings_1996_2011.jsonl"


def process_tag(original_tag):
    tag = original_tag.strip(">").strip("<")

    # Skip empty tags
    if not tag:
        return None

    tagname = tag.split()[0]

    # Skip paragraph, break, and chapter tags
    if tagname in ["P", "BRK", "CHAPTER", "/P"]:
        return None

    # For speaker tags, return the name
    if tagname == "SPEAKER":
        soup = bs4.BeautifulSoup(original_tag, "html.parser")
        name = soup.speaker["name"]
        return name

    # Raise a error here if there is a tag we don't know
    raise ValueError(f"Unknown tag {tag}")


def compute(f0):

    language = str(f0.parent).split("/")[-1]

    try:
        with open(f0, encoding="utf-8") as FIN:
            text = FIN.read()
    except:
        print(f"Failed to open {f0}")
        return None

    # Skip short sections (no usable text)
    if len(text) < 200:
        return None

    parsed_text = []

    for line in text.split("\n"):
        if line and line[0] == "<" and line[-1] == ">":
            line = process_tag(line)

            # Skip lines that we want to filter
            if line is None:
                continue

        parsed_text.append(line)

    text = "\n".join(parsed_text)

    data = {"text": text, "meta": {"language": language}}

    return data


source = Path("txt").glob("**/*.txt")
P = Pipe(source, prefilter=False)(compute, -1)

with jsonlines.open(f_save, "w") as FOUT:
    for row in P:
        if row is not None:
            FOUT.write(row)
