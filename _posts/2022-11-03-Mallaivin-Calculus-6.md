---
layout: post
title: Study of densities part 2
subtitle: Part 6 of the series on Malliavin calculus
thumbnail-img: /assets/img/Malliavin.jpg
share-img: /assets/img/Malliavin.jpg
tags: [Malliavin calculus, Densities]
authorpost: L.Llamazares
---

#  Three line summary

-   Solutions to SDEs of the form $dX=b(X) d t +\sigma (X)dW$ are
    Malliavin differentiable if $b,\sigma \in C^1({\mathbb R})$.

-   Their Malliavin differential $DX$ can be written as a stochastic
    integral.

-   This gives us an SDE linear in $DX$ and can be solved exactly to
    obtain an explicit expression for $DX$.

# Notation

The same as in the other posts of this series. In particular, we recall
the notation $\mathbb{L}^2(I\times\Omega)$ for the set of [progressively
measurable](https://nowheredifferentiable.com/2022-05-26-The-Ito-integral/#:~:text=mysterious%20term%20mean%3F-,Definition%201,-.%20A%20stochastic%20process) square integrable stochastic processes. Furthermore,
given a stochastic process $X$ such that $X(t)\in \mathbb{D}^{1,2}$ for
each $t\in I$ we write $D\U rX(t)$ for the Malliavin differential at time
$r\in I$ of $X(t)$. That is, if

<div>
 $$\label{ce}
    X(t)=\sum\U {n=0}^{\infty}  I\U n(f\U n(\cdot ,t)),\quad f\U n(\cdot ,t)\in L^2(S\U n).$$
</div>


is the [chaos expansion](https://nowheredifferentiable.com/2022-06-10-Malliavin-Calculus-2/#:~:text=.%20Then-,we%20know,-that%20by%20the) of $X(t)$ for each $t$ then we have that


<div>
 $$\label{ced}
    D\U rX(t)=\sum\U {n=0}^{\infty}  nI\U {n-1}(f\U n(\cdot ,r,t)) , \quad\forall r,t\in I.$$
</div>



# Introduction

As anticipated in the summary, we will be working with an SDE of the
form

<div>
 $$\label{SDE}
    dX=b(X) d t +\sigma (X)dW .$$
</div>

  It is a classical result of the theory
of SDEs that, if $b$ and $\sigma$ are Lipschitz continuous, then the
above equation has a unique solution for each initial data
$X\U 0\in L^2(\Omega)$. That is, there exists a unique continuous adapted
process $X\in \mathbb{L}^2(I\times\Omega)$ such that


<div>
 $$\label{X expression}
    X(t)=X(0)+\int\U {0}^t b(X(s)) ds+\int\U {0}^t \sigma(X(s))  dW(s).$$
</div>


Our goal will be to obtain an explicit expression for the derivative of
$X$. We will do so by directly differentiating in the expression above.
As a result, we will need two lemmas that tell us how to differentiate
each of the above integrals. The first of these is as follows.


**Lemma 1**. If $X\in \mathbb{L}^2(I\times\Omega)$ is Malliavin
differentiable for almost all $t$. Then $\int\U {0}^t X(s) dW(s)$ is
Malliavin differentiable and we have that


<div>
 $$D\U r \int\U {0}^t X(s) dW(s)=X(r)+\int\U {r}^t X(s) dW(s), \quad\forall r\leq t.$$
</div>





Proof. Suppose that $D\U tX$ is progressively measurable. Then, using
the previously studied divergence [property](https://nowheredifferentiable.com/2022-07-02-Malliavin-Calculus-4/#:~:text=be%20a-,stochastic,-process%20such%20that) and the fact that the
Skorohod integral is an [extension of the Itô integral](https://nowheredifferentiable.com/2022-06-10-Malliavin-Calculus-2/#:~:text=As%20we%20saw%20in%20the%20previous%20theorem) gives


<div>
 $$\begin{aligned}
        D\U r \int\U {0}^t X(s) dW(s) & =D\U r(\delta X1\U {[0,t]}) =X(r)1\U {[0,t]}(r)+\delta (D\U rX1\U {[0,t]}) \\&=X(r)+\int\U {0}^t D\U r(X(s)) dW(s).
    \end{aligned}$$
</div>

  We consider the chaos expansion of $X$. Then, as was
seen [previously](https://nowheredifferentiable.com/2022-06-10-Malliavin-Calculus-2/#:~:text=fn-,appearing,-in%20its%20chaos), we have that


<div>
 $$f\U n(t\U 1,\ldots,t\U n,t)=0,\quad\forall t\leq\max\U {i=1,\ldots,n} t\U i .$$
</div>


So, writing the chaos expansion for $D\U rX(s)$ gives


<div>
 $$D\U rX(s)=\sum\U {n=0}^{\infty}  nI\U {n-1}(f\U n(\cdot ,r,s))=0, \quad\forall r>t.$$
</div>


Substituting in the first equation we derived shows that


<div>
 $$D\U r \int\U {0}^t X(s) dW(s)=X(r)+\int\U {r}^t X(s) dW(s).$$
</div>

  As a result,
we only need to show that $D\U r X$ is progressively measurable for all
$r<t$. This follows by some knowledge of how the Malliavin differential
works with conditional expectations. We haven't covered this so we refer
the reader to [1](https://link.springer.com/book/10.1007/978-3-540-78572-9) page 34. ◻


Our second lemma shows how to differentiate deterministic integrals. In
this case, we need a stronger condition than $D\U rX(t)$ existing for each
fixed $t$.


**Lemma 2**. Let $X(s)\in \mathbb{D}^{1,2}$ be Malliavin differentiable
for each $s\in I$ with

<div>
 $$\int\U {I} \norm{D\U rX}\U {L^2(I\times\Omega)}^2dr$$
</div>


Then, given $h\in L^2(I)$ it holds that


<div>
 $$D\U t\left\langle X,h\right\rangle\U {L^2(I)}=\left\langle D\U tX,h\right\rangle\U {L^2(I)}.$$
</div>





Proof. We will apply Fubini, we have that


<div>
 $$\left\langle D\U rX,h\right\rangle\U {L^2(I)}=\int\U I\sum\U {n=0}^{\infty}nI\U {n-1}(f\U n(\cdot ,r,s))ds=\sum\U {n=0}^{\infty}nI\U {n-1}\left(\int\U If\U n(\cdot ,r,s)h(s)ds\right).$$
</div>


Where both Fubini and the commutation of the sum and the integrals are
justified by the condition of the lemma, which guarantees that the last
sum has finite $L^2(I\times\Omega)$ norm as

<div>
 $$\begin{gathered}
        \int\U {I} \norm{\sum\U {n=0}^{\infty}nI\U {n-1}\left(\int\U If\U n(\cdot ,r,s)h(s)ds\right)}\U {L^2(\Omega)}^2d r  \\
        \leq \int\U {I}\sum\U {n=0}^{\infty}n^2 \left(\int\U \mathbb{R}\norm{I\U {n-1}f\U n(\cdot ,r,s)}^2\U {L^2(\Omega)}d r\right)ds \norm{h}^2\U {L^2(I)}\\
        =\norm{h}^2\U {L^2(I)}\int\U {I}\sum\U {n=0}^{\infty}\norm{D\U tX}\U {L^2(I\times\Omega)}d t<\infty .
    \end{gathered}$$
</div>

  Where in the first inequality we applied Fubini,
Cauchy Schwartz, and the triangle inequality, and in the equality, we
used our old calculation of the [norm of the Malliavin derivative](https://nowheredifferentiable.com/2022-07-02-Malliavin-Calculus-3/#:~:text=DX.-,Proof.,-The%20proof%20of)


<div>
 $$\norm{D\U rX}\U {L^2(I\times\Omega)}^2=\sum\U {n=0}^{\infty} n!n\|f\U n(\cdot ,r )\|\U {L^2(I^{n+1})}<\infty.$$
</div>


The result now follows by noting that, by the linearity of the iterated
integrals, it holds that the terms

<div>
 $$\int\U If\U n(\cdot ,s)h(s)ds$$
</div>

  Is the
chaos expansion of $\left\langle X,h\right\rangle\U {L^2(I)}$. ◻


In particular, by setting $h=1\U {[0,t]}$, this shows that


<div>
 $$D\U r \int\U {0}^t X(s)ds=\int\U {0}^t D\U rX(s) ds.$$
</div>

  That is, we can commute
the derivative with deterministic integrals. The previous two lemmas
together with the chain rule show that, if we take $X\U 0\in {\mathbb R}$,
and the solution to our SDE verifies all necessary conditions, then


<div>
 $$D\U rX(t)=\sigma(X\U r)+\int\U {r}^tb'(X(s))D\U rX(s) ds+\int\U {r}^t \sigma'(X(s))D\U rX(s) dW(s) .$$
</div>




**Proposition 1**. Given our [SDE](https://nowheredifferentiable.com/2022-11-03-Mallaivin-Calculus-6/#:~:text=working%20with%20an-,SDE,-of%20the%20form) with
$\sigma ,b\in C^1\U b({\mathbb R})$ it holds that there exists a unique
solution $X\U t$ and for all $r\leq t$ we have

<div>
 $$\begin{gathered}
        D\U rX(t)=\sigma(X\U r)+\int\U {r}^tb'(X(s))D\U rX(s) ds+\int\U {r}^t \sigma'(X(s))DX(s) dW(s) .
    \end{gathered}$$
</div>





Proof. The proof is quite technical and we merely sketch it. The full
detail in [2](https://www.cambridge.org/core/books/introduction-to-malliavin-calculus/8E17E009769FE6797351721C024BDCAE) page 120. By the previous discussion, it
is only necessary to show that $X$ verifies the conditions of the lemma,
i.e. is Malliavin differentiable and its differential verifies that


<div>
 $$\int\U \mathbb{R}\norm{D\U tX}\U {L^2(I\times\Omega)} d t<\infty.$$
</div>

  This
is proved by a Picard iteration


<div>
 $$X\U {n+1}=x\U 0+\int\U {0}^t b(X\U n(s)) ds+\int\U {0}^t\sigma (X\U n(s)) dW(s).$$
</div>


The aim is to prove that $X\U n$ are differentiable with


<div>
 $$\norm{D\U rX\U n}\U {L^2(I\times\Omega)}^2<\infty , \quad\forall r\in I, \quad\forall n\in \mathbb{N}.$$
</div>


For the case $n=0$ this is clear as we have that


<div>
 $$D\U rX\U 1(t)=D\U r[x\U 0+b(x\U 0)t+\sigma (x\U 0) W(t)]=\sigma(x\U 0)+1\U {[r,t]}.$$
</div>


For the general case, the condition of the **Lemma 1** is a consequence of
the hypothesis of induction on $X\U n$ and the chain rule. Verifying the
conditions of **Lemma 2** (and in fact stronger bounds on the supremum of
$X$) can be done using the Burkholder--David--Gundy inequality. Once
that is done, one can prove through a discrete version of Gronwall's
inequality that $D\U rX\U n$ are bounded uniformly in $n$. Since we know by
classical theory of SDEs that $X\U n\to X\in L^2(I\times\Omega)$ this is
sufficient to show that

<div>
 $$\lim\U {n \to \infty}D\U rX\U n=D\U rX.$$
</div>

  Completing
the proof. ◻


We now show how to obtain an explicit expression for $D\U rX$ by using
that the equation verified by $D\U rX$ is linear (in $D\U rX$ as opposed to
$X$). Doing so uses a generalized version of Ito's formula for
stochastic coefficients.


**Theorem 1**. Let $b,\sigma \in C^1\U b(I)$ and $X$ verify the SDE


<div>
 $$X(t)=b(X(t))d t +\sigma(X(t)) dW(t).$$
</div>

  Then $X(t)$ is Malliavin
differentiable on $[0,t]$ with


<div>
 $$D\U r X\U t=\sigma\left(X\U t\right) \exp \left(\int\U r^t\left(b\left(X\U s\right)-\frac{1}{2}\left(\sigma^{\prime}\right)^2\left(X\U s\right)\right) d s+\int\U r^t \sigma^{\prime}\left(X\U s\right) d W(s)\right).$$
</div>




Proof. Let us fix any $r\leq t$ and set. Then


<div>
 $$Y\U r(s):=D\U rX(s);\quad  u(s):=b'(X(s));\quad v(s):=\sigma'(X(s))$$
</div>

  Then
we have that, since $b',\sigma '$ are bounded,
$u\in \mathbb{L}^1([0,t]\times\Omega),v\in \mathbb{L}^2([0,t]\times\Omega)$
and for each fixed $r\in  {\mathbb R}$ it holds that


<div>
 $$Y\U r(s)=Y\U r(r)+\int\U {r}^t u(s)Y\U r(s) ds+\int\U {r}^t v(s)Y\U r(s)  dW(s) .$$
</div>


Where we define $Y\U r(0):=\sigma (X\U r)$. Symbolically we have the family
of linear SDEs starting at time $r$


<div>
 $$dY\U r(s)=u(s)Y\U r(s) ds+v(s)Y\U r(s)  dW(s);\quad Y\U r(r)=\sigma(X(r)).$$
</div>


Consider


<div>
 $$Z(t):=\int\U r^t\left(u(t)-\frac{1}{2}v^2(s)\right) d s+\int\U r^t v(s) d W(s)$$
</div>


Which solves the differential equation


<div>
 $$dZ=\left(u-\frac{1}{2}v^2\right)d t+v(s)dW(s) .$$
</div>

  Applying Itô to
$g(z):=e^z$ gives


<div>
 $$d g(Z)=g'dZ+\frac{1}{2}g''v^2d t= e^Z[(u-\frac{1}{2}v^2+\frac{1}{2}v^2)d t+vdW]\\=
            g(Z)(u d t +vdW).$$
</div>

  Setting $Y\U r=Y\U r(r)g(Z)$ proves the
result by the uniqueness of solutions as both sides verify the same SDE
(note that $Y\U r(r)g(Z)$ has the same stochastic differential as $g(Z)$
but now takes initial data $Y\U r(r)$). ◻



We end this post by noting that [Proposition $1$](https://nowheredifferentiable.com/2022-11-03-Mallaivin-Calculus-6/#:~:text=it-,holds,-that%20there%20exists) has a
multidimensional generalization which can also be found in Nualart's
book [2](https://www.cambridge.org/core/books/introduction-to-malliavin-calculus/8E17E009769FE6797351721C024BDCAE), on page 119.
