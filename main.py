import marimo

__generated_with = "0.18.3"
app = marimo.App()


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _(mo):
    mo.md("""
    # Hello from linalgebra!
    """)
    return


if __name__ == "__main__":
    app.run()
