import requests


# GET Request Example
def test_get_request():
    # Define the API endpoint URL
    url = "https://jsonplaceholder.typicode.com/posts/1"
    
    response = requests.get(url)
    assert response.status_code == 200
    
    data = response.json()
    print("HERE IS THE DATA")
    print(data)
    
    assert data["userId"] == 1
    assert data["id"] == 1
    assert data["title"] == "sunt aut facere repellat provident occaecati excepturi optio reprehenderit"
    assert data["body"] == "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"

# POST Request Example
def test_post_request():
    # Define the API endpoint URL for creating a new post
    url = "https://jsonplaceholder.typicode.com/posts"

    
    # Define the payload (data) for the POST request
    payload = {
        "userId": 1,
        "title": "Test Post",
        "body": "This is a test post using requests and pytest."
    }
    
    # Send a POST request to create a new post
    response = requests.post(url, json=payload)
    
    # Check if the response status code is 201 (Created)
    assert response.status_code == 201
    
    # Parse the JSON response content
    data = response.json()
    print(data)
    assert data["userId"] == payload["userId"]
    assert data["title"] == payload["title"]
    assert data["body"] == payload["body"]