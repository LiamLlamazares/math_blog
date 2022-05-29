---
layout: post
title: The Skorohod integral
subtitle: How many integrals even are there?!?
thumbnail-img: /assets/img/Malliavin.jpg
share-img: /assets/img/Malliavin.jpg
tags: [Integration, Malliavin calculus, Skorohod integral, Chaos expansion, Itô integral, Stochastic Calculus]
---

#  Three line summary

-   By fixing $t$, one can obtain a chaos expansion for (possibly
    non-adapted) square integrable stochastic processes $X(t)$.

-   The Itô integral of an Itô integrable process $X(t)$ has a chaos
    expansion.

-   This chaos expansion can converge even when $X(t)$ is not adapted to
    the filtration $\mathcal{F}\U t$ (and thus not Itô integrable). This
    allows us to extend the Itô integral to non-adapted processes.

# Why should I care?

If you want to define the Malliavin derivative you need the Skorohod
integral.

# Notation

The same as in the previous post [1](https://liamllamazares.github.io/2022-05-26-Malliavin-Calculus-1/) on the chaos expansion. We
will also write $\mathbb{L}^2(I\times \Omega)$ for the space of Itô
integrable functions (this was defined in [2](https://liamllamazares.github.io/2022-05-26-The-Ito-integral/)).

# The chaos expansion of an Itô integral

Our goal in this post is to construct the Skorohod integral. This serves
as a generalization of the Itô integral and the starting point for the
definition of the Malliavin derivative. How is this done? Let us first
consider a (not-necessarily adapted) stochastic process $X$ such that
$X\U t\in L^2(\Omega,\mathcal{F}\U \infty)$ for each $t \in I$. Then we know
that by the chaos expansion proved in the previous post, for each $t$
there exists $f\U {n,t}\in L^2(S\U n)$ such that
<div>
 $$X=\sum\U {n=0}^{\infty} I\U n(f\U {n,t}).$$
</div>  Let us write
$f\U {n}(\cdot,t):=f\U {n,t}$. Note that we are now considering $f\U n$ as a
function of $n+1$ variables instead of $n$. In particular, we will be
able to consider expressions like $I\U {n+1}(f\U n)$ later on. The first
thing we do is study what the adaptedness of $X$ means in term of the
functions $f\U n$ appearing in its chaos expansion.


**Lemma 1**. Let $X(t) \in L^2(\Omega,\mathcal{F}\U \infty)$ for each
$t \in  I$, then $X$ is adapted iff
<div>
 $$f\U n(t\U 1,\ldots,t\U n,t)=0,\quad\forall t\leq\max\U {i=1,\ldots,n} t\U i .$$
</div> 



Proof. Firstly, we note that a stochastic process $X$ is adapted iff
<div>
 $$X\U t=\mathbb{E}\U {\mathcal{F}\U t}\zl X(t)\zr \quad\forall t\in I.$$
</div>  Since the
Itô integral is a martingale, we obtain that, by commuting the sum and
using the uniqueness of the chaos expansion this is equivalent to
requiring that, for all $t$ <div>
 $$\begin{gathered}
        I\U n(f\U n(\cdot,t))\\=    n!\mathbb{E}\U {\mathcal{F}\U t} \left[ \int\U {I} \left( \int\U {0}^{t\U n}\cdots \int\U {0}^{t\U 2}f(t\U 1\ldots t\U n,t) dW(t\U 1) \cdots dW(t\U {n-1}) \right)dW(t\U n)\right] \\
        =n!\int\U {0}^t \int\U {0}^{t\U n}\cdots \int\U {0}^{t\U 2}f(t\U 1\ldots t\U n,t) dW(t\U 1) \cdots dW(t\U {n-1})dW(t\U n)\\= I\U n(f\U n(\cdot,t) 1\U {\max\U {t\U i\leq t}})
    \end{gathered}$$
</div>  Where the commutation of the sum and the integral
is justified by the $L^2(\Omega)$ convergence of the chaos expansion
($L^1(\Omega)$ convergence would have been enough). ◻


In particular, we obtain that, since $f\U n$ is already symmetric in its
first n-coordinates, its symmetrization verifies that
<div>
 $$f\U {n,S}(t\U 1,\ldots,t\U n,t\U {n+1})=\frac{1}{n+1}f\U n(t\U 1,\ldots\hat{t\U {j}},\ldots,t\U {n+1},t\U j),\quad \text{where } j=\text{arg}\max\U i t\U i.$$
</div> 
Using this relationship we can directly calculate the Itô integral of a
stochastic process to obtain that.


**Theorem 1**. Let $X \in \mathbb{L}^2(I\times\Omega)$ then the Itô
integral of $X$ is
<div>
 $$\int\U {I} X(t) dW(t)=\sum\U {n=0}^{\infty} I\U {n+1}(f\U {n,S}).$$
</div> 



Proof. This is a direct calculation using the previous result as

<div>
 $$\begin{gathered}
        \int\U {I} X(t) dW(t)=\sum\U {n=0}^{\infty}\int\U {I} I\U n(f\U {n,t})dW(t)\\=\sum\U {n=0}^{\infty}n! \int\U {I}\int\U {S\U n}f\U {n,t}(t\U 1,\ldots,t\U n) dW(t\U 1)\ldots dW(t\U n) dW(t)\\=\sum\U {n=0}^{\infty}(n+1)! \int\U {I}\int\U {S\U n}f\U {n,S}(t\U 1,\ldots,t\U n,t) dW(t\U 1)\ldots dW(t\U n) dW(t)\\=\sum\U {n=0}^{\infty}(n+1)! J\U {n+1}(f\U {n,S}) =\sum\U {n=0}^{\infty}  I\U {n+1}(f\U {n,S}).
    \end{gathered}$$
</div>  ◻


# The Skorohod integral

The last term appearing in the equality is what we will call the
Skorohod integral.


**Definition 1**. Let $X(t)\in L^2(\Omega,\mathcal{F}\U \infty)$ be a
stochastic process such that
<div>
 $$\delta(X):=\int\U {I} X(t)\delta W(t):=\sum\U {n=0}^{\infty} I\U {n+1}(f\U {n,S})\in L^2(\Omega).$$
</div> 
Then we will say that $X$ has Skorohod integral $\delta(W)$ and write
$X\in dom(\delta)$.


As we saw in the previous theorem the Skorohod integral is equal to the
Itô integral for all stochastic processes in
$\mathbb{L}^2(I\times\Omega)$. However, it may also be defined for
non-adapted stochastic processes. In fact, by using the orthogonality of
the iterated integrals (what we called Itô's $n$-th isometry in the
last post [3](https://liamllamazares.github.io/2022-05-26-The-Ito-integral/), we deduce the following).


**Proposition 1**. A stochastic process
$X(t)\in L^2(\Omega,\mathcal{F}\U \infty)$ has a Skorohod integral iff
<div>
 $$\sum\U {n=0}^{\infty} (n+1)!\|f\U {n,S}\|\U {L^2(\zl 0,T\zr ^n)}<\infty.$$
</div> 



Proof. By Itô's $n$-th isometry we have that
<div>
 $$\norm{\delta(X)}\U {L^2(\Omega)}=\sum\U {n=0}^{\infty}  \norm{I\U {n+1}(f\U {n,S})}=\sum\U {n=0}^{\infty} (n+1)!\norm{f\U {n,S}}\U {L^2(I^{n+1})}.$$
</div>  ◻


Of course, a priori the above condition is not that easy to check for a
given function as it involves calculating the chaos expansion for the
given process $X$. In some cases however it is possible, to consider for
example the stochastic process defined by $X(t)=W(T)$ on the interval
$I=\zl 0,T\zr $. Then we have that <div>
 $$X(t)=\int\U {0}^T dW(t)=I\U 1(1).$$
</div>  Thus, for
all $t\in I$ we have that
<div>
 $$f\U 1=1;\quad f\U n=0\quad\forall n \in \mathbb{N}\setminus \{1\}  .$$
</div>  So
$X\in dom(\delta)$ with
<div>
 $$\delta(X)= I\U 2(1)=\int\U {0}^T\int\U {0}^t dW(t\U 1)dW(t)=\int\U {0}^T W(t) dW(t)= W^2(T)-T.$$
</div> 
Note however that the Itô integral of $W(T)$ is undefined as it is not
$\mathcal{F}\U t$ adapted. Since the Skorohod integral of $1$ is equal to
$W(T)$, the above example shows how one cannot simply "pull out
constants in $t$" in the sense that, if $G$ is a random variable
independent of $t$ and $X(t)=G\cdot u(t)$, then
<div>
 $$\int\U {I} X(t) \delta W(t)=\int\U {I}G\cdot u(t)\delta W(t) \neq G\int\U {I}u(t) dW(t).$$
</div> 
Though this may seem unintuitive, it is a consequence of the fact that,
even though $f\U i$ may not depend on $t$, the terms
<div>
 $$g(t):=\int\U {0}^t\int\U {0}^{t\U {n}}\cdots \int\U {0}^{t\U 2} f\U i dW(t\U 1)\cdots dW(t\U {n-1})dW(t\U n).$$
</div> 
Can depend on $t$. Despite this, the Skorohod integral still maintains
some of the natural properties we associate with integration.


**Proposition 2**. Let $X(t), Y(t)\in dom(\delta)$,
$\lambda \in {\mathbb R}$. Then it holds that

-   $X(t)+ \lambda Y(t) \in dom(\delta)$ with
    $\delta(X+\lambda Y)=\delta(X)+\lambda \delta(Y)$.

-   $\mathbb{E}\zl \delta(X)\zr =0$.

-   $X\cdot 1\U A \in dom(\delta)$ for any measurable subset
    $A \subset I$. Furthermore, if $A \cup B =I$ then
    <div>
 $$\int\U {A}X(t) \delta(t)+ \int\U {B}X(t)\delta W(t):=\delta(X\cdot 1\U A)+\delta(X\cdot 1\U B)=\delta(X).$$
</div> 



Proof. The first property is a consequence of the chaos expansion's
linearity (which is itself a consequence of the linearity of iterated
Itô integration). The second is due to the expectation of the Itô
integral being $0$. The final property is a consequence of the fact that
the chaos expansion of $X\cdot 1\U A$ is
<div>
 $$X\cdot 1\U A=\sum\U {n=0}^{\infty} I\U {n}(\zl f\U n 1\U A\zr \U S).$$
</div>  Which shown by
the equivalent characterization of Skorohod functions that
$X\cdot 1\U A\in dom(\delta)$. The final property is a consequence of the
previously proved linearity. ◻


We now know what the Skorohod expansion is, how to characterize it, and
its main properties, in the next post we will construct the Malliavin
derivative as its adjoint.
A pdf of version of this page is provided below:
<object data="/assets/Skorohod.pdf" width="1000" height="1000" type='application/pdf'></object>
