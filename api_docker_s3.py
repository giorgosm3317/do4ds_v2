from pins import board_s3
from vetiver import VetiverAPI, VetiverModel
# from dotenv import load_dotenv

# load_dotenv()

# 1. Connect to the board where your model is stored
model_board = board_s3("do4ds-lab-gm", allow_pickle_read=True)

# 2. Read the latest version of the pinned model
v = VetiverModel.from_pin(model_board, "penguin_model")

# 3. Create an API for the model
vetiver_api = VetiverAPI(v, check_prototype=True)

# 4. Run with uvicorn if script is executed directly
api = vetiver_api.app


# http://127.0.0.1:8080
# uv run uvicorn api_docker_s3:api --host 0.0.0.0 --port 8080
