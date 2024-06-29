# Задание 1. Есть некоторый текст.
# Реализуйте следующую функциональность:
# Изменить текст таким образом, чтобы каждое предложение начиналось с большой буквы;
# Посчитайте сколько раз цифры встречаются в тексте;
# Посчитайте сколько раз знаки препинания встречаются в тексте;
# Посчитайте количество восклицательных знаков в тексте.

def count_digits(text):
    return text.count("0") + text.count("1") + text.count("2") + text.count("3") + text.count("4") + text.count("5") + text.count("6") + text.count("7") + text.count("8") + text.count("9")


def count_ex(text):
    return text.count("!")


# В современной русской пунктуации десять знаков препинания:
# точка,
# вопросительный знак,
# восклицательный знак,
# запятая,
# многоточие,
# точка с запятой,
# двоеточие,
# тире,
# скобки,
# кавычки.
def count_signs(text):
    mult = text.count("...")
    return text.count(".") - 3 * mult + mult + text.count(chr(8212)) + text.count(";") + text.count("!") + text.count(",") + text.count("?") + text.count(":") + text.count(chr(151)) + text.count("(") + text.count(")") + text.count("\"")


def text_by_sents_with_upper(text):
    sents = list()
    length = len(text)
    if length == 0:
        return 0
    i = 0
    order = 0
    sent = ""
    while i < length:
        if text[i] in ".!?":
            if i == 0:
                i += 1
                sent += text[i]
                continue
            sent += text[i]
            order += 1
            if i == length - 1:
                sents.append(sent)
                sent = ""
            i += 1
            continue
        if order != 0:
            order = 0
            sents.append(sent)
            sent = text[i]
            i += 1
            continue
        sent += text[i]
        i += 1
    temp = ""
    for sent in sents:
        i = 0
        while i < len(sent):
            if sent[i] >= "a" and sent[i] <= "z" or sent[i] >= "A" and sent[i] <= "Z" or sent[i] >= "а" and sent[i] <= "я" or sent[i] >= "А" and sent[i] <= "Я" or sent[i] == "ё" or sent[i] == "Ё":
                sent = sent.replace(sent[i], sent[i].upper(), 1)
                break
            i +=  1
        temp += sent
    return temp


text_news = "как я уже говорил, — это не мое дело.мероприятие пройдет в столице 18 мая...\n\t\t\tкомпания VK организует для гостей и участников ряд активностей. какой восторг!!! так, в диджитал-зоне VK можно совершить заезд на велосимуляторе, узнать максимальную скорость и выиграть призы, подготовиться к заезду и отдохнуть после него в лаунж-пространстве, а также сделать фото и получить их по предварительной регистрации в мини-приложении велофестиваля. детям всё бесплатно?!! "

print(text_news)
print(text_by_sents_with_upper(text_news))
print(f"Количество цифр: {count_digits(text_news)}.")
print(f"Количество знаков препинания: {count_signs(text_news)}.")
print(f"Количество восклицательных знаков: {count_ex(text_news)}.")
