from modal import App, web_endpoint

app = App("json-endpoint-example")


@app.function()
@web_endpoint(method="GET")
def get_json():
    return {"message": "Hello, World!", "something": 52, "status": "success"}

