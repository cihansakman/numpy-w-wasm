# Data Analysis with Numpy in WebAssembly

Simple implementation of data analysis in WebAssembly with Numpy for given file.


## Prerequisites
- `componentize-py` >= 0.15
- `wasmtime` >= 26.0
- `Numpy` and `regex` builts for wasi

## Get the wasi compiled pakcages from wasi-wheels or built them yourself
We can built our own regex package but Numpy fails since dsutils no longer supported with Python3.12.
I'll try to compile numpy locally to wasm-wasi compiled version using wasm-wasi compiled Cpython3.11
```
curl -OL https://github.com/dicej/wasi-wheels/releases/download/latest/numpy-wasi.tar.gz
curl -OL https://github.com/dicej/wasi-wheels/releases/download/latest/regex-wasi.tar.gz
tar xf numpy-wasi.tar.gz
tar xf regex-wasi.tar.gz
```

## Build and run the wasm module

```
componentize-py -d wit -w analyze-dataset componentize app -o analyze-dataset.wasm
wasmtime run --dir files/::files/ analyze-dataset.wasm files/medical_cost.csv
```
Ensure that you mount the appropriate host directory when running the module.