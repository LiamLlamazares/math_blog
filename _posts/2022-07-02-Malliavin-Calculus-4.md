---
layout: post
title: The Malliavin Derivative 2
subtitle: Part 4 of the series on Malliavin calculus
thumbnail-img: /assets/img/Malliavin.jpg
share-img: /assets/img/Malliavin.jpg
tags: [Malliavin derivative, Chaos Expansion]
authorpost: B. Summers
---

# The Malliavin derivative as a Fréchet derivative

Let $C\U 0(\zl 0, T\zr )$ be the Banach space of all
continuous functions $f \colon \zl 0,
        T\zr  \to \mathbb{R}$ such that $f(0) = 0$. On this space, we can
associate a special Borel probability measure $\mu$ such that
$W\U t(\omega) := \omega(t)$ is a Brownian motion. Given a random variable
on $C\U 0(\zl 0, T\zr )$, i.e. a $\mu$-measurable function
$X \colon C\U 0(\zl 0, T\zr ) \to \mathbb{R}$, we want to know how the value
$X(\omega)$ changes upon perturbing the path $\omega$ by a small
quantity $\gamma \in C\U 0(\zl 0, T\zr )$. This can be described by the Fréchet
derivative $\nabla{X}(\omega)$, which is a bounded linear map
$C\U 0(\zl 0, T\zr ) \to
    \mathbb{R}$, i.e. a member of the dual space $C\U 0(\zl 0, T\zr )^$, giving
the best linear approximation to the difference
$X(\omega + \gamma) - X(\omega)$. Formally, $\nabla{X}$ satisfies


<div>
 $$X(\omega + \gamma)
    = X(\omega)
    + \angles{\nabla{X}(\omega), \gamma}
    + \mathrm{o}(\norm{\gamma}\U {C\U 0(\zl 0, T\zr )}).$$
</div>

  If $X$ has a Fréchet
derivative $\nabla{X} \colon C\U 0(\zl 0, T\zr ) \to C\U 0(\zl 0,
            T\zr )^$, we say it is Fréchet differentiable.

Within the Banach space $C\U 0(\zl 0, T\zr )$ lies a Hilbert space $H$ of
distinguished elements. This is the space of paths of the form


<div>
 $$\gamma(t) = \int\U 0^t \psi(s) \, \mathop{}\!\mathrm{d}{s}$$
</div>

  for some
$\psi \in L^2(\zl 0, T\zr )$. In other words, it is the space of $W^{1, 2}$
functions on $\zl 0, T\zr $ starting at 0. Its inner product is given by


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
derivative at $\omega$ to $H$, namely $\eval{\nabla{X}(\omega)}\U H$.
Since $H$ is continously imbedded in $C\U 0$, this restriction is an
element of $H^$. Then, as $H$ is a Hilbert space, the dual space $H^$
is isomorphic to $H$ through its inner product, so there exists some
$DX(\omega) \in L^2(\zl 0, T\zr )$ such that


<div>
 $$\angles{\nabla{X}(\omega), \int\U 0^\cdot \psi \, \mathop{}\!\mathrm{d}{t}}
    = \parens{\int\U 0^\cdot D\U t{X}(\omega) \, \mathop{}\!\mathrm{d}{t},
    \int\U 0^\cdot \psi \, \mathop{}\!\mathrm{d}{t}}\U H
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
 $$\parens{
            Y, \int\U 0^T X\U t \, \delta{W}\U t
        }\U {L^2(\Omega)}
        = \parens{
            D{Y}, X
        }\U {L^2(\zl 0,T\zr \times\Omega)}.$$
</div>

  More concretely,


