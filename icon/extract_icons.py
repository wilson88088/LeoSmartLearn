"""
Copy pre-cropped icons from ../extracted_learning_ui_elements_png/
into this `icon/` folder with shorter, consistent filenames that
match the CSS references in index.html.

Run once:
    py.exe extract_icons.py

No external dependencies needed (uses only the standard library).
"""
import shutil
from pathlib import Path

HERE = Path(__file__).parent
SRC = HERE.parent / "extracted_learning_ui_elements_png"

# Source filename -> Destination filename (under icon/)
MAPPING = {
    # Sidebar nav icons
    "nav_home_icon.png":                       "nav_home.png",
    "nav_calendar_icon.png":                   "nav_cal.png",
    "nav_subject_history_books_icon.png":      "nav_books.png",
    "nav_learning_reminder_bell_icon.png":     "nav_bell.png",
    "nav_parent_summary_people_icon.png":      "nav_parents.png",
    "nav_course_settings_gear_icon.png":       "nav_gear.png",

    # Mascots & decorations
    "sidebar_backpack_books_pencils.png":      "mascot_backpack.png",
    "schedule_calendar_character_graphic.png": "mascot_calendar.png",
    "schedule_backpack_book_pencil_graphic.png": "deco_schedule.png",
    "top_paper_airplane_trail.png":            "deco_airplane.png",
    "top_cloud_cluster.png":                   "deco_cloud.png",
    "decorative_sparkles_group.png":           "deco_sparkles.png",
    "decorative_confetti_dots_group.png":      "deco_confetti.png",
    "abc_background_motif.png":                "deco_abc.png",
    "pastel_dot_accents_group.png":            "deco_dots.png",

    # Avatar & badges
    "smiling_avatar_face.png":                 "avatar.png",
    "english_subject_badge.png":               "badge_english.png",
    "chinese_subject_badge.png":               "badge_chinese.png",
    "vertical_three_dot_menu_icon.png":        "menu_dots.png",

    # Course / lesson cards
    "course_management_section_icon.png":      "section_course.png",
    "lesson_card_notebook_pencil_icon.png":    "lesson_notebook.png",
    "lesson_card_open_book_icon.png":          "lesson_book.png",
    "date_picker_calendar_icon.png":           "date_picker.png",
    # app_logo_book_icon.png intentionally NOT copied to avoid overwriting
    # the existing icon/app_logo.png. Rename manually if you want to swap.
}


def main():
    if not SRC.exists():
        print(f"[error] Source folder not found: {SRC}")
        return
    copied = 0
    for src_name, dst_name in MAPPING.items():
        src = SRC / src_name
        dst = HERE / dst_name
        if not src.exists():
            print(f"[skip] missing source: {src_name}")
            continue
        shutil.copy2(src, dst)
        print(f"[ok] {src_name}  ->  icon/{dst_name}")
        copied += 1
    print(f"\nDone. Copied {copied} files to {HERE}")


if __name__ == "__main__":
    main()
