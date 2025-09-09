# questionSite.py
from playwright.sync_api import sync_playwright
import sys

def open_in_reading_view(surah: int, ayah: int, locale: str = "en"):
    base_url = f"https://quran.com/1/1"
    verse_url = f"https://quran.com/{surah}?startingVerse={ayah}"

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        # Step 1: Open base site
        print("Opening base site:", base_url)
        page.goto(base_url, wait_until="domcontentloaded")
        page.wait_for_timeout(3000)  # wait for React to render

        # Step 2: Click Reading view toggle
        clicked = page.evaluate("""() => {
            // Find the Reading toggle button
            const btns = Array.from(document.querySelectorAll('button'));
            for (const btn of btns) {
                if (btn.textContent && btn.textContent.toLowerCase().includes('reading')) {
                    btn.click();
                    return true;
                }
            }
            // fallback: search by svg
            const svgs = document.querySelectorAll('svg[xmlns="http://www.w3.org/2000/svg"]');
            for (const svg of svgs) {
                const b = svg.closest('button');
                if (b && b.textContent.toLowerCase().includes('reading')) {
                    b.click();
                    return true;
                }
            }
            return false;
        }""")

        if clicked:
            print("Switched to Reading view ✅")
        else:
            print("Could not find Reading toggle ❌")

        page.wait_for_timeout(1500)

        # Step 3: Navigate to the verse (still stays in Reading view)
        print("Navigating to verse:", verse_url)
        page.goto(verse_url, wait_until="domcontentloaded")
        page.wait_for_timeout(3000)

        print("Browser will stay open for 20s...")
        page.wait_for_timeout(20000)
        browser.close()

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python questionSite.py <surah> <ayah>")
        sys.exit(1)
    open_in_reading_view(int(sys.argv[1]), int(sys.argv[2]))
