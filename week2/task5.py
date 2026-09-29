if __name__ == '__main__':
    events = {
        "DIY Noise-Music Workshop": "2026-09-19 16:00",
        "Dortmunder Kunstverein Guided Tour 1": "2026-09-19 16:00",
        "New Silk Roads Exhibition & Bag Printing": "2026-09-19 16:00",
        "Speed Camera Photo Experience": "2026-09-19 16:00",
        "Chamber of Skilled Crafts Workshop Tours": "2026-09-19 16:00",
        "Voice Experimentation & Beatboxing": "2026-09-19 16:00",
        "3D Facade Mapping at Dortmunder U": "2026-09-19 16:00",
        "Dortmunder Kunstverein Guided Tour 2": "2026-09-19 18:00",
        "Dortmunder Kunstverein Guided Tour 3": "2026-09-19 20:00",
        "Marquess Latin-Pop Open-Air Concert": "2026-09-19 22:15",
        "Grand Finale Musical Fireworks Display": "2026-09-19 23:45"
    }
    print("\nDictionary of events in Dortmund during the Night of Museums in 2026:\n")
    for i, (k, v) in enumerate(events.items(), start=1):
        sv = v.split(" ")
        print(f"{i}) {k}\nDate: {sv[0]}\nStart time: {sv[1]}\n")