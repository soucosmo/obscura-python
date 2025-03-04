# Obscura Client For Python

## Using the `obscura-client` Library

This guide will walk you through the steps to install and use the `obscura-client` library in Python, and provide examples on how to handle errors and deserialize responses using `json`.

## Installation

First, install the `obscura-client` using pip:

```bash
pip install obscura-client
```

## Usage

Make sure to import the necessary modules in your Python script:

```python
from obscura_client import Client, ConfigMap
```

Here's an example demonstrating how to use the `Client` and `ConfigMap`:

```python
def main():
    url = "http://localhost:9797"
    token = "your token here"

    client = Client(url, token)
    config_map = ConfigMap(client)

    # Reading a key

    try:
        data = config_map.read("your path here")

        print(f"Deserialized JSON: {data}")
    except Exception as e:
        print(f"Failed to deserialize JSON: {e}")

    # Reading a key prefix
    try:
        data = config_map.read_with_prefix("your path prefix here")
        print(f"Deserialized JSON with prefix: {data}")
    except Exception as e:
        print(f"Failed to deserialize JSON with prefix: {e}")

if __name__ == "__main__":
    main()
```

## Error Handling

The example above includes error handling for:

- Failed HTTP requests
- Deserialization errors
- Missing keys

Ensure that you handle these errors appropriately in your application to maintain robustness.

## Additional Resources

For more information, refer to the server project repository [here](https://github.com/soucosmo/obscura).

This guide offers a basic understanding of using the `obscura-client` library. For more complex scenarios, consider exploring the library documentation and source code.
