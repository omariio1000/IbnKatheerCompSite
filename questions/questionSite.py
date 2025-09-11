import requests
import webbrowser

def quran_links(surah: int, ayah: int, locale: str = "en"):
    """
    Return (chapter_link, reading_link) for a given surah & ayah.

    chapter_link -> Quran.com chapter URL positioned at the ayah (Translation tab by default)
    reading_link -> Quran.com mushaf page URL (Reading-style layout)
    """
    # 1) Chapter link with the verse positioned (still opens in Translation view)
    chapter_link = f"https://quran.com/{surah}?startingVerse={ayah}"

    # 2) Reading-style link: look up the mushaf page number via a public API
    try:
        r = requests.get(
            f"https://api.alquran.cloud/v1/ayah/{surah}:{ayah}",
            timeout=10,
        )
        r.raise_for_status()
        page = r.json()["data"]["page"]
        reading_link = f"https://quran.com/{locale}/page/{page}"
    except Exception:
        # Fallback: if the API is unavailable, return None for the reading link
        reading_link = None

    return chapter_link, reading_link

if __name__ == "__main__":
    s, a = 4, 82
    chapter, reading = quran_links(s, a)
    print("Chapter (positions verse):", chapter)
    print("Reading-style (mushaf page):", reading or "(unavailable)")

    # Optional: open the reading-style link directly
    if reading:
        webbrowser.open(reading)