<div>
 $$\mathbb{E}\brackets{
            Y \int\U 0^T X\U t \, \delta{W}\U t
        }
        = \mathbb{E}\brackets{
            \int\U 0^T
            D\U t Y X\U t
            \, \mathop{}\!\mathrm{d}{t}
        }.$$
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
        \mathbb{E}\brackets{
            Y \int\U 0^T X\U t \, \delta{W}\U t
        }
         & = \mathbb{E}\brackets{
            \sum\U {n = 0}^\infty I\U n(g\U n)
            \sum\U {m = 0}^\infty I\U {m + 1}({f}\U {m,S})
        }                                                                 \\
         & = \sum\U {n = 0}^\infty \sum\U {m = 0}^\infty
        \mathbb{E}\zl I\U n(g\U n) I\U {m + 1}({f}\U {m,S})\zr                                \\
         & = \sum\U {n = 0}^\infty n! (g\U n, {f}\U {n - 1,S})\U {L^2(\zl 0, T\zr ^n)},
    \end{aligned}$$
</div>

  and on the other side,

<div>
 $$\begin{aligned}
        \mathbb{E}\brackets{
        \int\U 0^T D\U t{Y} X\U t \, \mathop{}\!\mathrm{d}{t}
        }
         & = \int\U 0^T \mathbb{E}\brackets{
            \sum\U {n = 1}^\infty n I\U {n - 1}(g\U n(\cdot, t))
            \sum\U {m = 0}^\infty I\U m(f\U m(\cdot, t))
        } \, \mathop{}\!\mathrm{d}{t}                                            \\
         & = \int\U 0^T \sum\U {n = 0}^\infty \sum\U {m = 0}^\infty
        n \mathbb{E}\brackets{
            I\U {n - 1}(g\U n(\cdot, t)) I\U m(f\U m(\cdot, t))
        } \, \mathop{}\!\mathrm{d}{t}                                            \\
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


 remark
**Remark 2**. The symbol $\delta$ is often used for a divergence-like
operator in Hodge theory. The analogy with our case is that in the Hodge
situation, $\delta$ is defined via a duality formula which looks like
$\angles{d{\alpha},
            \beta} = \angles{\alpha, \delta{\beta}}$, where $d$ is the
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
 $$\sum\U {n = 0}^\infty
        (n + 1)! \norm{{f}\U {n,S}}\U {L^2(\zl 0, T\zr ^{n + 1})}^2,$$
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





# Why should I care?

The Malliavin derivative is (somewhat unsurprisingly) a fundamental
object of Malliavin calculus and has many applications in finance,
numerical methods, and optimal control.

# Notation

The same as in previous posts. Furthermore we will shorten the notation
$L^2(\Omega,\mathcal{F}\U T)$ and
$L^2(I\times\Omega,\mathcal{B}(I)\otimes \mathcal{F}\U T)$ to
$L^2(\Omega)$ and $L^2(I\times\Omega)$ respectively.

# Introduction

The Malliavin derivative was originally introduced as an operator
associated with the Fréchet differential of random variables
$X: C(I)\to {\mathbb R}$. The aforementioned construction provides some
motivation behind the Malliavin derivative and will be developed in the
next post. However, a more general construction can be obtained via the
chaos expansion.


**Definition 1**. Given $X=\sum\U {n=0}^{\infty} I\U n(f\U n)\in L^2(\Omega)$
we say that $X$ is Malliavin differentiable if


<div>
 $$\|X\|\U {\mathbb{D}\U {1,2}}:=\sum\U {n=1}^{\infty} n n!\|f\U {n}\|\U {L^2(\zl 0,T\zr ^n)}<\infty,$$
</div>


and denote the space of Malliavin differentiable functions by


<div>
 $$\mathbb{D}\U {1,2}:=\{X\in L^2(\Omega):\|X\|\U {\mathbb{D}\U {1,2}}<\infty\}.$$
</div>


Furthermore, we define the Malliavin derivative of $X$ as


<div>
 $$D\U tX:=\sum\U {n=1}^{\infty} n I\U {n-1}(f\U {n}(\cdot ,t)),$$
</div>




The first questions to be asked is: "what kind of object is the
Malliavin derivative of a random variable? What is the link between
$\mathbb{D}\U {1,2}$ and $D\U t$? Is $\|\cdot \|\U {\mathbb{D}\U {1,2}}$ even a
norm?" We answer this in the next proposition and corollary.


**Proposition 1**. The Malliavin derivative is well defined on
$\mathbb{D}\U {1,2}$ and establishes a linear isometry

