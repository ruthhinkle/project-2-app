from sqlalchemy import create_engine

engine = create_engine("sqlite:///data.sqlite")

engine.execute('DROP TABLE IF EXISTS api_logs;')

engine.execute('''
CREATE TABLE api_logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    url TEXT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL
);
''')