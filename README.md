# The-Pile-EuroParl

Download, parse, and filter the [European Parliament Proceedings](http://www.statmt.org/europarl/), data-ready for [The-Pile](https://github.com/EleutherAI/The-Pile).

[**Stat Sheet**](docs/EuroParliamentProceedings_1996_2011.jsonl.md)

The Europarl parallel corpus is extracted from the proceedings of the European Parliament. It includes versions in 21 European languages: Romanic (French, Italian, Spanish, Portuguese, Romanian), Germanic (English, Dutch, German, Danish, Swedish), Slavik (Bulgarian, Czech, Polish, Slovak, Slovene), Finni-Ugric (Finnish, Hungarian, Estonian), Baltic (Latvian, Lithuanian), and Greek.

To use this parser, first download the source file

http://www.statmt.org/europarl/v7/europarl.tgz

and unpack it to the directory. The parser will look for all file within the `txt` subdirectory. Note that the download is slow and make take 12 or more hours.

The parser removes all basic tag information and only retains the name. The tag

    <SPEAKER ID=77 LANGUAGE="NL" NAME="Pronk">

Is reduced to

    Pronk

Extremely short files (<200 chracters) are removed as they did not contain useful language modeling text. A single file `txt/pl/ep-09-10-22-009.txt` fails to open with UTF-8 encoding and is skipped. No other filtering was done. 

Data souce temporary hosted at https://drive.google.com/file/d/12Q23Y7IKQyjF28xH0Aw6yZaYEx2YIOiB/view?usp=sharing