from dotenv import load_dotenv
from langchain.prompts.prompt import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import ChatOllama
from third_parties.linkedin import scrape_linkedin_profile
from langchain_openai import ChatOpenAI


if __name__ == "__main__":
    load_dotenv()

    summary_template = """
    given the Linkedin information {information} about a person I want you to create:
    1. A short summary based on her/his occupation and summary
    2. two interesting facts about them based on their experiences
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    # llm = ChatOpenAI(temperature=0)
    llm = ChatOllama(model='llama3')
    #llm = ChatOllama(model='mistral')  # with mistral the model create Hallucination about Elon Musk
    chain = summary_prompt_template | llm | StrOutputParser()  # https://python.langchain.com/v0.1/docs/modules/model_io/output_parsers/
    linkedin_data = scrape_linkedin_profile(
        linkedin_profile_url='https://gist.githubusercontent.com/cristiangodoyy/48627d926a3b76b630b75acad76e350a/raw/cbf4ce82940c4140574c55343568ef89cb2240af/cristian-godoy.json',
        mock=True
    )

    res = chain.invoke(input={"information": linkedin_data})

    print(res)
