# PageTrack

PageTrack is a simple web application for tracking and managing your book collection. It allows users to add, edit, and delete books, and stores the data in a JSON file. The app features a clean interface and is easy to use for personal book management.

## Features
- Add new books with details
- Edit existing book entries
- Delete books from your collection
- Data stored in a JSON file for easy backup and restore
- Simple, user-friendly web interface

## Project Structure
```
app.py                # Main Flask application
backups/              # Backup JSON files of the database
  └── *.json
static/
  └── style.css       # CSS styles
templates/            # HTML templates
  ├── base.html
  ├── index.html
  ├── add_book.html
  └── edit_book.html
database/
  └── books.json      # Main data storage
LICENCE.txt           # License information
```

## Getting Started

### Prerequisites
- Python 3.x
- Flask

### Installation
1. Clone the repository:
   ```powershell
   git clone https://github.com/OmGoyal27/PageTrack.git
   cd PageTrack
   ```
2. Install dependencies:
   ```powershell
   pip install flask
   ```

### Running the App
```powershell
python app.py
```
Then open your browser and go to `http://127.0.0.1:5000/`.

## Backup & Restore
- Backups of your book database are stored in the `backups/` folder as JSON files.
- The main database is `database/books.json`.

## License
See `LICENCE.txt` for license information.

## Author
Om Goyal