---
layout: post
title: The Malliavin Derivative 1
subtitle: Part 3 of the series on Malliavin calculus
thumbnail-img: /assets/img/Malliavin.jpg
share-img: /assets/img/Malliavin.jpg
tags: [Malliavin derivative, Chaos Expansion,Malliavin calculus]
authorpost: L. Llamazares-Elias
---

#  Three line summary

-   The Malliavin derivative is an operator defined by manipulating the
    chaos expansion of a square-integrable random variable.

-   The Malliavin derivative transforms square-integrable variables into
    square integrable processes.

-   The Malliavin derivative shares some properties with the classic
    derivative such as the product rule and chain rule, but the
    fundamental theorem of calculus only holds in some special cases.

# Why should I care?

The Malliavin derivative is (somewhat unsurprisingly) a fundamental
object of Malliavin calculus and has many applications in finance,
numerical methods, and optimal control.

# Notation

The same as in previous [posts](https://nowheredifferentiable.com/2022-05-26-Malliavin-Calculus-1/#:~:text=Iterated%20integrals-,We%20will%20write,-F). Furthermore we will shorten the notation
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
recall that by convention $L^2\U (S_0):={\mathbb R}$ and $I\U 0$ was
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
$\Omega=\mathcal{S}^\star({\mathbb R})$ is the dual of the Schwartz space
and we construct a probability measure $\mathbb{P}$ called the [white
noise probability measure](https://en.wikipedia.org/wiki/White_noise_analysis#:~:text=In%20probability%20theory%2C%20a%20branch,based%20on%20the%20Wiener%20process.) then the following version of the chain rule
also holds (see [2](https://link.springer.com/book/10.1007/978-3-540-78572-9) page $89$).


**Proposition 4** (Chain rule). Consider
$\varphi\in C\U 1({\mathbb R}^d)$ with
$\nabla \varphi\in {L^\infty({\mathbb R}^d\to{\mathbb R}^d)}$ and
$X=(X\U 1,\ldots,X\U d)$ such that $X\U i\in \mathbb{D}\U {1,2}$ for each
$i=1,\ldots,d$. Then it holds that $\varphi(X)\in \mathbb{D}\U {1,2}$ with


<div>
 $$D\U t\varphi(X)=\sum\U {i=0}^{d} \frac{\partial \varphi}{\partial x\U i}(X)D\U t(X\U i) .$$
</div>
