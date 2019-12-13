# point-gen
This library generates point sets for 3D shapes. The need for this project came about when I needed to verify some shape fitting functions, and I wrote a quick script to do so for a sphere. The library's only defined purpose is for generating test data, but if you'd like an additional purpose to be included, feel free to make a suggestion.

Currently the library only supports spheres, but the intention is to flesh this out to support all basic geometric shapes

The library is written in Python3 and is covered by unit tests. Help is welcome but please note that no pull requests will be accepted for new functionality without reasonable test coverage. 

To run all unit tests, at the root of the project run the following:

```bash
python -m unittest discover -v
```
