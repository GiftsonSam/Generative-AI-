from langchain_openai import OpenAI
from langchain import PromptTemplate

prompt = PromptTemplate(
    template = """/You are a naming consultant, give responses to the following/ 
    question: {question}. Do not use technical words, give easy/
to understand responses. Give your response in {language}""",
    input_variables = ["question", "language"]
)

#format the prompt to add variable’s values
prompt_formatted_str : str = prompt.format(
    
       question = "Suggest a good name for a company that makes socks?",
       language = "English"
       )
# instantiate the OpenAI instance
llm = OpenAI(temperature = 0.9)

# make a prediction
prediction = llm.predict(prompt_formatted_str)

# print the prediction
print(prediction)
