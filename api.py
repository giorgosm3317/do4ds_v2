from pins import board_folder
from vetiver import VetiverAPI, VetiverModel

# 1. Connect to the board where your model is stored
model_board = board_folder("data/model", allow_pickle_read=True)

# 2. Read the latest version of the pinned model
v = VetiverModel.from_pin(model_board, "penguin_model")

# 3. Create an API for the model
app = VetiverAPI(v, check_prototype=True)

# 4. Run with uvicorn if script is executed directly
app.run(port = 8080)
