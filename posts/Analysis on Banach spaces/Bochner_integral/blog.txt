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

-   The Bochner integral is a way of integrating functions $f$ from a
measure space to a Banach space.

-   Like the Lebesgue integral, it is first constructed for piecewise
constant functions $\mathcal{A}$ and extended continuously to the
completion $\overline{\mathcal{A}}$.

-   The completion $\mathcal{A}$ can be explicitly described as the
space of functions with separable image and with finite $L^1$ norm.
This naturally leads to the definition of $L^p$ spaces.

# Notation

1.  We consider a measure space $(\Omega,\mathcal{F},\mu )$ which may
not be $\sigma$-finite, and a Banach space $(X,\mathcal{B}(X))$
where $\mathcal{B}$ is the Borel sigma-algebra (that is, the
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
$$\begin{aligned}
f:(\Omega,\mathcal{F},\mu)\to ((X,\left\lVert \cdot \right\rVert),\mathcal{B}(X)).
\end{aligned}$$
</div>

When working with measure spaces, we are, in general,
not interested in what happens on sets of measure $0$. As a result, we
are contented with properties of interest holding perhaps not everywhere
but almost everywhere.


<b>Definition 1</b>. A property is said to hold $\mu$-almost everywhere
if there exists a set $N\in \mathcal{F}$ with $\mu(N)=0$ such that the
property holds on $\Omega\setminus N$.


As anticipated, we first consider the class of simple functions


<div>
$$\begin{aligned}
\mathcal{A}=\left\{\sum\U {k=1}^{n} 1\U {A\U k} \otimes x\U k: \quad x\U k\in X \text{ and } A\U k \in \mathcal{F}\text{ with } \mu(A\U K)< \infty\right\}.
\end{aligned}$$
</div>

We can define their integral quite naturally as


<div>
$$\begin{aligned}
\int\U \Omega f \,\mathrm{d}\mu=\int\U \Omega \sum\U {k=1}^{n} 1\U {A\U k} \otimes x\U k\,\mathrm{d}\mu=\sum\U {k=1}^n x\U k\mu({A\U k}).
\end{aligned}$$
</div>



If we take equivalence classes and identify functions that are equal
$\mu$ almost everywhere, we can define the norm

<div>
$$\begin{aligned}
\left\lVert f \right\rVert\U \mathcal{A}:=\int\U \Omega \left\lVert f \right\rVert \,\mathrm{d}\mu , \quad\forall f\in \mathcal{A}.
\end{aligned}$$
</div>

A verification shows that integration is linear and for
all $f\in\mathcal{A}$.

<div>
$$\begin{align}
\label{triangle}
\left\lVert \int\U \Omega f \,\mathrm{d}\mu \right\rVert\leq\int\U \Omega \left\lVert f \right\rVert \,\mathrm{d}\mu=\left\lVert f \right\rVert\U \mathcal{A}.
\end{align}$$
</div>

That is, integration is a linear and continuous map


<div>
$$\begin{aligned}
\int\U \Omega \cdot \,\mathrm{d}\mu : \left(\mathcal{A},\left\lVert \cdot \right\rVert\U \mathcal{A}\right)\to (X,\left\lVert \cdot \right\rVert).
\end{aligned}$$
</div>

Since $X$ is a complete, we can <a href="https://en.wikipedia.org/wiki/Continuous_linear_extension">linearly
extend</a>
integration in a unique way to the completion $\overline{\mathcal{A}}$
of $(\mathcal{A},\left\lVert \cdot \right\rVert\U A)$. The space
$\overline{\mathcal{A}}$, which can be built through taking limits of
simple functions, is thus the space of functions that we can integrate.
Our next step is to figure out what this is.


<b>Definition 2</b>. We say a function
$f:(\Omega,\mathcal{F})\to (X,\mathcal{B}(X))$ is $\mu$-strongly
measurable if there exists a sequence of simple functions $f\U n$ such
that

<div>
$$\begin{aligned}
f=\lim\U {n \to \infty} f\U n \quad \mu\text{-almost everywhere}.

\end{aligned}$$
</div>




Since the simple $f\U n$ are separately valued (that is,
$f\U N(\Omega )\subset X$ is separable), $f$ will also be (almost
everywhere) separably valued. As a result we will always end up working
with separable Banach spaces. The following properties are of use

 <a name="ex:separable">
<b>Exercise 1</b> </a> . Let $X$ be a <b>separable</b> Banach space with dual $X^\star $
, show that

a)  There exists $\left\\{x\U n^\star \right\\}\U {n=1}^\infty\subset X^\star $ such
that

