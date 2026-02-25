import subprocess
import time
import os
import shutil

# Configuration
TEX_FILE = "main.tex"
JOB_NAME = "main"
ITERATIONS = 1 # Number of times to repeat for stability (optional, keep 1 for speed)

# Define compilers/recipes to test
# Format: ("Name", "Clean Command", "Build Command")
# We use latexmk for standard engines as it handles bibtex etc automatically, mirroring LaTeX Workshop
RECIPES = [
    {
        "name": "latexmk (pdflatex)",
        "clean": ["latexmk", "-C"],
        "build": ["latexmk", "-pdf", "-interaction=nonstopmode", TEX_FILE]
    },
    {
        "name": "latexmk (xelatex)",
        "clean": ["latexmk", "-C"],
        "build": ["latexmk", "-xelatex", "-interaction=nonstopmode", TEX_FILE]
    },
    {
        "name": "latexmk (lualatex)",
        "clean": ["latexmk", "-C"],
        "build": ["latexmk", "-lualatex", "-interaction=nonstopmode", TEX_FILE]
    },
    {
        "name": "tectonic",
        "clean": [], # Tectonic manages its own cache, usually we just delete the PDF to be sure or pass --clean
        # Tectonic is a single run command, it behaves differently. 
        # We will manually clean auxiliary files if any exist, but tectonic keeps them in .tectonic usually or distinct.
        # Ideally we just remove main.pdf. 
        # Tectonic doesn't really have a 'clean' command like latexmk -C.
        "build": ["tectonic", TEX_FILE]
    }
]

def clean_aux_files():
    """Manual cleanup if needed."""
    exts = ['.aux', '.log', '.out', '.fdb_latexmk', '.fls', '.synctex.gz', '.toc', '.bbl', '.bcf', '.blg', '.run.xml', '.pdf']
    for ext in exts:
        f = JOB_NAME + ext
        if os.path.exists(f):
            try:
                os.remove(f)
            except OSError:
                pass

def check_command_exists(cmd_list):
    """Check if the executable exists."""
    from shutil import which
    return which(cmd_list[0]) is not None

def run_recipe(recipe):
    name = recipe["name"]
    clean_cmd = recipe.get("clean")
    build_cmd = recipe["build"]

    print(f"--- Benchmarking {name} ---")

    if not check_command_exists(build_cmd):
        print(f"Skipping {name}: Command '{build_cmd[0]}' not found.")
        return None

    # --- Fresh Start ---
    # Run clean command if it exists
    if clean_cmd:
        try:
            subprocess.run(clean_cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=False)
        except Exception:
            pass
    
    # Also manual clean to be safe
    clean_aux_files()

    start_time = time.time()
    try:
        # Capture output to suppress noise, check=True to raise error on failure
        proc = subprocess.run(build_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if proc.returncode != 0:
            print(f"Fresh Compilation Failed for {name}:")
            # print(proc.stdout.decode()[-500:]) # Print last bit of error
            # print(proc.stderr.decode()[-500:])
            return None
    except Exception as e:
        print(f"Error executing {name}: {e}")
        return None
    fresh_time = time.time() - start_time

    # --- Incremental Start ---
    # We do NOT clean commands here. We basically update the touch time of main.tex to force check?
    # Actually, latexmk checks changes. If we just run it again immediately, it might do nothing if no changes.
    # To simulate a 'change', we can touch the file.
    os.utime(TEX_FILE, None)
    
    start_time = time.time()
    try:
         proc = subprocess.run(build_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
         if proc.returncode != 0:
             print(f"Incremental Compilation Failed for {name}")
             return None
    except Exception as e:
        print(f"Error executing {name}: {e}")
        return None
    incremental_time = time.time() - start_time

    return (fresh_time, incremental_time)

def main():
    print("Starting Benchmark...")
    print(f"Target: {TEX_FILE}")
    print("-" * 60)
    print(f"{'Compiler':<25} | {'Fresh (s)':<10} | {'Incremental (s)':<15}")
    print("-" * 60)

    results = []

    for recipe in RECIPES:
        res = run_recipe(recipe)
        if res:
            fresh, inc = res
            print(f"{recipe['name']:<25} | {fresh:<10.2f} | {inc:<15.2f}")
            results.append((recipe['name'], fresh, inc))
        else:
            print(f"{recipe['name']:<25} | {'N/A':<10} | {'N/A':<15}")

    print("-" * 60)
    print("Benchmark Complete.")
    
    if results:
        best_fresh = min(results, key=lambda x: x[1])
        best_inc = min(results, key=lambda x: x[2])
        print(f"\nFastest Fresh Build:       {best_fresh[0]} ({best_fresh[1]:.2f}s)")
        print(f"Fastest Incremental Build: {best_inc[0]} ({best_inc[2]:.2f}s)")

if __name__ == "__main__":
    main()
