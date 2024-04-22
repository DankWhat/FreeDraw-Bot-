import json

SETTINGS_FILE = "settings.json"

def load_settings():
    try:
        with open(SETTINGS_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("Settings file not found. Using default settings.")
        return {
            "start_delay": 5,
            "draw_speed": 0.08,
            "x_offset": 15,
            "y_offset": 15,
            "progress_bar_style": 1
        }

def save_settings(settings):
    with open(SETTINGS_FILE, "w") as file:
        json.dump(settings, file, indent=4)
        print("Settings saved successfully.")

def change_settings():
    settings = load_settings()

    print("Current settings:")
    print(settings)

    print("Enter new settings:")
    settings["start_delay"] = int(input("Start Delay: "))
    settings["draw_speed"] = float(input("Drawing Speed: "))
    settings["x_offset"] = int(input("X Offset: "))
    settings["y_offset"] = int(input("Y Offset: "))
    settings["progress_bar_style"] = int(input("Progress Bar Style (1 or 2): "))

    save_settings(settings)

def get_setting(setting_name):
    settings = load_settings()
    return settings.get(setting_name)
