# import numpy as np

# # a = [[4,2,6],[5,5,5]]
# # b = np.argmin(a,axis = 1)
# # print( b )
# print(np.round(10.51,1))

import cv2
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "wertyyu"

if __name__ == '__main__':
    app.run(debug=True)