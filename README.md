
# Minesweeper Engine
A lightweight engine for minesweeper that runs on numpy, to eventually be made efficent enough for ML models and more.

### Current status
* Can make minesweeper boards of any size and bomb count
* Has flag and checking functionality through coordinate inputs
* Has the blank space checker done recursively
* Prints current state to terminal, with unicode characters for square size and colors


### To-do
* Add mouse and/or arrow inputs over coordinate
* Add fail state that prevents game interactions
* Optimise with numba for maximum efficency on ML
* Add the first-click generation over the current system (board made on startup)


### Prerequisites
You need Python 3 and the `numpy` package installed. If you don't have NumPy, install it via your terminal:
```bash
pip install numpy
```

## License
This project is licensed under the MIT License.
