from typer.testing import CliRunner

from tlylt.scripts.cli import app

runner = CliRunner()

def test_me():
    result = runner.invoke(app, ["me"])
    assert result.exit_code == 0
    assert "Hi!" in result.output
    assert "Welcome to tlylt utility scripts!" in result.output