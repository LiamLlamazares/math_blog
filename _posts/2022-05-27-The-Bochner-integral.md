---
layout: post
title: The Bochner integral
subtitle: Wait a second, how many integrals are there?
thumbnail-img: /assets/img/Hytonen.jpg
share-img: /assets/img/Hytonen.jpg
tags: [Analysis in Banach spaces]
authorpost: L.Llamazares-Elias
---

This is the first post in a series on extending analysis from
real-valued functions to functions valued in Banach spaces. Our first
topic is the Bochner integral. That is, the extension of the Lebesgue
integral to functions valued in Banach spaces.

# Three line summary

- The Bochner integral is a way of integrating functions $f$ from a
  measure space to a Banach space.

- Like the Lebesgue integral, it is first constructed for piecewise
  constant functions $\mathcal{A}$ and extended continuously to the
  completion $\overline{\mathcal{A}}$.

- The completion $\mathcal{A}$ can be explicitly described as the
  space of functions with separable image and with finite $L^1$ norm.
  This naturally leads to the definition of  $L^p$ spaces.

# Notation

1.  We consider a measure space $(\Omega,\mathcal{F},\mu )$ which may
    not be $\sigma$-finite,  and a Banach space $(X,\mathcal{B}(X))$
    where $\mathcal{B}$ is the Borel  sigma-algebra (that is, the
    smallest $\sigma$-algebra on $X$ containing all of the open sets) of
    $X$.

2.  We denote the dual space of $X$ as $X^\star $ and given $x^\star  \in X^\star $ we
denote the pairing of $x\in X$ and $x^\star $ as $(x,x^\star ):= x^\star (x)$.

3.  Given a subset $A\subset \Omega$ we denote the indicator function of
    $A$ as $1\U A$.

4.  Given $f: \Omega \to \mathbb{R}$ and $x \in X$ we define the
    function $f\otimes x: \Omega \to X$ by

<div>
$$\begin{aligned}
f \otimes x(\omega):= f(\omega)x.

\end{aligned}$$

</div>

# Strong measurability

Our goal is to define integration for functions valued in a Banach space

<div>
$$f:(\Omega,\mathcal{F},\mu)\to ((X,\left\lVert \cdot \right\rVert),\mathcal{B}(X)).$$
</div>

When working with measure spaces, we are, in general, not interested in
what happens on sets of measure $0$.  As a result, we are contented with
properties of interest holding perhaps not everywhere but almost
everywhere.

<b>Definition 1</b>. A property is said to hold $\mu$-almost everywhere
if there exists a set $N\in \mathcal{F}$ with $\mu(N)=0$ such that the
property holds on $\Omega\setminus N$.

As anticipated, we first consider the class of simple functions

<div>
$$\mathcal{A}=\left\{\sum_{k=1}^{n} 1_{A_k} \otimes x_k: \quad  x_k\in X \text{ and }  A_k \in \mathcal{F}\text{ with } \mu(A_K)< \infty\right\}.$$
</div>

We can define their integral quite naturally as

<div>
$$\int_\Omega f \,\mathrm{d}\mu=\int_\Omega \sum_{k=1}^{n} 1_{A_k} \otimes x_k\,\mathrm{d}\mu=\sum_{k=1}^n x_k\mu({A_k}).$$
</div>

If we take equivalence classes and identify functions that are equal
$\mu$ almost everywhere, we can define the norm

<div>
$$\left\lVert f \right\rVert_\mathcal{A}:=\int_\Omega \left\lVert f \right\rVert \,\mathrm{d}\mu , \quad\forall f\in \mathcal{A}.$$
</div>

A verification shows that integration is linear and for all
$f\in\mathcaalign

<div>
$$\label{triangle}
\left\lVert \int\U \Omega f \,\mathrm{d}\mu \right\rVert\leq\int\U \Omega \left\lVert f \right\rVert \,\mathrm{d}\mu=\left\lVert f \right\rVert\U \mathcal{A}$$
</div>

That is, integration is a linear and continuous map

<div>
$$\int\U \Omega \cdot \,\mathrm{d}\mu : \left(\mathcal{A},\left\lVert \cdot \right\rVert\U \mathcal{A}\right)\to (X,\left\lVert \cdot \right\rVert).$$
</div>

Since $X$ is a complete, we can  <a href="https://en.wikipedia.org/wiki/Continuous\U linear\U extension">linearly
extend</a>
integration in a unique way to the completion $\overline{\mathcal{A}}$
of $(\mathcal{A},\left\lVert \cdot \right\rVert_A)$. The space
$\overline{\mathcal{A}}$, which can be built through taking limits of
simple functions, is thus the space of functions that we can integrate.
Our next step is to figure out what this is.