<div>
 $$\begin{aligned}
        D: (\mathbb{D}\U {1,2},\|\cdot \|\U {\mathbb{D}\U {1,2}}) & \longrightarrow L^2(I\times\Omega,\|\cdot \|\U {L^2(I\times\Omega)}) \\
        X                                                   & \longmapsto D  X
        .\end{aligned}$$
</div>





Proof. The proof of the first part of the proposition is a
straightforward application of Itô's $n$-th isometry and the monotone
convergence theorem as we have that

<div>
 $$\begin{gathered}
        \|D  X\|^2\U {L^2(I\times\Omega)}=\int\U {I}\|\sum\U {n=1}^{\infty} n I\U {n-1}(f\U {n}(\cdot ,t))\|\U {L^2(\Omega)}^2 d t\\=\sum\U {n=1}^{\infty} n^2(n-1)!\int\U {I}\|f\U n(\cdot ,t)\| dt=\sum\U {n=1}^{\infty} n n!\|f\U {n}\|\U {L^2(\zl 0,T\zr ^n)}=\norm{X}\U {\mathbb{D}\U {1,2}}.
    \end{gathered}$$
</div>

  Finally, the linearity of $D$ follows from the
linearity of the iterated Itô integrals (which itself is a consequence
of the linearity of the Itô integral). ◻


In summary, the Malliavin derivative turns a square-integrable random
variable into a possibly non-adapted, stochastic process. You may recall
from our previous posts that we had an operator that went in the
opposite direction. The Skorohod integral $\delta$. In fact, the
Malliavin derivative and the Skorohod integral are adjoint operators in
a sense that will be made precise in the next post. For now, we show
that, as occurs with the ordinary derivative, a random variable has
Malliavin derivative $0$ if and only if it is constant.


**Corollary 1**. $(\mathbb{D}\U {1,2},\|\cdot \|\U {\mathbb{D}\U {1,2}})$ is
a seminormed space. Furthermore


<div>
 $$\|X\|\U {\mathbb{D}\U {1,2}}=0 \iff D\U tX=0\iff X\in {\mathbb R}.$$
</div>





Proof. The triangle inequality and the absolute homogeneity are direct
consequences of the isometry of the previous proposition. This shows
that $\|\cdot \|\U {\mathbb{D}\U {1,2}}$ is a seminorm. The second part
follows from the fact that


<div>
 $$\|X\|\U {\mathbb{D}\U {1,2}}=\sum\U {n=1}^{\infty} n n!\|f\U {n}\|\U {L^2(\zl 0,T\zr ^n)}.$$
</div>


So $\|X\|\U {\mathbb{D}\U {1,2}}=0$ if and only if $f\U n=0$ for all
$n\geq 1$, which in turn is equivalent to $X=I\U 0(f\U 0):=f\U 0$. Where we
recall that by convention $L^2\U {S}(I^0):={\mathbb R}$ and $I\U 0$ was
defined as the identity on ${\mathbb R}$. This concludes the proof. ◻


Before moving on we show a motivating example. Let us consider some
deterministic function $f\in L^2(I)$ and set


<div>
 $$X:=\delta(f)= \int\U {0}^T f(s)dW(s).$$
</div>

  Then, by construction, we have
$X=I\U 1(f)$ so

<div>
 $$D\U t X= I\U 0(f(t))=f(t).$$
</div>

  This is a nice result and it
might suggest something akin to the fundamental theorem of calculus such
as $D\U t(\delta Y)=Y$ for any Skorohod integrable process $Y$. However,
this will not hold in general and as, will be seen in the next post,
occurs if and only if $Y$ is a deterministic function in $L^2(\Omega)$.\
\
This said, we now show that $\mathbb{D}\U {1,2}$ is closed in the sense
that: given a convergent sequence $X\U m\to X$. If the derivatives
$D\U tX\U m$ converge then also $D\U t X\U m\to D\U t X$.


