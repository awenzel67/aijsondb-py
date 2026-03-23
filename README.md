# Python bindings for aijsondb

The idea behind aijsondb is rather simple:

* Use a single json data file as data source.
* Declare the content of json data with json schema.
* Query the data with a JavaScript expression.

Writing a JavaScript expression to query a json data is not very convenient for humans. On the other hand letting an LLM creating the JavaScript expression using the json schema works well.

Thus using aijsondb in an agentic workflow is a good option to "talk with data".

Python package aijsondb is only a wrapper for the [aijsondb](https://github.com/awenzel67/aijsondb) library.

## Installation

aijsondb is available for Linux and Windows.

**Supported Python versions:** Python 3.7 and above are recommended.

```
pip install aijsondbpy
```

## Usage

Import the package.

```
import aijsondb
```

Load and validate the json data into an in memory data structure.

```
path_data="data/500 KB_V2.json"
path_schema="data/employeeSchemaDescription_V2.json"
aijsondb.init_db(path_data,path_schema)
```

Now you can query the data.
```
res=aijsondb.query_data_javascript("var result=data.employees.length;")
print(res)
```
By convention the root json object is accessible as `data` in the query. Also, the result of the query must be stored in the variable `result`.

The return value is a JSON string containing the result.

Sample data are available on [aijsondb](https://github.com/awenzel67/aijsondb).

Python script test_agent.py shows you how to create an langchain agent to talk with your JSON data in python using the aijsonpy package.

## Sample json data

The file 500_KB_V2.json in the data folder is derived from the dataset "Employees { 10 } Level Nested Formatted Versions", specifically the "500 KB 10 Level Formatted" variant available at [page](https://sample.json-format.com/).

The files test.json and 500_KB_V2Err.json are also based on this dataset.

The JSON schema employeeSchemaDescription_V2.json was automatically generated from 500_KB_V2.json and subsequently edited by hand.