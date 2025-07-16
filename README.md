# 🤖 Reddit User Persona Generator

This tool scrapes a Reddit user's profile (posts and comments) and generates a detailed, structured **User Persona** using GPT-4. Each characteristic in the persona includes **citations** from the Reddit content that led to that insight.

---

## 🚀 Features

- 🔍 Scrapes up to 100 posts + 100 comments using Reddit API
- 🤖 Uses GPT-4 to infer age, job, personality, interests, etc.
- 📝 Cites Reddit sources for every persona trait
- 📄 Outputs clean `.txt` reports
- ✅ Easy to use with a single command

---

## 📂 Project Structure

```
reddit-user-persona/
├── persona_builder.py            # Main execution script
├── requirements.txt              # Python dependencies
├── .env                          # API keys (not uploaded)
├── README.md                     # This file
├── utils/
│   ├── reddit_scraper.py         # Reddit scraper logic
│   └── persona_generator.py      # GPT persona generator
└── personas/
    ├── kojied.txt
    └── Hungry-Move-6603.txt
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/your-username/reddit-user-persona.git
cd reddit-user-persona
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Create `.env` File

Create a `.env` file in the root directory and add your credentials:

```env
REDDIT_CLIENT_ID=your_reddit_client_id
REDDIT_CLIENT_SECRET=your_reddit_client_secret
REDDIT_USER_AGENT=reddit-persona:v1.0 (by u/yourusername)
OPENAI_API_KEY=your_openai_key
```

---

## ▶️ How to Use

```bash
python persona_builder.py https://www.reddit.com/user/Hungry-Move-6603/
```

- The script will fetch the Reddit user’s data
- Generate a complete persona
- Save the results to `personas/<username>.txt`

---

## 📄 Sample Output

### `personas/Hungry-Move-6603.txt`

```
👤 USER PERSONA: Hungry-Move-6603

- Name: Likely Jake  
  Cited from: "I’m Jake and I love building PCs."

- Age: Around 25  
  Cited from: "Graduated last year, working since."

- Occupation: IT Technician  
  Cited from: "At my help desk job we use..."

- Interests: Gaming, Building PCs, Cooking  
  Cited from: "I built my rig last summer and I’m into..."

- Personality Traits: Curious, helpful, introverted  
  Cited from: "I usually don’t post much, but I like helping out here..."
```

---

## ✅ Assignment Deliverables

- `persona_builder.py` - Executable script
- `README.md` - This file
- `requirements.txt` - Dependency list
- `/utils/` - Contains helper modules
- `/personas/` - Sample outputs for two Reddit users

---

## 👋 Author

This project was developed as part of a technical assignment for a paid internship opportunity.  
All code is original and ready to demonstrate skills in scraping, LLM prompt design, and persona generation.