\star \star Definition 2\star \star . \star We say a function
$f:(\Omega,\mathcal{F})\to (X,\mathcal{B}(X))$ is $\mu$-strongly
measurable if there exists a sequence of simple functions $f_n$ such
that

<div>
$$\begin{align}
f=\lim\U {n \to \infty} f\U n \quad \mu\text{-almost everywhere}.

\end{aligned}$$

</div>

\star

Since the simple $f_n$ are \star separately valued\star (that is,
$f_N(\Omega )\subset X$ is separable), $f$ will also be (almost
everywhere) separably valued. As a result we will always end up working
with separable Banach spaces. The following properties are of use

 <a name="ex:separable">
\star \star Exercise 1\star \star  </a> . Let $X$ be a \star \star separable\star \star  Banach space with dual $X^\star $
, show that

1.  There exists  $\left\{x*n^\star \right\}*{n=1}^\infty\subset X^\star $ such
    that

<div>
$$\begin{aligned}
\left\lVert x \right\rVert= \sup\U {n \geq1} \left| (x,x\U n^\star ) \right|.

\end{aligned}$$

</div>

Such a sequence is called a \star norming sequence\star .

2.  The Borel $\sigma$-algebra $\mathcal{B}(X)$ is equal to the
    $\sigma$-algebra generated by  $\left\{x_n^\star \right\}_{n=1}^\infty$,
    and by $X^\star $. That is,

<div>
$$\begin{aligned}
\mathcal{B}(X)=\sigma\left(\left\\{x\U n^\star \right\\}\U {n=1}^ \infty\right)=\sigma(X^\star )

\end{aligned}$$

</div>

If $X$ is not separable, the inclusion
$\mathcal{B}(X)\subset \sigma(X^\star )$ may fail. See
<a href="https://link.springer.com/book/10.1007/978-94-009-3873-1">Vakhania, 2012</a> page 23 for a counterexample.

3.  A function $f: \Omega \to X$ is measurable if and only if it is
    \star weakly measurable\star . That is, if and only if for all $x^\star \in X^\star $
the function $(f,x^\star ): \Omega \to \mathbb{R}$ is measurable.

4.  The dual $X^\star $ with the weak-$^\star $ topology (the topology generated
    by $X$ viewed as a subset of $X^{**}$) is separable .

<div class="exercise-container">
<button class="exercise-button" onclick="toggleExercise(this)">Hint</button>
<div class="exercise-text">

1.  Consider a countable dense subset $\left\{x_n\right\}_{n=1}^\infty$
    of $X$. By the Hahn-Banach theorem, there exists $x_n^\star \in X^\star $ such
    that

<div>
$$\begin{aligned}
(x\U n,x\U n^\star )= \left\lVert x\U n \right\rVert, \quad \left\lVert x\U n^\star  \right\rVert=1.

\end{aligned}$$

</div>

Show that $x_n^\star $ satisfies the desired property.

2.  The inclusion
    $\sigma (X^\star ) \subset \sigma\left(\left\{x_n^\star \right\}_{n=1}^ \infty\right)$
    always holds as the preimage by a continuous function of an open set
    is open.  To show the reverse inclusion, prove that every open ball
    in $X$ can be written as a countable union of balls
    $\overline{B}_r(x):= \left\{y \in X: \left\lVert x-y \right\rVert\leq r\right\}$.
    Now show that

<div>
$$\begin{aligned}
\overline{B}\U r(x)=\left\\{x\in X: \sup\U {n \geq1}(x,x\U n^\star ) \leq r\right\\} \subset \sigma\left(\left\\{x\U n^\star \right\\}\U {n=1}^ \infty\right).

\end{aligned}$$

</div>

To show that the inclusion
$\mathcal{B}(X)\subset \sigma(X^\star )$ may fail for

3.  The implication always holds. Use the previous point to prove that
    weakly measurable functions in separable Banach spaces are
    measurable.

4.  By the Hahn Banach theorem, a linear subspace $Y \subset X^\star $ is
dense if and only if it separates points. That is, for all $x\in X$
there exists $x^\star \in Y$ such that $x^\star (x)\neq 0$. Use this to show
that the space spanned by $\left\{x_n^\star \right\}_{n=1}^\infty$ is
dense in $X^\star $.
</div>
</div>

The following characterizes the space of strongly measurable functions

 <a name="thm:pettis">
\star \star Theorem 3\star \star  </a>  (Pettis measurability theorem). \star A function
$f:\Omega\to X$ is $\mu$-strongly measurable if and only if $f$ is
$\mu$-almost everywhere separately valued and $(f, x^\star )$ is $\mu$
strongly measurable for all $x^\star \in X^\star $.\star

