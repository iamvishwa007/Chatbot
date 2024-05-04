from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('localhost', 27017)
db = client.college_chatbot
collection = db.qa

def get_intent_response(user_input):
    result = collection.find_one({"$text": {"$search": user_input}})
    if result is None:
        return "Sorry, I didn't understand that."
    elif isinstance(result, str):
        return "Unexpected result type. Please check your data."
    else:
        return result["response"]


def main():
    print("Welcome to College Chatbot!")
    print("Ask me anything, or type 'exit' to quit.")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == 'exit':
            break
        
        response = get_intent_response(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    main()
