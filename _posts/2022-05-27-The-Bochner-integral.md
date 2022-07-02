---
layout: post
title: The Bochner integral
subtitle: Wait a second, how many integrals are there?
thumbnail-img: /assets/img/Liu-SPDE.jpg
share-img: /assets/img/Liu-SPDE.jpg
tags: [Integration, Banach spaces, Lp spaces]
authorpost: L. Llamazares-Elias
---

This is the first post in a series extending stochastic calculus to in
Banach spaces. Our first topic is the Bochner integral. That is, the
extension of the Lebesgue integral to functions valued in Banach spaces.

# Three line summary

-   The Bochner integral is a way of integrating functions $f$ from a
    measure space to a Banach space.

-   Like the Lebesgue integral, the Bochner integral is first constructed for piecewise
    constant functions $\mathcal{A}$ and extended continuously to the
    completion $\overline{\mathcal{A}}$.

-   The completion $\mathcal{A}$ can be explicitly described as the
    space of functions with separable image and with finite $L^1$ norm.
    This naturally leads to the definition of $L^p$ spaces.

# Why is this important?
Often functions will not take values in finite-dimensional spaces but in infinite-dimensional Banach spaces. For example, this occurs often when considering a function of multiple variables $f(t,x)$ and viewing $f(t)$ as taking values in a function space of the second coordinate. This situation commonly arises in [PDEs](https://terrytao.wordpress.com/2018/09/16/254a-notes-1-local-well-posedness-of-the-navier-stokes-equations/) and [SPDEs](https://www.hairer.org/SPDEs.pdf)

# Notation

We consider a measure space $(\Omega,\mathcal{F},\mu )$ and a Banach
space $(E,\mathcal{B}(E))$ where $\mathcal{B}$ is the Borel
sigma-algebra (that is, the smallest $\sigma$-algebra on $E$ containing
all of the open sets) of $E$. We will abbreviate that $f:\Omega\to E$ is
measurable as $f:\mathcal{F}\to \mathcal{B}(E)$.

# The Bochner integral

Ok, lets get right to it, our goal is to define integration for
functions valued in a Banach space
<div>
 $$f:(\Omega,\mathcal{F},\mu)\to ((E,\norm{\cdot}),\mathcal{B}(E))$$
</div>  As
anticipated, we first consider the class of simple functions
<div>
 $$\mathcal{A}=\left\{\sum\U {k=1}^{n} x\U k 1\U {A\U k}; x\U k\in E\quad A\U k \in \mathcal{F}\right\}.$$
</div>
We can define their integral quite naturally as
<div>
 $$\int f d\mu=\int \sum\U {k=1}^n x\U k 1\U {A\U k} d\mu=\sum\U {k=1}^n x\U k\mu({A\U k})$$
</div>
If we take equivalence classes, identifying functions that are equal
$\mu$ almost everywhere, we can define the norm
<div>
 $$\norm{f}\U \mathcal{A}:=\int\U \Omega \norm{f} d\mu.$$
</div>  Then we get that
integration is a linear and absolutely continuous function
<div>
 $$\int\U \Omega \cdot d\mu : \left(\mathcal{A},\norm{\cdot}\U A)\to (E,\norm{\cdot}\right).$$
</div>
As, by a calculation, for all $f\in\mathcal{A}$.
<div>
 $$\norm{\int\U \Omega f}\leq\int\U \Omega \norm{f} d\mu=\norm{f}\U \mathcal{A}$$
</div>
Since $E$ is a Banach space, this shows that we can extend
[1]("https://en.wikipedia.org/wiki/Continuous\U linear\U extension") integration in a unique way to the completion
$\overline{\mathcal{A}}$ of $(\mathcal{A},\norm{\cdot}\U A)$. Of course,
now the key is knowing what this space $\overline{\mathcal{A}}$ is so we
can figure out what kind of functions we can integrate. Our
next definitions are motivated by this.


**Definition 1**. We say a function
$f:(\Omega,\mathcal{F})\to (E,\mathcal{B}(E))$ is strongly measurable if
$f$ is measurable $f(\Omega)$ is separable.



**Definition 2**. For $1\leq p<\infty$ we define

<div>
 $$\begin{aligned}
        \mathcal{L}^p(\Omega,\mathcal{F},\mu,E)       & =\left\{f:\Omega\to X: f \text{ is strongly measurable and } \int \norm{f}^p d\mu<\infty\right\}. \\
        \hat{\mathcal{L}}^p(\Omega,\mathcal{F},\mu,E) & =\left\{f:\Omega\to X: f \text{ is measurable and }\int \norm{f}^p d\mu<\infty\right\}.
    \end{aligned}$$
</div>
We also define the semi-norms

<div>
 $$\begin{aligned}
        \norm{f}\U {L^p(\Omega\to E)}       & :=\left(\int \norm{f}^p d\mu)^{1/p},\quad f\in\mathcal{L}^p(\Omega,\mathcal{F},\mu,E\right).       \\
        \norm{f}\U {\hat{L}^p(\Omega\to E)} & :=\left(\int \norm{f}^p d\mu)^{1/p},\quad f\in\hat{\mathcal{L}}^p(\Omega,\mathcal{F},\mu,E\right).
    \end{aligned}$$
</div>  

Finally, we take equivalence classes by the above
semi-norms to obtain the metric spaces $L^p(\Omega\to E)$ and
$\hat{L}^p(\Omega\to E).$


An adaptation of the proof of the completion of $L^p$ spaces proves that
$L^p(\Omega\to E)$ and $\hat{L}^p(\Omega\to E)$ are also complete.


**Proposition 1**. Given a Banach space $E$, the space of $p$
integrable strongly measurable and measurable functions
$L^p(\Omega\to E),\hat{L}^p(\Omega\to E)$ are Banach spaces.



*Proof*. The proof is identical in both cases so we prove it only for
$f\in L^p(\Omega\to E)$ It suffices to show that if $f\U n$ is such that
<div>
 $$\sum\U {n=1}^\infty \norm{f\U n}\U {L^p(\Omega\to E)}<\infty.$$
</div>  Then there
exists $f\in L^p(\Omega\to E)$ such that
<div>
 $$f=\sum\U {n=1}^\infty f\U n\in L^p(\Omega\to E).$$
</div>
To do so one first applies [Minkowski's integral  inequality](https://en.wikipedia.org/wiki/Minkowski_inequality#:~:text=_%7Bp%7D%5E%7Bp%7D%7D%7D.%7D-,Minkowski%27s%20integral%20inequality,-%5Bedit%5D) for real valued functions to show
that
 <div>
 $$\sum\U {n=1}^\infty \norm{f\U n}\U X\in L^p(\Omega\to{\mathbb R}).$$
</div>
Thus, the sum is finite almost everywhere. Since $E$ is complete we have
that the above sum converges pointwise almost everywhere to some
function
<div>
 $$f(\omega):=\sum\U {n=1}^\infty f\U n(\omega)\in E.$$
</div>

Furthermore, we have that $f$ is strongly measurable as it is the limit of strongly
measurable functions (this is a small exercise). Finally, by Fatou's
lemma for real valued functions and the triangle inequality for norms
<div>
 $$\begin{gathered}
        \norm{f-\sum\U {n=1}^N f\U n}\U {L^p(\Omega\to E)}=\norm{\sum\U {n=N}^\infty f\U n}\U {L^p(\Omega\to E)}\leq \liminf\U {M\to \infty}\norm{\sum\U {n=N}^M f\U n}\U {L^p(\Omega\to E)}\\\leq \liminf\U {M\to \infty}\sum\U {n=N}^M \norm{f\U n}\U {L^p(\Omega\to X)}=\sum\U {n=N}^\infty \norm{f\U n}\U {L^p(\Omega\to X)}\xrightarrow{N\to\infty} 0.
    \end{gathered}$$
</div>  
Which shows convergence in $L^p(\Omega\to E)$. ◻


Just as in the case of Lebesgue integrals the proof of the completeness
of $L^p(\Omega\to E)$ serves to show that every convergent sequence must
have a subsequence converging almost everywhere. This proposition is not
necessary for the rest of the constructions, it's just a nice property
to have in reserve.


**Proposition 2**. Let $f\U n\to f\in L^p(\Omega\to E)$, then there
exists a subsequence $f\U {n\U k}$ converging to $f$ almost everywhere.



*Proof*. In the proof of the above proposition we saw that for any
absolutely convergent sum converges almost everywhere to its limit.
Further, since $f\U n$ is Cauchy, we can extract a subsequence $f\U {n\U k}$
with $\|f\U {n\U k}-f\U {n\U {k-1}}\|\leq 2^{-k}$. By construction the sequence
<div>
 $$\sum\U {k=0}^{\infty} f\U {n\U k}-f\U {n\U {k-1}},$$
</div>
is normally convergent and converges in $f$. By the above discussion we conclude the proof. ◻


Ok, so we've constructed some spaces of $p$-integrable functions and
shown that they are complete. You know where this is going, the next stop is
density town. In the standard construction of the Lebesgue integral, it
is used that every measurable function to $\mathbb{R}$ can be pointwise
approximated by simple functions. One can achieve the same result for
arbitrary metric spaces if the image of $f$ is separable.


**Lemma 1**. Let $(E,d)$ be a metric space and let $f$ be strongly
measurable. Then $f$ is the pointwise limit of simple functions
$f\U n \in \mathcal{A}$. Furthermore,\
$d\U n(\omega):=d(f\U n(\omega),f(\omega))$ is a non-increasing sequence for
each $\omega\in\Omega$



*Proof*. Consider a countable dense subset $\{e\U k\}\U {k=1}^\infty$ of
$f(\Omega)$. Now define $\varphi:E\to E$
<div>
 $$\varphi\U n(e):= e\U j \text{ where }  d(e\U j,e)=\min\U {1\leq m\leq n} d(e,e\U m).$$
</div>
And define $f\U n:=\varphi\U n \circ f$. A bit of thought shows that
$\varphi\U n$ is continuous and thus so is $f\U n$ (remember we are
considering the Borel $\sigma$-algebra) on $E$. Furthermore, since for
each fixed $\omega$ the above distance goes to $0$ we have that
<div>
 $$\lim\U {n\to\infty} f\U n(\omega)=f(\omega),\quad \forall \omega\in\Omega.$$
</div>
Finally, $f\U n$ is simple as $f\U n(\Omega)\in \{e\U 1,...,e\U n\}$ and the
non-increasing property of $d\U n(\omega)$ is clear by construction. ◻


In the above proof, we see that the reason for requiring that the image
of our class of integrable functions be separable is so that we can
approximate them by simple functions.


**Proposition 3**. Every function $f\in L^1(\Omega\to E)$ is the limit
of simple functions.



*Proof*. Since $f$ is strongly measurable, we can apply the above lemma
to obtain a sequence of simple functions $f\U n$ converging pointwise and
monotonically to $f$. Furthermore we have that, by the monotone
convergence theorem for integrals in $\mathbb{R}$,
<div>
 $$\lim\U {n\to\infty}\norm{f\U n-f}\U {L^1(\Omega\to E)}=\lim\U {n\to\infty}\int\U \Omega\norm{f\U n-f}d\mu=\int\U {\Omega}\lim\U {n \to \infty}\|f\U n-f\| d\mu =0.$$
</div>  ◻


As a corollary, we obtain the following


**Corollary 1**. $\mathcal{A}$ is a dense subset of
$\left(L^1(\Omega\to E),\norm{\cdot}\U {L^1(\Omega\to E)}\right)$.


In consequence, since we already saw that $L^1(\Omega\to E)$ is
complete, we have that $\overline{\mathcal{A}}= L^1(\Omega\to E)$. This
is exactly the space of integrable functions.


**Definition 3**. We define the integral on $L^1(\Omega\to E)$ as the
unique continuous extension with the norm
$\norm{\cdot}\U {L^1(\Omega\to E)}$ of the integral on $\mathcal{A}$. That
is, given $f\in L^1(\Omega\to E)$ we define
<div>
 $$\int\U \Omega f d\mu:=\lim\U {n\to\infty} \int\U \Omega f\U n d\mu.$$
</div>
Where $f\U n\in \mathcal{A}$ is any sequence such that
$\norm{f-f\U n}\U {L^1(\Omega\to E)}\to 0$.


The typical properties are now just a result of the definition and a
passage to the limit, as they hold for simple functions.


**Corollary 2**. Let $f\in L^1(\Omega,E)$ with $E$ a Banach space,
then

1.  $\norm{\int\U \Omega f d\mu}\leq\int\U \Omega{\norm{f}d\mu}$

2.  Let $Y$ be another Banach space and $L\in L(E,Y)$. Then

 <div>
 $$\int\U \Omega (L\circ f) d\mu=L\left(\int\U \Omega f d\mu\right).$$
</div>


Ok, that's it, this post was a bit more technical than some of the
others but you get the picture. Define an integral for simple functions,
and figure out what can be approximated by simple functions. As we saw,
the extra requirement that appears over the Lebesgue case is that the
function $f$ is separately valued and justifies why, as we will see in
future posts on SPDEs, the image of $f$ is often taken to be some
separable Hilbert space. Until the next time!

A pdf of version of this page is provided below:
<object data="/assets/Bochner.pdf" width="1000" height="1000" type='application/pdf'></object>
