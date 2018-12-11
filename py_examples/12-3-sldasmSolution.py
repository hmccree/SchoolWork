from pathlib import Path

for file in Path(".").glob("*.1"):
    name, ext, _ = file.name.split(".")  # There were no other .'s in the names
    file.rename(f"{name}.sld{ext}")