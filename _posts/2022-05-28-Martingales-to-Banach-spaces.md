---
layout: post
title: Martingales
subtitle: Doob's Martingale inequality is cool
thumbnail-img: /assets/img/Liu-SPDE.jpg
share-img: /assets/img/Liu-SPDE.jpg
tags: [Integration, Banach spaces, Lp spaces]
---

# Three line summary

-   Conditional expectations exist in a natural way for simple
    functions, by taking extensions they also exist for integrable
    functions to a Banach space $L^1(\Omega\to E)$.

-   Using conditional expectations we can define what a martingale is
    just like in the real case.

-   The space of continuous $p$-integrable martingales is a Banach
    space.

# Why should I care?

Banach valued martingales form the basis of SPDEs. This is because
analogously to Itô integration of real-valued processes. Integrating
against a Wiener process valued in a Banach space the same will produce
a square integrable continuous martingale.

# 1. Conditional expectation

In graduate-level probability courses, given a $\sigma-$algebra
$\mathcal{G}$ one shows that by applying Radon-Nikodyn's theorem, for
any real-valued random variable $X\in L^1(\Omega\to R)$ there exists a
conditional expectation $\mathbb{E}\U {\mathcal{G}}\zl X\zr $ verifying that


<div>
 $$\int\U A \mathbb{E}\U {\mathcal{G}}\zl X\zr =\int\U A X,\quad \forall A\in\mathcal{G}.$$
</div>


Of course, now that we have created an integral for the space of random
variables $L^1(\Omega\to E)$ to some Banach space $E$,  we would like to see
whether such a conditional expectation also exists for these functions.
To start off with, if we are given a simple function


<div>
 $$X=\sum\U {k=1}^n x\U k 1\U {A\U k}, \quad x\U k\in E, A\U k\in\mathcal{G}.$$
</div>

  It is
a simple calculation to show that

<div>
 $$\mathbb{E}\U {\mathcal{G}}\zl X\zr =\sum\U {k=1}^n x\U k \mathbb{E}\U {\mathcal{G}}\zl 1\U {A\U k}\zr ,$$
</div>


verifies the desired formula (we note that, since $1\U {A\U k}$ are real-valued, $\mathbb{E}\U {\mathcal{G}}\zl 1\U {A\U k}\zr $ are well defined). Furthermore, we have that
$\mathbb{E}\U \mathcal{G}$ is a linear, and pointwise continuous operator
with


<div>
 $$\|\mathbb{E}\U {\mathcal{G}}\zl X\zr \|\leq \sum\U {k=1}^n \|x\U k\| \mathbb{E}\U {\mathcal{G}}\zl 1\U {A\U k}\zr =\mathbb{E}\U {\mathcal{G}}\left[ \sum\U {k=1}^n \|x\U k\|1\U {A\U k}\right] =\mathbb{E}\U {\mathcal{G}}\left[ \|X\|\right] .$$
</div>


This allows us to show the following


**Theorem 1** (Existence and uniqueness of conditional expectation).
Let $X\in L^1(\Omega\to E)$ for some Banach space $E$. Then $X$ has a
conditional expectation satisfying


<div>
 $$\|\mathbb{E}\U {\mathcal{G}}\zl X\zr \|\leq\mathbb{E}\U {\mathcal{G}}\left[ \|X\|\right] .$$
</div>





