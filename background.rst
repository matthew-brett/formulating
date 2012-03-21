##########
Background
##########

*******************
Multiple regression
*******************

A simple slope and intercept regression model can be written as:

.. math::
    :label: model

    y_i = \beta x_i + c + e_i

where $i$ indexes the observations $1..N$.  By replacing $c$ with a vector of
length $N$ containing ones, we can rewrite this model in matrix form:

(Which is the same as :eq:`model`:

.. math::

    Y = X B + E

where:

* $Y$ is a column vector containing $y_1 .. y_N$
* $X$ is a matrix shape (N, 2), where the first column is the vector $x_1 ..
  x_N$, and the second column is a vector of ones.
* $B$ is the parameter matrix, shape (2, 1), where $B_{11} = \beta$ (above), and
  $B_{21} = c$ (above).
* $E$ is the vector of errors $e_1 .. e_N$.

$X$ is the *design matrix*.  $B$ is the *beta* matrix.

So far we have a single regressor $x_1 .. x_N$.   Let us append another regressor
to the model, $z$, with values $z_1 .. z_N$

.. math::

    y_i = \beta_x x_i + \beta_z z_i + c + e_i

The corresponding design matrix $X$ now has three columns with the second
containng $z_1 ..  z_N$, the parameter matrix $B$ contains three entries
$[\beta_x, \beta_z, c]$.  This is obviously *multiple regression*.

*******************
The contrast matrix
*******************

We can do hypothesis testing by applying a *contrast vector* $C$ to the
parameter matrix. Let $C$ be a column vector.  We express our hypothesis with:

.. math::

    C^T B

For example, on the null hypothesis of no effect of regressor $x$, we would
expect $\beta_x$ (== $B_{11}$) not to differ from 0. With $C = [1, 0, 0]^T$,
$C^T B == B_{11} == \beta_x$.  Thus $C^T B$ results in a number (here $B_{11}$)
that we expect to be 0 on the null hypothesis.

Although this example is trivial, the contrast vector obviously allows us to
test more complicated things like the difference between the slopes for the
first and second regressor, with $C = [1, -1, 0]^T$.

**********************
Formulae and contrasts
**********************

In the examples above, it is very simple to go from the regressors in the formal
model:

.. math::

    y_i = \beta_x x_i + \beta_z z_i + c + e_i

to the columns in the design matrix, and thence to the contrast matrix we need
to test for our effects.  However, imagine a model with more regressors, and
where the regressors have handy names, say:

.. math::

    y_i = \beta_f f_i + \beta_g g_i + \beta_h h_i + \beta_k k_i + c + e_i

Quick, what's the contrast for the slope of $k$ greater than the slope for $g$?
You can work it out by running your finger over the model and counting where $k$
and $g$ are in the regressor order, and get, correctly, $C = [0, -1, 0, 1,
0]^T$. But, even with this small number of regressors, it's probably easy to see
this could get ugly and error prone.
