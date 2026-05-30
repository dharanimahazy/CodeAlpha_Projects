import sys
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

FAQ_DATASET = {
    "What is Artificial Intelligence?": "Artificial Intelligence (AI) refers to the simulation of human intelligence in machines that are programmed to think and learn like humans.",
    "What are the main tasks in this internship?": "The core AI internship tasks include a Language Translation Tool, an FAQ Chatbot, an AI Music Generator, and an Object Detection system.",
    "How do I submit my completed tasks?": "You must upload your code to GitHub, share a video demonstration on LinkedIn tagging @CodeAlpha, and fill out the official submission form.",
    "What are the criteria for completing the internship?": "To be eligible for a certificate, you must complete a minimum of two or three tasks from your assigned domain.",
    "Who can I contact for internship support?": "You can reach out via email at services@codealpha.tech or contact support through the official WhatsApp group number."
}

questions = list(FAQ_DATASET.keys())
answers = list(FAQ_DATASET.values())

vectorizer = TfidfVectorizer(lowercase=True, stop_words='english')
tfidf_matrix = vectorizer.fit_transform(questions)

def get_chatbot_response(user_query):
    query_vector = vectorizer.transform([user_query])
    similarity_scores = cosine_similarity(query_vector, tfidf_matrix)
    
    best_match_index = similarity_scores.argmax()
    highest_score = similarity_scores[0][best_match_index]
    
    if highest_score > 0.25:
        return answers[best_match_index]
    else:
        return "I'm sorry, I couldn't find a close match for that question in my database. Please try rephrasing or check your spelling!"

def run_bot():
    print("==================================================")
    print("      CodeAlpha AI Internship FAQ Chatbot         ")
    print("==================================================")
    print("Type 'exit' or 'quit' at any time to close the chat.\n")
    print("Bot: Hello! I am your assistant. Ask me anything about the CodeAlpha internship.")
    
    while True:
        try:
            user_input = input("\nYou: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nBot: Goodbye!")
            sys.exit()
            
        if user_input.lower() in ['exit', 'quit']:
            print("Bot: Goodbye! Have a great day.")
            break
            
        if not user_input:
            print("Bot: Please type a valid question.")
            continue
            
        response = get_chatbot_response(user_input)
        print(f"Bot: {response}")

if __name__ == "__main__":
    run_bot()