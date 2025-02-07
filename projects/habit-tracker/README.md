# Pixela Graph API Project

This is a simple Python script that interacts with the Pixela API to create and update a graph for tracking lift sessions.

## Requirements
- Python 3.x
- `requests` library (install with `pip install requests`)

## Setup
1. Create an account on [Pixela](https://pixe.la/)
2. Generate a token from your Pixela account settings
3. Update the `TOKEN` variable in the script with your own token

## How It Works
- **Create a User** (commented out in the script)
- **Create a Graph** (commented out in the script)
- **Add Data (Pixel) to the Graph**
  - Automatically gets the current date
  - Adds a pixel with a weight of `25 Kg`

## Usage
1. Uncomment the relevant sections if you want to create a user or a graph.
2. Run the script:
   ```bash
   python script.py
   ```
3. Check your graph at:
   - Profile: [https://pixe.la/@shivam30](https://pixe.la/@shivam30)
   - Graph: [https://pixe.la/v1/users/shivam30/graphs/graph30.html](https://pixe.la/v1/users/shivam30/graphs/graph30.html)

## Notes
- Replace `TOKEN` with your actual Pixela token.
- The script is currently set to add `25 Kg` by default; modify as needed.

## Example Response
Successful pixel creation will return:
```json
{"message":"Success.", "isSuccess":true}
```


