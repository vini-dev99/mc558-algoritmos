from pathlib import Path
import pytest, glob, subprocess

FIXTURES = Path(__file__).parent / "fixtures"
cases = []
for in_path in FIXTURES.glob("*.in"):
    out_path = in_path.with_suffix(".out")
    if out_path.exists():
        cases.append((in_path, out_path))

# use o stem (nome sem extensão) como id: arq01, arq02…
ids = [in_path.stem for in_path, _ in cases]

@pytest.mark.parametrize("in_path,out_path", cases, ids=ids)
def test_compara_saida(in_path: Path, out_path: Path):
    input_data = in_path.read_text()
    proc = subprocess.run(
        ["python3", "t4.py"],
        input=input_data, text=True,
        capture_output=True, check=True
    )
    expected = out_path.read_text()
    assert proc.stdout == expected
