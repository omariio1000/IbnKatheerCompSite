import requests
from enum import Enum
import pandas as pd
import random
from collections import defaultdict


class CATEGORY(Enum):
    THIRTY = 0
    FIFTEEN1 = 1
    FIFTEEN2 = 2
    FIVE1 = 3
    FIVE2 = 4
    ONE = 5


# How many questions per contestant for each category
CATEGORY_QUESTIONS = {
    CATEGORY.ONE: 3,
    CATEGORY.FIVE1: 4,
    CATEGORY.FIVE2: 4,
    CATEGORY.FIFTEEN1: 5,
    CATEGORY.FIFTEEN2: 5,
    CATEGORY.THIRTY: 7,
}


def build_page_and_juz_map() -> dict:
    url = "https://api.alquran.cloud/v1/quran/quran-uthmani"
    r = requests.get(url, timeout=20)
    r.raise_for_status()
    data = r.json()["data"]["surahs"]

    page_map = {}
    for surah in data:
        for ayah in surah["ayahs"]:
            page_map[(surah["number"], ayah["numberInSurah"])] = (ayah["page"], ayah["juz"])

    return page_map


def get_page_and_juz(page_map, surah: int, ayah: int) -> tuple[int | None, int | None]:
    return page_map.get((surah, ayah), (None, None))


def read_contestants(file_path: str) -> dict:
    contestants = {}
    data = pd.read_excel(file_path, sheet_name="Sort by Alphabetical", header=0)
    for _, row in data.iterrows():
        name = row['Full Name']
        category = row['Category']
        session = row['Session']
        ID = row['ID']

        name = f"{ID}: {name}"

        category_list = []
        category_string_spliced = category.split(',')
        for category_str in category_string_spliced:
            category_str = category_str.removesuffix("Juz").strip()
            if category_str == "30":
                category_list.append(CATEGORY.THIRTY)
            elif category_str == "15":
                category_list.append(CATEGORY.FIFTEEN1)
                category_list.append(CATEGORY.FIFTEEN2)
            elif category_str == "5":
                category_list.append(CATEGORY.FIVE1)
                category_list.append(CATEGORY.FIVE2)
            elif category_str == "1":
                category_list.append(CATEGORY.ONE)
            else:
                raise ValueError(f"Unknown category: {category_str}")

        session_list = []
        session_string_spliced = session.split(',')
        for session_str in session_string_spliced:
            session_str = int(session_str.strip())
            session_list.append(session_str)

        contestants[name] = (category_list, session_list)

    return contestants


def read_questions(file_path: str, page_map: dict) -> dict:
    all_questions = {}
    data = []
    col_names = ['Question', 'Ayah Start']

    data.append(pd.read_excel(file_path, sheet_name="Juz 1-30", header=None, names=col_names))
    data.append(pd.read_excel(file_path, sheet_name="Juz 1-15", header=None, names=col_names))
    data.append(pd.read_excel(file_path, sheet_name="Juz 16-30", header=None, names=col_names))
    data.append(pd.read_excel(file_path, sheet_name="Juz 1-5", header=None, names=col_names))
    data.append(pd.read_excel(file_path, sheet_name="Juz 26-30", header=None, names=col_names))
    data.append(pd.read_excel(file_path, sheet_name="Juz 30", header=None, names=col_names))

    for i in range(len(data)):
        questions = []
        if data[i] is not None:
            for _, row in data[i].iterrows():
                question = row['Question']
                if pd.isna(question):
                    continue
                
                surah_and_ayah = question.split(':')
                surah = int(surah_and_ayah[0].split(' ')[-1].strip())
                ayah = int(surah_and_ayah[1].strip())

                page, juz = get_page_and_juz(page_map, surah, ayah)
                questions.append((f"{surah}:{ayah}", page, juz))

        all_questions[CATEGORY(i)] = questions

    return all_questions