\star <b>Proof.</b>\star We first prove the implication. For some
$x_k^{(n)} \in X , A_k^{(n)} \in \mathcal{F}$,

<div>
$$\begin{aligned}
f= \lim\U {n \to \infty} f\U n=\lim\U {n \to \infty} \sum\U {k=1}^n  1\U {A\U k^{(n)}}\otimes x^{(n)}\U {k} \quad \mu\text{-almost everywhere}.

\end{aligned}$$

</div>

As a result, $f$ takes almost everywhere values in the
separable space spanned by the countably many $x_k^{(n)}$. To see that
$(f,x^\star )$ is $\mu$-strongly measurable  we note that $g_n :=(f_n,x^\star )$
are simple functions and

<div>
$$\begin{aligned}
(f,x^\star )= \lim\U {n \to \infty} g\U n \quad \mu\text{-almost everywhere}.

\end{aligned}$$

</div>

We now prove the reverse implication. By assumption,
there exists $\Omega _1 \subset \Omega$ such that $\mu (\Omega _1^c)=0$
and $X_1=\overline{f(\Omega_1 )}$ is separable. As a result,  and by
point $1$ of exercise <a href="#ex:separable">1</a> there exists a norming sequence
$\left\{x_n^\star \right\}_{n=1}^\infty \subset X_1$.

Since we only need to prove limits almost everywhere, we can suppose
that $f$ is separably valued by restricting to $\Omega _1$. Now, by
assumption the functions $g_n:=(f,x_n^\star )$ are $\mu$-strongly measurable.
Let $K_n$ be the support of $g_n$ and $K=\cup_{n \geq 1}K_n$. By
definition of strongly $\mu$-measurable function and since the union of
countable sets is countable, $K$ is  $\sigma$-finite. Since $x_n^\star $
separate points, $f$ is $0$ outside of $K$, and by restricting to $K$ we
can suppose that $\mu$ is $\sigma$-finite.

Let $\left\{x_n\right\}_{n=1}^\infty$ be a countable dense subset of
$X_1$. Given $n \in \mathbb{N}$, we define $\varphi_n (x)$ to be the
$x_k \in \left\{x_j\right\}_{j=1}^ n$ which is the closest to $x$, and
where in the case of a tie we take the one with the smallest index $j$.
We can now define the simple functions

<div>
$$\begin{aligned}
F\U n := \varphi \U n(f(x)).

\end{aligned}$$

</div>

The function $F_n$ takes at most $n$-different values
$x_1,\dots, x_n$ with

<div>
$$\begin{align}
\label{eq:separably\U valued}
\left\\{F\U n=x\U k\right\\}=\left\\{\left\lVert f- x\U k \right\rVert = \min\U {1\leq j \leq n} \left\lVert f- x\U j \right\rVert < \min\U {1 \leq j <k} \left\lVert f-x\U j \right\rVert\right\\}.

\end{align}$$

</div>

Since $(f-x_k,x_n^\star )$ is $\mu$-strongly measurable, we
deduce that the following function is measurable almost everywhere.

<div>
$$\begin{aligned}
\left\lVert f- x\U k \right\rVert= \sup\U {n \geq1} (f- x\U k,x\U n^\star ).

\end{aligned}$$

</div>

So, without loss of generality, we may suppose they are
measurable by restricting once more. Then, by
(\ref{eq:separably\U valued})  $F_n$ is measurable. Since we had
restricted $u$ to be $\sigma$-finite, we may take a partition
$\left\{\Omega _n\right\}_{n=1}^\infty$ of $\Omega$ with finite measure.
Consider $f_n:=F_n 1_{\Omega _n}$, we have that $f_n$ is $\mu$ simple
(we need to multiply by $1_{\Omega _n}$ so that the support of the
indicators have finite measure) and converges to $f$ almost
everywhere. ◻

If we include $x_0=0$ in the norming sequence of Theorem
<a href="#thm:pettis">3</a>, we have
that $\left\lVert f_n-f \right\rVert$ as in the proof above is bounded
by $\left\lVert f \right\rVert$ almost everywhere and obtain the
following corollary which will be used later to show the density of
simple functions in the integrable ones.

 <a name="density corollary">
\star \star Corollary 4\star \star  </a> . \star Let $f : \Omega \to X$ be $\mu$-strongly measurable.
Then, there exists a sequence of simple functions $f_n$ converging to
$f$ almost everywhere and such that

<div>
$$\begin{aligned}
\left\lVert f\U n-f \right\rVert \leq \left\lVert f \right\rVert, \quad  \mu \text{-almost everywhere}.

