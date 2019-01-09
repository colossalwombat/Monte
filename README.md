# Monte

This is a simple python script to execute Monte-Carlo integration on a user defined function in one variable (I will extend it to multivariable functions eventually). [Monte-Carlo Integration](https://en.wikipedia.org/wiki/Monte_Carlo_integration) is a probabilistic approach for numerically integrating a function. We can express this relationship as 

![equation](https://latex.codecogs.com/gif.latex?%5Cint_a%5Eb%20f%28x%29dx%20%5Capprox%20A%20%5Ccdot%20%5Cfrac%7B%5Ctext%7BSamples%20Under%20Curve%7D%7D%7B%5Ctext%7BTotal%20Samples%7D%7D)

where A is a bounding box around the curve. 