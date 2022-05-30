---
layout: post
title: The Itô integral
subtitle: Can you really construct this thing?
thumbnail-img: /assets/img/karatzas.jpg
share-img: /assets/img/karatzas.jpg
tags: [Stochastic calculus,Itô integral, Adapted processes, Progressively measurable, Square integrable continuous martingales]
---
# Three line summary

-   The Itô integral is a way of integrating random variables against
    Brownian motion.

-   The Itô integral is well defined for piecewise constant adapted
    processes $\mathcal{E}$ and turns them isometrically into square
    integrable continuous martingales ($\mathcal{M}\U I^2$).

-   As a result the Itô integral can be extended isometrically to a
    function $\overline{\mathcal{E}}\to \mathcal{M}\U I^2$. Furthermore
    $\overline{\mathcal{E}}$ can be characterised explicitly as the
    square integrable adapted processes that are measurable in time and
    space.

# Why should I care?

The Itô integral forms the basis of the whole of stochastic calculus.
This comprises SDEs, SPDEs. Knowledge of what functions can be
integrated and what properties the integrated function has is
instrumental. In this post we construct the integral and address both of
the preceding issues.

# Notation

Given two measure spaces $(\Omega,\mathcal{F}),(\Omega',\mathcal{H})$
we abbreviate that $f:\Omega\to\Omega'$ is measurable between
$\mathcal{F}$ and $\mathcal{F}'$ as $f:\mathcal{F}\to\mathcal{F}'.$
Furthermore we will take $I=\zl 0,T\zr $ or $I=\zl 0,+\infty)$ to be the index
set of our stochastic processes and write
$\mathcal{F}\U \infty:=\vee\U {t\in I}\mathcal{F}\U t$. Finally, we will denote the Borel $\sigma$-algebra on some interval $J$ by $\mathcal{B}(J)$.

# Integrable functions: progressive measurability

As we will soon see the only stochastic process that can be integrated
are the square integrable and progressively measurable ones. But what does
this mysterious term mean?


**Definition 1**. A stochastic process $\{ X\U t \}\U {t\in I}$ is
progressively measurable if
<div>
 $$X:\mathcal{B}(\zl 0,t\zr )\otimes\mathcal{F}\U t\to \mathcal{H}$$
</div>  is
measurable for all $t\in I$.


Whenever we're given a stochastic process and a filtration the first
thing to check is that it is adapted. In fact, since
$\omega\to(t,\omega)$ is
$\mathcal{F}\U t\to \mathcal{B}(\zl 0,t\zr )\otimes \mathcal{F}\U t$ measurable
for all $t$ we have that the following holds.


**Lemma 1**. Progressively measurable processes are adapted.


Additionally, stochastic processes can be viewed path-wise but also be
seen as functions of a product space, this leads to the following
definition.


**Definition 2**. We say that a stochastic process $\{X\U t\}\U {t\in I}$
is jointly measurable if
<div>
 $$X:\mathcal{B}(I)\otimes\mathcal{F}\U \infty\to \mathcal{H}$$
</div>


In the definition of progressive measurability we imposed some kind of
measurability, in fact the condition leads to the following


**Proposition 1** (Progressive implies jointly measurable). Let
$I\subset{\mathbb R}$, and $\{X\U t\}\U {t\in I}$ be progressively
measurable. Then it is also jointly measurable.



Proof. Given $A\in\mathcal{H}$ we have that
<div>
 $$\begin{gathered}
        \left.{X^{-1}}\right|\U {\zl 0,t\zr \times\Omega}(A)\in\mathcal{B}(\zl 0,t\zr )\otimes\mathcal{F}\U t\quad\forall t\in I\\ \iff X^{-1}(A)\cap(\zl 0,t\zr \times\Omega)\in\mathcal{B}(\zl 0,t\zr )\otimes\mathcal{F}\U t\quad\forall t\in I\\\implies X^{-1}(A)=\bigcup\U {n \in  \mathbb{N}}X^{-1}(A)\cap(\zl 0,t\U n\zr \times\Omega) \in\mathcal{B}(I)\otimes\mathcal{F}\U \infty
    \end{gathered}$$
</div>
Where $t\U n\in I$ is a sequence converging to the
endpoint of $I$. ◻


Note however that the converse isn't true, for example if $X$ is
constant in $t$ then, for some $B\subset \Omega$
<div>
 $$X^{-1}(A)=I\times B;\quad {X^{-1}}|\U {\zl 0,t\zr \times\Omega}(A)= \zl 0,t\zr \times B$$
</div>
So it suffices to consider some Construction where
$B\in\mathcal{F}\U \infty$ but $B\not\in\mathcal{F}\U t$. It is also
important to note the following.


**Lemma 2** (SDE coefficients are progressive). Let $X\U t$ be a
progressively measurable stochastic process and let
$f:\mathcal{H}\to\mathcal{G}$ be measurable, then $f(t,X\U t)$ is
progressively measurable.



Proof. This follows from considering $(t,\omega)\to (t,X(t,w))$. Where
the arrow is measurable as, due to the progressive measurability of $X$,
each component is adapted. ◻


