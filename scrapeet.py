import sys
from scrapper import scrape_data

def ouput(id: int, title: str, question: str, difficulty: str, example: str, constraint: str):
    with(open("ouput.txt", "w")) as f:
        f.write("------------------------------------\n")
        f.write(f'{id} : {title}\n')
        f.write("------------------------------------\n\n")
        
        f.write("------------------------------------\n")
        f.write(f'Difficulty: {difficulty}\n')
        f.write("------------------------------------\n\n")
        
        f.write("------------------------------------\n")
        f.write(f'{question}\n')
        f.write("------------------------------------\n\n")
        
        f.write("------------------------------------\n")
        f.write(f'{example}\n')
        f.write("------------------------------------\n\n")
        
        f.write("------------------------------------\n")
        f.write(f'{constraint}\n')
        f.write("------------------------------------\n")

if __name__ == "__main__":
    if len(sys.argv) != 1:
        link = sys.argv[1]
    else:
        print(f'Usage: python scrapeet.py <https://leetcode.com/problems/{{problem}}/description/>')
        sys.exit(1)
    
    questionId, title, question, difficulty, example, constraint = scrape_data(link)
    ouput(questionId, title, question, difficulty, example, constraint)
    print(f'Output written to ouput.txt')