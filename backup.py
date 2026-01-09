import shutil
from datetime import datetime
from pathlib import Path

def backup_project():
    BASE_DIR = Path(__file__).resolve().parent
    BACKUP_ROOT = BASE_DIR.parent / "Back_up_Django"
    BACKUP_ROOT.mkdir(parents=True, exist_ok=True)

    from_dir = BASE_DIR 
    date_str = f"{datetime.now():%Y%m%d_%H%M%S}"
    to_dir = BACKUP_ROOT / date_str

    # 除外するディレクトリ、ファイルを設定
    ignore = shutil.ignore_patterns("venv", "*.pyc", "__pycache__", ".env")

    # バックアップを実行
    shutil.copytree(from_dir, to_dir, ignore=ignore, dirs_exist_ok=True)

    # ログを作成しておく
    log_file = BACKUP_ROOT / "backup.log"
    with open(log_file, mode="a", encoding="utf-8") as f:
        f.write(f"{datetime.now():%Y-%m-%d %H:%M:%S}: Backup created at {to_dir}\n")

    print(f"Backup to {to_dir}")

if __name__ == "__main__":
    backup_project()
