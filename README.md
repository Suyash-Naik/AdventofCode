# **Advent of Code** — my first repository

## Description

This is the repository where I learn to code. It holds my [Advent of Code](https://adventofcode.com/) solutions, starting with the 2022 event on 1 December 2022 — the first commit here is the first real Python I ever wrote and pushed. Nothing has been retro-fitted or cleaned up: the early scripts still open their input with a `tkinter` file dialog, still carry hard-coded paths from three different machines, and still print intermediate state to the terminal because that was my debugger. The commit messages are half solution log, half diary.

I have kept it that way on purpose. Read top to bottom it is a reasonable record of going from `open(filename).readlines()` and a `pandas` DataFrame used as a dictionary, to type-hinted functions, `sys.argv`, regex, and a locked `pixi` environment.

This repo is maintained by me, [Dr. Suyash Naik](mailto:suyashanaik[at]gmail.com). Questions welcome by email below.

### A note on the folder names

`Scripts/2023/` contains the **2022** event (Day 1 calorie counting through Day 10 CRT) — the folder is named for when I organised it, not for the puzzle year. `Scripts/2024/` is the 2024 event. The `DDMM` prefixes on the older filenames (`0412_`, `0812_`) are the December date the puzzle was released.

## Repository structure

```bash
.
├── README.md                                  # This file
├── pixi.toml                                  # pixi environment: Python 3.14, Jupyter, numpy, pandas, matplotlib, seaborn, holoviews, numba
├── pixi.lock                                  # Locked dependency versions for a reproducible environment
├── Data/                                      # Puzzle inputs — NOT committed, see "Inputs" below
│   └── 3/input.txt
└── Scripts/
    ├── 2023/                                  # ← Advent of Code 2022
    │   ├── Code1.py                           # Day 1  — Calorie Counting. The very first script. pandas used as a glorified dict
    │   ├── RSPCode_0222.ipynb                 # Day 2  — Rock Paper Scissors, scored with lookup dicts in a DataFrame
    │   ├── 312_rucksack.ipynb                 # Day 3  — Rucksack Reorganization, set intersection + ord() arithmetic
    │   ├── 0412_CleaningPairs.py              # Day 4  — Camp Cleanup, subsets and intersections
    │   ├── 0512_ElvenTowers.py                # Day 5  — Supply Stacks, crate towers as lists in a dict
    │   ├── 0612_signalsubrouter.py            # Day 6  — Tuning Trouble, sliding-window uniqueness (4- and 14-char markers)
    │   ├── 0812_Treehouse.py                  # Day 8  — Treetop Tree House, first time reaching for numpy on a grid
    │   ├── Day09/0912_Rope.py                 # Day 9  — Rope Bridge. Incomplete: tail follow / wrapping never fully worked
    │   └── Day10/1012_CRT.py                  # Day 10 — Cathode-Ray Tube. Empty stub, input downloaded and never solved
    └── 2024/                                  # ← Advent of Code 2024
        ├── 1/day1.py, 1stday.ipynb            # Day 1  — Historian Hysteria, sorted-list distance + similarity score
        ├── 2/day2.py, notebookday2.ipynb      # Day 2  — Red-Nosed Reports, safe/unsafe with the single-level Dampener
        └── 3/day3.py, day3p2test.ipynb        # Day 3  — Mull It Over, regex mul() with do()/don't() gating (part 2 still being debugged)
```

The general pattern is a notebook for working the problem out and a `.py` file once it behaved. In 2022 that split was accidental; by 2024 it was deliberate.

## Usage

The environment is managed with [pixi](https://pixi.sh), added late (2026) so the older scripts still run on a current Python.

1. Install the environment (first time only): `pixi install`

2. Start JupyterLab from the project root: `pixi run lab`

3. Or run a script directly:

```bash
# 2024 scripts take the input path as an argument
pixi run python Scripts/2024/2/day2.py Data/2024/2/input.txt

# 2022 scripts open a tkinter file dialog — pick the input file when the window appears
pixi run python Scripts/2023/0412_CleaningPairs.py
```

A few of the older files (`0612_signalsubrouter.py`, `Day09/0912_Rope.py`, the first cells of the 2024 notebooks) still contain absolute paths from my old Linux and macOS machines. Point them at your own input before running.

### Inputs

Puzzle inputs are **not committed**. Advent of Code inputs are generated per user and Eric Wastl asks that they not be redistributed, so `Data/` is local only. Log in at [adventofcode.com](https://adventofcode.com/) and save your own input as `Data/<year>/<day>/input.txt` to match what the notebooks expect.

## What I learned here

Roughly in the order it happened, since that is the point of keeping this repo:

- **Day 1, 2022** — files, loops, `int()`, and that `pandas` is not the answer to every problem.
- **Days 3–4** — sets. `issubset` and `&` turned two nested loops into one line, which was the first time the language felt like it was helping.
- **Day 5** — mutable state and why reversing a list in place will ruin your evening.
- **Day 6** — sliding windows, and writing a function twice before noticing it should take the window length as an argument.
- **Day 8** — `numpy` arrays and indexing a grid in four directions.
- **Day 9–10** — where 2022 stopped. Left unfinished on purpose.
- **2024** — type hints, docstrings, `sys.argv` instead of a file dialog, `re`, and small pure functions that are testable on the worked example before touching the real input.
- **2026** — `pixi` and a lockfile, so the whole thing is reproducible instead of dependent on whatever was on my `PATH` in 2022.

## Badges

The tools this repo has used across its life:

![Python Badge](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=fff&style=plastic) | <img src="https://img.shields.io/badge/Python-3.14-3776AB?logo=python&amp;logoColor=fff&amp;style=plastic" alt="Python"> | [![Pixi Badge](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/prefix-dev/pixi/main/assets/badge/v0.json)](https://pixi.sh) | ![Jupyter Badge](https://img.shields.io/badge/Jupyter-F37626?logo=jupyter&logoColor=fff&style=plastic) | ![NumPy Badge](https://img.shields.io/badge/NumPy-013243?logo=numpy&logoColor=fff&style=plastic) | ![pandas Badge](https://img.shields.io/badge/pandas-150458?logo=pandas&logoColor=fff&style=plastic) | <img src="https://img.shields.io/badge/Advent%20of%20Code-2022%20%7C%202024-0f0f23?logo=adventofcode&logoColor=fff&style=plastic" alt="Advent of Code"> |

## Authors and acknowledgment

* Suyash Naik: suyash.naik@ista.ac.at

Thanks to [@guptadivyansh](https://github.com/guptadivyansh) for sticking out the early days with me — the Day 5 commit message still says so. Thanks to Eric Wastl for building Advent of Code, which is a far better first project than any tutorial I tried.

## License

The solutions here are free to read, learn from, and reuse. Puzzle text and inputs belong to Advent of Code and are not redistributed in this repository.

## Project status

Reawakened but not abandoned — 2022 stopped at Day 9, 2024 stopped at Day 3, and I pick it back up when the mood strikes to learn and develop. 