<div>
$$\begin{aligned}
\left\lVert x \right\rVert= \sup\U {n \geq1} \left| (x,x\U n^\star ) \right|.

\end{aligned}$$
</div>

Such a sequence is called a norming sequence.

b)  The Borel $\sigma$-algebra $\mathcal{B}(X)$ is equal to the
$\sigma$-algebra generated by $\left\\{x\U n^\star \right\\}\U {n=1}^\infty$,
and by $X^\star $. That is,

<div>
$$\begin{aligned}
\mathcal{B}(X)=\sigma\left(\left\{x\U n^\star \right\}\U {n=1}^ \infty\right)=\sigma(X^\star )

\end{aligned}$$
</div>

If $X$ is not separable, the inclusion
$\mathcal{B}(X)\subset \sigma(X^\star )$ may fail. See
<a href="https://link.springer.com/book/10.1007/978-94-009-3873-1">Vakhania, 2012</a> page 23 for a counterexample.

c)  A function $f: \Omega \to X$ is measurable if and only if it is
weakly measurable. That is, if and only if for all $x^\star \in X^\star $
the function $(f,x^\star ): \Omega \to \mathbb{R}$ is measurable.

d)  The dual $X^\star $ with the weak-$^\star $ topology (the topology generated
by $X$ viewed as a subset of $X^{\star \star }$) is separable .


<div class="exercise-container">
<button class="exercise-button" onclick="toggleExercise(this)">Hint</button>
<div class="exercise-text">

1.  Consider a countable dense subset $\left\\{x\U n\right\\}\U {n=1}^\infty$
of $X$. By the Hahn-Banach theorem, there exists $x\U n^\star \in X^\star $ such
that

<div>
$$\begin{aligned}
(x\U n,x\U n^\star )= \left\lVert x\U n \right\rVert, \quad \left\lVert x\U n^\star  \right\rVert=1.

\end{aligned}$$
</div>

Show that $x\U n^\star $ satisfies the desired property.

2.  The inclusion
$\sigma (X^\star ) \subset \sigma\left(\left\\{x\U n^\star \right\\}\U {n=1}^ \infty\right)$
always holds as the preimage by a continuous function of an open set
is open. To show the reverse inclusion, prove that every open ball
in $X$ can be written as a countable union of balls
$\overline{B}\U r(x):= \left\\{y \in X: \left\lVert x-y \right\rVert\leq r\right\\}$.
Now show that

<div>
$$\begin{aligned}
\overline{B}\U r(x)=\left\{x\in X: \sup\U {n \geq1}(x,x\U n^\star ) \leq r\right\} \subset \sigma\left(\left\{x\U n^\star \right\}\U {n=1}^ \infty\right).

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
that the space spanned by $\left\\{x\U n^\star \right\\}\U {n=1}^\infty$ is
dense in $X^\star $.
</div>
</div>

The following characterizes the space of strongly measurable functions

 <a name="thm:pettis">
<b>Theorem 3</b> </a>  (Pettis measurability theorem). A function
$f:\Omega\to X$ is $\mu$-strongly measurable if and only if $f$ is
$\mu$-almost everywhere separately valued and $(f, x^\star )$ is $\mu$
strongly measurable for all $x^\star \in X^\star $.



<b>Proof.</b> We first prove the implication. For some
$x\U k^{(n)} \in X , A\U k^{(n)} \in \mathcal{F}$,

<div>
$$\begin{aligned}
f= \lim\U {n \to \infty} f\U n=\lim\U {n \to \infty} \sum\U {k=1}^n 1\U {A\U k^{(n)}}\otimes x^{(n)}\U {k} \quad \mu\text{-almost everywhere}.

\end{aligned}$$
</div>

