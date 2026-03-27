import aijsondb
import json
import pprint
from langchain.agents import create_agent
from langchain_mistralai.chat_models import ChatMistralAI

path_data="data/500 KB_V2.json"
path_schema="data/employeeSchemaDescription_V2.json"

aijsondb.init_db(path_data,path_schema)

with open(path_schema) as f:
    jschema = json.load(f) 


def query_json_javascript(query: str) -> any:
    """Run a javascript expression on the provided data."""
    try:
        matches=aijsondb.query_data_javascript(query)
        return matches
    except Exception as e:  
        serr=f"Error running the javascript expression: {e}"
        return [serr] 

schema = json.dumps(jschema, indent=4)


template = f"""
I have a JSON data object.

The JSON schema for the data object you will work with is:
{schema}

Fetch data from the JSON object using javascript to query the data.

Use the tool: 
query_json_javascript: returns the entities using a given javascript programm as query.

The data are in a javascript variable named: data.
The final result is always saved in variable result: eg. var result.

Always use the available tools to fetch data.
Only use the data from tools defined above to answer the question.
"""

llmm = ChatMistralAI(
    model="mistral-large-latest",
    temperature=0,
    max_retries=3
)
agent = create_agent(
    model=llmm,
    tools=[query_json_javascript],
    system_prompt=template,
)

#output=agent.invoke({"messages": [{"role": "user", "content": "How many employees are in the data?"}]})
#print(output['messages'][-1].content)


output=agent.invoke({"messages": [{"role": "user", "content": "Which employees have the greatest experience?"}]})
print(output['messages'][-1].content)
#pprint.pprint(output)

with open("result.json", "w") as f:
    pprint.pprint(output,f)
