---
layout: post
title: The Malliavin Derivative 2
subtitle: Part 4 of the series on Malliavin calculus
thumbnail-img: /assets/img/Malliavin.jpg
share-img: /assets/img/Malliavin.jpg
tags: [Malliavin derivative, Chaos Expansion]
authorpost: B. Summers
---
# Foreword by Liam
This is the first post of Billy on the blog. Not only did he provide the reading group with an excellent presentation, but he also typed up some wonderful notes which he is very graciously sharing today. Round of applause for Billy please! 

# The Malliavin derivative as a Fréchet derivative
Let $C\U 0(\zl 0, T\zr )$ be the Banach space of all
continuous functions $f \colon \zl 0,
        T\zr  \to \mathbb{R}$ such that $f(0) = 0$. On this space, we can
associate a special Borel probability measure $\mu$ such that
$W\U t(\omega) := \omega(t)$ is a Brownian motion. Given a random variable
on $C\U 0(\zl 0, T\zr )$, i.e. a $\mu$-measurable function
$X \colon C\U 0(\zl 0, T\zr ) \to \mathbb{R}$, we want to know how the value
$X(\omega)$ changes upon perturbing the path $\omega$ by a small
quantity $\gamma \in C\U 0(\zl 0, T\zr )$. This can be described by the [Fréchet
derivative](https://en.wikipedia.org/wiki/Fr%C3%A9chet_derivative) $\nabla{X}(\omega)$, which is a bounded linear map
$C\U 0(\zl 0, T\zr ) \to
    \mathbb{R}$, i.e. a member of the dual space $C\U 0(\zl 0, T\zr )^\star $, giving
the best linear approximation to the difference
$X(\omega + \gamma) - X(\omega)$. Formally, $\nabla{X}$ satisfies


<div>
 $$X(\omega + \gamma)
    = X(\omega)
    + \left\langle{\nabla{X}(\omega), \gamma}\right\rangle
    + \mathrm{o}(\norm{\gamma}\U {C\U 0(\zl 0, T\zr )}).$$
</div>

  If $X$ has a Fréchet
derivative $\nabla{X} \colon C\U 0(\zl 0, T\zr ) \to C\U 0(\zl 0,
            T\zr )^\star $, we say it is Fréchet differentiable.

Within the Banach space $C\U 0(\zl 0, T\zr )$ lies a Hilbert space $H$ of
distinguished elements. This is the space of paths of the form


<div>
 $$\gamma(t) = \int\U 0^t \psi(s) \, \mathop{}\!\mathrm{d}{s}$$
</div>

  for some
$\psi \in L^2(\zl 0, T\zr )$. In other words, it is the space of [$W^{1, 2}$
functions](https://en.wikipedia.org/wiki/Sobolev_space#One-dimensional_case:~:text=%5Bedit%5D-,One%2Ddimensional%20case,-%5Bedit%5D) on $\zl 0, T\zr $ starting at 0. Its inner product is given by


<div>
 $$(\gamma\U 1, \gamma\U 2)\U H = (\dot{\gamma}\U 1, \dot{\gamma}\U 2)\U {L^2(\zl 0, T\zr )}.$$
</div>


$H$ is continuously imbedded in $C\U 0$ by the theory of Sobolev spaces.
We call $H$ the Cameron-Martin space. It acts in some sense as the
heart of $C\U 0(\zl 0, T\zr )$ with the probability measure $\mu$, with its
elements having better analytical properties compared to a general
element in $C\U 0(\zl 0, T\zr )$. Ideally, we could restrict $\mu$ to this space
and only work here, but unfortunately $\mu$ is not a measure on $H$ (in
particular, it is not $\sigma$-additive), forcing us to work in a larger
Banach space.

Returning to our Fréchet differentiable random variable $X$, given some
path $\omega \in C\U 0(\zl 0, T\zr )$, we consider the restriction of its
derivative at $\omega$ to $H$, namely ${\nabla{X}(\omega)}|\U H$.
Since $H$ is continously imbedded in $C\U 0$, this restriction is an
element of $H^\star $. Then, as $H$ is a Hilbert space, the dual space $H^\star $
is isomorphic to $H$ through its inner product, so there exists some
$DX(\omega) \in L^2(\zl 0, T\zr )$ such that


<div>
 $$\left\langle{\nabla{X}(\omega), \int\U 0^\cdot \psi \, \mathop{}\!\mathrm{d}{t}}\right\rangle
    = \left({\int\U 0^\cdot D\U t{X}(\omega) \, \mathop{}\!\mathrm{d}{t},
    \int\U 0^\cdot \psi \, \mathop{}\!\mathrm{d}{t}}\right)\U H
    = \int\U 0^T D\U t{X}(\omega) \psi(t) \, \mathop{}\!\mathrm{d}{t}.$$
</div>


This object $DX$ is precisely the Malliavin derivative of $X$.

# The Skorokhod integral and the Malliavin derivative

Given a stochastic process
$(X\U t)\U {t \in \zl 0, T\zr } \in L^2(\zl 0,T\zr \times\Omega,
    \mathop{}\!\mathrm{d}{t}\otimes\mathbb{P})$ such that $X\U t$ is
$\mathscr{F}\U T$-measurable for all $t \in
    \zl 0, T\zr $, let

<div>
 $$X\U t = \sum\U {n = 0}^\infty I\U n(f\U n(\cdot, t))$$
</div>

  be its
chaos expansion for some $f\U n \in L^2(\zl 0, T\zr ^{n + 1})$ symmetric in the
first $n$ variables. Recall we say $X$ is Skorokhod integrable, and
define its Skorokhod integral by


<div>
 $$\int\U 0^T X\U t \, \delta{W}\U t := \sum\U {n = 0}^\infty I\U {n + 1}({f}\U {n,S}),$$
</div>


whenever this sum converges in $L^2(\Omega)$. The following result is
fundamental.


**Theorem 1**. The Skorokhod integral and Malliavin derivative are
adjoint in the following sense:

Let $(X\U t)\U {t \in \zl 0, T\zr }$ be a Skorokhod-integrable. Let
$Y \in \mathbb{D}^{1,
            2}$ be a Malliavin differentiable random variable. Then


<div>
 $$\left({
            Y, \int\U 0^T X\U t \, \delta{W}\U t
        }\right)\U {L^2(\Omega)}
        = \left({
            D{Y}, X
        }\right)\U {L^2(\zl 0,T\zr \times\Omega)}.$$
</div>

  More concretely,


<div>
 $$\mathbb{E}\left[{
            Y \int\U 0^T X\U t \, \delta{W}\U t
        }\right]
        = \mathbb{E}\left[{
            \int\U 0^T
            D\U t Y X\U t
            \, \mathop{}\!\mathrm{d}{t}
        }\right].$$
</div>





Proof. As usual, we apply the definitions in terms of the chaos
expansions. Let

<div>
 $$X\U t = \sum\U {n = 0}^\infty I\U n(f\U n(\cdot, t))$$
</div>

  be the
chaos expansion of $X$, and

<div>
 $$Y = \sum\U {n = 0}^\infty I\U n(g\U n)$$
</div>

  the
chaos expansion of $Y$. Then

<div>
 $$\begin{aligned}
        \mathbb{E}\left[{
            Y \int\U 0^T X\U t \, \delta{W}\U t
        }\right]
         & = \mathbb{E}\left[{
            \sum\U {n = 0}^\infty I\U n(g\U n)
            \sum\U {m = 0}^\infty I\U {m + 1}({f}\U {m,S})
        }\right]                                                                 \\
         & = \sum\U {n = 0}^\infty \sum\U {m = 0}^\infty
        \mathbb{E}\zl I\U n(g\U n) I\U {m + 1}({f}\U {m,S})\zr                                \\
         & = \sum\U {n = 0}^\infty n! (g\U n, {f}\U {n - 1,S})\U {L^2(\zl 0, T\zr ^n)},
    \end{aligned}$$
</div>

  and on the other side,

<div>
 $$\begin{aligned}
        \mathbb{E}\left[{
        \int\U 0^T D\U t{Y} X\U t \, \mathop{}\!\mathrm{d}{t}
        }\right]
         & = \int\U 0^T \mathbb{E}\left[{
            \sum\U {n = 1}^\infty n I\U {n - 1}(g\U n(\cdot, t))
            \sum\U {m = 0}^\infty I\U m(f\U m(\cdot, t))
        } \, \mathop{}\!\mathrm{d}{t}\right]                                            \\
         & = \int\U 0^T \sum\U {n = 0}^\infty \sum\U {m = 0}^\infty
        n \mathbb{E}\left[{
            I\U {n - 1}(g\U n(\cdot, t)) I\U m(f\U m(\cdot, t))
        }\right]  \, \mathop{}\!\mathrm{d}{t}                                           \\
         & = \sum\U {n = 0}^\infty
        n (n - 1)! \int\U 0^T
        (g\U n(\cdot, t), f\U {n - 1}(\cdot, t))\U {L^2(\zl 0, T\zr ^{n - 1})}
        \, \mathop{}\!\mathrm{d}{t}                                              \\
         & = \sum\U {n = 0}^\infty
        n! (g\U n, f\U {n - 1})\U {L^2(\zl 0, T\zr ^n)}.
    \end{aligned}$$
</div>

  Finally, by definition of the symmetrization,


<div>
 $$\begin{aligned}
        (g\U n, f\U {n - 1,S})\U {L^2(\zl 0, T\zr ^n)}
         & = \int\U {\zl 0, T\zr ^n}
        g\U n(t\U 1, \dots, t\U n)
        \frac{1}{n} \sum\U {k = 1}^n
        f(t\U 1, \dots, t\U {k - 1}, t\U n, t\U {k + 1}, \dots, t\U {n - 1}, t\U k)
        \, \mathop{}\!\mathrm{d}{t\U 1} \cdots \mathop{}\!\mathrm{d}{t\U n}                       \\
         & = \frac{1}{n} \sum\U {k = 0}^n \int\U {\zl 0, T\zr ^n}
        g\U n(t\U 1, \dots, t\U n)
        f\U {n - 1}(t\U 1, \dots, t\U n)
        \, \mathop{}\!\mathrm{d}{t\U 1} \cdots \mathop{}\!\mathrm{d}{t\U n}                       \\
         & = (g\U n, f\U {n - 1})\U {L^2(\zl 0, T\zr ^n)},
    \end{aligned}$$
</div>

  where we change variables
$t\U k \mapsto t\U n, t\U n \mapsto t\U k$, use the property that $g\U n$ is
symmetric, and apply Fubini's theorem. ◻



**Remark 2**. The symbol $\delta$ is often used for a divergence-like
operator in Hodge theory. The analogy with our case is that in the Hodge
situation, $\delta$ is defined via a duality formula which looks like
$\left\langle{d{\alpha},
            \beta}\right\rangle = \left\langle{\alpha, \delta{\beta}}\right\rangle$, where $d$ is the
exterior derivative on differential forms. Indeed, even in vector
calculus, the negative of the divergence is in some sense adjoint to the
gradient:


<div>
 $$\int\U \Omega \mathop{\mathrm{div}}{f} \phi \, \mathop{}\!\mathrm{d}{x}
        = - \int\U \Omega f \cdot \nabla{\phi} \, \mathop{}\!\mathrm{d}{x}$$
</div>


whenever $\phi$ has zero boundary. So, in a sense, the Skorokhod
integral is just a divergence operator.


Using this, we can immediately prove the following:

**Corollary 3**. Let $(X^n)\U {n \in \mathbb{N}}$ be a sequence of
Skorokhod-integrable stochastic processes. Suppose there exist
$X \in L^2(\zl 0,T\zr \times\Omega)$ and $Y
        \in L^2(\Omega)$ such that $X^N \to X$ in
$L^2(\zl 0,T\zr \times\Omega)$, and $\delta{X^N} \to Y$ in $L^2(\Omega)$. Then
$X$ is Skorokhod integrable, and $\delta{X^N} \to \delta{X}$.



Proof. Recall that Skorokhod integrability of $X$ can be expressed in
terms of convergence of the series

<div>
 $$\sum\U {n = 0}^\infty(n + 1)! \|{f}\U {n,S}\|\U {L^2(\zl 0, T\zr ^{n + 1})}^2,
        $$
</div>
where
$f\U n(\cdot, t)$ are the components of the chaos expansion of $X$. Since
$X^N \to X$ strongly in $L^2$, and each $X^N$ is Skorokohod integrable,
the components of their chaos expansions must satisfy the above
condition, and we can take limits.

Let $Z \in \mathbb{D}^{1, 2}$. Then by adjointness,


<div>
$$(Z, \delta{X^N})\U {L^2(\Omega)}
      = (DZ, X^N)\U {L^2(\zl 0,T\zr \times\Omega)}.$$
</div>

Taking limits on both
sides and using adjointness on the limiting objects gives us


<div>
$$(Z, Y)\U {L^2(\Omega)}
      = (DZ, X)\U {L^2(\zl 0,T\zr \times\Omega)}
      = (Z, \delta{X})\U {L^2(\Omega)}.$$
</div>

Then, since
$\mathbb{D}^{1, 2}$ is dense in $L^2(\Omega)$, we see that $Y =
      \delta{X}$ a.s., as required. ◻



**Remark 4**. Perhaps a more intuitive way to say the Skorokhod integral
is "closable" in the book's words is that it is sequentially continuous
as a map $D(\delta) \subseteq L^2(\zl 0,T\zr \times\Omega) \to L^2(\Omega)$
with respect to the strong $L^2$ topology in its domain and weak $L^2$
topology in its codomain.



**Theorem 5**. Let $X \in L^2(\zl 0,T\zr \times\Omega)$ be a Skorokhod
integrable random process, and let $Y \in \mathbb{D}^{1, 2}$ be such
that $FX$ is also Skorokhod integrable. Then


<div>
$$Y \int\U 0^T X\U t \, \delta{W}\U t
      = \int\U 0^T Y X\U t \, \delta{W}\U t + \int\U 0^T D\U t Y X\U t \, \mathop{}\!\mathrm{d}{t}$$
</div>


almost surely.



Proof. Suppose $Y$ has finite chaos expansion, and choose some
$Z \in \mathbb{D}^{1, 2}$ also with finite chaos expansion. Then by
adjointness and the product rule,

<div>
$$\begin{aligned}
      \mathbb{E}\left[{
          Z \int\U 0^T Y X\U t \, \delta{W}\U t
      }\right]
       & = \mathbb{E}\left[{
      \int\U 0^T D\U t{Z} Y X\U t \, \mathop{}\!\mathrm{d}{t}
      }\right]                     \\
       & = \mathbb{E}\left[{
      \int\U 0^T (D\U t(YZ) - Z D\U t{Y}) X\U t \, \mathop{}\!\mathrm{d}{t}
      }\right]                     \\
       & = \mathbb{E}\left[{
          YZ \int\U 0^T X\U t \, \delta{W}\U t
      }\right]  - \mathbb{E}\left[{
      Z \int\U 0^T D\U t{Y} X\U t \, \mathop{}\!\mathrm{d}{t}
      }\right] .
  \end{aligned}$$
</div>

Since the set of all test functions
$Z \in \mathbb{D}^{1, 2}$ with finite chaos expansion is dense in
$L^2(\Omega)$, we conclude the result for $Y$ with finite chaos
expansion. For general $Y$, we approximate. ◻



**Remark 6**. A similar formula crops up in vector calculus, namely the
following:


<div>
 $$\mathop{\mathrm{div}}(fX) = \nabla{f} \cdot X + f \mathop{\mathrm{div}}{X},$$
</div>


where $f$ is a scalar function and $X$ a vector field. Again, in the
above theorem, the Malliavin derivative takes the place of the gradient,
the Skorokhod integral take the place of the divergence, and the usual
inner product on $\mathbb{R}^n$ (the dot product) is replaced with the
$L^2(\zl 0, T\zr )$ inner product. There is a sign difference owing to the
fact the adjointness in the Malliavin case does not induce a sign
change, unlike in the vector calculus case (see the remark above).



**Theorem 7**. Let $X \in L^2(\zl 0,T\zr \times\Omega)$ be a stochastic
process such that for all $s \in \zl 0, T\zr $, $X\U s$ is in
$\mathbb{D}^{1, 2}$, $D{X\U s}$ is Skorokhod integrable, and


<div>
 $$\int\U 0^T DX\U s \, \delta{W}\U s \in L^2(\zl 0,T\zr \times\Omega).$$
</div>

  Then
$\delta{X}$ lies in $\mathbb{D}^{1, 2}$, and


<div>
 $$D\U t(\delta{X}) = \int\U 0^T D\U t{X\U s} \, \delta{W}\U s + X\U t.$$
</div>




**Remark 8**. The technical constraints in the theorem above are an
unfortunate consequence of the fact the Skorokhod and Malliavin
operators $\delta$ and $D$ are not defined on the full space
$L^2(\zl 0,T\zr \times\Omega)$ and $L^2(\Omega)$ respectively - we have to
ensure an operator throws us to the right spot before we can consider
applying the other one.

Note that this theorem is simply an expression of the Malliavin
derivative and Skorokhod integral's failure to commute, with the error
simply being the identity on $L^2(\Omega \times \zl 0, 1\zr )$. That is,


<div>
 $$D\delta = \delta D + \mathop{\mathrm{id}}.$$
</div>

  This contrasts with our
vector calculus analogy, where the divergence and gradient most
certainly commute (assuming enough regularity).

A pdf of version of this page is provided below:
<object data="/assets/part4.pdf" width="1000" height="1000" type='application/pdf'></object>
