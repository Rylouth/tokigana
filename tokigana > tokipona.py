import re

# Original dictionary: toki pona -> (tokigana, roman)
original_dict = {
    "li": ("の", "no"), "e": ("て", "te"), "mi": ("か", "ka"), "jan": ("た", "ta"),
    "ni": ("と", "to"), "la": ("に", "ni"), "tawa": ("い", "i"), "sina": ("は", "ha"),
    "ala": ("を", "wo"), "lon": ("る", "ru"), "pi": ("し", "shi"), "ona": ("な", "na"),
    "tenpo": ("つ", "tsu"), "mute": ("れ", "re"), "pona": ("ら", "ra"), "kama": ("も", "mo"),
    "seme": ("す", "su"), "toki": ("う", "u"), "wile": ("こ", "ko"), "o": ("り", "ri"),
    "ken": ("ま", "ma"), "sona": ("さ", "sa"), "tomo": ("き", "ki"), "tan": ("け", "ke"),
    "lukin": ("く", "ku"), "pali": ("め", "me"), "jo": ("あ", "a"), "pilin": ("ん", "nya"),
    "lili": ("よ", "yo"), "pini": ("え", "e"), "ma": ("や", "ya"), "ale": ("のれ", "nore"),
    "ali": ("けり", "geri"), "ike": ("わ", "wa"), "kepeken": ("へ", "he"), "pana": ("ち", "chi"),
    "telo": ("せ", "se"), "sama": ("み", "mi"), "ijo": ("ろ", "ro"), "moku": ("お", "o"),
    "suno": ("ほ", "ho"), "ilo": ("ひ", "hi"), "anu": ("ふ", "fu"), "suli": ("む", "mu"),
    "lawa": ("ね", "ne"), "meli": ("ゆ", "yu"), "taso": ("ぬ", "nu"), "sewi": ("てき", "deki"),
    "mije": ("かよ", "gayo"), "sitelen": ("たれ", "dare"), "musi": ("とし", "doshi"),
    "nasin": ("にし", "nishi"), "wawa": ("いわ", "iwa"), "sin": ("はし", "pashi"),
    "kin": ("をき", "woki"), "weka": ("るか", "ruka"), "wan": ("しわ", "jiwa"),
    "ante": ("なて", "nate"), "nasa": ("つさ", "tsusa"), "tu": ("れつ", "retsu"),
    "awen": ("らを", "rawo"), "pakala": ("もら", "mora"), "soweli": ("すり", "zuri"),
    "en": ("うえ", "ue"), "lipu": ("こふ", "gofu"), "sike": ("りけ", "rike"),
    "poka": ("まか", "maka"), "mani": ("さに", "zani"), "mama": ("きま", "gima"),
    "lape": ("くへ", "guhe"), "kalama": ("めま", "mema"), "open": ("あへ", "ahe"),
    "olin": ("にり", "niri"), "len": ("よれ", "yore"), "kon": ("えこ", "eko"),
    "luka": ("やか", "yaka"), "kasi": ("そし", "zoshi"), "seli": ("わり", "wari"),
    "nimi": ("へみ", "pemi"), "insa": ("ちさ", "chisa"), "utala": ("せら", "zera"),
    "supa": ("みは", "miha"), "pimeja": ("ろや", "roya"), "moli": ("おり", "ori"),
    "sijelo": ("ほろ", "poro"), "kute": ("ひて", "pite"), "kulupu": ("ふふ", "pufu"),
    "esun": ("むす", "musu"), "poki": ("ねき", "neki"), "anpa": ("ゆは", "yuha"),
    "nanpa": ("ぬは", "nuha"), "linja": ("りゆ", "riyu"), "noka": ("のか", "noka"),
    "uta": ("うた", "uta"), "sinpin": ("しひ", "shipi"), "suwi": ("すを", "suwo"),
    "kiwen": ("きわ", "kiwa"), "lete": ("れて", "rete"), "akesi": ("けし", "keshi"),
    "kule": ("くれ", "kure"), "lupa": ("るは", "rupa"), "monsi": ("もし", "moshi"),
    "a": ("くり", "kuri"), "selo": ("せろ", "sero"), "walo": ("わろ", "waro"),
    "kili": ("きり", "kiri"), "jaki": ("やき", "yaki"), "ko": ("こな", "kona"),
    "loje": ("ろゆ", "royu"), "waso": ("わそ", "waso"), "nena": ("ねな", "nena"),
    "pipi": ("ひひ", "bihi"), "pan": ("はん", "ban"), "mun": ("むん", "mun"),
    "palisa": ("りさ", "risa"), "alasa": ("らさ", "rasa"), "jelo": ("やろ", "yaro"),
    "kala": ("から", "kara"), "laso": ("らそ", "raso"), "unpa": ("ぬは", "nuha"),
    "mu": ("もも", "momo"), "pu": ("ほん", "hon")
}

# Reverse map: tokigana -> tokipona
tokigana_to_toki = {kana: toki for toki, (kana, _) in original_dict.items()}

def transliterate_back(tokigana_sentence):
    words = tokigana_sentence.split()
    toki_words = []

    for word in words:
        match = re.match(r"([^\W_]+)(\W*)", word)
        if match:
            base = match.group(1)
            punct = match.group(2)

            toki = tokigana_to_toki.get(base, base)
            toki_words.append(toki + punct)
        else:
            toki_words.append(word)

    print("Toki Pona: ", ' '.join(toki_words))


if __name__ == "__main__":
    print("Enter a Tokigana sentence:")
    input_sentence = input("> ")
    transliterate_back(input_sentence)
