# Reverse dictionary: Roman → (Tokigana, Toki Pona)
reverse_dict = {
    "no": ("の", "li"), "te": ("て", "e"), "ka": ("か", "mi"), "ta": ("た", "jan"),
    "to": ("と", "ni"), "ni": ("に", "la"), "i": ("い", "tawa"), "ha": ("は", "sina"),
    "wo": ("を", "ala"), "ru": ("る", "lon"), "shi": ("し", "pi"), "na": ("な", "ona"),
    "tsu": ("つ", "tenpo"), "re": ("れ", "mute"), "ra": ("ら", "pona"), "mo": ("も", "kama"),
    "su": ("す", "seme"), "u": ("う", "toki"), "ko": ("こ", "wile"), "ri": ("り", "o"),
    "ma": ("ま", "ken"), "sa": ("さ", "sona"), "ki": ("き", "tomo"), "ke": ("け", "tan"),
    "ku": ("く", "lukin"), "me": ("め", "pali"), "a": ("あ", "jo"), "nya": ("ん", "pilin"),
    "yo": ("よ", "lili"), "e": ("え", "pini"), "ya": ("や", "ma"), "nore": ("のれ", "ale"),
    "geri": ("けり", "ali"), "wa": ("わ", "ike"), "he": ("へ", "kepeken"), "chi": ("ち", "pana"),
    "se": ("せ", "telo"), "mi": ("み", "sama"), "ro": ("ろ", "ijo"), "o": ("お", "moku"),
    "ho": ("ほ", "suno"), "hi": ("ひ", "ilo"), "fu": ("ふ", "anu"), "mu": ("む", "suli"),
    "ne": ("ね", "lawa"), "yu": ("ゆ", "meli"), "nu": ("ぬ", "taso"), "deki": ("てき", "sewi"),
    "gayo": ("かよ", "mije"), "dare": ("たれ", "sitelen"), "doshi": ("とし", "musi"),
    "nishi": ("にし", "nasin"), "iwa": ("いわ", "wawa"), "pashi": ("はし", "sin"),
    "woki": ("をき", "kin"), "ruka": ("るか", "weka"), "jiwa": ("しわ", "wan"),
    "nate": ("なて", "ante"), "tsusa": ("つさ", "nasa"), "retsu": ("れつ", "tu"),
    "rawo": ("らを", "awen"), "mora": ("もら", "pakala"), "zuri": ("すり", "soweli"),
    "ue": ("うえ", "en"), "gofu": ("こふ", "lipu"), "rike": ("りけ", "sike"),
    "maka": ("まか", "poka"), "zani": ("さに", "mani"), "gima": ("きま", "mama"),
    "guhe": ("くへ", "lape"), "mema": ("めま", "kalama"), "ahe": ("あへ", "open"),
    "niri": ("にり", "olin"), "yore": ("よれ", "len"), "eko": ("えこ", "kon"),
    "yaka": ("やか", "luka"), "zoshi": ("そし", "kasi"), "wari": ("わり", "seli"),
    "pemi": ("へみ", "nimi"), "chisa": ("ちさ", "insa"), "zera": ("せら", "utala"),
    "miha": ("みは", "supa"), "roya": ("ろや", "pimeja"), "ori": ("おり", "moli"),
    "poro": ("ほろ", "sijelo"), "pite": ("ひて", "kute"), "pufu": ("ふふ", "kulupu"),
    "musu": ("むす", "esun"), "neki": ("ねき", "poki"), "yuha": ("ゆは", "anpa"),
    "nuha": ("ぬは", "nanpa"), "riyu": ("りゆ", "linja"), "noka": ("のか", "noka"),
    "uta": ("うた", "uta"), "shipi": ("しひ", "sinpin"), "suwo": ("すを", "suwi"),
    "kiwa": ("きわ", "kiwen"), "rete": ("れて", "lete"), "keshi": ("けし", "akesi"),
    "kure": ("くれ", "kule"), "rupa": ("るは", "lupa"), "moshi": ("もし", "monsi"),
    "kuri": ("くり", "a"), "sero": ("せろ", "selo"), "waro": ("わろ", "walo"),
    "kiri": ("きり", "kili"), "yaki": ("やき", "jaki"), "kona": ("こな", "ko"),
    "royu": ("ろゆ", "loje"), "waso": ("わそ", "waso"), "nena": ("ねな", "nena"),
    "bihi": ("ひひ", "pipi"), "ban": ("はん", "pan"), "mun": ("むん", "mun"),
    "risa": ("りさ", "palisa"), "rasa": ("らさ", "alasa"), "yaro": ("やろ", "jelo"),
    "kara": ("から", "kala"), "raso": ("らそ", "laso"), "momo": ("もも", "mu"),
    "hon": ("ほん", "pu")
}

def transliterate(roman_input):
    words = roman_input.split()
    kana_output = []
    toki_output = []

    for word in words:
        match = reverse_dict.get(word)
        if match:
            kana_output.append(match[0])
            toki_output.append(match[1])
        else:
            kana_output.append(word)
            toki_output.append(word)

    print("Tokigana: ", ' '.join(kana_output))
    print("Toki Pona:", ' '.join(toki_output))


if __name__ == "__main__":
    print("Enter Romanized Tokigana (e.g. `ka u ra`):")
    input_sentence = input("> ")
    transliterate(input_sentence)