As a result, $f$ takes almost everywhere values in the
separable space spanned by the countably many $x\U k^{(n)}$. To see that
$(f,x^\star )$ is $\mu$-strongly measurable we note that $g\U n :=(f\U n,x^\star )$
are simple functions and

<div>
$$\begin{aligned}
(f,x^\star )= \lim\U {n \to \infty} g\U n \quad \mu\text{-almost everywhere}.

\end{aligned}$$
</div>

We now prove the reverse implication. By assumption,
there exists $\Omega \U 1 \subset \Omega$ such that $\mu (\Omega \U 1^c)=0$
and $X\U 1=\overline{f(\Omega\U 1 )}$ is separable. As a result, and by
point $1$ of exercise <a href="#ex:separable">1</a> there exists a norming sequence
$\left\\{x\U n^\star \right\\}\U {n=1}^\infty \subset X\U 1$.

Since we only need to prove limits almost everywhere, we can suppose
that $f$ is separably valued by restricting to $\Omega \U 1$. Now, by
assumption the functions $g\U n:=(f,x\U n^\star )$ are $\mu$-strongly measurable.
Let $K\U n$ be the support of $g\U n$ and $K=\cup\U {n \geq 1}K\U n$. By
definition of strongly $\mu$-measurable function and since the union of
countable sets is countable, $K$ is $\sigma$-finite. Since $x\U n^\star $
separate points, $f$ is $0$ outside of $K$, and by restricting to $K$ we
can suppose that $\mu$ is $\sigma$-finite.

Let $\left\\{x\U n\right\\}\U {n=1}^\infty$ be a countable dense subset of
$X\U 1$. Given $n \in \mathbb{N}$, we define $\varphi\U n (x)$ to be the
$x\U k \in \left\\{x\U j\right\\}\U {j=1}^ n$ which is the closest to $x$, and
where in the case of a tie we take the one with the smallest index $j$.
We can now define the simple functions

<div>
$$\begin{aligned}
F\U n := \varphi \U n(f(x)).

\end{aligned}$$
</div>

The function $F\U n$ takes at most $n$-different values
$x\U 1,\dots, x\U n$ with

<div>
$$\begin{align}
\label{sv}
\left\{F\U n=x\U k\right\}=\left\{\left\lVert f- x\U k \right\rVert = \min\U {1\leq j \leq n} \left\lVert f- x\U j \right\rVert < \min\U {1 \leq j <k} \left\lVert f-x\U j \right\rVert\right\}.

\end{align}$$
</div>

Since $(f-x\U k,x\U n^\star )$ is $\mu$-strongly measurable, we
deduce that the following function is measurable almost everywhere.


<div>
$$\begin{aligned}
\left\lVert f- x\U k \right\rVert= \sup\U {n \geq1} (f- x\U k,x\U n^\star ).

\end{aligned}$$
</div>

So, without loss of generality, we may suppose they are
measurable by restricting once more. Then, by
(\ref{sv})  $F\U n$ is
measurable. Since we had restricted $u$ to be $\sigma$-finite, we may
take a partition $\left\\{\Omega \U n\right\\}\U {n=1}^\infty$ of $\Omega$
with finite measure. Consider $f\U n:=F\U n 1\U {\Omega \U n}$, we have that
$f\U n$ is $\mu$ simple (we need to multiply by $1\U {\Omega \U n}$ so that
the support of the indicators have finite measure) and converges to $f$
almost everywhere. ◻


If we include $x\U 0=0$ in the norming sequence of Theorem
<a href="#thm:pettis">3</a>, we have
that $\left\lVert f\U n-f \right\rVert$ as in the proof above is bounded
by $\left\lVert f \right\rVert$ almost everywhere and obtain the
following corollary which will be used later to show the density of
simple functions in the integrable ones.

 <a name="density corollary">
<b>Corollary 4</b> </a> . Let $f : \Omega \to X$ be $\mu$-strongly measurable.
Then, there exists a sequence of simple functions $f\U n$ converging to
$f$ almost everywhere and such that

<div>
$$\begin{aligned}
\left\lVert f\U n-f \right\rVert \leq \left\lVert f \right\rVert, \quad \mu \text{-almost everywhere}.

