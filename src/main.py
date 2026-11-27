from dotenv import load_dotenv
import os
#!/usr/bin/python

load_dotenv(dotenv_path='.env')

def print_author():
    author = os.getenv('AUTHOR')
    print(f"Автор проекта: {author}")