def assign_questions(contestants: dict, all_questions: dict) -> dict:
    assignments = defaultdict(dict)

    grouped = defaultdict(list)

    for name, (categories, sessions) in contestants.items():
        cat_idx = 0
        sess_idx = 0

        while cat_idx < len(categories) and sess_idx < len(sessions):
            cat = categories[cat_idx]

            if cat == CATEGORY.FIVE1 and cat_idx + 1 < len(categories) and categories[cat_idx + 1] == CATEGORY.FIVE2:
                grouped[(CATEGORY.FIVE1, sessions[sess_idx])].append(name)
                grouped[(CATEGORY.FIVE2, sessions[sess_idx])].append(name)
                cat_idx += 2
                sess_idx += 1
            elif cat == CATEGORY.FIFTEEN1 and cat_idx + 1 < len(categories) and categories[cat_idx + 1] == CATEGORY.FIFTEEN2:
                grouped[(CATEGORY.FIFTEEN1, sessions[sess_idx])].append(name)
                grouped[(CATEGORY.FIFTEEN2, sessions[sess_idx])].append(name)
                cat_idx += 2
                sess_idx += 1
            else:
                grouped[(cat, sessions[sess_idx])].append(name)
                cat_idx += 1
                sess_idx += 1

    for (cat, sess), names in grouped.items():
        names = sorted(names)
        questions_pool = all_questions[cat][:]
        random.shuffle(questions_pool)

        needed_per_person = CATEGORY_QUESTIONS[cat]
        total_needed = len(names) * needed_per_person

        if total_needed > len(questions_pool):
            for name in names:
                assignments[name][cat] = (sess, [])
            continue

        idx = 0
        for name in names:
            selected = []
            used_juz = set()

            for q in questions_pool[idx:]:
                surah, ayah = q[0].split(":")
                _, _, juz = q
                if cat != CATEGORY.ONE and juz not in used_juz:
                    selected.append(q)
                    used_juz.add(juz)
                if len(selected) == needed_per_person:
                    break

            if len(selected) < needed_per_person:
                for q in questions_pool[idx:]:
                    if q not in selected:
                        selected.append(q)
                    if len(selected) == needed_per_person:
                        break

            assignments[name][cat] = (sess, selected)
            questions_pool = [q for q in questions_pool if q not in selected]

    return dict(sorted(assignments.items()))


def write_assignments(assignments: dict, filename: str) -> None:
    with open(filename, "w", encoding="utf-8") as f:
        merged_categories = [
            CATEGORY.THIRTY,
            CATEGORY.FIFTEEN1,
            CATEGORY.FIVE1,
            CATEGORY.ONE,
        ]

        for cat in merged_categories:
            if cat in (CATEGORY.FIVE1, CATEGORY.FIVE2):
                title = "FIVE"
            elif cat in (CATEGORY.FIFTEEN1, CATEGORY.FIFTEEN2):
                title = "FIFTEEN"
            else:
                title = cat.name

            f.write(f"=== {title} ===\n\n")

            contestants = [
                (name, data) for name, data in assignments.items()
                if any(c in data for c in (
                    [cat, cat] if cat in (CATEGORY.ONE, CATEGORY.THIRTY)
                    else [CATEGORY.FIVE1, CATEGORY.FIVE2] if "FIVE" in title
                    else [CATEGORY.FIFTEEN1, CATEGORY.FIFTEEN2]
                ))
            ]
            contestants.sort(key=lambda x: x[0])

            for name, data in contestants:
                if title == "FIVE":
                    sess, q1 = data.get(CATEGORY.FIVE1, (None, []))
                    _, q2 = data.get(CATEGORY.FIVE2, (None, []))
                elif title == "FIFTEEN":
                    sess, q1 = data.get(CATEGORY.FIFTEEN1, (None, []))
                    _, q2 = data.get(CATEGORY.FIFTEEN2, (None, []))
                else:
                    sess, q1 = data.get(cat, (None, []))
                    q2 = []

                f.write(f"{name} (Session {sess}):\n")

                if title in ("FIVE", "FIFTEEN"):
                    if title in "FIVE":
                        f.write("  OPTION 1 (Juz 1 - Juz 5):\n")
                    else:
                        f.write("  OPTION 1 (Juz 1 - Juz 15):\n")
                    for surah_ayah, page, juz in q1:
                        surah = surah_ayah.split(":")[0]
                        ayah = surah_ayah.split(":")[1]
                        f.write(f"      {surah_ayah} (Page {page}, Juz {juz})\n")
                        f.write(f"        https://quran.com/{surah}?startingVerse={ayah}\n")
                    if title in "FIVE":
                        f.write("  OPTION 2 (Juz 26 - Juz 30):\n")
                    else:
                        f.write("  OPTION 2 (Juz 16 - Juz 30):\n")
                    for surah_ayah, page, juz in q2:
                        surah = surah_ayah.split(":")[0]
                        ayah = surah_ayah.split(":")[1]
                        f.write(f"      {surah_ayah} (Page {page}, Juz {juz})\n")
                        f.write(f"        https://quran.com/{surah}?startingVerse={ayah}\n")
                else:
                    for surah_ayah, page, juz in q1:
                        surah = surah_ayah.split(":")[0]
                        ayah = surah_ayah.split(":")[1]
                        f.write(f"  {surah_ayah} (Page {page}, Juz {juz})\n")
                        f.write(f"    https://quran.com/{surah}?startingVerse={ayah}\n")

                f.write("\n")

            f.write("\n")


def main():
    contestants = read_contestants("C:\\Users\\omari\\Downloads\\Ibn Katheer Quran Competition - Sessions 2025.xlsx")
    page_map = build_page_and_juz_map()
    questions = read_questions("C:\\Users\\omari\\Downloads\\question bank - ibn kathir comp.xlsx", page_map)

    assignments = assign_questions(contestants, questions)

    out_path = "C:\\Users\\omari\\Downloads\\assignments.txt"
    write_assignments(assignments, out_path)
    
    print(f"✅ Assignments written to {out_path}")


if __name__ == "__main__":
    main()
