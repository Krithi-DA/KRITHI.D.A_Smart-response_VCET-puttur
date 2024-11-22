import openai

# Replace with your OpenAI API key
openai.api_key = "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"

def generate_auto_response(client_info):
    # Craft the prompt with provided client information
    prompt = f"""
    A client has filled a form to start a large project and has provided some initial requirements. Below are the details:
    
    From Name: {client_info['from_name']}
    Client First Name: {client_info['first_name']}
    Client Last Name: {client_info['last_name']}
    Client Email: {client_info['email']}
    Client Country: {client_info['country']}
    Client Location: {client_info.get('location', 'Not provided')}
    Client Language: {client_info['language']}
    Project Type: {client_info['project_type']}
    Service Category: {client_info['service_category']}
    Client Website: {client_info.get('website', 'No')}
    Additional Information: "{client_info['additional_info']}"

    Based on this information, write a professional and natural email response to the client, ensuring it is human-like and polished. Avoid generic phrases that sound AI-generated.
    """

    # Use `ChatCompletion.create` for GPT-3.5-turbo or GPT-4
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a professional assistant crafting email responses."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=300
    )

    # Extract and return the response text
    return response['choices'][0]['message']['content'].strip()

def chatbot():
    print("Welcome to the Professional Email Response Chatbot!")
    print("Please provide the required details for generating an email response.")
    print("Type 'exit' at any point to quit the chatbot.\n")
    
    while True:
        # Collect client information interactively
        from_name = input("Enter your full name: ")
        if from_name.lower() == 'exit':
            break
        
        first_name = input("Enter your first name: ")
        if first_name.lower() == 'exit':
            break
        
        last_name = input("Enter your last name: ")
        if last_name.lower() == 'exit':
            break
        
        email = input("Enter your email: ")
        if email.lower() == 'exit':
            break
        
        country = input("Enter your country: ")
        if country.lower() == 'exit':
            break
        
        location = input("Enter your location (optional): ")
        if location.lower() == 'exit':
            break
        
        language = input("Enter your preferred language: ")
        if language.lower() == 'exit':
            break
        
        project_type = input("Enter the project type: ")
        if project_type.lower() == 'exit':
            break
        
        service_category = input("Enter the service category: ")
        if service_category.lower() == 'exit':
            break
        
        website = input("Does the client have a website? (Yes/No): ")
        if website.lower() == 'exit':
            break
        
        additional_info = input("Enter additional information or requirements: ")
        if additional_info.lower() == 'exit':
            break
        
        # Create client_info dictionary
        client_info = {
            "from_name": from_name,
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "country": country,
            "location": location if location else "Not provided",
            "language": language,
            "project_type": project_type,
            "service_category": service_category,
            "website": website,
            "additional_info": additional_info,
        }
        
        print("\nGenerating your email response...\n")
        try:
            response = generate_auto_response(client_info)
            print("Here is the generated email response:")
            print("="*50)
            print(response)
            print("="*50)
        except Exception as e:
            print(f"An error occurred: {e}")
        
        # Ask if the user wants to continue
        continue_chat = input("\nWould you like to generate another response? (Yes/No): ")
        if continue_chat.lower() != 'yes':
            print("Thank you for using the chatbot. Goodbye!")
            break

# Run the chatbot
if __name__ == "__main__":
    chatbot()