\end{aligned}$$
</div>




Most typically, one works in the case where $\mu$ is $\sigma$-finite
(for example, if $\mu$ is the Lebesgue measure or any probability
measure) and identifies functions that are equal almost everywhere. In
this case, the following more simple statement holds.

 <a name="thm:pettis2">
<b>Theorem 5</b> </a>  (Pettis theorem for $\sigma$-finite measures). Let
$(\Omega, \mu, \mathcal{F})$ be a $\sigma$-finite measure space and
identify functions that are equal almost everywhere. Then $f$ is
$\mu$-strongly measurable if and only if $f$ is separately valued and
measurable.



<b>Proof.</b> Let $f$ be $\mu$-strongly measurable. Then, $f$ is the limit of
separately valued and measurable functions. As a result, $f$ is
separately valued and measurable.

Suppose now that $f$ is separately valued and measurable. Then, the same
is true for $f 1\U {\Omega\U n}$ where
$\left\\{\Omega\U n\right\\}\U {n=1}^\infty$ is a partition of $\Omega$ with
finite measure. Moreover, these functions are strongly measurable as the
measure of $\Omega \U n$ is finite (one can start from $f 1\U {\Omega\U n}$
and form $F\U n$ as in the previous proof converging to $f 1\U {\Omega \U n}$)
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
real-valued function
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
\left\lVert f \right\rVert\U {L^\infty(\Omega\to X)} & :=\inf\{r>0: \mu ( \left\lVert f \right\rVert> r)=0\},
\end{align}$$
</div>

where the infimum is defined to be $\infty$ if the set
is empty.

Knowledge of the real-valued case shows that
(\ref{Lp})  and
(\ref{Linfty})  define
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
<b>Definition 6</b> </a> . Given a measure space $(\Omega,\mathcal{F},\mu)$, a
Banach space $(X,\mathcal{B}(X))$ we define the space of $p$-integrable
functions as (the equivalence classes)

<div>
$$\begin{aligned}
L^p(\Omega \to X) & :=\left\{f:\Omega\to X: f \text{ is strongly measurable and } \left\lVert f \right\rVert\U {L^p(\Omega \to X)}<\infty\right\}.

\end{aligned}$$
</div>




If one wishes to be explicit about the underlying measure space one can
also write $L^p(\Omega,\mathcal{F},\mu, X)$. As in the real case, the
$L^p$ spaces are complete.

 <a name="thm:completeness">
<b>Theorem 7</b> </a>  (Fischer-Riesz). The space $L^p(\Omega\to X)$ is a Banach
space for all $p\in [1,\infty].$



<b>Proof.</b> The proof follows along the lines of the real case,
substituting the absolute value in $\mathbb{R}$ by the norm in $X$ as
necessary. We first prove the case $p \in [1,\infty)$ Recall that a
normed space is complete if and only if every absolutely convergent
series converges.That is, we need to show that if
$f\U n \in L^p(\Omega \to X)$ is such that

<div>
$$\begin{aligned}
\sum\U {n=1}^\infty \left\lVert f\U n \right\rVert\U {L^p(\Omega\to X)}<\infty.

\end{aligned}$$
</div>

Then there exists $f\in L^p(\Omega\to X)$ such that


<div>
$$\begin{aligned}
f=\sum\U {n=1}^\infty f\U n\in L^p(\Omega\to X).

\end{aligned}$$
</div>

To do so, one first applies
<a href="https://en.wikipedia.org/wiki/Minkowski_inequality#:~:text=.-,Minkowski%27s,-integral%20inequality%5B">Minkowski's</a>
inequality for real-valued functions to show that

<div>
$$\begin{aligned}
\sum\U {n=1}^\infty \left\lVert f\U n \right\rVert\U X\in L^p(\Omega\to\mathbb{R}).

\end{aligned}$$
</div>

Thus, the sum is finite almost everywhere. Since $X$ is
complete, we have that the above sum converges pointwise almost
everywhere to some function

<div>
$$\begin{aligned}
f(\omega):=\sum\U {n=1}^\infty f\U n(\omega)\in X.

\end{aligned}$$
</div>