Proof. We have already proved the above inequality for simple
processes. By the previous post, [1](https://liamllamazares.github.io/2022-05-27-The-Bochner-integral/) we can take $X\U n$ converging
to $X$ in $L^1(\Omega\to E)$ to obtain that

<div>
 $$\begin{gathered}
        \|\mathbb{E}\U {\mathcal{G}}\zl X\U n-X\U m\zr \|\leq\mathbb{E}\U {\mathcal{G}}\left[ \|X\U n-X\U m\|\right] \\\implies \mathbb{E}\zl \|\mathbb{E}\U {\mathcal{G}}\zl X\U n\zr -\mathbb{E}\U {\mathcal{G}}\zl X\U m\zr \|\zr \leq \mathbb{E}\left[ \|X\U n-X\U m\|\right] \to 0
    \end{gathered}$$
</div>

  As a result, $\mathbb{E}\U {\mathcal{G}}\zl X\U n\zr $ is a
Cauchy sequence in the complete space $L^1(\Omega\to E)$ and so converges to some function
$Z$, passing to the limit in the defining equation for the conditional
expectation shows that $Z=\mathbb{E}\U \mathcal{G}\zl X\zr $. Finally, to prove
uniqueness we have that if both $Z\U 1,Z\U 2$ satisfy


<div>
 $$\int\U A Z\U 1=\int\U A X=\int\U A Z\U 2,\quad \forall A\in\mathcal{G}.$$
</div>

  Then
using the linearity of the integral we obtain that $w(Z\U 1)=w(Z\U 2)$ for
all linear function $w$, so $Z\U 1=Z\U 2$. ◻


# Martingales

Okay, so we leveraged some inequalities to prove the existence of a
conditional expectation. This done, the following definition, which mimicks
the real case, is quite natural


**Definition 1**. Let $\\{M(t)\\}\U {t\in I}$, be a stochastic process on
$(\Omega, \mathcal{F}, \mathbb{P})$ with a filtration
$\\{\mathcal{F}\U {t}\\}\U {t \in I}$. The process $M$ is called an
$\mathcal{F}\U {t}$-martingale, if:

1.  $M(t)\in L^1(\Omega\to E)$ for all $t\in I$

2.  $M(t):\mathcal{F}\U {t} \to \mathcal{B}(E)$ for all $t\in I$,

3.  $\mathbb{E}\U {\mathcal{F}\U {s}}\left[ M(t)\right] =M(s)$ for all
    $s \leq t$.


The concept of submartingale (supermartingale) is defined by replacing the equality in 3.
with a $\geq$ (with a $\leq$). In the real case the absolute value of a martingale is a submartingale. To obtain this result for Banach valued Martingales we need to assume that $E$ is separable so that we can use the following result.

**Lemma 1**  Let $E$ be a separable metric space, then there exists a countable family of linear functions $\ell_n\U n\ in E^*$ such that

<div>
 $$\norm{e}=\sup\U {n\in \mathbb{N}}\ell_n(e)\quad\forall e\in E$$.
</div>

Proof. Let $e\U n$ be a countable dense subset of $E$. By Hahn Banach's theorem we may take $\ell\U n$ such that
<div>
 $$\norm{l\U n}=1;\quad \norm{l\U n}(e\U_ n)=\norm{e \U n} \forall n\in \mathbb{N}$$.
</div>
By now taking $e\U {n\U k} \to e$ we have that
<div>
 $$\norm{l\U {n\U k}}(e)\geq\norm{l\U {n\U k}}(e\U {n\U k})-\norm{l\U {n\U k}(e-e\U {n\U k})}\geq \norm{e\U {n\U k}}-\norm{e-e\U {n\U k}} $$.
</div>


 Let us abbreviate $\mathbb{E}\U {\mathcal{F}\U t}$ by
$\mathbb{E}\U t$. Then, as in the real case, we have the following.


**Lemma 1** (Norm is submartingale). Let $M(t)$ be a martingale, then
$\norm{M(t)}$ is a martingale



Proof. We recall that, by the Hahn Banach theorem, it holds for any
metric space that given $y\in E$


<div>
 $$\norm{z}=\sup\U {\ell\in E^:\|\ell\|=1}\ell(z)$$
</div>

  As a result, by the
linearity of the integral and abbreviating the supremum to just
$\sup\U \ell$,

<div>
 $$\begin{gathered}
        \|M(s)\|=\|\mathbb{E}\U {s}\zl M(t)\zr \|= \sup\U \ell \ell\left(\mathbb{E}\U {s}\zl M(t)\zr \right)=\sup\U \ell\|{\mathbb{E}\U {s}\left[ \ell(M(t))\right] \|}\\
        \leq \mathbb{E}\U {s}\left[ \sup\U \ell\ell(M(t))\right] =\mathbb{E}\U {s}\left[ \|M(t)\|\right]
    \end{gathered}$$
</div>

  ◻


Let us recall the following result for real-valued martingales


**Lemma 2** (Doob's maximal Martingale inequality). Let
$\\{X\U k\\}\U {k=1}^\infty$ be a real-valued sub-martingale. Then it holds
that


<div>
 $$\norm{\max\U {k\in\\{1,...,n\\}}X\U k}\U {L^p(\Omega)}\leq \frac{p}{p-1}\norm{X\U n}\U {L^p(\Omega)}$$
</div>


As a consequence, if $X\U t,t\in\zl 0,T\zr $ is left (or right) continuous then


<div>
 $$\norm{\max\U {t\in\zl 0,T\zr }X\U k}\U {L^p(\Omega)}\leq \frac{p}{p-1}\norm{X\U T}\U {L^p(\Omega)}.$$
</div>




The idea of the above result is that, since $X\U k$ is a submartingale,
$X\U k\lesssim X\U {k+1}\lesssim...\lesssim X\U n$. Getting from the
continuous to the discrete case is possible by using the continuity of
$X$ and approximating it on some finer and finer mesh $t\U 0,...,t\U n$.
This said, applying Doob's maximal martingale inequality together with
the Lemma $1$ gives that


**Theorem 2** (Maximal Inequality). Let $p>1$ and let $E$ be a
separable Banach space. If $M(t)$, is a right-continuous $E$-valued
$\mathcal{F}\U {t}$-martingale, then

<div>
 $$\begin{gathered}
        \left(E\left(\sup \U {t \in\zl 0, T\zr }\|M(t)\|^{p}\right)\right)^{\frac{1}{p}} \leq \frac{p}{p-1} \sup \U {t \in\zl 0, T\zr }\left(E\left(\|M(t)\|^{p}\right)\right)^{\frac{1}{p}} \\
        =\frac{p}{p-1}\left(E\left(\|M(T)\|^{p}\right)\right)^{\frac{1}{p}}
    \end{gathered}$$
</div>





Proof. This follows by using that $\norm{M(t)}$ is a sub-martingale
and Doob's maximal inequality. ◻


Doob's inequality is essentially an equality between different function
norms we can place on the space of continuous Martingales and will
provide a very powerful tool later on.


**Corollary 1**. Let $M$ be a (left or right) continuous martingale to
a separable Banach space $E$. Then the following are equivalent

-   $M\in \hat{L}^\infty(\zl 0,T\zr \to \hat{L}^2(\Omega\to E))$

-   $M\in \hat{L}^2(\Omega\to \hat{L}^\infty(\zl 0,T\zr \to E))$

-   $\mathbb{E}\zl \norm{M(T)}^2\zr <\infty$

Where we recall from the previous post that $\hat{L}^p$ symbolizes that
$M$ may not be separately valued and only have an integrable norm. That
said, the same reasoning shows that the above result also holds for the
integrable $L^p$ spaces.


A useful space of Martingales is as follows


**Definition 2**. Let $M(t)$ be a $E$ valued martingale with index set
$I=\zl 0,T\zr $, then we define


<div>
 $$\mathcal{M}\U T^2(E):=\left\\{\text{continuous martingales } M:\mathbb{E}\zl \norm{M(T)}^2\zr <\infty\right\\}$$
</div>


and give it the norm


<div>
 $$\norm{M}\U {\mathcal{M}\U T^2(E)}:=\mathbb{E}\zl \norm{M(T)}^2\zr .$$
</div>




By Theorem $2$ we have that


<div>
 $$\mathcal{M}\U T^2(E)\subset \hat{L}^\infty(\zl 0,T\zr \to \hat{L}^2(\Omega\to E))\cap \hat{L}^2(\Omega\to \hat{L}^\infty(\zl 0,T\zr \to E)).$$
</div>


and that any of the norms of these spaces is equivalent to the one set
on $\mathcal{M}\U T^2(E)$. This is useful in the following result


**Proposition 1**. Let $E$ be a separable Banach (Hilbert) space, then
$\mathcal{M}\U T^2(E)$ is a Banach (Hilbert) space.



Proof. Let us first consider the case when $E$ is a Banach space. By the previous observation and the completeness of the
$\hat{L}^p$ spaces proved in the previous post, $\mathcal{M}\U T^2(E)$ is
a subspace of a Hilbert space. As a result, it is sufficient to show
that it is closed. Let $M\U n$ converge to $M$. Then, by the equivalence
of the norms we have that
$M\U n(t)\to M(t)\in \hat{L}^1(\Omega\to E)\subset \hat{L}^2(\Omega\to E)$
so that for all $A\in\mathcal{F}\U s$


<div>
 $$\int\U A M(s)d\mathbb{P}=\lim\U {n\to\infty}\int\U A M\U n(s)d\mathbb{P}=\lim\U {n\to\infty}\int\U A M\U n(t)d\mathbb{P}=\int\U A M(t)d\mathbb{P}.$$
</div>


This shows that $M$ is a martingale. Furthermore, as was seen in the
previous post, there exists a subsequence $M\U {n\U k}$ such that


<div>
 $$\lim\U {n\to\infty}{M\U {n\U k}}(\cdot,\omega)=M(\cdot,\omega)\in \hat{L}^\infty(\zl 0,T\zr \to E)\quad a.e.\quad \omega\in\Omega$$
</div>


Since $M\U {n\U k}(\cdot,\omega)$ are continuous and continuity is preserved
by uniform limits this proves that $M$ is continuous almost everywhere. This shows that $\mathcal{M}\U T^2(E)$ is closed and thus a Banach space. In the case where $E$ is a Hilbert space we can endow $\mathcal{M}\U T^2(E)$ with the inner product

<div>
 $$\langle{M\U 1, M \U 2\rangle}\U {\mathcal{M}\U T^2(E)}:= \mathbb{E} \left[ \langle{M\U 1(T), M \U 2(T)\rangle}\U E \right ]$$
</div>

This concludes the proof. ◻


In future installments, we will prove that a Banach valued Wiener
process belongs to this space and use it to define the stochastic
integral that leads to the construction of SPDEs.


**Proposition 2**. Let $W(t)$ be a $E$ valued $\Sigma$-Wiener process
with respect to a filtration $\mathcal{F}\U t$. Then
$W(t)\in \mathcal{M}\U T^2(E)$.



Proof. It is a martingale as it is adapted and, given
$A\in\mathcal{G}\U S$ and $u\in E$, by the linearity of the integral and
Independence of $W(t)-W(s)$ with $\mathcal{G}\U s$

<div>
 $$\begin{gathered}
        \left\langle\int\U A W(t)-W(s)d\mathbb{P},u\right\rangle=\int\U A \left\langle W(t)-W(s),u\right\rangle d\mathbb{P}\\=
        \mathbb{P}(A)\mathbb{E}\zl \left\langle W(t)-W(s),u\right\rangle\zr =0
    \end{gathered}$$
</div>

  As a result


<div>
 $$\int\U A W(t)d\mathbb{P}=\int\U A W(s)d\mathbb{P}=0\quad \forall A\in\mathcal{G}\U s\implies \mathbb{E}\U s\zl W(t)\zr =W(s).$$
</div>


Finally, we have that $\mathbb{E}\zl W(t)^2\zr =t<\infty$ for all $t$ and $W$
is continuous by construction. This concludes the proof. ◻

A pdf of version of this page is provided below:
<object data="/assets/Martingales.pdf" width="1000" height="1000" type='application/pdf'></object>
