import requests
from enum import Enum
import pandas as pd
import time

class CATEGORY(Enum):
    THIRTY = 1
    FIFTEEN1 = 2
    FIFTEEN2 = 3
    FIVE1 = 4
    FIVE2 = 5
    ONE = 6

def get_page_number(surah: int, ayah: int) -> int | None:
    """
    Return the mushaf page number for a given surah & ayah using a public API.
    If the API is unavailable or the request fails, return None.
    """
    try:
        r = requests.get(
            f"https://api.alquran.cloud/v1/ayah/{surah}:{ayah}",
            timeout=10,
        )
        r.raise_for_status()
        page = r.json()["data"]["page"]
        time.sleep(0.5)
        return page
    except Exception:
        return None
    
def read_contestants(file_path: str) -> dict:
    contestants = {}
    data = pd.read_excel(file_path, sheet_name="Sort by Alphabetical",header=0)
    for _, row in data.iterrows():
        name = row['Full Name']
        category = row['Category']
        session = row['Session']

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

def read_questions(file_path: str) -> dict:
    all_questions = {}
    data = []
    col_names = ['Question', 'Ayah Start']

    data.append(pd.read_excel(file_path, sheet_name="Juz 1-30",header=None, names=col_names))
    data.append(pd.read_excel(file_path, sheet_name="Juz 1-15",header=None, names=col_names))
    data.append(pd.read_excel(file_path, sheet_name="Juz 16-30",header=None, names=col_names))
    # data.append(pd.read_excel(file_path, sheet_name="Juz 1-5",header=None, names=col_names))
    data.append(pd.read_excel(file_path, sheet_name="Juz 26-30",header=None, names=col_names))
    # data.append(pd.read_excel(file_path, sheet_name="Juz 30",header=None, names=col_names))

    for i in range(len(data)):
        questions = []
        for _, row in data[i].iterrows():
            question = row['Question']
            ayah_start = row['Ayah Start']
            if pd.isna(question) or pd.isna(ayah_start):
                continue
            
            surah_and_ayah = question.split(' ')[1].split(':')
            print(surah_and_ayah)
            surah = int(surah_and_ayah[0])
            ayah = int(surah_and_ayah[1])

            page = get_page_number(surah, ayah)

            questions.append((question, ayah_start, page))
        all_questions[i] = questions
    
    return all_questions

def main():
    contestants = read_contestants("C:\\Users\\omari\\Downloads\\Ibn Katheer Quran Competition - Sessions 2025.xlsx")
    for contestant in contestants:
        print(contestant, contestants[contestant])

    questions = read_questions("C:\\Users\\omari\\Downloads\\question bank - ibn kathir comp.xlsx")
    for question in questions:
        print(questions, questions[question])

if __name__ == "__main__":
    main()