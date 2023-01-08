import pyttsx3


def split_by_sentence(text):
    text_by_sentence = text.split(".")
    text_by_sentence[0] = text_by_sentence[0] + "."
    cumulative_text = [text_by_sentence[0]]
    for t in range(1, len(text_by_sentence)):
        text_by_sentence[t] = text_by_sentence[t] + "."
        cumulative_text.append(cumulative_text[t - 1] + text_by_sentence[t])
    for text in text_by_sentence:
        print(text)
    return [text_by_sentence, cumulative_text]


def transform_text_to_speech(text, number):
    print(str(number) + ": " + text)
    converter = pyttsx3.init()
    converter.save_to_file(text, "audio" + number + ".mp3")
    converter.runAndWait()
    print("audio" + number + ".mp3 is converted")
