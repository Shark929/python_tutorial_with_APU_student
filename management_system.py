def read_user_data():
    user_data = []
    with open('userdata.txt', 'r') as file:
        for line in file:
            name, username, password = map(str.strip, line.split(','))
            user_data.append({'name': name, 'username': username, 'password': password})
    return user_data


def read_subjects(file_path):
    subjects = {}
    with open(file_path, 'r') as file:
        for line in file:
            subject, *topics = map(str.strip, line.split(','))
            subjects[subject] = topics
    return subjects


def create_question_file(subject, topics, question, answer):
    file_name = f"questions.txt"
    with open(file_name, 'a') as file:
        file.write(f"Subject: {subject}\nTopics: {topics}\nQuestion: {question}\nAnswer: {answer}\n\n")
    print(f"Question and answer saved in {file_name}")


def save_user_data(user_data):
    with open('userdata.txt', 'w') as file:
        for user in user_data:
            file.write(f"{user['name']}, {user['username']}, {user['password']}\n")


def find_user_index(username, user_data):
    for index, user in enumerate(user_data):
        if user['username'] == username:
            return index
    return -1


def edit_user_data(user_data, username):
    index = find_user_index(username, user_data)
    #index = 0

    if index != -1:
        print(f"Editing user: {user_data[index]['name']}")

        new_name = input("Enter new name: ")
        new_username = input("Enter new username: ")
        new_password = input("Enter new password: ")

        #user_data[0]['name'] = Ivan Lim
        user_data[index]['name'] = new_name
        user_data[index]['username'] = new_username
        user_data[index]['password'] = new_password

        print("User information updated successfully.")
        save_user_data(user_data)
    else:
        print("User not found.")


def login(user_data, max_attempts=3):
    attempts_left = max_attempts

    while attempts_left > 0:
        entered_username = input("Enter your username: ")
        entered_password = input("Enter your password: ")

        for user in user_data:
            if user['username'] == entered_username and user['password'] == entered_password:
                return user['username']

        attempts_left -= 1
        print(f"Invalid username or password. {attempts_left} {'attempts' if attempts_left != 1 else 'attempt'} left.")

    print("Login failed. Too many attempts.")
    return None

def read_questions(file_path):
    questions = []
    with open(file_path, 'r') as file:
        current_question = None
        for line in file:
            line = line.strip()
            if line.startswith("Subject:"):
                current_question = {'subject': line[len("Subject:"):].strip(), 'topics': [], 'question': '', 'answer': ''}
            elif line.startswith("Topics:"):
                current_question['topics'] = line[len("Topics:"):].strip().split(',')
            elif line.startswith("Question:"):
                current_question['question'] = line[len("Question:"):].strip()
            elif line.startswith("Answer:"):
                current_question['answer'] = line[len("Answer:"):].strip()
                questions.append(current_question)
    return questions


def save_questions(questions, file_path):
    with open(file_path, 'w') as file:
        for question in questions:
            file.write(f"Subject: {question['subject']}\n")
            file.write(f"Topics: {', '.join(question['topics'])}\n")
            file.write(f"Question: {question['question']}\n")
            file.write(f"Answer: {question['answer']}\n\n")


def edit_question_data(questions, subject, topic):
    matching_questions = [q for q in questions if q['subject'] == subject and topic in q['topics']]

    if not matching_questions:
        print("No questions found for the specified subject and topic.")
        return

    print("Available questions:")
    for i, question in enumerate(matching_questions, 1):
        print(f"{i}. {question['question']}")

    choice = input("Enter the number of the question you want to edit: ")
    try:
        choice = int(choice)
        if 1 <= choice <= len(matching_questions):
            chosen_question = matching_questions[choice - 1]
            new_question = input("Enter the new question: ")
            new_answer = input("Enter the new answer: ")

            chosen_question['question'] = new_question
            chosen_question['answer'] = new_answer

            print("Question updated successfully.")
            save_questions(questions, 'questions.txt')
        else:
            print("Invalid choice. Exiting.")
    except ValueError:
        print("Invalid input. Exiting.")

def main():
    subject_file_path = 'subject.txt'
    subjects = read_subjects(subject_file_path)

    print("Available subjects:")
    for subject in subjects:
        print(subject)

    chosen_subject = input("Enter the subject: ").strip()
    if chosen_subject not in subjects:
        print("Invalid subject. Exiting.")
        return

    print(f"Available topics for {chosen_subject}:")
    for topic in subjects[chosen_subject]:
        print(topic)

    chosen_topic = input("Enter the topic: ").strip()
    if chosen_topic not in subjects[chosen_subject]:
        print("Invalid topic. Exiting.")
        return

    questions_file_path = 'questions.txt'
    questions = read_questions(questions_file_path)

    edit_question_data(questions, chosen_subject, chosen_topic)
    # subject_file_path = 'subject.txt'
    # subjects = read_subjects(subject_file_path)
    #
    # print("Available subjects:")
    # for subject in subjects:
    #     print(subject)
    #
    # chosen_subject = input("Enter the subject: ").strip()
    # if chosen_subject not in subjects:
    #     print("Invalid subject. Exiting.")
    #     return
    #
    # print(f"Available topics for {chosen_subject}:")
    # for topic in subjects[chosen_subject]:
    #     print(topic)
    #
    # chosen_topic = input("Enter the topic: ").strip()
    # if chosen_topic not in subjects[chosen_subject]:
    #     print("Invalid topic. Exiting.")
    #     return
    #
    # question = input("Enter your question: ")
    # answer = input("Enter the answer: ")
    #
    # create_question_file(chosen_subject, chosen_topic, question, answer)


if __name__ == "__main__":
    main()
