import requests

# Make the request
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')

# Print the type of request
print(type(res))

# Check request was successful
print(res.status_code == requests.codes.ok)

# Print the length of the requested text
print(len(res.text))

# Print the request (only the first 250 characters)
print(res.text[:250])