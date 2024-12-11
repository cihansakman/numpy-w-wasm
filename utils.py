import numpy as np
import re
import sys


def load_data(file_path):
    print(f'Reading {file_path}...')
    # Load data 
    data = np.genfromtxt(
        file_path, delimiter=",", dtype=None, names=True, encoding="utf-8", missing_values=""
    )
    return data

#identify column types and perform analysis
def analyze_data(data):
    #separate columns by type
    column_names = data.dtype.names
    report = {}

    #regex  to identify columns like id
    index_column_pattern = re.compile(r"(?i)^id$")  #match id case-insensitive

    for col in column_names:
        #skip columns matching the regex
        if index_column_pattern.search(col):
            print(f"Index column detected: '{col}' - Not processed.")
            continue

        col_data = data[col]
        if np.issubdtype(col_data.dtype, np.number):
            report[col] = {
                "mean": np.nanmean(col_data),
                "min": np.nanmin(col_data),
                "max": np.nanmax(col_data),
                "std_dev": np.nanstd(col_data),
            }
        else:
            unique_values, counts = np.unique(col_data, return_counts=True)
            report[col] = {
                "unique_values": unique_values.tolist(),
                "counts": counts.tolist(),
            }
    return report


def help_message():
        print("""
=================================================================================
                    WebAssembly File Analysis Tool with Numpy
=================================================================================

    This tool is a WebAssembly (Wasm) module designed to analyze datasets 
    provided as input files. Due to the sandboxed nature of Wasm, explicit 
    permissions are required to access files on the host system.

    Ensure that you mount the appropriate host directory when running the module 
    using a Wasm runtime like Wasmtime.

    Example Usage with Wasmtime:
    --------------------------------
    $ wasmtime run --dir <HOST_DIR[::GUEST_DIR]> <wasm-module> <GUEST_DIR/file_path>
    
    Where:
        [HOSTPATH]  : Path to the host directory containing the file.
        [GUESTPATH] : Path where the directory is mounted inside the Wasm runtime.

    Example:
    $ wasmtime run --dir /home/user/datasets::/data analyze-dataset.wasm data/file.csv

    Usage:
    --------------------------------
    $ analyze-dataset <file-path>

    Arguments:
        <file-path> : Path to the file to be analyzed (relative to the Wasm sandbox).

=================================================================================
    """, file=sys.stderr)