**Proposition 2**. Let $X\U m \in \mathbb{D}\U {1,2}$ such that $X\U m$ is a
Cauchy sequence in both $L^2(\Omega)$ and in $\mathbb{D}\U {1,2}$. Then,
there exists $X \in \mathbb{D}\U {1,2}$ such that


<div>
 $$\lim\U {m \to \infty}\|X\U m-X\|\U {L^2(\Omega)}=\lim\U {n \to \infty}\|D\U tX\U m-D\U tX\|\U {L^2(I\times\Omega)}.$$
</div>





Proof. First of all, we note that since $L^2(\Omega)$ is complete
$X\U m$ must converge to some $X\in L^2(\Omega)$. Let us write the
respective chaos expansions as


<div>
 $$X=\sum\U {n=0}^{\infty} I\U n(f\U n);\quad X\U m=\sum\U {n=0}^{\infty} I\U n(f\U n^{(m)}).$$
</div>


By Itô's isometry and the convergence $X\U m\to X\in L^2(\Omega)$ we
deduce that also $f^{(m)}\U n\to f\U n\in L^2(I^n)$ for each $n$. By now
applying Fatou's lemma and the fact that $X\U m$ is by hypothesis Cauchy
in $\mathbb{D}\U {1,2}$ we obtain that

<div>
 $$\begin{gathered}
        \lim\U {m \to \infty}\|X-X\U m\|\U {\mathbb{D}\U {1,2}}=\lim\U {m \to \infty}\sum\U {n=1}^{\infty} n!n \|f\U n(x)-f\U n^{(m)}\|\U {L^2(I^n)}\\\leq \lim\U {m \to \infty}\liminf\U {k \to \infty}\sum\U {n=1}^{\infty} n!n \|f\U n^{(k)}(x)-f\U n^{(m)}\|\U {L^2(I^n)}=\lim\U {m \to \infty}\liminf\U {k \to \infty}\norm{X\U m-X\U k}\U {\mathbb{D}\U {1,2}}=0.
    \end{gathered}$$
</div>

  As desired. ◻


We now conclude this post by stating two properties of the Malliavin
derivative that are analogous to those verified by the derivative of
ordinary functions. Firstly, an analog to the chain rule for the
ordinary derivative. The proof can be found on page $29$ of Nunno and
Øksendal's book [1](https://link.springer.com/book/10.1007/978-3-540-78572-9) but is rather technical and relies
on Hermite polynomials which were not discussed previously, so we omit
it.


**Definition 2**. We write $\mathbb{D}\U {1,2}^0\subset L^2(\Omega)$ for
the space of square integrable random variables
$X=\sum\U {n=0}^{\infty} I\U n(f\U n)$ such that $f\U n=0$ for all but finitely
many $n$.



**Proposition 3** (Product rule). Given $X\U 1,X\U 2\in \mathbb{D}^0\U {1,2}$
it holds that

<div>
 $$D\U t(X\U 1X\U 2)=X\U 1D\U tX\U 2+X\U 2D\U tX\U 1.$$
</div>




Finally, though we shall not use it, we mention that if
$\Omega=\mathcal{S}^({\mathbb R})$ is the dual of the Schwartz space
and we construct a probability measure $\mathbb{P}$ called the white
noise probability measure then the following version of the chain rule
also holds (see [2](https://link.springer.com/book/10.1007/978-3-540-78572-9) page $89$).


**Proposition 4** (Chain rule). Consider
$\varphi\in C\U 1({\mathbb R}^d)$ with
$\nabla \varphi\in {L^\infty({\mathbb R}^d\to{\mathbb R}^d)}$ and
$X=(X\U 1,\ldots,X\U d)$ such that $X\U i\in \mathbb{D}\U {1,2}$ for each
$i=1,\ldots,d$. Then it holds that $\varphi(X)\in \mathbb{D}\U {1,2}$ with


<div>
 $$D\U t\varphi(X)=\sum\U {i=0}^{d} \frac{\partial \varphi}{\partial x\U i}(X)D\U t(X\U i) .$$
</div>



A pdf of version of this page is provided below:
<object data="/assets/Malliavin3.pdf" width="1000" height="1000" type='application/pdf'></object>
