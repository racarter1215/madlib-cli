import re

Name = {"Please write a name"}
Profession = {"Please write a profession"}
Month = {"Please write a month"}
Dog_Trait = {"Please write an adjective describing a dog"}

def madlib_template(path):
    try:
        with open(path, 'r') as path_string:
            contents = path_string.read()
            returned_string = str(contents)
            print(returned_string)
        return(returned_string)
    except FileNotFoundError:
        raise FileNotFoundError("File not found")

def parse_template(string):
    parse = re.findall(r'\{.*?\}', string)
    final_list = []
    for i in parse:
        string_edit = (i[1:-1])
        final_list.append(string_edit)
    correct_list = tuple(final_list)
    template = re.sub(r'\{.*?}', "{}", string)
    return(template, correct_list)

def user_input(prompt: str) -> str:
    message = 'Please enter'
    answer = input(message)
    while answer == '':
        answer = input(f'This answer is not accepted/n{message}')
    return input(f'{message} {prompt}\n>>')

def collect_user_answers(prompts: list) -> list:
    answers = []
    for answer in correct_list:
        answer = user_input(question)
        answers.append(answer)
    return answers

def replace_template(template: str, answers: list) -> str:
    for answer in answers:
        completed = re.sub(r'\{{\},', answer, template, 1)
    return completed

def save_template(template: str):
    file = open('madlib_cli/madlib_template.txt', 'w')
    file.write(template)
    file.close()


def start_madlib():
    string = read_template('madlib_cli/madlib_template.txt')
    template = correct_list = parse_template(string)
    answers = collect_user_answers(correct_list)
    completed = replace_template(template, answers)
    print(completed)
    save_template(completed)

if __name__ == "__main__":
    start_madlib()

print("Hello, my name is {Name} and my job is that of a {Profession}.")
print("I started Code Fellows in {Month} and I really like taking the night classes.") 
print("My dog, Rover, is very {Dog_Trait}.")
