from itertools import permutations

prefixdict = {"punc": "insi",
              "cc": "crita",
              "cd": "acri",
              "elec": "vexi",
              "heat": "igni",
              "fr": "croni",
              "cold": "geli",
              "imp": "magna",
              "sd": "deci",
              "slash": "sci",
              "sc": "hexa",
              "tox": "toxi",
              "ammo": "ampi",
              "mag": "arma",
              "dmg": "visi",
              "ms": "sati",
              "pfs": "conci",
              "pt": "lexi",
              "rec": "zeti",
              "rs": "feva",
              "corp": "manti",
              "grin": "argi",
              "inf": "pura",
              "zoom": "hera",
              "range": "locti",
              "ic": "para",
              "eff": "forti"}

sufixdict = {"punc": "cak",
             "cc": "cron",
             "cd": "tis",
             "elec": "tio",
             "heat": "pha",
             "fr": "dra",
             "cold": "do",
             "imp": "ton",
             "sd": "des",
             "slash": "sus",
             "sc": "dex",
             "tox": "tox",
             "ammo": "bin",
             "mag": "tin",
             "dmg": "ata",
             "ms": "can",
             "pfs": "nak",
             "pt": "nok",
             "rec": "mag",
             "rs": "tak",
             "corp": "tron",
             "grin": "con",
             "inf": "ada",
             "zoom": "lis",
             "range": "tor",
             "ic": "um",
             "eff": "us"}

def get_riven_name(stat1,stat2,stat3):
    return f"{str(prefixdict.get(stat1)).capitalize()}-{prefixdict.get(stat2)}{sufixdict.get(stat3)}"

if __name__ == "__main__":
	string = ""

	with open("input.txt", 'r') as f:
		stats = [i.replace("\n", "").split() for i in f.readlines()]

	for i in stats:
		combinations = [' '.join(f) for f in permutations(i, 3)]
		for v in combinations:
			stat1 = v.split(' ')[0]
			stat2 = v.split(' ')[1]
			stat3 = v.split(' ')[2]
			string += get_riven_name(stat1, stat2, stat3)+"\n"

	zalupa = string.split("\n")
	string = ""
	for i in sorted(zalupa):
		string += i+"\n"
	
	with open("output.txt", 'w+') as f:
		f.write(string[1:])