\end{aligned}$$

</div>

\star

Most typically, one works in the case where $\mu$ is $\sigma$-finite
(for example, if $\mu$ is the Lebesgue measure or any probability
measure) and identifies functions that are equal almost everywhere. In
this case, the following more simple statement holds.

 <a name="thm:pettis2">
\star \star Theorem 5\star \star  </a>  (Pettis theorem for $\sigma$-finite measures). \star Let
$(\Omega, \mu, \mathcal{F})$ be a $\sigma$-finite measure space and
identify functions that are equal almost everywhere. Then $f$ is
$\mu$-strongly measurable if and only if $f$ is separately valued and
measurable.\star

\star <b>Proof.</b>\star Let $f$ be $\mu$-strongly measurable. Then, $f$ is the limit of
separately valued and measurable functions. As a result, $f$ is
separately valued and measurable.

Suppose now that $f$ is separately valued and measurable. Then, the same
is true for $f 1_{\Omega_n}$ where
$\left\{\Omega_n\right\}_{n=1}^\infty$ is a partition of $\Omega$ with
finite measure. Moreover, these functions are strongly measurable as the
measure of $\Omega _n$ is finite (one can start from $f 1_{\Omega_n}$
and form $F_n$ as in the previous proof converging to $f 1_{\Omega _n}$)
and since they form a partition of $\Omega$,

<div>
$$\begin{aligned}
f=\lim\U {n \to \infty} f 1\U {\Omega\U n}.

\end{aligned}$$

</div>

By a basic argument, the limit of $\mu$-strongly
measurable functions is $\mu$-strongly measurable and we conclude that
$f$ is $\mu$-strongly measurable, as desired. ◻

# Construction of the Bochner integral

Since the norm $\left\lVert \cdot  \right\rVert$ is a continuous
function, given a measurable function $f: \Omega \to X$, the
\star real-valued\star function
$\left\lVert f \right\rVert: \Omega \to \mathbb{R}$ is also measurable.
As a result, we can define the Lebesgue integrals

<div>
$$\begin{align}
\label{Lp}
\left\lVert f \right\rVert\U {L^p(\Omega\to X)} & :=\left(\int\U \Omega \left\lVert f \right\rVert^p \,\mathrm{d}\mu\right)^{1/p},\quad \quad p \in [1,\infty).
\end{align}$$
</div>

Likewise, the sets $\left\lVert f \right\rVert>r$ are in
the $\sigma$-algebra $\mathcal{F}$ and we can define

<div>
$$\begin{align}
\label{Linfty}
\left\lVert f \right\rVert\U {L^\infty(\Omega\to X)} & :=\inf\\{r>0: \mu ( \left\lVert f \right\rVert> r)=0\\},
\end{align}$$
</div>

where the infimum is defined to be $\infty$ if the set
is empty.

Knowledge of the real-valued case shows that
(\ref{Lp}) and
(\ref{Linfty}) define
a seminorm on the spaces of measurable function where they are finite,
and they define a norm if we define the equivalence relation

<div>
$$\begin{aligned}
f \sim g\quad \text{ if } f=g\quad \mu\text{-almost everywhere}.
\end{aligned}$$
</div>

Following common practice, we will identify functions
that are equal almost everywhere from now on and make no distinction
between functions and their equivalence classes. Finally, we arrive at
the following definition.

 <a name="def:Lp">
\star \star Definition 6\star \star  </a> . \star Given a measure space $(\Omega,\mathcal{F},\mu)$, a
Banach space $(X,\mathcal{B}(X))$ we define the space of $p$-integrable
functions as (the equivalence classes)

<div>
$$\begin{aligned}
L^p(\Omega \to X) & :=\left\\{f:\Omega\to X: f \text{ is strongly measurable and } \left\lVert f \right\rVert\U {L^p(\Omega \to X)}<\infty\right\\}.

\end{aligned}$$

</div>

\star

If one wishes to be explicit about the underlying measure space one can
also write $L^p(\Omega,\mathcal{F},\mu, X)$. As in the real case, the
$L^p$ spaces are complete.

 <a name="thm:completeness">
\star \star Theorem 7\star \star  </a>  (Fischer-Riesz). \star The space $L^p(\Omega\to X)$ is a Banach
space for all $p\in [1,\infty].$\star

\star <b>Proof.</b>\star The proof follows along the lines of the real case,
substituting the absolute value in $\mathbb{R}$ by the norm in $X$ as
necessary. We first prove the case $p \in [1,\infty)$ Recall that a
normed space is complete if and only if every absolutely convergent
series converges.That is, we need to show that if
$f_n \in L^p(\Omega \to X)$ is such that