Furthermore we have that $f$ is strongly measurable as
it is the limit of strongly measurable functions. Finally, using Fatou's
lemma for real-valued functions and the triangle inequality for norms
shows that

<div>
$$\begin{aligned}
\left\lVert f-\sum\U {n=1}^N f\U n \right\rVert\U {L^p(\Omega\to X)} & =\left\lVert \sum\U {n=N}^\infty f\U n \right\rVert\U {L^p(\Omega\to X)}\leq \liminf\U {M\to \infty}\left\lVert \sum\U {n=N}^M f\U n \right\rVert\U {L^p(\Omega\to X)} \\&\leq \liminf\U {M\to \infty}\sum\U {n=N}^M \left\lVert f\U n \right\rVert\U {L^p(\Omega\to X)}=\sum\U {n=N}^\infty \left\lVert f\U n \right\rVert\U {L^p(\Omega\to X)}\xrightarrow{N\to\infty} 0.

\end{aligned}$$
</div>

Which shows convergence in $L^p(\Omega\to X)$ for
$p\in [1,\infty)$.

For the case $p=\infty$ consider a Cauchy sequence
$f\U n \in L^p(\Omega \to X)$ and write

<div>
$$\begin{aligned}
A\U {nm}:=\left\{\omega\in \Omega: \left\lVert f\U n(\omega)-f\U m(\omega) \right\rVert \leq\left\lVert f\U n-f\U m \right\rVert\U {L^\infty(\Omega \to X)}\right\}, \quad A := \bigcup\U {m,n=1}^\infty A\U {nm}.

\end{aligned}$$
</div>

By construction, $A\U {nm}$ and thus $\mathbb{A}^c$ have
measure zero and $f\U n$ converges uniformly on $A$. As a result, $f\U n$
converges almost everywhere to some $f\in L^\infty(\Omega\to X)$. This
completes the proof. ◻


Just as in the case of Lebesgue integrals, the proof of the completeness
of $L^p(\Omega\to X)$ serves to show that every convergent sequence must
have a subsequence converging almost everywhere. This proposition is not
necessary for the rest of the constructions, it's just a nice property
to have in reserve.


<b>Proposition 8</b>. Let $f\U n\to f\in L^p(\Omega\to X)$, then there
exists a subsequence $f\U {n\U k}$ converging to $f$ almost everywhere.



<b>Proof.</b> In the proof of the above proposition, we saw that for any
absolutely convergent sum converges almost everywhere to its limit.
Further, since $f\U n$ is Cauchy, we can extract a subsequence $f\U {n\U k}$
with $\|f\U {n\U k}-f\U {n\U {k-1}}\|\leq 2^{-k}$. By construction, the sequence


<div>
$$\begin{aligned}
\sum\U {k=0}^{\infty} f\U {n\U k}-f\U {n\U {k-1}},

\end{aligned}$$
</div>

is normally convergent and converges in $f$. By the
above discussion we conclude the proof. ◻


Ok, so we've constructed some spaces of $p$-integrable functions and
shown that they are complete. You know where this is going. Next stop is
density town. In the standard construction of the Lebesgue integral, it
is used that every measurable function to $\mathbb{R}$ can be pointwise
approximated by simple functions. One can achieve the same result for
arbitrary metric spaces if the image of $f$ is separable.


<b>Proposition 9</b>. Every function in $L^p(\Omega\to X)$ is the limit
almost everywhere and in the norm of a sequence of simple functions.



<b>Proof.</b> By Corollary <a href="#density corollary">4</a>, there exists a sequence of simple
functions $f\U n$ converging to $f$ almost everywhere and such that
$\left\lVert f\U n-f \right\rVert<\left\lVert f \right\rVert$ almost
everywhere. By the dominated convergence theorem for real valued
functions, we have that

<div>
$$\begin{aligned}
\lim\U {n\to\infty}\left\lVert f\U n-f \right\rVert^p\U {L^p(\Omega\to X)}=\lim\U {n\to\infty}\int\U \Omega\left\lVert f\U n-f \right\rVert^p\,\mathrm{d}\mu=\int\U {\Omega}\lim\U {n \to \infty}\|f\U n-f\|^p \,\mathrm{d}\mu =0.

