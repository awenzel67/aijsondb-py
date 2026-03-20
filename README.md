# Python bindings for dominodb

The idea behind dominodb is rather simple:

* Use a single json data file as data source.
* Declare the content of json data with json schema.
* Query the data with a JavaScript expression.

Writing a JavaScript expression to query a json data is not very convenient for humans. On the other hand letting an LLM creating the JavaScript expression using the json schema works well.

Thus using dominodb in an agentic workflow is a good option to "talk with data".

Python package dominodb is only a wrapper for the [dominodb](https://github.com/awenzel67/dominodb) library.

## Installation

dominodb is available for Linux and Windows.

**Supported Python versions:** Python 3.7 and above are recommended.

```
pip install dominodb
```

## Usage

Import the package.

Load and validate the json data into an in memory data structure.

```
dominodb.init_db(path_data, path_schema)
path_schema="data/employeeSchemaDescription_V2.json"
dominodb.init_db(path_data,path_schema)
```

Now you can query the data.
```
res=dominodb.query_data_javascript("var result=data.employees.length;")
print(res)
```
By convention the root json object is accessible as `data` in the query. Also, the result of the query must be stored in the variable `result`.

The return value is a JSON string containing the result.