<div>
$$\sum\U {n=1}^\infty \left\lVert f\U n \right\rVert\U {L^p(\Omega\to X)}<\infty.$$
</div>

Then there exists $f\in L^p(\Omega\to X)$ such that

<div>
$$f=\sum\U {n=1}^\infty f\U n\in L^p(\Omega\to X).$$
</div>

To do so, one first
applies
<a href="https://en.wikipedia.org/wiki/Minkowski\U inequality#:~:text=.-,Minkowski%27s,-integral%20inequality%5B">Minkowski's</a>
inequality for real-valued functions to show that

<div>
$$\sum\U {n=1}^\infty \left\lVert f\U n \right\rVert\U X\in L^p(\Omega\to\mathbb{R}).$$
</div>

Thus, the sum is finite almost everywhere. Since $X$ is complete, we
have that the above sum converges pointwise almost everywhere to some
function

<div>
$$f(\omega):=\sum\U {n=1}^\infty f\U n(\omega)\in X.$$
</div>

Furthermore
we have that $f$ is strongly measurable as it is the limit of strongly
measurable functions. Finally, using Fatou's lemma for real-valued
functions and the triangle inequality for norms shows that

<div>
$$\begin{aligned}
\left\lVert f-\sum\U {n=1}^N f\U n \right\rVert\U {L^p(\Omega\to X)} & =\left\lVert \sum\U {n=N}^\infty f\U n \right\rVert\U {L^p(\Omega\to X)}\leq \liminf\U {M\to \infty}\left\lVert \sum\U {n=N}^M f\U n \right\rVert\U {L^p(\Omega\to X)} \\&\leq \liminf\U {M\to \infty}\sum\U {n=N}^M \left\lVert f\U n \right\rVert\U {L^p(\Omega\to X)}=\sum\U {n=N}^\infty \left\lVert f\U n \right\rVert\U {L^p(\Omega\to X)}\xrightarrow{N\to\infty} 0.

\end{aligned}$$

</div>

Which shows convergence in $L^p(\Omega\to X)$ for
$p\in [1,\infty)$.

For the case $p=\infty$ consider a Cauchy sequence
$f_n \in L^p(\Omega \to X)$ and write

<div>
$$\begin{aligned}
A\U {nm}:=\left\\{\omega\in \Omega: \left\lVert f\U n(\omega)-f\U m(\omega) \right\rVert \leq\left\lVert f\U n-f\U m \right\rVert\U {L^\infty(\Omega \to X)}\right\\}, \quad A := \bigcup\U {m,n=1}^\infty A\U {nm}.

\end{aligned}$$

</div>

By construction, $A_{nm}$ and thus $\mathbb{A}^c$ have
measure zero and $f_n$ converges uniformly on $A$. As a result, $f_n$
converges almost everywhere to some $f\in L^\infty(\Omega\to X)$. This
completes the proof. ◻

Just as in the case of Lebesgue integrals, the proof of the completeness
of $L^p(\Omega\to X)$ serves to show that every convergent sequence must
have a subsequence converging almost everywhere. This proposition is not
necessary for the rest of the constructions, it's just a nice property
to have in reserve.

\star \star Proposition 8\star \star . \star Let $f_n\to f\in L^p(\Omega\to X)$, then there
exists a subsequence $f_{n_k}$ converging to $f$ almost everywhere.\star

\star <b>Proof.</b>\star In the proof of the above proposition, we saw that for any
absolutely convergent sum converges almost everywhere to its limit.
Further, since  $f_n$ is Cauchy, we can extract a subsequence  $f_{n_k}$
with  $\|f_{n_k}-f_{n_{k-1}}\|\leq 2^{-k}$. By construction, the
sequence

<div>
$$\sum\U {k=0}^{\infty} f\U {n\U k}-f\U {n\U {k-1}},$$
</div>

is normally
convergent and converges in $f$. By the above discussion we conclude the
proof. ◻

Ok, so we've constructed some spaces of $p$-integrable functions and
shown that they are complete. You know where this is going. Next stop is
density town. In the standard construction of the Lebesgue integral, it
is used that every measurable function to $\mathbb{R}$ can be pointwise
approximated by simple functions. One can achieve the same result for
arbitrary metric spaces if the image of $f$ is separable.

\star \star Proposition 9\star \star . \star Every function in $L^p(\Omega\to X)$ is the limit
almost everywhere and in the norm of a sequence of simple functions.\star

\star <b>Proof.</b>\star By Corollary <a href="#density corollary">4</a>, there exists a sequence of simple
functions $f_n$ converging to $f$ almost everywhere and such that
$\left\lVert f_n-f \right\rVert<\left\lVert f \right\rVert$ almost
everywhere. By the dominated convergence theorem for \star real valued\star
functions, we have that

