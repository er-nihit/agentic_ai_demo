# FastAPI

### 1. Endpoints
Each API endpoint is added using a function with decorator with HTTP task.  

The endpoint with `/docs` automatically generates a documentation with all details of the eligible endpoints.  

Execute the python file as a Web Server (using Uvicorn):  
uvicorn \<filename>:<fast_api_obj_name>  
**Example**: `uvicorn main.app`  

Reload the uvicorn server automatically when any changes are made in the python file: `uvicorn main.app --reload`  

### 2. Path Params
Path parameters are dynamic segments of a URL path used to identify a specific resource.  

Provide dynamic attribute in GET calls.  
**Example:** `app.get("patient/{patient_id}")` : This will return the patient data with patient_id as user input.  

### 3. Path() function 
The Path() function in FastAPI is used to provide metadata, validation rules and documentation hints for path parameters in the API endpoints.  
In simple words, we can declare examples or description to the endpoints for better understanding for client.

**Example:** `def view_patient(patient_id: str = Path(..., descrition="ID of the patient", example="P001")):`

#### 3.1 HTTPException
HTTPException is a special built-in exception in FastAPI used to return custom HTTP error responses when something goes wrong in your API.  

Instead of returning a normal JSON or crashing the server, you can gracefully raise an error with:  
- a proper HTTP status code (like 404, 400, 403, etc.)
- a custom error message
- (optional) extra headers

**Example**: `raise HTTPException(status_code=404, detail='Patient Not Found')`


### 4. Query Parameter
Query parameters are optional key-value pairs appended to the end of a URL, used to pass additional data to the server in an HTTP request. They are typically employed for operations like filtering, sorting, searching, and pagination, without altering the endpoint path itself. 

\- The `?` marks the start of query parameters.  
\- Each parameter is a key-value pair: `key=value`  
\- Multiple parameters are separated by `&` 

**Example:** `/patients?city=Delhi&sort_by=age`
- `city=Delhi` is a query parameter for filtering
- `sort_by=age` is a query parameter for sorting

### 5. Pydantic
Pydantic is type validation library in python which is used to validate multiple elements of a variable.  

It can perform data type validations.  
Specific validations for Email, Phone numbers or URL  
Validations based on REGEX.  

#### 5.1 `@field_validator()`
It is used to add additional validations based on the application/company-specific requirements.  

**Use Cases:**
- validating the email domain belongs to a particular/list of supported domains.
- Name should be always converted to a upper case.
- Height should always in cm. 

It is important to provide a `@field_validator('<variable_name>')`  and `@classmethod` decorators during the function definition.   

**`mode`** parameter in `field_validator()` is used to define where the function needs to performed before or after the type checking from the defined class. Value of mode value can either be `after` **(default)** or `before`.  

**Example**:
`@field_validator('age', mode='after')` will first check the data type of age, thereafter will perform field validation.  
`@field_validator('age', mode='before')` will first perform the field validation thereafter perform the data-type check for age.   

#### 5.2 `@model_validator()`
It is used when we need to perform multiple validations which is not possible to perform using field_validator().  

Here we do not need to pass any specific variable, instead we need to pass the whole model instead.  

**Example:** 
`@model_validator(model='after')`
`def check_age(cls, model):`

#### 5.3 `@computed_field()`
It is used where the value of a variable is not provided by the user, instead it is calculated by the model itself.  

To use this feature, it is important to include `@computed_field` and `@property` decorators.  

#### 5.4  Nested Models
When we use one model as a field in an another model, it is called nested models.  

We define a class for the first model. It can then be used as an object in the second model.  

**Example**: Create a `Address` pydantic class with address, city, pincode variables.  
Create next pydantic class `Patient` which can have a address variable which performs type checking with `Address` class, ensuring, the fields address, city and pincode are provided.  

#### 5.5 Serialization
Export the pydantic model as a python dict, which can be therafter converted into a json file, which can be used for data transfers.  

*`obj.model_dump()`* provides a dump of all variables in python dict format.  
*`obj.model_dump_json()`* provides a dump of all variables in json (str) format.  

There are a few attributes like `exclude`, `include`, or `exclude_unset` which provides addiional functionalities.  




# HTTP Status Codes
| Status Code | Status | Description | 
|:------------|:-------|:------------|
|`2xx`|Success|The request was successfully received and processed|
|`3xx`|Redirection|Further action needs to taken (like, redirection)|
|`4xx`|Client Error|Something is wrong with the request from the client|
|`5xx`|Server Error|Something went wrong on the server side|


### Common HTTP Status Codes

|CODE|Meaning|Description|
|:---|:------|:----------|
|`200`|`OK`|Standard Success. A `GET` or `POST` succeeded|
|`201`|`Created`|After a `POST` that creates something|
|`204`|`No content`|Success, but no data returned. After a `DELETE` request|
|`400`|`Bad Request`|Mal-formatted or invalid request. Missing field or wrong data type|
|`401`|`Unauthorized`|No/Invalid authentication. Login required.|
|`403`|`Forbidden`|Authenticated, but no permission. Logged in but not allowed.|
|`404`|`Not Found`|Resource doesn't exist. Patient ID is not in the DB|
|`500`|`Internal Server Error`|Generic Failure. Something broke on the server end.|
|`502`|`Bad Gateway`|Gateway (like nginx) failed to reach backend.|
|`503`|`Service Unavailable`|Server is down or overloaded.|