\end{aligned}$$
</div>

◻


As a corollary, we obtain the following


<b>Corollary 10</b>. The simple functions $\mathcal{A}$ are a dense subset
of $L^p(\Omega\to X)$.


Since $L^1(\Omega\to X)$ is complete, we have that the closure of
$\overline{\mathcal{A}}$ with the norm
$\left\lVert \cdot  \right\rVert\U {L^1(\Omega \to X)}$ is
$L^1(\Omega\to X)$. Furthermore, by the triangle inequality
(\ref{triangle}) ,
integration is continuous with this norm. This continuity allows us to
extend integration to $L^1(\Omega \to X)$ and shows that the space of
integrable functions is $L^1(\Omega\to X)$.

 <a name="def int">
<b>Definition 11</b> </a> . We define the integral on $L^1(\Omega\to X)$ as the
unique continuous extension with the norm
$\left\lVert \cdot \right\rVert\U {L^1(\Omega\to X)}$ of the integral on
$\mathcal{A}$. That is, given $f\in L^1(\Omega\to X)$ we define


<div>
$$\begin{aligned}
\int\U \Omega f \,\mathrm{d}\mu:=\lim\U {n\to\infty} \int\U \Omega f\U n \,\mathrm{d}\mu.

\end{aligned}$$
</div>

Where $f\U n\in \mathcal{A}$ is any sequence such that
$\left\lVert f-f\U n \right\rVert\U {L^1(\Omega\to X)}\to 0$.



<b>Observation 1</b>. We could also work with the spaces

<div>
$$\begin{aligned}
\hat{L}^p(\Omega,\mathcal{F},\mu,X) & =\left\{f:\Omega\to X: \int\U \Omega \left\lVert f \right\rVert^p \,\mathrm{d}\mu<\infty\right\}.

\end{aligned}$$
</div>

These spaces are once more complete, however, they do
not contain simple functions as a dense subset. As a result, given
$f \in \hat{L}^1(\Omega \to X)$ it is not possible to make sense of the
expression $\int\U \Omega f \,\mathrm{d}\mu$.


# Familiar properties

Many properties of integration hold for the Bochner integral as well.
For example, the following is a result of the definition of the Bochner
integral and a passage to the limit, as it holds for simple functions.

 <a name="corollary easy">
<b>Corollary 12</b> </a> . Let $f\in L^1(\Omega,X)$ with $X$ a Banach space,
then

1.  $\left\lVert \int\U \Omega f \,\mathrm{d}\mu \right\rVert\leq\int\U \Omega{\left\lVert f \right\rVert\,\mathrm{d}\mu}$

2.  Let $Y$ be another Banach space and $L\in L(X,Y)$. Then


<div>
$$\begin{aligned}
\int\U \Omega (L\circ f) \,\mathrm{d}\mu=L\left(\int\U \Omega f \,\mathrm{d}\mu\right).

\end{aligned}$$
</div>




Knowledge of scalar-valued results also goes a long way; for example, we
can prove the following

 <a name="ex:fubini">
<b>Exercise 2</b> </a>  (Fubini-Tonelli). Let
$(\Omega\U 1, \mathcal{F}\U 1 , \mu \U 1 )$ and
$(\Omega\U 2, \mathcal{F}\U 2 , \mu \U 2 )$ be $\sigma$-finite measure spaces
and consider the space $\Omega\U 1\times \Omega\U 2$ with the
$\sigma$-algebra $\mathcal{F}\U 1 \otimes \mathcal{F}\U 2$ generated by sets
of the form $A\U 1 \times A\U 2$ with $A\U i \in \Omega \U i$ and the unique
measure $\mu \U 1 \otimes \mu \U 2$ such that
$(\mu \U 1 \otimes \mu \U 2)(A\U 1 \times A\U 2)=\mu \U 1(A\U 1)\mu \U 2(A\U 2)$. Let
$X$ be a Banach space and $f:\Omega\U 1\times \Omega\U 2 \to X$ be strongly
measurable. Then

1.  The functions $f(\omega\U 1,\cdot )$ and $f(\cdot,\omega\U 2)$ are
strongly measurable.

