from pins import board_folder
from vetiver import VetiverAPI, VetiverModel

# 1. Connect to the board where your model is stored
model_board = board_folder("./data/model", allow_pickle_read=True)

# 2. Read the latest version of the pinned model
v = VetiverModel.from_pin(model_board, "penguin_model", version = '20250824T130103Z-49eca')

# 3. Create an API for the model
vetiver_api = VetiverAPI(v, check_prototype=True)

# 4. Run with uvicorn if script is executed directly
api = vetiver_api.app


# http://127.0.0.1:8080
# uv run uvicorn api_docker:api --host 0.0.0.0 --port 8080


