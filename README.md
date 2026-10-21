# AI Code Evaluation Benchmark

## Project Overview

The AI Code Evaluation Benchmark is a self-directed Python portfolio project designed to evaluate AI-generated programming answers against explicit requirements, reference solutions, and automated test cases.

The project focuses on correctness, edge-case handling, code clarity, reasoning quality, and instruction following.

## Objectives

- Create programming questions with clear specifications.
- Implement reference solutions.
- Develop automated test cases.
- Prepare deliberately incorrect or incomplete candidate answers.
- Build a repeatable evaluation system.
- Define a transparent scoring rubric.
- Generate a report analyzing evaluation results.

## Technologies

- Python
- Git and GitHub
- Python's built-in unittest framework
- JSON
- Markdown

## Project Structure

- `benchmark/` — Reference solutions, candidate answers, test cases, and evaluation logic.
- `tests/` — Automated tests.
- `data/` — Candidate answers and evaluation data.
- `reports/` — Results and analysis.
- `QUESTIONS.md` — Programming question specifications.
- `RUBRIC.md` — Evaluation criteria and scoring rules.
- `run_benchmark.py` — Main benchmark execution script.

## Evaluation Methodology

Each programming question will have a defined specification, a reference solution, and automated test cases.

Candidate answers will be evaluated using automated tests. Clarity, reasoning, and instruction following will be assessed separately using a documented rubric.

The final report will summarize results, identify common failure patterns, and discuss limitations.

## Project Status

Day 1: Repository setup and initial documentation.

## Disclosure

This is a self-directed learning and portfolio project. It is not professional client work, and its results should not be interpreted as an industry-standard assessment of AI systems.

## Limitations

The initial benchmark will contain a small number of programming questions. Its results will depend on the selected questions, test cases, and evaluation criteria.

Passing the benchmark tests does not guarantee correctness for every possible input or establish that one AI model is generally better than another.

## Future Improvements

- Expand the programming question set.
- Add additional edge cases and randomized tests.
- Compare AI-generated answers under consistent conditions.
- Improve evaluation reproducibility.
- Extend the reporting system.