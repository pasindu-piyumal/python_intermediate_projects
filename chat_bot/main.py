from difflib import get_close_matches

def get_best_match(user_question: str, questions: dict) -> str | None:
    questions: list[str] = [q for q in questions]
    matches: list = get_close_matches(user_question, questions, n=1, cutoff=0.6)

    if matches:
        return matches[0]
    
def chat_bot(knowledge: dict):
    user_input: str = input('You: ')
    best_match: str | None = get_best_match(user_input, knowledge)

    if answer := knowledge.get(best_match):
        print(f'Bot: {answer}')
    else:
        print("Bot: I'm sorry, I don't understand the question.")

if __name__ == "__main__":
    brain: dict = {
        'hello': 'Hi there!',
        'how are you?': "I'm doing well, thank you!",
        'what is your name?': "I'm a simple chat bot created in Python.",
        'what can you do?': "I can answer simple questions based on my knowledge base.",
        'what time is it?': "I don't have a clock, but you can check the time on your device.",
        'bye': 'Goodbye! Have a great day!'
    }

    while True:
        chat_bot(knowledge=brain)