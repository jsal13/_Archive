# Advent of Code 2021

**TL;DR**: These are my attempts at [AoC2021](https://adventofcode.com/2021).  

I wanted to make this repo I could share to give an idea of my coding style and quality in **Python**, so in lieu of "quick" solutions I opted for **readable, tested, reasonably-organized** code over cleverness.  

(This quality varies by degrees, depending on the day, of course!)

<hr/>


## Project Structure

It's a small project:

```
aoc/        Contains project modules.
├─ data/    Contains input data.
docs/       Contains documentation.
```

<hr/>

## Things I Focused On


I like clean code.  I like linting.  I like formatting.  I like type-hints.  In line with this, I did my best at the following:

- Linting + Formatting Code (**[Black](https://github.com/psf/black), [Pylint](https://pylint.org/)**)
- [Type-Hinting](https://docs.python.org/3/library/typing.html) (**[Mypy](https://mypy.readthedocs.io/en/stable/), [Pydantic](https://pydantic-docs.helpmanual.io/)**)
- Documenting Methods + Generating Documentation (**[Numpy Style](https://numpydoc.readthedocs.io/en/latest/format.html)** when verbosely documenting, **[Sphinx](https://www.sphinx-doc.org/en/master/)** for generating docs)
- Associated requirements for use in venv

<hr/>

## Things I Can Still Improve On

- [ ] Better documentation of methods w/ examples.
- [ ] Better documentation of the problem we're trying to solve.
- [ ] Unittests in the earlier problems.

<hr/>

## Things to Note

Here's some weird stuff you might see and wonder why I did it.

- This isn't a package, and I didn't want to make it a package since it's not a cohesive unit.  Therefore, **unit-tests were done in the same module as the problem** instead of in their own files in a separate folder.
- Data is included for reproduction purposes.
- I worked on Windows, so `make_docs.ps1` is a Powershell script to re-make the documentation.