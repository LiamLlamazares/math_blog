---
layout: post
title: The Ornstein-Uhlenbeck Semigroup
subtitle: Part 7 of the series on Malliavin calculus
thumbnail-img: /assets/img/Malliavin.jpg
share-img: /assets/img/Malliavin.jpg
tags: [Malliavin calculus, Semigroups]
authorpost: L.Llamazares
---
#  Three line summary

-   There is a natural extension of the Laplacian to the Wiener space.

-   The generator of the Laplacian is the Ornstein-Uhlenbeck semigroup.

-   The Ornstein-Uhlenbeck semigroup in finite dimensions is the
    generator of the Ornstein-Uhlenbeck process, from which it derives
    its name.
    # The Laplacian of a random variable

    First, we give some finite-dimensional motivation. Suppose that
    $f\in C\U c^\infty({\mathbb R}^d\to{\mathbb R}^d)$ and
    $g\in C\U c^\infty({\mathbb R}^d)$. Then an integration by parts shows
    that the adjoint of the gradient in $L^2({\mathbb R}^d)$ is minus the
    divergence. That is,


    <div>
     $$\int\U \mathbb{R}^df(x) \cdot \nabla g(x) dx=-\int\U \mathbb{R}^d\nabla\cdot  f(x) \nabla g(x) dx.$$
    </div>


    Then, we define the Laplacian as minus the adjoint of the gradient
    $\nabla$ composed with the gradient


    <div>
     $$\Delta := -\nabla^\circ \nabla .$$
    </div>

      Which gives the familiar


    <div>
     $$\Delta\U \mathbb{R}^d =\nabla\cdot \nabla=\partial\U 1^2+\ldots\partial \U d^2.$$
    </div>
