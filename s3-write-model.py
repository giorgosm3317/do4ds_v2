## Load Environment

from dotenv import load_dotenv

load_dotenv()

from pins import board_folder
from vetiver import VetiverAPI, VetiverModel

# 1. Connect to the board where your model is stored
model_board = board_folder("data/model", allow_pickle_read=True)

# 2. Read the latest version of the pinned model
v = VetiverModel.from_pin(model_board, "penguin_model")

# 3. Write to S3

from pins import board_s3
from vetiver import vetiver_pin_write

board = board_s3("do4ds-lab-gm", allow_pickle_read=True)
vetiver_pin_write(board, v)