<div>
$$\lim\U {n\to\infty}\left\lVert f\U n-f \right\rVert^p\U {L^p(\Omega\to X)}=\lim\U {n\to\infty}\int\U \Omega\left\lVert f\U n-f \right\rVert^p\,\mathrm{d}\mu=\int\U {\Omega}\lim\U {n \to \infty}\|f\U n-f\|^p \,\mathrm{d}\mu =0.$$
</div>

◻

As a corollary, we obtain the following

\star \star Corollary 10\star \star . \star The simple functions $\mathcal{A}$ are a dense subset
of $L^p(\Omega\to X)$.\star

Since  $L^1(\Omega\to X)$ is complete, we have that the closure of
$\overline{\mathcal{A}}$ with the norm
$\left\lVert \cdot  \right\rVert_{L^1(\Omega \to X)}$ is
$L^1(\Omega\to X)$. Furthermore, by the triangle inequality
(\ref{triangle}) ,
integration is continuous with this norm. This continuity allows us to
extend integration to $L^1(\Omega \to X)$ and shows that the space of
integrable functions is $L^1(\Omega\to X)$.

 <a name="def int">
\star \star Definition 11\star \star  </a> . \star We define the integral on $L^1(\Omega\to X)$ as the
unique continuous extension with the norm
$\left\lVert \cdot \right\rVert_{L^1(\Omega\to X)}$ of the integral on
$\mathcal{A}$. That is, given $f\in L^1(\Omega\to X)$ we define

<div>
$$\int\U \Omega f \,\mathrm{d}\mu:=\lim\U {n\to\infty} \int\U \Omega f\U n \,\mathrm{d}\mu.$$
</div>

Where $f_n\in \mathcal{A}$ is any sequence such that
$\left\lVert f-f_n \right\rVert_{L^1(\Omega\to X)}\to 0$.\star

\star \star Observation 1\star \star . We could also work with the spaces

<div>
$$\begin{aligned}
\hat{L}^p(\Omega,\mathcal{F},\mu,X) & =\left\\{f:\Omega\to X: \int\U \Omega \left\lVert f \right\rVert^p \,\mathrm{d}\mu<\infty\right\\}.

\end{aligned}$$

</div>

These spaces are once more complete, however, they do
not contain simple functions as a dense subset. As a result, given
$f \in \hat{L}^1(\Omega \to X)$ it is not possible to make sense of the
expression $\int_\Omega f \,\mathrm{d}\mu$.

# Familiar properties

Many properties of integration hold for the Bochner integral as well.
For example, the following is a result of the definition of the Bochner
integral and a passage to the limit, as it holds for simple functions.

 <a name="corollary easy">
\star \star Corollary 12\star \star  </a> . \star Let $f\in L^1(\Omega,X)$ with $X$ a Banach space,
then\star

1.  \star $\left\lVert \int_\Omega f \,\mathrm{d}\mu \right\rVert\leq\int_\Omega{\left\lVert f \right\rVert\,\mathrm{d}\mu}$\star

2.  \star Let $Y$ be another Banach space and $L\in L(X,Y)$. Then

<div>
$$\int\U \Omega (L\circ f) \,\mathrm{d}\mu=L\left(\int\U \Omega f \,\mathrm{d}\mu\right).$$
</div>

\star

Knowledge of scalar-valued results also goes a long way; for example, we
can prove the following

 <a name="ex:fubini">
\star \star Exercise 2\star \star  </a>  (Fubini-Tonelli). Let
$(\Omega_1, \mathcal{F}_1 , \mu _1 )$ and
$(\Omega_2, \mathcal{F}_2 , \mu _2 )$ be $\sigma$-finite measure spaces
and consider the space $\Omega_1\times \Omega_2$ with the
$\sigma$-algebra $\mathcal{F}_1 \otimes \mathcal{F}_2$ generated by
sets of the form $A_1 \times A_2$ with $A_i \in \Omega _i$ and the
unique measure $\mu _1 \otimes \mu _2$ such that
$(\mu _1 \otimes \mu _2)(A_1 \times A_2)=\mu _1(A_1)\mu _2(A_2)$. Let
$X$ be a Banach space and $f:\Omega_1\times \Omega_2 \to X$ be strongly
measurable. Then

1.  The functions $f(\omega_1,\cdot )$ and $f(\cdot,\omega_2)$ are
    strongly measurable.

2.  If any of the following integrals is finite