2.  If any of the following integrals is finite

<div>
$$\begin{align}  \label{norm ints}
\int\U {\Omega\U 1 \times \Omega \U 2} \left\lVert f \right\rVert \,\mathrm{d}(\mu\U 1 \otimes \mu \U 2), \quad  \int\U {\Omega\U 1}\left(\int\U {\Omega\U 2} \left\lVert f \right\rVert\,\mathrm{d}\mu\U 2\right)\,\mathrm{d}\mu\U 1, \quad \int\U {\Omega\U 2}\left(\int\U {\Omega\U 1} \left\lVert f \right\rVert\,\mathrm{d}\mu\U 1\right)\,\mathrm{d}\mu\U 2.

\end{align}$$
</div>

Then all of the integrals in
(\ref{norm ints})  are equal, and

<div>
$$\begin{align}  \label{ints}
\int\U {\Omega\U 1 \times \Omega \U 2} f \,\mathrm{d}(\mu\U 1 \times \mu \U 2)= \int\U {\Omega\U 1}\left(\int\U {\Omega\U 2} f\,\mathrm{d}\mu\U 2\right)\,\mathrm{d}\mu\U 1=\int\U {\Omega\U 2}\left(\int\U {\Omega\U 1} f\,\mathrm{d}\mu\U 1\right)\,\mathrm{d}\mu\U 2.

\end{align}$$
</div>




<div class="exercise-container">
<button class="exercise-button" onclick="toggleExercise(this)">Hint</button>
<div class="exercise-text">

1.  From Fubini's theorem, we know that the
<a href="https://proofwiki.org/wiki/Horizontal_Section_of_Measurable_Function_is_Measurable">sections</a>
$f(\omega\U 1,\cdot )$ and $f(\cdot,\omega\U 2)$ are measurable. Since
$f$ is separately valued so are $f(\omega\U 1,\cdot )$ and
$f(\cdot,\omega\U 2)$. As a result, by Theorem
<a href="#thm:pettis2">5</a>,
they are strongly measurable.

2.  By
<a href="https://en.wikipedia.org/wiki/Fubini%27s_theorem#Fubini%E2%80%93Tonelli_theorem:~:text=the%20uncompleted%20product.-,For,-integrable%20functions%5B">Fubini-Tonelli's</a>
theorem we know that if any of the integrals in
(\ref{norm ints})  is finite, then all of them are equal. By the
first point, we conclude from the characterization of the integrable
functions (Definitions <a href="#def:Lp">6</a>, <a href="#def int">11</a>) that all the integrals in
(\ref{ints})  are well
defined, and it remains to see they are equal. To do so, let
$x^\star  \in X^\star $ be and then, by Fubini-Tonelli for real-valued
functions

<div>
$$\begin{aligned}
\int\U {\Omega\U 1 \times \Omega \U 2} (f,x^\star ) \,\mathrm{d}(\mu\U 1 \otimes \mu \U 2) & = \int\U {\Omega\U 1}\left(\int\U {\Omega\U 2} (f,x^\star )\,\mathrm{d}\mu\U 2\right)\,\mathrm{d}\mu\U 1=\int\U {\Omega\U 2}\left(\int\U {\Omega\U 1} (f,x^\star )\,\mathrm{d}\mu\U 1\right)\,\mathrm{d}\mu\U 2.

\end{aligned}$$
</div>

By Point $2$ of Corollary
<a href="#corollary easy">12</a> and, since we just proved that all the
integrals in (\ref{ints})  are well defined, we may pull $x^\star $ out of the
integrals. By the Hahn-Banach theorem, $X^\star $ separates points of
$X$, and the proof follows.
</div>
</div>

Sometimes the following theorem is more useful when instead of using the
product measure $\mu\U 1 \otimes \mu\U 2$ on $X \times Y$, we use its
completion $\overline{\mu\U 1 \times \mu\U 2}$. In this case,
Fubini-Tonelli's Theorem <a href="#ex:fubini">2</a> still holds. It is only necessary to note that
the sections of $f$ are now almost always measurable (see
<a href="https://www.stat.rice.edu/~dobelman/courses/texts/qualify/Measure.Theory.Tao.pdf">Tao, 2011</a> page 203 for more details).


