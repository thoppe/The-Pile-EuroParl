# The-Pile-EuroParl

Download, parse, and filter the [European Parliament Proceedings](http://www.statmt.org/europarl/), data-ready for [The-Pile](https://github.com/EleutherAI/The-Pile).

The Europarl parallel corpus is extracted from the proceedings of the European Parliament. It includes versions in 21 European languages: Romanic (French, Italian, Spanish, Portuguese, Romanian), Germanic (English, Dutch, German, Danish, Swedish), Slavik (Bulgarian, Czech, Polish, Slovak, Slovene), Finni-Ugric (Finnish, Hungarian, Estonian), Baltic (Latvian, Lithuanian), and Greek.

To use this parser, first download the source file

http://www.statmt.org/europarl/v7/europarl.tgz

and unpack it to the directory. The parser will look for all file within the `txt` subdirectory. Note that the download is slow and make take 12 or more hours.

The parser removes all basic tag information and only retains the name. The tag

    <SPEAKER ID=77 LANGUAGE="NL" NAME="Pronk">

Is reduced to

    Pronk

Extremely short files (<200 chracters) are removed as they did not contain useful language modeling text. A single file `txt/pl/ep-09-10-22-009.txt` fails to open with UTF-8 encoding and is skipped. No other filtering was done. 

     ✔ Saved to EuroParliamentProceedings_1996_2011.jsonl
     ℹ Saved 187,072 articles
     ℹ Uncompressed filesize   4,941,430,389
     ℹ Compressed filesize     1,475,803,930

Data souce temporary hosted at https://drive.google.com/file/d/15kQ6jAGHsI3ZrA0ibXGuTmzGdib9NA63/view?usp=sharing

     > sha256sum EuroParliamentProceedings
    dfc7cd52beba0eb03cbc0498993983f9a5d03da017bcc8f74257be942bf41877  EuroParliamentProceedings_1996_2011.jsonl.zst