<div>
$$\begin{align}  \label{norm ints}
\int\U {\Omega\U 1 \times \Omega \U 2} \left\lVert f \right\rVert \,\mathrm{d}(\mu\U 1 \otimes \mu \U 2), \quad  \int\U {\Omega\U 1}\left(\int\U {\Omega\U 2} \left\lVert f \right\rVert\,\mathrm{d}\mu\U 2\right)\,\mathrm{d}\mu\U 1, \quad \int\U {\Omega\U 2}\left(\int\U {\Omega\U 1} \left\lVert f \right\rVert\,\mathrm{d}\mu\U 1\right)\,\mathrm{d}\mu\U 2.

\end{align}$$

</div>

Then all of the integrals in
(\ref{norm ints}) are equal, and

<div>
$$\label{ints}
\int\U {\Omega\U 1 \times \Omega \U 2} f \,\mathrm{d}(\mu\U 1 \times \mu \U 2)= \int\U {\Omega\U 1}\left(\int\U {\Omega\U 2} f\,\mathrm{d}\mu\U 2\right)\,\mathrm{d}\mu\U 1=\int\U {\Omega\U 2}\left(\int\U {\Omega\U 1} f\,\mathrm{d}\mu\U 1\right)\,\mathrm{d}\mu\U 2.$$
</div>

<div class="exercise-container">
<button class="exercise-button" onclick="toggleExercise(this)">Hint</button>
<div class="exercise-text">

1.  From Fubini's theorem, we know that the
    <a href="https://proofwiki.org/wiki/Horizontal\U Section\U of\U Measurable\U Function\U is\U Measurable">sections</a>
    $f(\omega_1,\cdot )$ and $f(\cdot,\omega_2)$ are measurable. Since
    $f$ is separately valued so are $f(\omega_1,\cdot )$ and
    $f(\cdot,\omega_2)$. As a result, by Theorem
    <a href="#thm:pettis2">5</a>,
    they are strongly measurable.

2.  By
    <a href="https://en.wikipedia.org/wiki/Fubini%27s\U theorem#Fubini%E2%80%93Tonelli\U theorem:~:text=the%20uncompleted%20product.-,For,-integrable%20functions%5B">Fubini-Tonelli's</a>
    theorem we know that if any of the integrals in
    (\ref{norm ints}) is finite, then all of them are equal. By the
    first point, we conclude from the characterization of the integrable
    functions (Definitions <a href="#def:Lp">6</a>, <a href="#def int">11</a>) that all the integrals in
    (\ref{ints}) are well
    defined, and it remains to see they are equal. To do so, let
    $x^\star \in X^\star $ be and then, by Fubini-Tonelli for real-valued
    functions

<div>
$$\begin{aligned}
\int\U {\Omega\U 1 \times \Omega \U 2} (f,x^\star ) \,\mathrm{d}(\mu\U 1 \otimes \mu \U 2) & =  \int\U {\Omega\U 1}\left(\int\U {\Omega\U 2} (f,x^\star )\,\mathrm{d}\mu\U 2\right)\,\mathrm{d}\mu\U 1=\int\U {\Omega\U 2}\left(\int\U {\Omega\U 1} (f,x^\star )\,\mathrm{d}\mu\U 1\right)\,\mathrm{d}\mu\U 2.

\end{aligned}$$

</div>

By Point $2$ of Corollary
<a href="#corollary easy">12</a> and, since we just proved that all the
integrals in (\ref{ints}) are well defined, we may pull $x^\star $ out of the
integrals. By the Hahn-Banach theorem, $X^\star $ separates points of
$X$, and the proof follows.

</div>
</div>

Sometimes the following theorem is more useful when instead of using the
product measure $\mu_1 \otimes \mu_2$ on $X \times Y$, we use its
completion $\overline{\mu_1 \times \mu_2}$. In this case,
Fubini-Tonelli's Theorem <a href="#ex:fubini">2</a> still holds. It is only necessary to note that
the sections of $f$ are now almost always measurable (see
<a href="https://www.stat.rice.edu/~dobelman/courses/texts/qualify/Measure.Theory.Tao.pdf">Tao, 2011</a> page 203 for more details).