The difference between progressively measurable and adapted is quite
subtle. In fact every adapted and jointly measurable stochastic process
has a progressively measurable modification (see
[1](https://link.springer.com/book/10.1007/978-1-4612-0949-2) page $5$). The proof of this fact is very
lengthy and technical. Thus, if
$X\in L^2(\mathcal{B}(I)\otimes\mathcal{F}\U \infty)$ (and in particular
is jointly measurable), we may always choose a representative that is
progressively measurable. This leads to some authors giving the
defintion of the class of Itô integrable functions in terms of joint
measurability instead of progressive measurability. In the end both lead
to equivalent definition. That said, this technicality is usually of
little importance due to the following result.


**Lemma 3** (Continuity is progressive). Let $\{X\U t\}\U {t\in I}$ be a
left or right continuous stochastic process. Then $X$ is progressively
measurable.



Proof. Suppose for example that $X$ is right continuous, then we
consider
<div>
 $$X\U {s}^{(n)}(\omega)=X\U {(k+1) ! / 2^{n}}(\omega) \text { for } \frac{k t}{2^{n}}<s \leq \frac{k+1}{2^{n}} t$$
</div>
The pre-image of any set $A\in\mathcal{H}$ is of the form
<div>
 $$X^{-1}(A)=\bigcup\U {i\in \mathbb{N}}(t\U i,t\U {i+1}\zr \times X\U {t\U i}^{-1}(A).$$
</div>
So $X^{(n)}$ is progressively measurable. We conclude as by right
continuity $\lim\U {n \to \infty}X^{(n)}=X$. ◻


Also we used that the pointwise limit of progressively measurable
functions is progressively measurable. This is because the pointwise
limit of measurable functions is measurable.


**Lemma 4**. For any $p \in\zl 1, \infty)$, the elementary processes are
$L^{p}$-dense in the space $\mathbb{L}^{p}(I\times\Omega)$ of
progressively measurable processes in
$L^p(\mathcal{B}(I)\otimes\mathcal{F}\U \infty)$. That is, for any
$Y \in \mathbb{L}^{p}$ there is a sequence $V\U {n}$ of elementary
functions such that
<div>
 $$\mathbb{E}\zl \int\U {I}|Y(t)-V\U {n}(t)|^{p} dt\zr  \longrightarrow 0.$$
</div>


The proof of this fact is also rather technical and long. See Chapter
$2$ of [2](http://galton.uchicago.edu/~lalley/Courses/385/Old/ItoIntegral-2012.pdf). Furthermore, we have that


**Theorem 1**. Let
$(\mathcal{E},\|\cdot\|\U {L^2(I\times\Omega)},\mathcal{F}\U t)$ be the set
of simple stochastic processes adapted to $\{\mathcal{F}\U t\}\U {t\in I}$
with the $L^2$ norm. Then it's completion is
<div>
 $$\mathbb{L}^2(I\times\Omega):=\{X\in L^2(\zl 0,T\zr \times\Omega)\text{ progressively measurable }\}.$$
</div>


The proof of this is by the previous approximation result together with
the fact that the Ito integral of simple processes is an isometry and
the fact that $\mathbb{L}^2(I\times\Omega)$ is complete. This last
property follows from the completeness of the $L^p$ spaces and the fact
that pointwise limits of progressively measurable functions are
progressively measurable (and from every convergent sequence in $L^p$ we
can extract a convergent sub-sequence which must also converge to the
$L^p$ limit). This finally leads us to be able to define the stochastic
integral.


**Theorem 2**. Let $t\in I$ and define for a simple process
$f\in\mathcal{E}$
<div>
 $$\int\U {0}^t X dW=\sum\U {n=0}^{N-1} X(t\U n)(W(t\cap t\U {n+1})-W(t\U n)).$$
</div>
Then the above defines an isometry to the space of continuous square
integrable martingales $\mathcal{M}\U I^2$ as
    <div>
 $$\begin{aligned}
        int: \left(\mathcal{E},\|\cdot\|\U {L^2(I\times\Omega)}\right) & \longrightarrow  \left(\mathcal{M}\U I^2,\|\cdot\|\U {L^2(I\times\Omega)}\right) \\
        X(t)                                          & \longmapsto \int\U {0}^t X dW
        .\end{aligned}$$
</div>
    Thus, it extends uniquely to the closure
$\overline{\mathcal{E}}=\mathbb{L}^2(I\times\Omega)$. Furthermore the
extension also has image in $\mathcal{M}\U I^2.$



Proof. The first part of the proof is a calculation using the
definition of integral of simple process, the adaptedness of $X$ and the
definition of $W$. The second part is slightly more tricky. The fact
that $X$ is a martingale is due to $L^2$ convergence ($L^1$ would
suffice).\
\
Then, one takes a sequence of elementary processes $X\U n$ converging to
$X$. By the first part one may apply Doob's martingale inequality and
$L^2$ convergence to get a measure of the set where the supremum
<div>
 $$\sup\U {t\in I}  |X\U n(t)-X\U m(t)|>2^{-k},$$
</div>  which can be made small for
$n,m \to\infty$. One can then extract a subsequence and apply
Borel-Cantelli to deduce that the above supremum goes to $0$ almost
everywhere. This shows that $X\U n$ is almost everywhere Cauchy in
$L^\infty$ and thus converges almost everywhere to some continuous
process $Y$. This process must be $X$ by $L^2$ convergence to $X$ which
concludes the proof. ◻

A pdf of version of this page is provided below:
<object data="/assets/ItoInt.pdf" width="1000" height="1000" type='application/pdf'></object>
