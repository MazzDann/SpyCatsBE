# SpyCatsBE
A BackEnd for Spy Cat Agency task


## Prerequisites
- Python 3.8+
- pip
- Git

## Setup Instructions
1. **Clone the repository**:
   ```bash
   git clone https://github.com/MazzDann/SpyCatsBE.git
   cd sca-backend
   ```

2. **Set up a virtual environment**:
   ```bash
   python -m venv SCvenvB
   SCvenvB\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   SCvenvB\Scripts\python.exe -m pip install  -r requirements.txt
   ```

4. **Run the application**:
   ```bash
   python -m uvicorn src.main:app --reload
   ```
   The API will be available at `http://localhost:8000`.

# EP
- Endpoints include:
  - `POST /cats/`: Create a cat.
  - `GET /cats/`: List all cats.
  - `GET /cats/{cat_id}`: Get a specific cat.
  - `PUT /cats/{cat_id}/salary`: Update a cat's salary.
  - `DELETE /cats/{cat_id}`: Delete a cat.
  - `POST /missions/`: Create a mission with targets.
  - `GET /missions/`: List all missions.
  - `GET /missions/{mission_id}`: Get a specific mission.
  - `DELETE /missions/{mission_id}`: Delete a mission.
  - `PUT /missions/{mission_id}/assign_cat`: Assign a cat to a mission.
  - `PUT /targets/{target_id}/notes`: Update target notes.
  - `PUT /targets/{target_id}/complete`: Mark a target as complete.