<b>Exercise 3</b> (Minkowski's integral inequality). Show that given
$p \in [1,\infty)$ and $f \in L^1(\Omega\U 1 \to L^p(\Omega\U 2 \to Y))$ it
holds that

<div>
$$\begin{aligned}
\left(\int\U {\Omega \U 1}\left\lVert \int\U {\Omega\U 2 } f \,\mathrm{d}\mu \U 2  \right\rVert^p \,\mathrm{d}\mu \U 1\right)^{1/p}\leq \int\U {\Omega\U 2}\left(\int\U {\Omega \U 1} \left\lVert f \right\rVert^p \,\mathrm{d}\mu\U 1\right)^{1/p}\,\mathrm{d}\mu\U 2 .

\end{aligned}$$
</div>




<div class="exercise-container">
<button class="exercise-button" onclick="toggleExercise(this)">Hint</button>
<div class="exercise-text">
Apply the triangle inequality
(\ref{triangle})
with $X= L^p(\Omega\U 2 \to Y)$.
</div>
</div>


<b>Exercise 4</b> (Dominated convergence theorem). Let
$f\U n,f\in L^1(\Omega\to X)$ be such that $f\U n\to f$ almost everywhere
and there exists $g\in L^1(\Omega\to X)$ such that
$\left\lVert f\U n \right\rVert\leq g$ almost everywhere. Then


<div>
$$\begin{aligned}
\int\U \Omega f\U n \,\mathrm{d}\mu\to \int\U \Omega f \,\mathrm{d}\mu.

\end{aligned}$$
</div>




<div class="exercise-container">
<button class="exercise-button" onclick="toggleExercise(this)">Hint</button>
<div class="exercise-text">
We have that $\left\lVert f\U n-f \right\rVert\leq 2g$ almost
everywhere. As a result, by the dominated convergence theorem for
real-valued functions, we have that

<div>
$$\begin{aligned}
\lim\U {n\to\infty}\int\U \Omega\left\lVert f\U n-f \right\rVert\,\mathrm{d}\mu=0.

\end{aligned}$$
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
functions, can be used to prove the <a href="https://nowheredifferentiable.com/2023-07-12-PDEs-3-Sobolev_spaces/#:~:text=example%2C%208%20444R.-,Smoothing,-in">standard approximation
theorems</a>.

 <a name="thm:approx">
<b>Theorem 13</b> </a>  (Convolution, regularization and smooth approximation).
Let $p \in [1,\infty)$ and consider $f\in L^p(\mathbb{R}^d\to X)$ and
$\phi \in L^1(\mathbb{R}^d)$.

a)  <b>Young's inequality</b>. The convolution

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



b)  <b>Mollifiers</b>. Define
$\phi\U \epsilon(x):=\epsilon^{-d}\phi(x/\epsilon)$. Then,


<div>
$$\begin{aligned}
f\star \phi\U \epsilon \to f \quad \text{in } L^p(\mathbb{R}^d\to X).

\end{aligned}$$
</div>



c)  <b>Smoothing</b>. If $\phi \in C^k\U c(\mathbb{R}^d)$ then
$f\star \phi\U \epsilon \in C^k(\mathbb{R}^d\to X)$ with

<div>
$$\begin{aligned}
D^\alpha f\star \phi=f\star (D^\alpha \phi), \quad\forall \left| \alpha \right|\leq k.

\end{aligned}$$
</div>



d)  <b>Smooth approximation</b>. The space $C\U c^\infty(\mathbb{R}^d)$ is
dense in $L^p(\mathbb{R}^d\to X)$.


Ok, that's it. This post was a bit more technical than some of the
others, but you get the picture. Define an integral for simple
functions, and figure out what can be approximated by simple functions.
As we saw, the extra requirement that appears over the Lebesgue case is
that the function $f$ is separately valued and justifies why, as we will
see in future posts on SPDEs, the image of $f$ is often taken to be some
separable Hilbert space. Until the next time!

A (possibly not updated) pdf of version of this page is provided [here](/assets/pdfs/Analysis in Banach spaces/The-Bochner-Integral.pdf).