import json
import requests

# Load translations
with open("translations.json", "r", encoding="utf-8") as f:
    translations = json.load(f)

LANGUAGES = translations["LANGUAGES"]
UI_TEXT = translations["UI_TEXT"]

def get_weather(city, lang_code="en"):
    url = f"https://wttr.in/{city}?format=j1&lang={lang_code}"
    try:
        response = requests.get(url)
        data = response.json()
        current = data['current_condition'][0]
        temp_c = current['temp_C']
        temp_f = current['temp_F']
        desc = current['weatherDesc'][0]['value']
        return f"Weather in {city}: {temp_c}°C / {temp_f}°F, {desc}"
    except Exception as e:
        return f"Could not get weather data: {e}"

def choose_language():
    print(UI_TEXT["choose_language"]["en"])  # Show language menu header in English
    for i, lang in enumerate(LANGUAGES.keys(), 1):
        print(f"{i}. {lang.capitalize()}")

    while True:
        choice = input("Enter the number for your preferred language: ").strip()
        if choice.isdigit():
            idx = int(choice)
            if 1 <= idx <= len(LANGUAGES):
                lang = list(LANGUAGES.keys())[idx - 1]
                return LANGUAGES[lang]
        print("Invalid choice. Please try again.")

def main():
    lang_code = choose_language()
    name = input(UI_TEXT["name_prompt"].get(lang_code, UI_TEXT["name_prompt"]["en"])).strip()

    welcome_msg = UI_TEXT["welcome"].get(lang_code, UI_TEXT["welcome"]["en"])
    print(f"{welcome_msg} {name}!")

    while True:
        city = input(UI_TEXT["enter_city"].get(lang_code, UI_TEXT["enter_city"]["en"])).strip()
        print(get_weather(city, lang_code))

        print(UI_TEXT["choose_action"].get(lang_code, UI_TEXT["choose_action"]["en"]))
        print(UI_TEXT["option_1"].get(lang_code, UI_TEXT["option_1"]["en"]))
        print(UI_TEXT["option_2"].get(lang_code, UI_TEXT["option_2"]["en"]))

        choice = input().strip()
        if choice == '2':
            goodbye_msg = UI_TEXT["goodbye"].get(lang_code, UI_TEXT["goodbye"]["en"])
            # Insert name before the exclamation mark, assuming message ends with "!"
            if goodbye_msg.endswith("!"):
                goodbye_msg = goodbye_msg[:-1] + f" {name}!"
            else:
                goodbye_msg += f" {name}!"
            print(goodbye_msg)
            break
        elif choice != '1':
            print(UI_TEXT["invalid_choice"].get(lang_code, UI_TEXT["invalid_choice"]["en"]))
            break

if __name__ == "__main__":
    main()