\star \star Exercise 3\star \star (Minkowski's integral inequality). Show that given
$p \in [1,\infty)$ and $f \in L^1(\Omega_1 \to L^p(\Omega_2 \to Y))$ it
holds that

<div>
$$\left(\int\U {\Omega \U 1}\left\lVert \int\U {\Omega\U 2 } f \,\mathrm{d}\mu \U 2  \right\rVert^p \,\mathrm{d}\mu \U 1\right)^{1/p}\leq \int\U {\Omega\U 2}\left(\int\U {\Omega \U 1} \left\lVert f \right\rVert^p \,\mathrm{d}\mu\U 1\right)^{1/p}\,\mathrm{d}\mu\U 2 .$$
</div>

<div class="exercise-container">
<button class="exercise-button" onclick="toggleExercise(this)">Hint</button>
<div class="exercise-text">
Apply the triangle inequality
(\ref{triangle})
with $X= L^p(\Omega_2 \to Y)$.
</div>
</div>

\star \star Exercise 4\star \star (Dominated convergence theorem). Let
$f_n,f\in L^1(\Omega\to X)$ be such that $f_n\to f$ almost everywhere
and there exists $g\in L^1(\Omega\to X)$ such that
$\left\lVert f_n \right\rVert\leq g$ almost everywhere. Then

<div>
$$\int\U \Omega f\U n \,\mathrm{d}\mu\to \int\U \Omega f \,\mathrm{d}\mu.$$
</div>

<div class="exercise-container">
<button class="exercise-button" onclick="toggleExercise(this)">Hint</button>
<div class="exercise-text">
We have that $\left\lVert f_n-f \right\rVert\leq 2g$ almost
everywhere. As a result, by the dominated convergence theorem for
real-valued functions, we have that

<div>
$$\lim\U {n\to\infty}\int\U \Omega\left\lVert f\U n-f \right\rVert\,\mathrm{d}\mu=0.$$
</div>

The triangle inequality concludes the proof.

</div>
</div>

The dominated convergence theorem is a powerful tool that allows us to
pass to the limit under the integral sign. For example, it can be used
to show that, under necessary conditions, if $f(t,\omega )$ is
continuous (differentiable) in $t$ then so is
$\int f(t,\omega )\,\mathrm{d}\mu(\omega)$ (see
<a href="https://nowheredifferentiable.com/2023-01-29-PDE-1-Fourier/#:~:text=assumed%20for%20commodity.-,Proposition%201,-(Continuity%20of%20the">here</a>
for a proof). These results, together with the density of simple
functions, can be used to prove the <a href="https://nowheredifferentiable.com/2023-07-12-PDEs-3-Sobolev\U spaces/#:~:text=example%2C%208%20444R.-,Smoothing,-in">standard approximation
theorems</a>.

 <a name="thm:approx">
\star \star Theorem 13\star \star  </a>  (Convolution, regularization and smooth approximation).
\star Let $p \in [1,\infty)$ and consider $f\in L^p(\mathbb{R}^d\to X)$ and
$\phi \in L^1(\mathbb{R}^d)$.\star

1.  \star \star \star Young's inequality\star \star . The convolution

<div>
$$\begin{aligned}
f\star \phi(x):=\int\U {\mathbb{R}^d} f(x-y)\phi(y)\,\mathrm{d}y,

\end{aligned}$$

</div>

is well-defined almost everywhere and satisfies

<div>
$$\begin{aligned}
\left\lVert f\star \phi \right\rVert\U {L^p(\mathbb{R}^d\to X)}\leq \left\lVert f \right\rVert\U {L^p(\mathbb{R}^d\to X)}\left\lVert \phi \right\rVert\U {L^1(\mathbb{R}^d)}.

\end{aligned}$$

</div>

\star

2.  \star \star \star Mollifiers\star \star . Define
    $\phi_\epsilon(x):=\epsilon^{-d}\phi(x/\epsilon)$. Then,

<div>
$$f\star \phi\U \epsilon \to f \quad \text{in } L^p(\mathbb{R}^d\to X).$$
</div>

\star

3.  \star \star \star Smoothing\star \star . If $\phi \in C^k_c(\mathbb{R}^d)$ then
    $f\phi_\epsilon \in C^k(\mathbb{R}^d\to X)$ with

<div>
$$D^\alpha f\star \phi=f\star (D^\alpha \phi), \quad\forall \left| \alpha \right|\leq k.$$
</div>

\star

4.  \star \star \star Smooth approximation\star \star . Taking
    $\phi \in C_c^\infty(\mathbb{R}^d)$ to be any and normalizing so
    that $\int \phi \,\mathrm{d}x=1$ we deduce that
    $C_c^\infty(\mathbb{R}^d)$ is dense in $L^p(\mathbb{R}^d\to X)$.\star

Ok, that's it. This post was a bit more technical than some of the
others, but you get the picture. Define an integral for simple
functions, and figure out what can be approximated by simple functions.
As we saw, the extra requirement that appears over the Lebesgue case is
that the function $f$ is separately valued and justifies why, as we will
see in future posts on SPDEs, the image of $f$ is often taken to be some
separable Hilbert space. Until the next time!

A (possibly not updated) pdf of version of this page is provided [here](/assets/pdfs/Analysis in Banach spaces/The-Bochner-Integral.pdf).
