---
layout: post
title: Sobolev spaces
subtitle: Denisty, trace and embeddings
thumbnail-img: /assets/img/Narici.jpg
share-img: /assets/img/Narici.jpg
tags: [PDEs]
authorpost: L.Llamazares
---

#  Three line summary

-   Given open $U \subset \mathbb{R}^d$ the Sobolev spaces $W^{k,p}(U)$
are **complete** spaces of **weakly differentiable** functions.

-   **Smooth functions are dense** in $W^{k,p}(\Omega)$ if $\Omega$ is
smooth and bounded. This lets us perform formal manipulations as if
everything is smooth and then take limits. In particular, we can
**extend and restrict** functions to $\partial \Omega$.

-   Functions in $W^{k,p}(\Omega)$ enjoy various inequalities. Cashing
in differentiability for integrability we can **compactly embed**


<div>
$$\begin{aligned}
W^{k,p}(\Omega) \hookrightarrow L^q(\Omega).\end{aligned}$$
</div>


Where $q\equiv q(d,k,p)$ decreases with the dimension $d$, increases
with differentiability $k$ and integrability $p$, and is larger than
$p$.

# Why should I care?

Sobolev spaces allow us to extend the notion of differentiability to a
wider class of functions. The fact that these spaces are complete and
compactly embedded in $L^q$ spaces is an important tool to extract
convergent sub-sequences. This is useful when solving differential
equations as a common technique is to take a Cauchy sequence whose limit
is the solution to the equation.

# Notation

-   In this post we will be dealing with functions over a variety of
domains. To facilitate interpretation of the notation we will stick
to the convention that $K$ is a compact set, $U, V$ are open sets,
and $\Omega$ is an open bounded set with $C^1$ boundary.

-   Given a topological space $X$ and a subset $A \subset X$ we
abbreviate $A$ is dense in $X$ with the topology of $X$ by


<div>
$$\begin{aligned}
\overline{A}=X.
\end{aligned}$$
</div>

We stress that in practice $X$ may be
itself a subset of some larger space $Y$ (for example
$X= H^s(\mathbb{R}^d)$ and $Y= L^p(\mathbb{R}^d)$) . However, the
above notation will always mean the closure with the topology of $X$
and not $Y$.

-   A related notation is we will write given $a\U n \in  A$


<div>
$$\begin{aligned}
\lim\U {n \to \infty}a\U n =x \in X.
\end{aligned}$$
</div>

To mean the limit in the topology of $X$.

-   Given two sets $A,B$ we write $A \Subset B$ and say that $A$ is
compactly included in $B$ if $\overline{A}$ is compact and
strictly included in $B$.

-   We also write

<div>
$$\begin{aligned}
A+B=\left\{x+y:x \in A, y \in  B\right\} .
\end{aligned}$$
</div>



-   Given a topological vector space $X$ we write $X'$ for the dual of
$X$ and denote given $\in X', \varphi \in X$ the duality pairing as


<div>
$$\begin{aligned}
(\varphi,w):= w(\varphi) .
\end{aligned}$$
</div>



-   We will always write $\alpha$ for a multi-index
$\alpha \in \mathbb{N}^d$ and use the notation

<div>
$$\begin{aligned}
D^\alpha f := \partial \U 1^{\alpha\U 1}\cdots \partial \U d^{\alpha\U d}.
\end{aligned}$$
</div>

In the case $\alpha =0$ we use the
convention $D^0 =f$.

-   Given a space of functions $X$ with domain $A$ and $B \subset A$ we
write

<div>
$$\begin{aligned}
\left.X\right|\U {B}:=\left\{\left.f\right|\U {B}: f\in X\right\} .
\end{aligned}$$
</div>



-   Given two quantities $M,N$ we write $M \lesssim N$ to mean that
there exists some constant $C$ independent of $M$ and $N$ such that
$M \leq C N$.

-   We write $B\U r(x)$ for the ball centered at $x$ with radius $r$ and
$B\U r$ if $x=0$. The space where the ball is contained depending on
context.

# Introduction

In practice, one often wants to solve a differential equation


<div>
$$\begin{align}
\label{PDE1}
\mathcal{L}u = f\quad  \mathrm{ on  }\quad  D .\end{align}$$
</div>

Where
$D$ is some domain in $\mathbb{R}^d$. In a previous post on the [Fourier
transform](https://nowheredifferentiable.com/2023-01-29-PDE-1-Fourier/#:~:text=Sobolev%20spaces-,Sobolev,-spaces%20form%20a)
we saw how to define the Sobolev spaces $H^s(D)$ when $D$ is the whole
Euclidean space $\mathbb{R}^d$ or the torus $\mathbb{T}^d$. These spaces
correspond to $s$-times weakly differentiable functions and we saw how
these spaces could help us solve
(\ref{PDE1}) . However, in
practice $D$ may be an open set in $\mathbb{R}^d$ or even some
$d$-dimensional manifold with a boundary condition

<div>
$$\begin{align}
\label{bc}
\left.u\right|\U {\partial  D}= g.\end{align}$$
</div>

Note that equation
(\ref{bc})  is a priori
ill-defined as the Lebesgue measure of $\partial D \subset \mathbb{R}^d$
is zero. Thus, it is necessary to extend the theory to a wider class of
domains and to explain what we mean by the restriction of a function to
its boundary of definition.

## A first attempt

Suppose for example $D=U$ is an open set and $u: U \to \mathbb{R}$.
Then, we can try to define $H^s(U)$ using our knowledge of
$H^s(\mathbb{R}^d)$ by:

1.  Extending $u$ by zero outside of $U$ to form

<div>
$$\begin{aligned}
\tilde{u}(x):=\begin{cases}
u(x) & \quad x \in U     \\
0    & \quad x \not\in U
\end{cases}.
\end{aligned}$$
</div>



2.  Studying if $\tilde{u} \in  H^s(\mathbb{R}^d)$. That is, as we saw
in the [previous
post](https://nowheredifferentiable.com/2023-01-29-PDE-1-Fourier/#:~:text=fact%2C%20since%20the-,Fourier,-transform%20is%20a),
checking if

<div>
$$\begin{aligned}
\left\lVert \tilde{u} \right\rVert\U {H^s(\mathbb{R}^d)}^2= \int\U {\mathbb{R}^d}\left\langle\xi \right\rangle^{2s}\widehat{\tilde{u}}(\xi )^2 \,\mathrm{d}\xi < \infty\end{aligned}$$
</div>



3.  Saying that $u \in H^s(U)$ if and only if
$\tilde{u} \in H^s(\mathbb{R}^d)$.

However, this runs into problems as is shown in the following example:


**Example 1**. Let $U=(0,1)$ and take $u: (0,1) \to \mathbb{R}$ defined
to be identically equal to $1$. Note that $u \in C^\infty(U)$ so we
expect that $u \in H^s((0,1))$ for all $s \in \mathbb{R}$. However, it
holds that $\tilde{u}= {1}\U {(0,1)}$ with

<div>
$$\begin{aligned}
\widehat{\tilde{u}}(\xi )=\frac{1-e^{-2 \pi i \xi }}{2 \pi i \xi }.
\end{aligned}$$
</div>




As we can see, by substituting in our naive definition of $H^s(U)$ gives
that $u \in H^s((0,1))$ if and only if $s< \frac{1}{2}$. Thus, our
program of extending $u$ by zero and studying the regularity of the
extension is not going to work. The reason for this is that, by
extending by zero we introduce a discontinuity on $\tilde{u}$ at the
boundary of $U$.

## A second approach

Alternatively, we could also define

<div>
$$\begin{aligned}
H^s(U)= \left.H^s(\mathbb{R}^d)\right|\U {U}:= \left\{\left.f\right|\U {u}: f \in H^s(\mathbb{R}^d)\right\} .\end{aligned}$$
</div>


As we will see later (Corollary [19](#restriction)) this is a better approach. However, it is not
optimal as it requires some conditions on $U$. For example, if $U$ is
not smooth we cannot assert that
$\left.C^\infty(\mathbb{R}^d)\right|\U {U}= C^\infty(U)$.

# Test functions and distributions

## Seminorms and their topologies

We need a new approach. Motivated as in the previous post by
[duality](https://nowheredifferentiable.com/2023-01-29-PDE-1-Fourier/#:~:text=is%20called%20the-,duality,-method%20and%20appears)
we should begin by defining what is meant by a weak derivative of a
function $u$ in $L^p(U)$. If $u,\varphi$ are smooth functions then we
have by integration by parts

<div>
$$\begin{aligned}
(\varphi, D^\alpha u):= \int\U {D} \varphi D^\alpha u  = (-1)^{\left| \alpha \right| }\int\U {D}(D^{\alpha} \varphi) u + \text{ boundary effects}  .\end{aligned}$$
</div>


In the previous post, we used that

-   If $D =\mathbb{R}^d$ we can take as our test functions
$\varphi \in  \mathcal{S}(\mathbb{R}^d)$ and use that $\varphi$
multiplied by any function in $L^2$ ($u$ and its derivatives) vanish
at infinity to get rid of the boundary effects.

-   If $D =\mathbb{T}^d$ we can take as our test functions
$\varphi \in  C^\infty(\mathbb{T}^d)$ as the boundary effect of
periodic functions cancels out.

To obtain this cancellation on a general open $D$ we need to impose that
our test function $\varphi$ vanishes in a neighborhood of the boundary.
That is we need our test functions to have compact support.


**Definition 1**. Let $U$ be an open set, then we define
$C\U c^\infty(U)$ to be the space of smooth functions whose support is
some compact set $K \subset U$.


Another notation for $C^\infty\U c(U)$ is $\mathcal{D}(U)$ and it is often
called the space of test functions for reasons we will later see.
Given a compact subset $K \subset U$ we define for each
$k \in \mathbb{N}$


**Definition 2**. Given a compact subset $K$ of an open set $U$ we
define

<div>
$$\begin{aligned}
C\U c^\infty(K):= \left\{\varphi \in C\U c^\infty(U): \mathbf{supp}(\varphi) \subset K \right\} .
\end{aligned}$$
</div>

We endow $C\U c^\infty(K)$ with the [topology
generated by the countable family of
seminorms](https://nowheredifferentiable.com/2023-01-29-PDE-1-Fourier/#:~:text=together-,with,-a%20countable%20family)


<div>
$$\begin{align}
\label{local smooth norms}
\left\lVert \varphi \right\rVert\U {C^k(K)}:= \sup\U {x \in K} \sum\U {\left| \alpha \right|\leq k } \left| D^\alpha \varphi \right|, \quad  k \in \mathbb{N}\U {0}
\end{align}$$
</div>




Later we will need to generate topologies when the family of seminorms
is uncountable.


**Definition 3**. Let $X$ be a vector space and let
$\rho \in \mathcal{P}$ be a family of seminorms on $X$. Then we define
the topology generated by $\mathcal{P}$ to be the topology generated
by the local basis

<div>
$$\begin{aligned}
x+\left\{\rho^{-1}(B\U \epsilon): \epsilon>0\right\}
\end{aligned}$$
</div>




The above topology is equivalent to the initial topology generated by
the family

<div>
$$\begin{aligned}
\left\{\rho(\cdot-x): x\in X, \rho \in \mathcal{P}\right\}.\end{aligned}$$
</div>


We include some exercises to help the reader get more used to the
topology that arises. I recommended trying to solve them for a few
minutes before checking the hints.

 <a name="TVS ex">
**Exercise 1** </a> . Write $\tau\U {\mathcal{P}}$ for the topology generated
by $\mathcal{P}$, Show that $\tau\U {\mathcal{P}}$ is the coarsest
topology that makes $X$ into a topological vector space
([TVS](https://en.wikipedia.org/wiki/Topological_vector_space)).


<div class="exercise-container">
<button class="exercise-button" onclick="toggleExercise(this)">Hint</button>
<div class="exercise-text">
The fact that $(X,\tau\U \mathcal{P})$ is a TVS follows from the
triangle inequality and homogeneity of seminorms. The fact that it is
the coarsest that makes $\rho$ continuous is that
$\rho^{-1}(B\U \epsilon)$ must be an open neighborhood of the origin and
in a TVS, by continuity of the sum, translation of an open set must be
open.
</div>
</div>

 <a name="convex ex">
**Exercise 2** </a> . Show that $(X,\tau\U \mathcal{P})$ is locally convex.
That is, every point has a local basis of convex sets


<div class="exercise-container">
<button class="exercise-button" onclick="toggleExercise(this)">Hint</button>
<div class="exercise-text">
Show that $\rho^{-1}(B\U \epsilon)$ is convex.
</div>
</div>

 <a name="convergence TVS">
**Exercise 3** </a> . Show that the topology $(X,\tau\U \mathcal{P})$ is
determined by the following property.

-   Given a
[net](https://en.wikipedia.org/wiki/Net_(mathematics)#:~:text=%5Bedit%5D-,Any,-function%20whose%20domain)
$x\U \bullet\in (X,\tau\U \mathcal{P})$ it holds that

<div>
$$\begin{aligned}
\lim x\U \bullet =x \in  X  \iff      \rho(x\U \bullet-x)\to 0 \quad\forall \rho \in \mathcal{P}.
\end{aligned}$$
</div>




<div class="exercise-container">
<button class="exercise-button" onclick="toggleExercise(this)">Hint</button>
<div class="exercise-text">
The topology of any topological space is completely determined
by the convergence of nets. So it is enough to show that the property
holds. The implication holds by the continuity of $\rho$, the reverse
follows from being able to fit $x\U \bullet$ into any basic set
$x+\rho(B\U \epsilon)$.
</div>
</div>


**Exercise 4**. Show that $C\U c^\infty(K)$ is complete and thus a
[Fréchet](https://en.wikipedia.org/wiki/Fr%C3%A9chet_space#:~:text=locally%20convex%20metrizable%20topological%20vector%20space)
space.


<div class="exercise-container">
<button class="exercise-button" onclick="toggleExercise(this)">Hint</button>
<div class="exercise-text">
The topology is
[metrizable](https://nowheredifferentiable.com/2023-01-29-PDE-1-Fourier/#:~:text=together-,with,-a%20countable%20family)
as the family of seminorms is countable Use Exercise
[3](#convergence TVS)
to show that if $\varphi\U n \in C\U c^\infty(K)$ is Cauchy then the
sequence of derivatives $D^\alpha \varphi\U n$ converge uniformly to
$\varphi^{(\alpha)} \in C\U c^0(K)$ for all $\alpha$. It remains to show
that

<div>
$$\begin{aligned}
\varphi^{(0)}= \lim\U {n \to \infty} \varphi\U n \in  C\U c^\infty(K).
\end{aligned}$$
</div>

To do so use the fundamental theorem of calculus and
induction.
</div>
</div>

Using $C\U c^\infty(K)$ as a stepping stone we can build a topology on
$C\U c^\infty(U)$. We use the approach in [Terence Tao's blog post on
distributions](https://terrytao.wordpress.com/2009/04/19/245c-notes-3-distributions/#:~:text=is%20clearly%20a-,vector,-space.%20Now%20we).
Let us call a seminorm on $C\U c^\infty(U)$ restrictable if it is a
continuous function on $C\U c^\infty(K)$ for all $K \subset U$.


**Definition 4**. The topology on $C\U c^\infty(U)$ is the one generated
by all the restrictable seminorms on $C\U c^\infty(U)$. We call this
topology the smooth topology.



**Exercise 5**. Give an infinite restrictable family of seminorms.


<div class="exercise-container">
<button class="exercise-button" onclick="toggleExercise(this)">Hint</button>
<div class="exercise-text">
Valid answers include all the $L^p(U)$ and $C^k(U)$ norms.
</div>
</div>


**Exercise 6**. Show that $C\U c^\infty(\Omega)$ with the smooth topology
is a locally convex topological vector space (LCTVS).


<div class="exercise-container">
<button class="exercise-button" onclick="toggleExercise(this)">Hint</button>
<div class="exercise-text">
See Exercises [1](#TVS ex)-[2](#convex ex)
</div>
</div>

 <a name="local convergence">
**Exercise 7** </a>  (Smooth convergence is equal to local convergence). Show
that $\varphi\U n \to \varphi \in \mathcal{D}(U)$ if and only if there
exists a compact set $K$ such that for all $n$ the support of $f\U n$ and
$f$ are in $K$ and

<div>
$$\begin{aligned}
\lim\U {n \to \infty}\varphi\U n  =\varphi \in  C\U c^\infty(K).
\end{aligned}$$
</div>




<div class="exercise-container">
<button class="exercise-button" onclick="toggleExercise(this)">Hint</button>
<div class="exercise-text">
Given any sequence
$\mathbf{a}=\left\\{a\U j\right\\}\U {j\in \mathbb{N}} \in \mathbb{R}\U +$ and
an increasing set of compact sets $K\U j$ with
$U=\bigcup\U {j\in \mathbb{N}} K\U j$ show that

<div>
$$\begin{aligned}
p\U {\mathbf{a}}(\varphi):=\sup \U {j \in \mathbb{N}}{a\U j} \sum\U {|\alpha| \leq j}\left\lVert D^\alpha \varphi(x) \right\rVert\U {L^\infty(U\setminus K\U j)}.
\end{aligned}$$
</div>

Is a restrictable seminorm. Why does this prevent
the support of $\varphi\U n$ escaping to infinity? Now knowing all
functions are supported in some $K$ use that
$\left\lVert \cdot  \right\rVert\U {C^k(K)}$ is restrictable to conclude
the proof.
</div>
</div>


**Exercise 8** (Completeness). Show that $C\U c^\infty(\Omega)$ with the
smooth topology is complete.


<div class="exercise-container">
<button class="exercise-button" onclick="toggleExercise(this)">Hint</button>
<div class="exercise-text">
Given a Cauchy net $\varphi\U {\bullet} \in C\U c^\infty(U)$ show
as in Exercise [7](#local convergence) that the support of $\varphi\U {\bullet}$
cannot escape a compact set $K$. Conclude using the completeness on
$C\U c^\infty(K)$ and Exercise [3](#convergence TVS).
</div>
</div>


**Exercise 9**. Show that $C\U c^\infty(\Omega)$ with the smooth topology
is Hausdorff.


<div class="exercise-container">
<button class="exercise-button" onclick="toggleExercise(this)">Hint</button>
<div class="exercise-text">
The initial topology of a set of functions that separates
points is Hausdorff.
</div>
</div>


**Observation 1**. The topology on $C\U c^\infty(U)$ is not metrizable
(note the family of seminorms used to generate it is not countable) and
as a result $C\U c^\infty(U)$ **is not** a Fréchet space. This and more
can be found in [1](https://bookstore.ams.org/gsm-105#:~:text=A%20First%20Course%20in%20Sobolev%20Spaces&text=Sobolev%20spaces%20are%20a%20fundamental,BV%20functions%20of%20one%20variable.) page 286.


The construction of the topology on $C\U c^\infty(U)$ is a bit technical a
more intuitive construction would be to define the family of seminorms


<div>
$$\begin{aligned}
\left\lVert \varphi \right\rVert\U j := \sup\U {\left| \alpha \right| \leq j}  \left\lVert D^\alpha \varphi \right\rVert\U {L^\infty(U)}.\end{aligned}$$
</div>


And then define the topology on $C\U c^\infty(U)$ to be the one generated
by this family of seminorms. This has the following problem.


**Exercise 10**. Show that $C\U c^\infty(U)$ with the topology generated
by $\left\lVert \cdot  \right\rVert\U j$ is not complete.


<div class="exercise-container">
<button class="exercise-button" onclick="toggleExercise(this)">Hint</button>
<div class="exercise-text">
Construct a sequence that is Cauchy with respect to every
$\left\lVert \cdot  \right\rVert\U j$ whose support escapes to infinity.
</div>
</div>

Using the smooth topology we can now work with the dual of
$C\U c^\infty(U)$


**Definition 5**. We define the space of distributions to be


<div>
$$\begin{aligned}
\mathcal{D}'(U):= (C\U c^\infty(U))'.
\end{aligned}$$
</div>

And give it the
[weak-$\star $](https://en.wikipedia.org/wiki/Weak_topology) topology.



**Observation 2**. The inclusions

<div>
$$\begin{aligned}
C\U c^\infty(U) \hookrightarrow C\U c^\infty(\mathbb{R}^d) \hookrightarrow \mathcal{S}(\mathbb{R}^d)
\end{aligned}$$
</div>

are continuous. As a result,
$\mathcal{S}'(\mathbb{R}^d) \hookrightarrow \mathcal{D}'(U)$. That is,
distributions are a larger or more general class than tempered
distributions.


Of course, not all smooth functions have compact support. Other (in this
case Fréchet) spaces of smooth functions are

<div>
$$\begin{aligned}
C^\infty(U)                & :=\left\{\varphi: \left\lVert \varphi \right\rVert\U j:= \sup\U {\left| \alpha \right| \leq j}  \left\lVert D^\alpha \varphi \right\rVert\U {L^\infty(U)}<\infty,\quad \forall k \in \mathbb{N} \right\}                 \\
C^\infty\U {\mathrm{loc}}(U) & :=\left\{\varphi: \left\lVert \varphi \right\rVert\U {k,K}:= \sup\U {\left| \alpha \right| \leq k}  \left\lVert D^\alpha \varphi \right\rVert\U {L^\infty(K)}<\infty,\quad \forall k \in \mathbb{N}, K \subset U \right\}\end{aligned}$$
</div>


Where, we give them respectively the topologies generated by
$\left\lVert \cdot \right\rVert\U k$ and
$\left\lVert \cdot \right\rVert\U {k,K}$.

An equivalent characterization of $\mathcal{D}'(U)$ (see
[2](https://books.google.co.uk/books?id=wI4fAwAAQBAJ&printsec=frontcover&hl=fr&source=gbs_ge_summary_r&cad=0#v=onepage&q&f=false) page 241 ) is that, $\omega \in  \mathcal{D}'(U)$
if and only if for all $\varphi \in C\U c^\infty(U)$ the operator
$\varphi w$ defined by

<div>
$$\begin{align}
\label{equiv}
(f, \varphi w):= (\varphi f, w), \quad\forall f \in C^\infty(U),\end{align}$$
</div>


is continuous on $C^\infty(U)$.

## Locally integrable functions as distributions

In our post on the Fourier transform [we
saw](https://nowheredifferentiable.com/2023-01-29-PDE-1-Fourier/#:~:text=One-,may,-verify%20that%20we)
that integrable functions could naturally be considered as tempered
distributions. The analogous is true for distributions. In this case,
since our test functions are compactly supported, the functions we pair
them up with only need to be locally integrable. We recall the
definition


**Definition 6**. Given $p\in [1,\infty]$ we write
$L^p\U {\mathrm{loc}}(U)$ for the space of locally $p$ integrable
functions,

<div>
$$\begin{aligned}
L^p\U {\mathrm{loc}}(U):= \left\{f: \left\lVert f \right\rVert\U {L^p(K)}< \infty, \,\text{   for all compact }  K \subset U\right\}.
\end{aligned}$$
</div>

And endow it with the [topology generated by the
family of
seminorms](https://nowheredifferentiable.com/2023-01-29-PDE-1-Fourier/#:~:text=together-,with,-a%20countable%20family)


<div>
$$\begin{aligned}
\rho\U {K\U n,p}(f):= \left\lVert f \right\rVert\U {L^p(K\U n)}.
\end{aligned}$$
</div>

Where $K\U n$ are selected such that
$\bigcup\U {n \in \mathbb{N}} K\U n =U$.


Note that $L^q\U {\mathrm{loc}}(U) \subset L^p\U {\mathrm{loc} }(U)$ for all
$q \leq p$.


**Exercise 11**. Show that $L^p\U {\mathrm{loc} }(U)$ is a Fréchet
space.


<div class="exercise-container">
<button class="exercise-button" onclick="toggleExercise(this)">Hint</button>
<div class="exercise-text">
The topology is
[metrizable](https://nowheredifferentiable.com/2023-01-29-PDE-1-Fourier/#:~:text=together-,with,-a%20countable%20family)
as the family of seminorms is countable. By Exercise
[3](#convergence TVS)
if $f\U n \in L^p\U {\mathrm{loc}}(U)$ is Cauchy then $f\U n$ is Cauchy for
all $L^p(K)$ $D^\alpha \varphi\U n$ so converges to some $f\U K \in L^p(K)$.
Show that $f\U K= \left.f\right|\U {K}$ where $f \in L^p\U {\mathrm{loc}}(U)$
to conclude the proof.
</div>
</div>

 <a name="motivation">
**Theorem 1** </a>  (Locally integrable functions as distributions). The
mapping

<div>
$$\begin{aligned}
T:L^1\U {\mathrm{loc}}(U) & \hookrightarrow  \mathcal{D}'(U) \\
u                       & \longmapsto     T\U u
.\end{aligned}$$
</div>

Defined by

<div>
$$\begin{align}
\label{duality}
(\varphi,T\U u):= \int\U {U}\varphi u   , \quad\forall \varphi\in C\U c^\infty(U).
\end{align}$$
</div>

Is injective and continuous.



Proof. We begin by showing that $T\U u \in \mathcal{D}'(U)$. Firstly,
the integral in (\ref{duality})  is finite as $\varphi$ has compact support.
Secondly, if we write $K$ for the support of $\varphi$, it holds that


<div>
$$\begin{aligned}
(f,\varphi u)= \int\U {K}\varphi f u \leq \left\lVert u \right\rVert\U {L^1(K)} \left\lVert \varphi f \right\rVert\U {C^0\U c(K)} .
\end{aligned}$$
</div>

Which, by our equivalent characterization of
$\mathcal{D}'(U)$ in (\ref{equiv})  shows that $T\U u \in  \mathcal{D}'(U)$. We now show
that the identification is injective. That is, if

<div>
$$\begin{aligned}
\int\U {U}\varphi u=0 , \quad\forall \varphi \in C\U c^\infty(U) .
\end{aligned}$$
</div>

Then $u=0$. Consider a compact set $K \subset U$ and
write $g$ for the extension of $\mathrm{sign}(u)$ by zero outside of
$K$. Clearly $g \subset L^1(\mathbb{R}^d)$. Consider an approximation to
the identity $\phi\U n$ (see Appendix
[12](#smooth section) )
and set

<div>
$$\begin{aligned}
\varphi\U n :=  g\star \phi\U n.
\end{aligned}$$
</div>

By the approximation and smoothing of Propositions
[6](#app pn)-[7](#smooth) we obtain a bounded sequence with
$\varphi\U n \subset C\U c^\infty(U)$ for $n$ large enough and such that


<div>
$$\begin{aligned}
\lim\U {n \to \infty}\varphi\U n =g \in L^1(\mathbb{R}^d) ; \quad \left\lVert \varphi\U n \right\rVert\U {L^\infty(\mathbb{R}^d)} \leq \left\lVert g \right\rVert\U {L^\infty(\mathbb{R}^d)}=1.
\end{aligned}$$
</div>

By the first part of the above, we may take a
subsequence $\varphi\U {n\U k}$ converging to $g$ almost everywhere, and by
the second we may apply the dominated convergence theorem to obtain that


<div>
$$\begin{aligned}
0= \lim\U {k \to \infty}\int\U {U}\varphi\U {n\U k} u=\int\U {K}\left| u \right|.
\end{aligned}$$
</div>

As a result, $u=0$ vanishes on $K$. Since $K$ was
any compact subset of $U$ and every open set can be written as a union
of compact sets we conclude that $u=0$ as desired. The continuity of $T$
follows from the estimate

<div>
$$\begin{aligned}
(\varphi,T\U {u} -T\U v)\leq \left\lVert \varphi \right\rVert\U {C\U c^k(K)}\left\lVert u-v \right\rVert\U {L^1\U {\mathrm{loc}}(U)}.
\end{aligned}$$
</div>

Where $\varphi \in C\U c^\infty(U)$ has support $K$
(remember we are considering the weak-$\star $ topology on
$\mathcal{D}'(U)$). ◻


Due to the above immersion, we will naturally consider
$L^1\U {\mathrm{loc}}(U)$ as a subspace of $\mathcal{D}'(U)$. In
particular, any subspaces of $L^1\U {\mathrm{loc} }(U)$ such as $L^p(U)$
or $C^\infty(U)$ can also be considered as distributions.


**Exercise 12**. Show that the $L^1\U {\mathrm{loc}}(U)$ is not closed in
$\mathcal{D}'(U)$ .


<div class="exercise-container">
<button class="exercise-button" onclick="toggleExercise(this)">Hint</button>
<div class="exercise-text">
Show that an approximation to the identity converges to a
Dirac delta $\delta \U 0 \in \mathcal{D}'(U)$. However
$\delta \U 0 \not\in L^1\U {\mathrm{loc}}(U)$.
</div>
</div>

## Support of a distribution

In the continuous case, the support of a function is well-defined as the
smallest closed set outside of which the set is zero. However, when
working with an equivalence class of functions the definition must be
amended (consider for example the support of $0=1\U {\mathbb{Q}}$). This
is resolved by the following definitions.


**Definition 7**. We say that a distribution $w \in \mathcal{D}'(U)$
**vanishes** on $V \subset U$ if

<div>
$$\begin{aligned}
(\varphi, w)=0 , \quad\forall \varphi \in C\U c^\infty(U) \text{ with } \mathbf{supp}(\varphi) \subset V  .
\end{aligned}$$
</div>

And write

<div>
$$\begin{aligned}
w =0 \text{ on } V.
\end{aligned}$$
</div>




If a function vanishes on a collection of sets it also vanishes on their
union, this extends to distributions.

 <a name="biggest vanish">
**Lemma 1** </a> . Let $\left\\{U\U \alpha\right\\}\U {\alpha \subset I}$ be a
collection of open sets in $U$ and suppose that

<div>
$$\begin{aligned}
w=0 \text{ on  } U\U \alpha , \quad\forall \alpha \in I.
\end{aligned}$$
</div>

Then $w$ vanished on
$U:=\bigcup\U {\alpha \in  I}U\U \alpha$.



Proof. Let $\varphi$ have support in $U$. Then, by compactness, we can
extract a finite covering $\left\\{U\U i\right\\}\U {i=1}^n$ of
$\mathbf{supp}(\varphi)$. Let $\left\\{\rho \U i\right\\}\U {i=1}^n$ be a
partition of unity subordinate to $U\U i$ (see Appendix
[13](#local to global)). Then

<div>
$$\begin{aligned}
(\varphi,\omega)=\left(\sum\U {i=1}^n \rho \U i \varphi,w \right)=\sum\U {i=1}^n (\rho \U i \varphi,w )=0 .
\end{aligned}$$
</div>

Since $\varphi$ was any test function supported in
$U$ this concludes the proof. ◻


By the just proved Lemma [1](#biggest vanish) we see that there is a largest set on which
$w$ vanishes. As a result, we can make the following definition.

 <a name="support def">
**Definition 8** </a> . Let $w \in C\U c^\infty(U)$ and let $V$ be the largest
open set on which $w$ vanishes. Then, we define the **support** of $w$
as

<div>
$$\begin{aligned}
\mathbf{supp}(w)= V^c .
\end{aligned}$$
</div>




Since $L^1\U {\mathrm{loc}}(U)$ is naturally included in $\mathcal{D}'(U)$
we obtain in particular the definition of support of a function
$f \in L^1\U {\mathrm{loc}}(U)$.


**Exercise 13**. If $f \in L^1\U {\mathrm{loc}}(U)$ the support of $f$ is
the complementary of the largest open set on which $f$ is $0$ almost
everywhere. In particular, if $f$ is continuous, the (distributional)
support of $f$ coincides with the classical support of $f$.


<div class="exercise-container">
<button class="exercise-button" onclick="toggleExercise(this)">Hint</button>
<div class="exercise-text">
We saw in Theorem [1](#motivation) that $f$ is $0$ almost everywhere on some open
set if and only if it integrates to $0$ against any test function on the
open set. This shows the first part and the second follows immediately.
</div>
</div>

# Sobolev spaces

Now that we have built the space of distributions we can define weak
derivatives of test functions just as we did with tempered
distributions.


**Definition 9**. Given $w \in \mathcal{D}'(U)$ we define the (weak)
$\alpha$-th derivative by

<div>
$$\begin{aligned}
(u,D^\alpha \omega):=(-1)^{\left| \alpha \right| }(D^\alpha u, \omega).
\end{aligned}$$
</div>





**Exercise 14**. Show that $D^\alpha w \in\mathcal{D}'(U)$.


<div class="exercise-container">
<button class="exercise-button" onclick="toggleExercise(this)">Hint</button>
<div class="exercise-text">
Show that $D^\alpha$ is continuous on $\mathcal{D}(U)$ by
using that $\left\lVert \cdot  \right\rVert\U {C^k(U)}$ are restrictable
seminorms. Conclude by using that $D^\alpha$ defined on
$\mathcal{D}'(U)$ is the
[adjoint](https://en.wikipedia.org/wiki/Transpose_of_a_linear_map) of
$D^\alpha$ defined on $\mathcal{D}(U)$
</div>
</div>

A prerequisite for the definition to make sense is that the notion
corresponds to that of classical derivative.


**Exercise 15**. Let $u \in C\U {\mathrm{loc}}^1(U)$ have classical
derivatives $u^{(i)}$. Then $u^{(i)}= \partial\U i u$.


<div class="exercise-container">
<button class="exercise-button" onclick="toggleExercise(this)">Hint</button>
<div class="exercise-text">
By definition of weak derivatives and the chain rule, we have
the distributional equality

<div>
$$\begin{aligned}
T\U {u^{(i)}}-T\U {\partial \U i u}=T\U {u^{(i)}-\partial \U i u}=0 \in \mathcal{D}'(U)   .
\end{aligned}$$
</div>

The result follows by the injectivity of $T$.
</div>
</div>

 <a name="sobolev def">
**Definition 10** </a>  (Sobolev spaces). Given an open set
$U \subset \mathbb{R}^d$, $k \in \mathbb{N}$ and $p \in [1,\infty]$ we
define

<div>
$$\begin{aligned}
W^{k,p}(U):=\left\{ u: D^{\alpha}u \in L^p(U) \hookrightarrow \mathcal{D}'(\mathbb{R}^d), \quad\forall \left| \alpha \right|\leq k   \right\} .
\end{aligned}$$
</div>

Where $L^p(U)$ is identified as a subspace of
$\mathcal{D}'(U)$ by Theorem [1](#motivation). We give $W^{k,p}(U)$ the norm

<div>
$$\begin{aligned}
\left\lVert u \right\rVert\U {W^{k,p}(U)}&:=\sum\U {\left| \alpha \right|\leq k } \left\lVert D^\alpha u \right\rVert\U {L^p(U)}.        \end{aligned}$$
</div>




That is, $W^{k,p}(U)$ is the space of $k$-times (weakly) differentiable
functions with derivatives in $L^p(U)$. An equivalent norm that is also
sometimes used is

<div>
$$\begin{aligned}
\left\lVert u \right\rVert\U {W^{k,p}(U)}\sim \sum\U {j=1}^k \left\lVert \nabla^j u \right\rVert\U {L^p(U\to \mathbb{R}^{d^j})} .\end{aligned}$$
</div>



The local Sobolev spaces $W^{k,p}\U {\mathrm{loc}}(U)$ are defined
similarly, where we now only require that

<div>
$$\begin{aligned}
D^\alpha u \in L^p\U {\text{loc}}(U) , \quad\forall \left| \alpha \right|\leq k .\end{aligned}$$
</div>


And now generate the topology by local seminorms analogously to
$L^p\U {\mathrm{loc}}(U)$.


**Theorem 2** (Completeness of Sobolev spaces). For all
$k \in \mathbb{N}$ and $p \in [1,\infty]$ both $W^{k,p}(U)$ and
$W^{k,p}\U {\mathrm{loc}}(U)$ are Banach spaces. If $p \in (1,\infty)$
these spaces are also reflexive.



Proof. Let $\left\\{u\U n\right\\}\U {n=1}^\infty$ be a Cauchy sequence in
$W^{k,p}(U)$. Then, by definition of the norm on $W^{k,p}(U)$ the
sequence of derivatives $D^\alpha u\U n$ is Cauchy in $L^p(U)$ for each
$\left| \alpha \right|\leq k$ and since $L^p(U)$ is complete, converge
to some functions $u^{\alpha}$

<div>
$$\begin{aligned}
\lim\U {n \to \infty} D^\alpha u\U n = u^{(\alpha)} \in L^p(U) , \quad\forall \left| \alpha \right| \leq k  .
\end{aligned}$$
</div>

To conclude, it suffices to show that $u:= u^{(0)}$
verifies

<div>
$$\begin{aligned}
D^\alpha u= u^{(\alpha)}.
\end{aligned}$$
</div>

This holds as, for every test function
$\varphi \in  \mathcal{D}(U)$

<div>
$$\begin{aligned}
\int\U {U} u^{(\alpha)}\varphi =\lim\U {n \to \infty}\int\U {U} u\U n^{(\alpha)}\varphi=\lim\U {n \to \infty}(-1)^{\left| \alpha \right| }\int\U {U} u\U nD^\alpha\varphi=(-1)^{\left| \alpha \right| }\int\U {U} uD^\alpha\varphi  .
\end{aligned}$$
</div>

Where the first and last inequality follows from the
continuous immersion of $L^p(U)$ in $\mathcal{D}'(U)$ (Hölder's
inequality). Reflexivity follows from the fact that the mapping


<div>
$$\begin{aligned}
T: W^{k,p}(U) & \longrightarrow (L^p(U))\U {\left| \alpha \right|\leq k }
\\
u             & \longmapsto     (D^{\alpha}(u))\U {\left| \alpha \right|\leq k }
.\end{aligned}$$
</div>

Is an isometry, so $\mathbf{Im}(T)$ is closed
in the reflexive Banach space $(L^p(U))\U {\left| \alpha \right|\leq k }$
and thus reflexive (see [3](https://link.springer.com/book/10.1007/978-0-387-70914-7) page 70). The case of
$W^{k,p}\U {\mathrm{loc}}(U)$ is proved identically now working with the
local seminorms. ◻


We now show some relevant properties of the weak derivative all of which
are to be expected knowing the classical case. These can be greatly
generalized with tools we will later develop.

 <a name="properties">
**Proposition 1** </a>  (Properties). Let $u \in W^{k,p}(U)$. Then it holds
that

1.  Leibniz rule: given $\varphi \in C^1(U)$ it holds that


<div>
$$\begin{aligned}
\partial \U {i} (u \varphi)= \partial\U i u \varphi+ u \partial \U i \varphi .
\end{aligned}$$
</div>



2.  The translation $\tau\U y u(x):=u(x-y) \in W^{k,p}(U)$ with
$D^\alpha \tau\U y u = \tau\U y D^\alpha u$.

3.  Let $u \in W^{k,p}(\mathbb{R}^d)$ and $v \in L^1(\mathbb{R}^d)$.
Then

<div>
$$\begin{aligned}
D^\alpha (v\star u)= v\star  D^\alpha u
\end{aligned}$$
</div>





Proof. Points 1 and 2 follow by the definition of weak derivative and
the relevant properties for classical derivatives. The third property
follows from the second as, by Fubini,

<div>
$$\begin{aligned}
& (v\star u,D^\alpha\varphi )  = \int\U {\mathbb{R}^d}v(y)\left(\int\U {\mathbb{R}^d}D^\alpha \varphi(x) u(x-y) \,\mathrm{d}x \right) \,\mathrm{d}y \\&
=(-1)^{\left| \alpha \right| } \int\U {\mathbb{R}^d}v(y)  \left(\int\U {\mathbb{R}^d}\varphi(x) D^\alpha u(x-y) \,\mathrm{d}x \right) \,\mathrm{d}y             =(-1)^{\left| \alpha \right| }(v\star D^\alpha u, \varphi).
\end{aligned}$$
</div>

◻


A natural question is what relationship there is between Sobolev
functions and classical derivatives. For example, in $1$ dimension a
classical result is that $u \in W^{1,1}(a,b)$ if and only if $u$ is
absolutely continuous and has derivative almost everywhere. A more
general result is as follows.


**Proposition 2** (Absolute continuity on lines). The following are
equivalent

-   $u \in W^{1,p}\U {\mathrm{loc}}(U)$.

-   $u \in L^p\U {\mathrm{loc}}(U)$ is almost everywhere differentiable
with classical derivatives $u^{(i)} \in L^p\U {\mathrm{loc}}(U)$ and,
given $V \Subset U$ it holds that $u$ is absolutely continuous on
almost all (with respect to the Lebesgue measure on
$\mathbb{R}^{d-1}$) line segments in $V$ parallel to the coordinate
axis.

The above holds true if we replace
$W^{1,p}\U {\mathrm{loc}}(U),L^p\U {\mathrm{loc}}(U)$ with their none local
counterparts $W^{1,p}(U),L^p(U)$.


We omit the proof which can be found in [4](https://math.aalto.fi/~jkkinnun/files/sobolev_spaces.pdf) pages $39-43$. The next
exercise show that, perhaps somewhat unexpectedly, to have
$u \in  W^{1,p}(U)$ it is not sufficient to require that $u$ is
differentiable almost everywhere with integrable derivatives.


**Example 2**. The [devil's
staircase](https://en.wikipedia.org/wiki/Cantor_function) $c$ is
differentiable almost everywhere with $c'=0$.


As a result, if $c \in W^{1,p}(0,1)$ then $u$ would be constant (which
it is not). In fact, $c \not\in W^{1,p}(0,1)$ as it is not absolutely
continuous.

# Smooth approximation of Sobolev functions

The definition of weak derivative requires one to integrate against
smooth functions whenever trying to prove some property holds. This is
somewhat cumbersome. One would much rather

1.  Work pretending all Sobolev functions are (classically) smooth.

2.  Manipulate them according to the standard rules of calculus.

3.  Obtain a result that holds for all Sobolev functions (and not just
the classically smooth ones).

This process can be rigorously justified by the density of various
spaces of smooth functions in Sobolev spaces. Or to use Tao's
terminology, by giving ourselves [an epsilon of
room](https://terrytao.wordpress.com/2009/02/28/tricks-wiki-give-yourself-an-epsilon-of-room/).

In this section, we prove the relevant results. These rely heavily on
the analogous density results for functions in $L^p(U)$ (see Appendix
[12](#smooth section)).
As a result, they will not when $p=\infty$. We start without making any
assumptions on $U$ and obtain two local-type results. Throughout this
section we will often be switching between different open sets and, if
following the proofs, making some drawings is recommended.

 <a name="local">
**Theorem 3** </a>  (Local approximation by smooth functions). Let
$u \in W^{k,p}(U)$ for $p < \infty$, denote its extension by zero
$\tilde{u}$ and let $\left\\{\phi\U n\right\\}\U {n=1}^\infty$ be an
approximation to unity. Then

<div>
$$\begin{aligned}
u=\lim\U {n \to \infty} \tilde{u}\star \phi\U n  \in W^{k,p}(V) , \quad\forall V \Subset U.
\end{aligned}$$
</div>

As a result, for any $V \Subset U$,


<div>
$$\begin{aligned}
\overline{\left.C\U c^\infty(\mathbb{R}^d)\right|\U {V}}=\left.W^{k,p}(U)\right|\U {V}\quad \text{ and } \quad \overline{\left.C\U c^\infty(\mathbb{R}^d)\right|\U {U}}=W\U {\mathrm{loc}}^{k,p}(U)
\end{aligned}$$
</div>





Proof. Given a compactly embedded set $V \Subset U$ we can take $n$
large enough so that $V+  B \left(0, \frac{1}{n}\right) \subset U$ and
as a result, the convolution $\varphi\U n:= \tilde{u} \star  \phi\U n$ verifies
(see Observation [6](#local smoothing))

<div>
$$\begin{aligned}
\varphi\U n= u\star  \phi\U n \quad  \text{ on  } V .
\end{aligned}$$
</div>

Thus, by the third property
[1](#properties), for all
$\left| \alpha \right| \leq k$

<div>
$$\begin{aligned}
D^\alpha \varphi\U n = D^\alpha u \star  \phi\U n \quad \text{ on } V.
\end{aligned}$$
</div>

Taking limits we conclude from Proposition
[6](#app pn) that


<div>
$$\begin{aligned}
\lim\U {n \to \infty}D^\alpha \varphi\U n =D^\alpha u \in L^p(V) .
\end{aligned}$$
</div>

To conclude density of $C\U c^\infty(\mathbb{R}^d)$ in
$\left.W^{k,p}(U)\right|\U {V}$ consider $K$ such that

<div>
$$\begin{aligned}
V \subset K; \quad  K+ B\U {1 /n}\subset U.
\end{aligned}$$
</div>

And a bump function
$\eta\U V \in C\U c^\infty(\mathbb{R}^d)$ that is equal to $1$ on $V$ and is
supported in $K$ (this is possible by Uryshon's lemma and a
convolution). Then,

<div>
$$\begin{aligned}
\varphi\U {V,n}:= \varphi\U n \eta \U V \in C\U c^\infty(\mathbb{R}^d); \quad \lim\U {n \to \infty}\varphi\U {V,n}=u \in W^{k,p}(V).
\end{aligned}$$
</div>

The density of $C\U c^\infty(\mathbb{R}^d)$ in
$W^{k,p}\U {\mathrm{loc}}(U)$ follows by taking $V\U n$ converging to $U$
and $u\U n:= \varphi\U {V\U n,n}$ as then, for every compactly included
$W \Subset  U$

<div>
$$\begin{aligned}
\lim\U {n \to \infty}u\U {n}=u \in W^{k,p}(W) .
\end{aligned}$$
</div>

This concludes the proof as by Exercise
[3](#convergence TVS)
local convergence is equivalent to convergence on every compactly
included subset. ◻



**Observation 3**. Note that, without further assumptions on $U$ it is
impossible to get a global approximation by smooth functions defined on
all of $\mathbb{R}^d$. This is because, the convolution $f\star  \phi\U n$ can
only be defined on

<div>
$$\begin{aligned}
U\U {1/n}:= \left\{x \in U: d(x,\partial U)> \frac{1}{n}\right\} .
\end{aligned}$$
</div>




The above issue disappears when $U =\mathbb{R}^d$. This shows that

 <a name="approx rd">
**Theorem 4** </a>  (Global approximation in $\mathbb{R}^d$). It holds that
for all $p<\infty$,

<div>
$$\begin{aligned}
\overline{C\U c^\infty(\mathbb{R}^n)}=W^{k,p}(\mathbb{R}^d).
\end{aligned}$$
</div>





Proof. Let $\eta   \in C\U c^\infty(\mathbb{R}^d)$ be equal to $1$ on
$B\U 1$ and set $\eta  \U n(x):=\eta  (x /n)$. Then, given
$u \in W^{k,p}(\mathbb{R}^n)$ and a smooth approximation to unity
$\phi\U n$ we obtain that, by the triangle inequality

<div>
$$\begin{aligned}
u= \lim\U {n \to \infty}(u\star \phi\U n)\eta  \U n \in W^{k,p}(\mathbb{R}^d).
\end{aligned}$$
</div>

◻


The following Theorem shows a global-type approximation.

 <a name="Meyers">
**Theorem 5** </a>  (Meyers-Serrin: local till boundary approximation). Let
$U \subset \mathbb{R}^d$ be open, then for all $p<\infty$


<div>
$$\begin{aligned}
\overline{C^\infty\U {\mathrm{loc}}(U)\cap W^{k,p}(U)}=W^{k,p}(U).
\end{aligned}$$
</div>





Proof. The proof is an instructive way of using a partition of unity
to piece together a local result (in this case Theorem
[3](#local)) to get a global
one. Let $\epsilon >0$ and consider an open covering
$\left\\{V\U i\right\\}\U {i=0}^\infty$ of $U$ with $V\U 0 =\emptyset$ and
$V\U {i} \Subset V\U {i+1}$. By Theorem
[17](#partition) we may
obtain a partition of unity $\rho \U i$ subordinate to the "rings"
$U\U {i}:= V\U {i+1}\setminus \overline{V\U {i-1}}$ (the trickery with the
indices is so that the $U\U i$ actually cover $U$). Where we relabel so
that

<div>
$$\begin{aligned}
\mathbf{supp}(\rho \U i)\subset U\U i .
\end{aligned}$$
</div>

We have that $\rho\U i u \in C\U c^\infty({V\U {i+1}})$
with $V\U {i+1} \Subset U$ so by the local approximation in Theorem
[3](#local) we can find $n\U i$
such that

<div>
$$\begin{aligned}
\left\lVert \phi\U {n\U i}\star (\rho\U i u)-\rho\U i u \right\rVert\U {W^{k,p}(U)}=\left\lVert \phi\U {n\U i}\star (\rho\U i u)-\rho\U i u \right\rVert\U {V\U {i+1}}\leq \frac{\epsilon }{2^i} .
\end{aligned}$$
</div>

Now we obtain the global approximation by taking


<div>
$$\begin{aligned}
\varphi:= \sum\U {i=1}^\infty \phi\U {n\U i}\star  (\rho\U i u) \in C\U {\mathrm{loc}}^\infty(U) .
\end{aligned}$$
</div>

As then

<div>
$$\begin{aligned}
\left\lVert \varphi-u \right\rVert
\U {W^{k,p}(U)}\leq\sum\U {i=1}^\infty \left\lVert \phi\U {n\U i}\star (\rho\U i u)-\rho\U i u  \right\rVert\U {W^{k,p}(U)}\leq \sum\U {i=1}^\infty \frac{\epsilon }{2^i}=\epsilon   .
\end{aligned}$$
</div>

◻


Note that Theorem [5](#Meyers)
is not strictly stronger than theorem [3](#local) as it is not, in general, possible to extend
functions in $C^\infty\U {\mathrm{loc}}(U)$ to $C\U c^\infty(\mathbb{R}^n)$.
As a corollary of Meyers-Serrin's theorem, we obtain an equivalent
definition of $W^{k,p}(U)$.

 <a name="eq def">
**Exercise 16** </a> . Let $U \subset \mathbb{R}^d$ be an open set and
$p<\infty$. Then $W^{k,p}(U)$ is equal to the completion of
$C^\infty\U {\mathrm{loc}}(U)\cap W^{k,p}(U)$ with the
$\left\lVert \cdot  \right\rVert\U {W^{k,p}(U)}$ norm.


<div class="exercise-container">
<button class="exercise-button" onclick="toggleExercise(this)">Hint</button>
<div class="exercise-text">
Use that $W^{k,p}(U)$ is complete and that the completion of
a metric space is unique.
</div>
</div>

Before Theorem [5](#Meyers) was
proved, both our original definition
[10](#sobolev def)
(distributions with derivatives in $L^p(U)$) and the one in Corollary
[16](#eq def) (closure of
smooth functions with Sobolev norm) were used as the definition of
$W^{k,p}(U)$. But it was unclear which was the "correct" Sobolev space.
This debate was settled by Meyers and Serrin who proved that, as we just
showed, both are equal.

We now show an example of how these kinds of density results can be
useful. The following generalizes the second point of Proposition
[1](#properties)

 <a name="change of variables">
**Exercise 17** </a>  (Change of variables). Let $V,U$ be open in
$\mathbb{R}^d$ and $\Phi: V \simeq U$ be bijective with
$\Phi \in C^k(V \to \mathbb{R}^d), \Phi^{-1} \in C^1(U\to \mathbb{R}^d)$.
Then for any $u \in  W^{k,p}(U)$ it holds that
$u \circ\Phi \in W^{k,p}(V)$ and the usual chain rule holds. For example


<div>
$$\begin{align}
\label{chain}
\partial \U i (u\circ \Phi) = \sum\U {j=1}^d (\partial \U i \Phi\U j)(\partial \U j u\U j)\circ \Phi\U j  .
\end{align}$$
</div>




<div class="exercise-container">
<button class="exercise-button" onclick="toggleExercise(this)">Hint</button>
<div class="exercise-text">
Give yourself an $\epsilon$ of room. By induction, it
suffices to consider the case $k=1$.We can approximate $u$ on each
compact $K \subset U$ by a sequence of functions
$u\U n \in C\U c^\infty(\mathbb{R}^d)$. For $u\U n$ the equality
(\ref{chain})  holds.
Furthermore, by a change of variables,
(\ref{chain})  is
continuous in $u\in W^{1,p}(\Omega)$ so we may pass to the limit and
obtain (\ref{chain})  for
$u$ on $K$. Since $K$ was any, the equality also holds on the whole of
$U$.
</div>
</div>

In Exercise [17](#change of variables) it is important that $\Phi$ is
diffeomorphic so that composition with $\Phi$ is continuous.


**Exercise 18**. Show that the conclusion of Exercise
[17](#change of variables) is false if we only assume that
$\Phi \in C^k(\mathbb{R}^d)$ and do not impose invertibility.


<div class="exercise-container">
<button class="exercise-button" onclick="toggleExercise(this)">Hint</button>
<div class="exercise-text">
Divide by zero.
</div>
</div>

Now we provide a final global approximation result in the case where the
domain is smooth (see Appendix [14](#boundary) for a review on manifolds with boundary) and
bounded.

 <a name="global">
**Theorem 6** </a>  (Global, smooth on boundary approximation). Let $\Omega$
be a **bounded** open domain with **$C^1$ boundary**, then for all
$p<\infty$.

<div>
$$\begin{aligned}
\overline{\left.C\U c^\infty(\mathbb{R}^d)\right|\U {\Omega}}= W^{k,p}(\Omega).
\end{aligned}$$
</div>





Proof. The idea will be to locally translate points close to the
boundary further into $\Omega$ so that we can convolve with an
approximation of unity and then recover the global case with a partition
of unity. We begin by "straightening the boundary". That is, since
$\partial \Omega$ is $C^1$, given $x\U 0 \in \partial  \Omega$ there
exists an open set $V \subset \mathbb{R}^d$ and a function
$\gamma \in  C^1(\mathbb{R}^{d-1})$ such that, relabeling and flipping
the last coordinate axis if necessary

<div>
$$\begin{aligned}
V \cap \Omega = \left\{x \in V :x\U d  >\gamma (x\U 1,\ldots,x\U {d-1})\right\}  .
\end{aligned}$$
</div>

By considering a translation in the last coordinate
$e\U d=(0,\ldots,0,1)$ and its mollification by an approximation of unity
$\phi\U n$

<div>
$$\begin{aligned}
u\U n(x):= u\left(x+ \frac{2}{n}e\U d \right); \quad \varphi\U n:= u\U n \star \phi\U n .
\end{aligned}$$
</div>

For $n$ big enough we have that $\varphi$ is well
defined ans smooth on $W\U 0:=B\U {\frac{1}{n}}(x\U 0)$. Since translation is
continuous on $L^p(U)$ for $p \in [1,\infty)$ and by the behavior of
differentiation with convolution (see Proposition
[1](#properties)), for $n$
large enough

<div>
$$\begin{aligned}
\left\lVert u -\varphi\U n \right\rVert\U {W^{k,p}(W\U 0)}\leq \left\lVert u -u\U n \right\rVert\U {W^{k,p}(W\U 0)}+\left\lVert u\U n -u\U n\star \phi\U n \right\rVert\U {W^{k,p}(W\U 0)}\leq \epsilon.
\end{aligned}$$
</div>

Now, since $\Omega$ is bounded $\partial \Omega$ is
compact we may extract a finite covering
$\left\\{W\U i:=B\U {\frac{1}{n\U i}}(x\U i)\right\\}\U {i=0}^n$ of
$\partial \Omega$ and functions $\left\\{\varphi\U i\right\\}\U {i=1}^n$
smooth on $W\U i$ such that

<div>
$$\begin{aligned}
\left\lVert u -\varphi\U n \right\rVert\U {W^{k,p}(W\U i)}\leq \frac{\epsilon}{n+2}  .
\end{aligned}$$
</div>



Now we take an open set $W\U {n+1} \Subset \Omega$ such that
$\left\\{W\U i\right\\}\U {i=0}^{n+1}$ cover $\Omega$. By the local
approximation of Theorem [3](#local) we know we can approximate $u$ on $W\U {n+1}$ by some
$\varphi\U {n+1} \in C\U c^\infty(\mathbb{R}^d)$

<div>
$$\begin{aligned}
\left\lVert u-\varphi\U {n+1} \right\rVert\U {W^{k,p}(W\U {n+1})}\leq\frac{\epsilon}{n+2} .
\end{aligned}$$
</div>

Finally, we take a smooth partition of unity
$\left\\{\rho \U i\right\\}\U {i=0}^{n+1}$ subordinate to
$\left\\{W\U i\right\\}\U {i=0}^{n+1}$ and a bump function
$\eta \in C\U c^\infty(\mathbb{R}^d)$ which is equal to $1$ on $\Omega$
and is supported on $\bigcup\U {i=0}^{n+1} W\U i$ (see example
[5](#bump example2)) and
set

<div>
$$\begin{aligned}
\varphi:= \eta \sum\U {i=0}^{n+1} \rho \U i \varphi\U i \in  C^\infty\U c(\Omega) .
\end{aligned}$$
</div>

This gives the desired approximation


<div>
$$\begin{aligned}
\left\lVert u-\varphi \right\rVert\U {W^{k,p}(\Omega)} \leq \sum\U {i=0}^{n+1} \left\lVert \rho \U i(u-\varphi\U i) \right\rVert\U {W^{k,p}(W\U i)} \leq  \epsilon  .
\end{aligned}$$
</div>

This concludes the proof. ◻


In contrast to Theorem [5](#Meyers), Theorem [6](#global) shows that Sobolev functions on smooth bounded
domains can be approximated by functions that are also smooth on the
boundary of the domain $\Omega$. This will prove fundamental in the
next section. Both to extend them to the whole of $\mathbb{R}^d$ and to
restrict them to $\partial \Omega$.

# <a name="extension section">  Extensions and restrictions  </a>

Using the approximation of Sobolev functions by functions smooth on the
boundary we can extend functions in $W^{k,p}(\Omega)$ to the whole of
$\mathbb{R}^d$. However, the extension is not unique.

 <a name="extension">
**Theorem 7** </a>  (Extension theorem). Let $\Omega\subset \mathbb{R}^d$ be
a **bounded** open set with **$C^k$** **boundary** where
$k \in \mathbb{N}\U +$. Then for all $p \in [1,\infty)$ . Then, given an
open set $W$ with $\Omega \Subset W$ there exists a continuous operator


<div>
$$\begin{aligned}
E: W^{k,p}(\Omega)\to W^{k,p}(\mathbb{R}^d); \quad E: C^{k}(\Omega)\to C^k(\mathbb{R}^d).
\end{aligned}$$
</div>

such that

<div>
$$\begin{aligned}
Eu = \begin{cases}
u \quad & \text{ on  }  \Omega \\
0 \quad & \text{ on }  W^c
\end{cases}.
\end{aligned}$$
</div>

We call $E u$ an **extension** of $u$ to
$\mathbb{R}^n$.



Proof. We work first in the upper half-space (the canonical example of
a manifold with boundary)

<div>
$$\begin{aligned}
\mathcal{H}^d =\left\{x=(x\U 1,\ldots,x\U d) \in \mathbb{R}^d : x\U d \geq 0\right\} .
\end{aligned}$$
</div>

That is, we suppose that there is some open set
$\Omega' \subset  \mathbb{R}^d$ such that

<div>
$$\begin{aligned}
\Omega=\Omega' \cap \mathcal{H}^d\U {>0}.
\end{aligned}$$
</div>

Where

<div>
$$\begin{aligned}
\quad \mathcal{H}^d\U {>0} =\mathrm{int}(\mathcal{H}^d)=\left\{x=(x\U 1,\ldots,x\U d) \in \mathbb{R}^d : x\U d >0\right\} .
\end{aligned}$$
</div>

By Theorem [6](#global) we also give ourselves an epsilon of room by
supposing that $u \in C^k(\overline{\Omega})$. We define the extension
of $u$ to $\Omega'$ as

<div>
$$\begin{aligned}
Eu(x) = \begin{cases}
u(x) \quad                                 & x\U {d}                                 \geq 0      \\
\sum\U {j=1}^{k+1} a\U j  u\U j(x - j e\U d) \quad & x\U d                                           < 0
\end{cases}.
\end{aligned}$$
</div>

We will have $Eu \in C^k(\Omega')$ as long as we can
get the derivatives to match up on the boundary
$\\{x\U d=0\\}\cap \overline{\Omega'}$. That is, as long as $a\U j$ verify


<div>
$$\begin{aligned}
\sum\U {j=1}^{k+1}(-j)^l a\U j =1 , \quad l=0,1,\ldots,k .
\end{aligned}$$
</div>

The above is a system of $k+1$ equations with
$k+1$-unknowns $a\U j$. Its matrix is the [Vandermonde
matrix](https://en.wikipedia.org/wiki/Vandermonde_matrix) (which is
invertible). As a result, the system may be solved to extend $u$. By the
form of $Eu$ we have the bound

<div>
$$\begin{aligned}
\left\lVert Eu \right\rVert\U {W^{k,p}(\Omega')} \leq c\left\lVert u \right\rVert\U {W^{k,p}(\Omega)} .
\end{aligned}$$
</div>

Where
$c:= (k+1)^{l+1}\max \left\\{1,\left\lVert a \right\rVert\U \infty\right\\}$.
Working now in the general case for $\Omega$, we may cover the compact
$\overline{\Omega}$ by a finite amount of bounded open sets
$\Omega\U i \subset W$ such that

<div>
$$\begin{aligned}
\Phi\U i : \Omega\U i \xrightarrow{\sim} \Omega\U i'\quad \text{and}  \quad \Phi\U i : \Omega\U i \cap \Omega \xrightarrow{\sim} \Omega\U i' \cap \mathcal{H}^d .
\end{aligned}$$
</div>

Where $\Omega\U i'$ are open in $\mathbb{R}^{d}$ and
$\Phi\U i$ are $C^k$ diffeomorphisms. By the previous case, we can extend
$u'\U i:=u \circ \Phi\U i^{-1} \in C^k (\Omega\U i' \cap \mathcal{H}^d)$ to
functions $\widetilde{u'\U i} \in C^k(\Omega\U i')$ and then transform back
to the original space to get

<div>
$$\begin{aligned}
\tilde{u\U i}:= \widetilde{u'\U i} \circ \Phi\U i \in C^k(\Omega\U i).
\end{aligned}$$
</div>

Where

<div>
$$\begin{align}
\label{bound}
\left\lVert \tilde{u\U i} \right\rVert\U {W^{k,p}(\Omega\U i)}\lesssim  \left\lVert u\U i \right\rVert\U {W^{k,p}(\Omega)}.
\end{align}$$
</div>

The hidden constant depending only on
$c,\left\lVert \Phi\U i \right\rVert\U {C^k(\Omega\U i)}\left\lVert \Phi\U i^{-1} \right\rVert\U {C^k(\Omega\U i')}$.
Next, using a partition of unity subordinate to
$\left\\{\Omega\U i\right\\}\U {i=1}^n$ we glue the local extensions together
to form an extension to all of $\Omega$

<div>
$$\begin{aligned}
\tilde{u}:= \sum\U {i=1}^n \rho \U i{u\U i} \in C^k(\Omega).
\end{aligned}$$
</div>

The desired extension can now be obtained by
multiplying $\tilde{u}$ with a bump function $\eta$ that is supported in
$W$ and equal to $1$ on $\Omega$.

<div>
$$\begin{aligned}
Eu := \eta \tilde{u} \in C^k(\mathbb{R}^d).
\end{aligned}$$
</div>

By (\ref{bound})  we have that

<div>
$$\begin{aligned}
\left\lVert E u \right\rVert\U {W^{k,p}(\mathbb{R}^d)} \lesssim  \left\lVert u \right\rVert\U {W^{k,p}(\Omega)}.
\end{aligned}$$
</div>

As a result, $E$ is a (bounded) linear operator. So
far we had considered $u \in  C^k(\overline{\Omega})$. Now, since by
Theorem [6](#global) the space
$C^k(\overline{\Omega})$ is dense in $W^{k,p}(\Omega)$ we may extend $E$
to a linear operator on the whole of $W^{k,p}(\Omega)$. A verification
shows that $E$ is also bounded as an operator from $C^k(\Omega)$ to
$C^k(\mathbb{R}^d)$. This concludes the proof. ◻


 <a name="restriction">
**Exercise 19** </a>  (Restriction). Under the conditions of Theorem
[7](#extension) it holds
that

<div>
$$\begin{aligned}
W^{k,p}(\Omega)= \left.W^{k,p}(\mathbb{R}^d)\right|\U {\Omega}; \quad C^{k}(\Omega)= \left.C^{k}(\mathbb{R}^d)\right|\U {\Omega}.
\end{aligned}$$
</div>

That is, functions in
$W^{k,p}(\Omega),C^{k}(\Omega)$ are equal to the restriction of
functions in $W^{k,p}(\mathbb{R}^d),C^{k}(\mathbb{R}^d)$ respectively.


<div class="exercise-container">
<button class="exercise-button" onclick="toggleExercise(this)">Hint</button>
<div class="exercise-text">
Given $u \in W^{k,p}(\Omega)$ we can extend it to
$Eu \in W^{k,p}(\mathbb{R}^d)$ by the just proved extension theorem
[7](#extension). By
definition $u= \left.Eu\right|\U {\Omega}$. The case
$u \in C^k(\mathbb{R}^d)$ is identical.
</div>
</div>

Using extensions also gives us a way to define the Sobolev spaces
$H^s(\Omega)$ when the exponent $s$ is real valued.


**Definition 11**. Given a **bounded** open set $\Omega$ with
**boundary** of type $C^k$ with $k \in \mathbb{N}\U +$, we define for all
real $s \in [0,k]$

<div>
$$\begin{aligned}
H^s(\Omega):=\left.H^s(\mathbb{R}^d)\right|\U {\Omega} .
\end{aligned}$$
</div>




To further generalize this definition to domains where restriction is
not possible one needs to use [complex
interpolation](https://en.wikipedia.org/wiki/Interpolation_space) (see
for example [5](https://books.google.co.uk/books?id=wI4fAwAAQBAJ&printsec=frontcover&hl=fr&source=gbs_ge_summary_r&cad=0#v=onepage&q&f=false) pages 321-333).

# Trace theorem

As we already discussed, a PDE often incorporates boundary information
such as $\left.u\right|\U {\partial \Omega}=0$. This is well defined if
$u$ is continuous, however, if $u \in  W^{k,p}(U)$, and is thus only
defined **almost everywhere**, then $\left.u\right|\U {\partial  U}$ is a
priori not well defined. The following theorem remedies this issue.

 <a name="trace">
**Theorem 8** </a>  (Trace). Let $\Omega$ be a **bounded** open set of
$\mathbb{R}^d$ with $C^1$ **boundary**. Then, there exists a continuous
linear operator

<div>
$$\begin{aligned}
T: W^{1,p}(U)\to L^p(\partial U) .
\end{aligned}$$
</div>

Such that $Tu =\left.u\right|\U {\partial \Omega}$ for
all $u \in C(\overline{\Omega}) \cap W^{1,p}(\Omega)$.



Proof. As in previous results, the trick is to suppose first $u$ is
smooth, work locally, and then obtain a global result using a partition
of unity and the density in Theorem [6](#global).\
Given $x\U 0 \in \partial  \Omega$ we take a open set
$U \subset \mathbb{R}^d$ containing $x\U 0$. Flattening out the boundary
by $\Phi : U \simeq U'$ where necessarily the boundary is preserved


<div>
$$\begin{aligned}
\Phi: U \cap  \partial \Omega\xrightarrow{\sim}U' \cap \partial  \mathcal{H}^d,
\end{aligned}$$
</div>

and using the extension theorem
[7](#extension) to extend
$u':= u\circ \Phi$ to $\widetilde{u}'$ with compact support
$K \subset \mathbb{R}^d$ we obtain by the [divergence
theorem](https://en.wikipedia.org/wiki/Divergence_theorem#:~:text=space%5Bedit%5D-,We,-are%20going%20to%20prove)


<div>
$$\begin{aligned}
\int\U {U'\cap \partial \mathcal{H}^d}\left| u' \right|^p  \leq\int\U {\partial \mathcal{H}^d} \left| \widetilde{u}' \right|^p=\int\U {\mathcal{H}^d} \partial\U {d} \left| \widetilde{u}' \right|^p\leq\int\U {\mathcal{H}^d} p\left| \widetilde{u}' \right|^{p-1}\left| \partial\U {d} u \right|   \lesssim \left\lVert \widetilde{u}' \right\rVert\U {W^{1,p}(\mathcal{H}^d)}^p  .
\end{aligned}$$
</div>

Where in the second inequality we used the chain
rule and in the last Hölder's inequality. Since $\Phi^{-1}$ is $C^k$ and
by the continuity of the extension we obtain what we are looking for in


<div>
$$\begin{align}
\label{estimate local}
\left\lVert u \right\rVert\U {L^p(U \cap \partial \mathcal{H}^d)}\lesssim \left\lVert \widetilde{u}' \right\rVert\U {W^{1,p}(\mathcal{H}^d)}\lesssim \left\lVert u' \right\rVert\U {W^{1,p}(U'\cap \mathcal{H}^d)}\lesssim  \left\lVert u \right\rVert\U {W^{1,p}(U\cap \Omega)}
\end{align}$$
</div>

We had supposed $u$ smooth, now taking a finite
covering $\left\\{U\U i\right\\}\U {i=1}^n$ of $\partial  \Omega$ (this is
possible by compactness of $\partial  \Omega$) and taking a subordinate
partition of unity $\rho \U i$ we conclude from
(\ref{estimate local})  that

<div>
$$\begin{aligned}
\int\U {\partial \Omega} \left| u \right|^p  =\sum\U {i=1}^n \int\U { U\U i \cap \partial \Omega} \left| u \right|^p \lesssim \sum\U {i=1}^n \left\lVert u \right\rVert\U {W^{1,p}(U\U i \cap \Omega)}^p =\left\lVert u \right\rVert\U {W^{1,p}(U)}^p .
\end{aligned}$$
</div>

That is,

<div>
$$\begin{aligned}
\left\lVert T u \right\rVert\U {L^p( \partial \Omega)}\lesssim  \left\lVert u \right\rVert\U {W^{1,p}(U)} .
\end{aligned}$$
</div>

Using Theorem [6](#global) to extend $T$ continuously to
$W^{k,p}(\Omega)= \overline{\left.C\U c^\infty(\mathbb{R}^d)\right|\U {\Omega}}$
concludes the proof. ◻



**Definition 12**. We define the **trace** of $u \in W^{k,p}(\Omega)$
as $Tu$. We also use the notation

<div>
$$\begin{aligned}
\left.u\right|\U {\partial \Omega}:= Tu.
\end{aligned}$$
</div>




To get an estimate on the trace we paid $1$-degree of regularity. We can
do better and only pay ${1}/{p}$ degrees of regularity. This uses the
theory of [Sobolev--Slobodeckij
spaces](https://en.wikipedia.org/wiki/Trace_operator#For_p_=_1:~:text=%5Bedit%5D-,A%20more,-concrete%20representation%20of)
which we will not develop here. In the case $p=2$ we can use Hölder
spaces $H^s(\Omega)$ to get the improved result.


**Theorem 9**. For all real $s> 1 /2$ the trace operator is a
continuous operator

<div>
$$\begin{aligned}
T: H^s(\Omega) \to H^{s -\frac{1}{2}}(\Omega).
\end{aligned}$$
</div>





Proof. Straightening out the boundary and using the extension operator
as in the trace theorem [8](#trace), it is sufficient to work in the case where $u$ is
smooth and defined on $\mathcal{H}^{d}$. By Fourier inversion, if we
write $\xi=(\xi',\xi \U d)$

<div>
$$\begin{aligned}
\widehat{Tu}(\xi ')=\int\U {\mathbb{R}}\widehat{u}(\xi) \,\mathrm{d}\xi \U d .
\end{aligned}$$
</div>

So, by Cauchy Schwartz

<div>
$$\begin{align}
\label{f1}
\left| \widehat{Tu}(\xi ) \right|^2\leq \int\U {\mathbb{R}}\left| \widehat{u}(\xi) \right|^2\left\langle\xi \right\rangle^{2s} \,\mathrm{d}\xi \U d \int\U {\mathbb{R}}\left\langle\xi \right\rangle^{-2s} \,\mathrm{d}\xi \U d.
\end{align}$$
</div>

The change of variables
$\xi \U d \to \left\langle\xi '\right\rangle\xi \U d$ shows that


<div>
$$\begin{align}
\label{f2}
\int\U {\mathbb{R}}\left\langle\xi \right\rangle^{-2s} \,\mathrm{d}\xi \U d=\left\langle\xi' \right\rangle^{-2(s-\frac{1}{2})} \int\U {\mathbb{R}}\left\langle\xi \U d\right\rangle^{-2s}\,\mathrm{d}\xi \U d\lesssim  \left\langle\xi' \right\rangle^{-2(s-\frac{1}{2})}
\end{align}$$
</div>

Where in the inequality it was used that $s> 1 /2$.
We deduce from (\ref{f1})  and
(\ref{f2})  on taking norms
that

<div>
$$\begin{aligned}
\left\lVert u \right\rVert\U {H^{s-1 /2}(\mathbb{R}^{d-1})} \lesssim  \left\lVert u \right\rVert\U {H^s(\mathbb{R}^d)}.
\end{aligned}$$
</div>

Which concludes the proof. ◻


A particularly useful space of functions related to the trace operator
is the following


**Definition 13**. We define the space of functions with trace zero as


<div>
$$\begin{aligned}
W^{k,p}\U 0(U):=\overline{C\U c^\infty(U)}\subset W^{k,p}(U).
\end{aligned}$$
</div>

Where the closure is with respect to the topology on
$W^{k,p}(U)$.


 <a name="trace 0">
**Exercise 20** </a> . Show that for all $u \in W^{k,p}\U 0(\Omega)$


<div>
$$\begin{aligned}
\left.u\right|\U {\partial \Omega}=0.
\end{aligned}$$
</div>




<div class="exercise-container">
<button class="exercise-button" onclick="toggleExercise(this)">Hint</button>
<div class="exercise-text">
Use the continuity of the trace operator.
</div>
</div>

The converse to Exercise [20](#trace 0) holds but is far from trivial.


**Proposition 3**. Let $\Omega$ be a **bounded** open set with $C^1$
**boundary**. Then

<div>
$$\begin{aligned}
W^{k,p}\U 0(\Omega)=\left\{u \in W^{k,p}(U): Tu=0\right\} .
\end{aligned}$$
</div>




The proof is very technical, see [6](https://math24.files.wordpress.com/2013/02/partial-differential-equations-by-evans.pdf) page 274 for the
details.\
Being able to approximate functions in $W\U 0^{k,p}(U)$ by smooth
functions compactly supported **inside of** $U$ gives us many more
tools. For example, a function $u$ in $W^{k,p}\U 0(U)$ can be extended by
zero to obtain an element $\widetilde{u}$ in $W^{k,p}(\mathbb{R}^d)$
even for non-smooth unbounded domains.


**Exercise 21** (Extension trace 0). Let $U$ be an open set, and define


<div>
$$\begin{aligned}
\widetilde{u}:=\begin{cases}
u & \text{ on } U   \\
0 & \text{ on } U^c
\end{cases}.
\end{aligned}$$
</div>

Then

<div>
$$\begin{aligned}
E: W\U 0^{k,p}(U) \to W^{k,p}(\mathbb{R}^d); \quad  u \to \widetilde{u}
\end{aligned}$$
</div>

is a linear with $\left\lVert E \right\rVert=1$.


<div class="exercise-container">
<button class="exercise-button" onclick="toggleExercise(this)">Hint</button>
<div class="exercise-text">
It is immediate that
$\left\lVert \widetilde{u} \right\rVert\U {W^{k,p}(\mathbb{R}^d)}=\left\lVert \widetilde{u} \right\rVert\U {W^{k,p}(U)}$
for $u \in C\U c^\infty(U)$. As a result, we can extend $E$ by density to
the closure $C\U c^\infty(U)$ in $W^{k,p}(U)$. Which by definition is
$W^{k,p}\U 0(U)$.
</div>
</div>


**Observation 4**. The fact that we can extend functions in
$W^{k,p}\U 0(U)$ for arbitrary $U$ allows one to derive results that when
stated for the whole of $W^{k,p}(U)$ require $U$ to be smooth so that it
is possible to extend $U$.



**Exercise 22** (Integration by parts 1). Let $U$ be any open set and
consider $u \in  W^{1,p}\U 0(U), v \in W^{1,p'}(U)$ then

<div>
$$\begin{aligned}
\int\U {U} (\partial \U iu) v = -\int\U {U}u \partial \U i v  .
\end{aligned}$$
</div>




<div class="exercise-container">
<button class="exercise-button" onclick="toggleExercise(this)">Hint</button>
<div class="exercise-text">
Give yourself an epsilon of room and take limits.
</div>
</div>


**Exercise 23** (Integration by parts 2). Let $\Omega$ be a **bounded**
open set of $\mathbb{R}^d$ with $C^1$ **boundary** and consider
$u \in  W^{1,p}(\Omega), v \in W^{1,p'}(\Omega)$ then

<div>
$$\begin{aligned}
\int\U {\Omega} (\partial \U iu) v = -\int\U {\Omega}u \partial \U i v+ \int\U {\partial \Omega} u v \textbf{n}\U i  \,\mathrm{d}.
\end{aligned}$$
</div>

Where $\textbf{n}$ is the outward pointing unit
normal vector to $\partial \Omega$.


<div class="exercise-container">
<button class="exercise-button" onclick="toggleExercise(this)">Hint</button>
<div class="exercise-text">
Give yourself an epsilon of room, apply the [divergence
theorem](https://en.wikipedia.org/wiki/Divergence_theorem#:~:text=space%5Bedit%5D-,We,-are%20going%20to%20prove)
and take limits.
</div>
</div>

# Sobolev embeddings and inequalities

Sobolev inequalities are relationships that bound the norm of $u$ in
different function spaces depending on how differentiable and integrable
$u$ is. For example, such a relationship could look like


<div>
$$\begin{align}
\label{example}
\left\lVert u \right\rVert\U {W^{ l,p^\star  }(\Omega)}\leq \left\lVert u \right\rVert\U {W^{k,p}(\Omega)}.\end{align}$$
</div>


By considering the rescaling $u(\lambda x)$, performing a change of
variables, and taking $\lambda$ to $\infty$ we see that for such a
relationship to hold it is necessary that

<div>
$$\begin{align}
\label{conjugate}
l-     \frac{d}{p^\star }=k-\frac{d}{p}  .\end{align}$$
</div>

The case
$k=l+1$ gives rise to the following definition


**Definition 14**. The **Sobolev conjugate** of $1\leq p<d$ is $p^\star $
defined by

<div>
$$\begin{aligned}
\frac{1}{p^\star }= \frac{1}{p} -\frac{1}{d} .
\end{aligned}$$
</div>




Note that $p<p^\star $. The idea behind inequalities such as
(\ref{example})  is
to cash in some differentiability for some integrability. The main
results used to do this are based on the fundamental theorem of
calculus. First, we need the following lemma.

 <a name="whitney">
**Lemma 2** </a>  (Loomis-Whitney inequality). Let $d \geq 1$, let
$f\U 1, \ldots, f\U d \in L^p\left(\mathbb{R}^{d-1}\right)$ for some
$p \in (0,\infty]$, and define

<div>
$$\begin{aligned}
F\U d\left(x\U 1, \ldots, x\U d\right):=\prod\U {i=1}^d f\U i\left(x\U 1, \ldots, x\U {i-1}, x\U {i+1}, \ldots, x\U d\right).
\end{aligned}$$
</div>

Then,

<div>
$$\begin{align}
\label{loomis ineq}
\left\lVert F\U d \right\rVert\U {L^{p}/({d-1})}\leq\prod\U {i=1}^d\|f\U i\|\U {L^p\left(\mathbb{R}^{d-1}\right)} .
\end{align}$$
</div>





Proof. The case $d=2$ is immediate by Fubini. The general case follows
from induction on $d$ . We write $(x\U 1,\ldots x\U {d+1})=(x',x\U {d+1})$


<div>
$$\begin{align}
\label{induc}
& \left\lVert F\U {d+1} \right\rVert\U {L^{p /d}(\mathbb{R}^{d+1})}  =\left(\int\U {\mathbb{R}}\left(\int\U {\mathbb{R}^d} F\U d(x)^{\frac{p}{d}} f\U {d+1}(x')^{\frac{p}{d}} \,\mathrm{d}x'  \right)  \,\mathrm{d}x\U {d+1} \right)^{\frac{d}{p} }          \\
& \leq \left(\int\U {\mathbb{R}}         \left(\int\U {\mathbb{R}^d} F\U d(x)^{\frac{p}{d-1}} \,\mathrm{d}x'  \right)^{\frac{d-1}{d}}\,\mathrm{d}x\U {d+1} \right)^{\frac{d}{p} }\left\lVert f\U {d+1} \right\rVert\U {L^p(\mathbb{R}^d)}      \notag               \\
& \leq \left(\int\U {\mathbb{R}} \prod\U {i=1}^d\|f\U i(x\U {d+1})\|\U {L^p\left(\mathbb{R}^{d}\right)}^{\frac{p}{d}} \,\mathrm{d}x\U {d+1}\right)^{\frac{d}{p}}\left\lVert f\U {d+1} \right\rVert\U {L^p(\mathbb{R}^{d})}    \end{align}$$
</div>


Where in the first inequality we applied Cauchy-Schwartz with
$q= d /(d-1), q' =d$. Now applying the general version of
Hölder's

<div>
$$\begin{aligned}
\left\lVert g\U 1\cdots g\U n  \right\rVert\U {L^1} \leq \left\lVert g\U 1 \right\rVert\U {L^{p\U 1}}\cdots\left\lVert g\U 1 \right\rVert\U {L^{p\U n}}; \quad  \frac{1}{p\U 1}+\cdots \frac{1}{p\U n}=1\notag          .\end{aligned}$$
</div>



to
$g\U i:= \left\lVert f\U i(\cdot ) \right\rVert^{\frac{p}{d}}\U {L^p(\mathbb{R}^{d})} \in L^{d}(\mathbb{R})$
gives



<div>
$$\begin{aligned}
\int\U {\mathbb{R}}\prod\U {i=1}^{d}g\U i \leq \prod\U {i=1}^{d} \left\lVert g\U i \right\rVert\U {L^d(\mathbb{R})}    .
\end{aligned}$$
</div>

Substituting into
(\ref{induc})  concludes
the proof. ◻


Using the Loomis-Whitney inequality and the fundamental theory of
calculus gives us our first Sobolev inequality

 <a name="est1">
**Theorem 10** </a>  (Sobolev-Gagliardo-Niremberg). Given $1 \leq p<d$ it
holds that

<div>
$$\begin{aligned}
\left\lVert u \right\rVert\U {L^{p^\star }(\mathbb{R}^d)}\lesssim  \left\lVert \nabla u \right\rVert\U {L^p (\mathbb{R}^d)}.
\end{aligned}$$
</div>





Proof. By density (see Theorem [4](#approx rd)), it is enough to take
$u \in C\U c^\infty(\mathbb{R}^d)$. Applying the fundamental theorem of
calculus gives

<div>
$$\begin{aligned}
\left| u \right|^m=\int\U {-\infty}^\cdot \partial \U i \left| u \right|^m \,\mathrm{d}x\U i  \leq \int\U {\mathbb{R}}\left| u \right|^{m-1}\left| \partial \U i u \right| \,\mathrm{d}x\U i=: f\U i , \quad\forall i=1,\ldots,d.
\end{aligned}$$
</div>

Multiplying all these inequalities together gives


<div>
$$\begin{aligned}
\left| u \right|^{md} \leq \prod\U {i=1}^{d} f\U i   .
\end{aligned}$$
</div>

Applying the Loomis-Whitney inequality
(\ref{loomis ineq})  "with $p=1$" and Hölder's inequality shows


<div>
$$\begin{align}
\label{hard}
\left\lVert u \right\rVert\U {L^{ md /(d-1)}(\mathbb{R}^d)}^{md}\lesssim  \prod\U {i=1}^{d}  \left\lVert u^{m-1}\partial\U iu \right\rVert\U {L^1(\mathbb{R}^d)} \leq \left\lVert u \right\rVert\U {L^{(m-1)p'}(\mathbb{R}^d)}^{(m-1)d}\left\lVert \nabla u \right\rVert\U {L^{p}(\mathbb{R}^d \to  \mathbb{R}^d)}^d
\end{align}$$
</div>

It remains to choose $m$ such that

<div>
$$\begin{aligned}
\frac{md}{d-1}= (m-1)p' \implies m= \frac{(d-1)p^\star }{d} =\frac{dp -p}{d-p} \geq 1.
\end{aligned}$$
</div>

Substituting into
(\ref{hard})  gives


<div>
$$\begin{aligned}
\left\lVert u \right\rVert\U {L^{ p^\star }(\mathbb{R}^d)}^{m}\lesssim \left\lVert u \right\rVert\U {L^{p^\star }(\mathbb{R}^d)}^{m-1}\left\lVert \nabla u \right\rVert\U {L^{p}(\mathbb{R}^d \to  \mathbb{R}^d)} .
\end{aligned}$$
</div>

This concludes the proof. ◻


 <a name="est12">
**Exercise 24** </a> . Given $p<\frac{d}{k}$ define $p^{k\star }$ by
$\frac{1}{p^{k\star }}=\frac{1}{p}-\frac{k}{d}$. Then,

<div>
$$\begin{aligned}
\left\lVert u \right\rVert\U {L^{p^{k\star }}(\mathbb{R}^d)} \lesssim  \left\lVert \nabla^k u \right\rVert\U {L^p(\mathbb{R}^d)}    \end{aligned}$$
</div>




<div class="exercise-container">
<button class="exercise-button" onclick="toggleExercise(this)">Hint</button>
<div class="exercise-text">
Apply induction on $k$ using Theorem
[10](#est1).
</div>
</div>

The result can also be further
[generalized](https://en.wikipedia.org/wiki/Gagliardo%E2%80%93Nirenberg_interpolation_inequality)
An estimate for the endpoint $d=p$ can also be achieved

 <a name="estt2">
**Theorem 11** </a> . It holds that

<div>
$$\begin{aligned}
W^{1,d}(\mathbb{R}^d) \hookrightarrow L^q(\mathbb{R}^d) , \quad\forall  q \in [d,+\infty)
\end{aligned}$$
</div>





Proof. Setting $p=d$ in our estimate
(\ref{hard})  gives


<div>
$$\begin{aligned}
\left\lVert u \right\rVert\U {L^{ m d/(d-1)}(\mathbb{R}^d)}^{m}\lesssim  \left\lVert u \right\rVert\U {L^{(m-1)d /(d-1)}(\mathbb{R}^d)}^{m-1}\left\lVert \nabla u \right\rVert\U {L^{d}(\mathbb{R}^d \to  \mathbb{R}^d)} .
\end{aligned}$$
</div>

Applying Young's product inequality with
$p = \frac{m}{m-1}, p'= m$ and using that raising to a power is convex
gives

<div>
$$\begin{align}
\label{22}
\left\lVert u \right\rVert\U {L^{ m d/(d-1)}(\mathbb{R}^d)}\lesssim \left\lVert u \right\rVert\U {L^{(m-1)d/(d-1)}(\mathbb{R}^d)}+\left\lVert \nabla u \right\rVert\U {L^{d}(\mathbb{R}^d \to  \mathbb{R}^d)} , \quad\forall  m \geq 1.
\end{align}$$
</div>

Taking $m=d$ above gives

<div>
$$\begin{aligned}
\left\lVert u \right\rVert\U {L^{d^2 /(d-1)}(\mathbb{R}^d)} \lesssim  \left\lVert u \right\rVert\U {W^{1,d}(\mathbb{R}^d)}.
\end{aligned}$$
</div>

We also trivially have
$\left\lVert u \right\rVert\U {L^d(\mathbb{R}^d)} \leq\left\lVert u \right\rVert\U {W^{1,d}(\mathbb{R}^d)}$
so by
[interpolation](https://en.wikipedia.org/wiki/Riesz%E2%80%93Thorin_theorem#:~:text=%5Bedit%5D-,First,-we%20need%20the)
we can extend the inequality to

<div>
$$\begin{align}
\label{step 1}
\left\lVert u \right\rVert\U {L^{q}(\mathbb{R}^d)} \lesssim  \left\lVert u \right\rVert\U {W^{1,d}(\mathbb{R}^d)} , \quad\forall q \in \left[d,\frac{d^2}{d-1}\right].
\end{align}$$
</div>

We now iterate, taking $m=d+1$ gives


<div>
$$\begin{aligned}
\left\lVert u \right\rVert\U {L^{ (d+1)d/(d-1)}(\mathbb{R}^d)}\lesssim \left\lVert u \right\rVert\U {L^{d^2/(d-1)}(\mathbb{R}^d)}+\left\lVert \nabla u \right\rVert\U {L^{d}(\mathbb{R}^d \to  \mathbb{R}^d)}             \end{aligned}$$
</div>


Which combined with (\ref{step 1})  and interpolating gives

<div>
$$\begin{aligned}
\left\lVert u \right\rVert\U {L^{q}(\mathbb{R}^d)} \lesssim  \left\lVert u \right\rVert\U {W^{1,d}(\mathbb{R}^d)} , \quad\forall q \in \left[d,\frac{(d+1)d}{d-1}\right].
\end{aligned}$$
</div>

Iterating this process (taking $m=d+2,\ldots, m=d+k$
in (\ref{22}) ) shows that


<div>
$$\begin{aligned}
\left\lVert u \right\rVert\U {L^{q}(\mathbb{R}^d)} \lesssim  \left\lVert u \right\rVert\U {W^{1,d}(\mathbb{R}^d)} , \quad\forall q \in \left[d+k,\frac{(d+k)d}{d-1}\right].
\end{aligned}$$
</div>

From this, we conclude the result. ◻


 <a name="est22">
**Exercise 25** </a> . It holds that

<div>
$$\begin{aligned}
W^{k,\frac{d}{k}}(\mathbb{R}^d) \hookrightarrow L^q(\mathbb{R}^d) , \quad\forall  q \in [d /k,+\infty)
\end{aligned}$$
</div>




<div class="exercise-container">
<button class="exercise-button" onclick="toggleExercise(this)">Hint</button>
<div class="exercise-text">
Use induction on $k$ with Theorem
[11](#estt2).
</div>
</div>

Note that the constant in our above estimate blows up on iterating. As a
result, we do not expect

<div>
$$\begin{aligned}
W^{1,d}(\mathbb{R}^d) \hookrightarrow L^\infty(\mathbb{R}^d).\end{aligned}$$
</div>


This holds if and only if $d=1$. Otherwise, we require more
integrability. However, this extra integrability can be converted into
regularity in the style of [Sobolev
spaces](https://nowheredifferentiable.com/2023-01-29-PDE-1-Fourier/#:~:text=.%C2%A0%E2%97%BB-,As%20a%20corollary,-of%20this%2C%20we).
First, we recall the following definition


**Definition 15**. Let $U \subset \mathbb{R}^d$ be open and
$\gamma \in \mathbb{R}\U +$, we define the Holder space

<div>
$$\begin{aligned}
C^{k,\gamma }(\mathbb{R}^d):= \left\{u \in C^k(U): \left\lVert u \right\rVert\U {C^{k,\gamma }(U)}<\infty\right\} .
\end{aligned}$$
</div>

Where the Holder norm is defined as


<div>
$$\begin{aligned}
\left\lVert u \right\rVert\U {C^{0,\gamma }(U)} & := \sup\U {x \neq y \in \mathbb{R}^d} \frac{\left| u(x)-u(y) \right| }{\left| x-y \right|^\gamma  }          \\
\left\lVert u \right\rVert\U {C^{k,\gamma }(U)} & :=\left\lVert u \right\rVert\U {C^{k}(U)}+\sum\U {\left| \alpha \right|= k } \left\lVert D^\alpha u \right\rVert\U {C^{0,\gamma }(U)}   .
\end{aligned}$$
</div>




For $\gamma =1$ the $C^{k,\gamma }$ is the space of functions with
bounded derivatives up to order $k$ and whose $k$-th order derivatives
are Lipschitz continuous.

 <a name="est3">
**Theorem 12** </a>  (Morrey). Let $p>d$ and set $\gamma=1-\frac{d}{p}$.
Then, the following inclusion is continuous

<div>
$$\begin{aligned}
W^{1,p}(\mathbb{R}^d) \hookrightarrow C^{0,\gamma }(\mathbb{R}^d).
\end{aligned}$$
</div>




The proof is technical and can be found in [7](https://link.springer.com/book/10.1007/978-0-387-70914-7) page
282.

As is logical, as $p$ approaches $d$ from above the extra
differentiability we get goes to $0$. Furthermore, no matter how much
integrability we cash in, we can never get more differentiability than
we started with, so $\gamma \to 1$ as $p \to \infty$.

 <a name="est32">
**Exercise 26** </a>  (Sobolev regularity). Let $p>d$ and set
$\gamma=1-\frac{d}{p}$. Then, the following inclusion is continuous


<div>
$$\begin{aligned}
W^{k,p}(\mathbb{R}^d) \hookrightarrow C^{k,\gamma }(\mathbb{R}^d).
\end{aligned}$$
</div>




<div class="exercise-container">
<button class="exercise-button" onclick="toggleExercise(this)">Hint</button>
<div class="exercise-text">
This holds for the case $k=1$. We now proceed by induction.
Since $\nabla u \in W^{k-1,p}(\mathbb{R}^d \to  \mathbb{R}^d)$ by
hypothesis of induction we obtain

<div>
$$\begin{aligned}
\nabla u \in C^{k-1,\widetilde{\gamma }}(\mathbb{R}^d \to \mathbb{R}^d); \quad \widetilde{\gamma }:= k-1 -\frac{d}{p} .
\end{aligned}$$
</div>

In consequence,

<div>
$$\begin{aligned}
u \in C^{k-1+1,\widetilde{\gamma}+1}(\mathbb{R}^d )=C^{k,\gamma}(\mathbb{R}^d ) .
\end{aligned}$$
</div>


</div>
</div>

Combining the three results gives

 <a name="rellich">
**Theorem 13** </a>  (Rellich-Kondrachov). Let $\Omega$ either be
$\mathbb{R}^d$ or **bounded** with $C^k$ boundary, then following
inclusions are continuous

<div>
$$\begin{aligned}
& W^{k,p}(\Omega) \hookrightarrow L^q(\Omega) ,           \quad\forall q \in [1,p^{k\star })    & \text{ and }     p<\frac{d}{k}  \\
& W^{k,p}(\Omega) \hookrightarrow L^q(\Omega) ,           \quad\forall q \in [p,\infty) & \text{ and }   p=\frac{d}{k}  \\
& W^{k,p}(\Omega) \hookrightarrow C^{k,\gamma }(\overline{\Omega}) \hookrightarrow C^{k}(\overline{\Omega}) ,  \quad                         & \text{ and }  p>\frac{d}{k}    \end{aligned}$$
</div>


Where $p^{k\star }$ is defined by the relation
$\frac{1}{p^{k\star }}=\frac{1}{p}-\frac{k}{d}$ and $\gamma =1 -\frac{p}{d}$.
Furthermore, the first, second, fourth, and third composed with fourth
inclusions are
[compact](https://en.wikipedia.org/wiki/Compact_embedding).



Proof. The fact that the above inclusions are continuous follows by
our three Sobolev inequalities in Exercises
[24](#est12),[25](#est22),[26](#est32)
together with the extension theorem [7](#extension).

The compactness of the embeddings requires reduce to showing that the
unit ball in each of the embedded spaces is
[equicontinuous](https://en.wikipedia.org/wiki/Equicontinuity).

1.  For the first inclusion we will use
[Fréchet--Kolmogorov's](https://en.wikipedia.org/wiki/Fr%C3%A9chet%E2%80%93Kolmogorov_theorem)
theorem. First we note that we can suppose $q>p$ as
$L^q(\Omega) \hookrightarrow L^p(\Omega)$. Let $B\U 1$ be the unit
ball in $W^{k,p}(\Omega)$. By continuity of the inclusion $B\U 1$ is
bounded in $L^q(\Omega)$ and it only remains to show that $B\U 1$ is
equicontinuous. We have that

<div>
$$\begin{aligned}
\left\lVert \tau\U h u-u \right\rVert\U {L^p(\Omega)}\leq \left\lVert \nabla u \right\rVert\U {L^p(\Omega)}\left| h \right| , \quad\forall u \in W^{1,p}(\Omega) .
\end{aligned}$$
</div>

Where the above is known to be true for
smooth functions by the fundamental theorem of calculus and extends
by density to $W^{k,p}(\Omega)$ (we recall translation is continuous
on $L^p$ for $p<\infty$). The above also holds for $p^{k\star }$ and
since $p<q<p^{k\star }$ we can write

<div>
$$\begin{aligned}
\frac{1}{q}=\frac{\alpha}{p}+\frac{1-\alpha}{p^{k\star }}   .\end{aligned}$$
</div>


By
[interpolation](https://en.wikipedia.org/wiki/Riesz%E2%80%93Thorin_theorem#:~:text=the%20sumset%20formulation.-,Riesz%E2%80%93Thorin,-interpolation%20theorem%C2%A0%E2%80%94%C2%A0)
we obtain that

<div>
$$\begin{aligned}
\left\lVert \tau\U h u-u \right\rVert\U {L^q(\Omega)}\leq \left\lVert \nabla u \right\rVert\U {L^p(\Omega)}^\alpha\left\lVert \nabla u \right\rVert\U {L^{p^{k\star }}(\Omega)}^{1-\alpha}\left| h \right| , \quad\forall u \in W^{1,p}(\Omega) .
\end{aligned}$$
</div>

This shows equicontinuity and concludes the
first case.

2.  The compactness of the second inclusion is proved identically.

3.  For the compactness of the last inclusion we use [Arzelà--Ascoli
theorem](https://en.wikipedia.org/wiki/Arzel%C3%A0%E2%80%93Ascoli_theorem#:~:text=%2C%20%C2%A7IV.6.7)
on a "derivative by derivative basis". By definition of Hölder norm,


<div>
$$\begin{aligned}
\left| D^\alpha u(x)- D^\alpha u(y) \right|&\lesssim  \left\lVert u \right\rVert\U {C^{k}(\mathbb{R}^d)}\left| x-y \right| , &&\quad\forall \left| \alpha \right|<k\\
\left| D^\alpha u(x)- D^\alpha u(y) \right|&\lesssim  \left\lVert u \right\rVert\U {C^{k,\gamma }(\mathbb{R}^d)}\left| x-y \right|^\gamma  , &&\quad\forall \left| \alpha \right|=k.
\end{aligned}$$
</div>

As a result, for each
$\left| \alpha \right|\leq k$ the family

<div>
$$\begin{aligned}
A\U \alpha:=\left\{D^\alpha u: u \in B\U 1 \subset C^{k,\gamma }(\overline{\Omega})\right\},\end{aligned}$$
</div>


is equicontinuous. So by Arzelà--Ascoli we may extract a sequence
$u\U {n}$ such that $D^\alpha u\U n$ converges uniformly to some
$u^{(\alpha)}$. By the fundamental theorem of calculus we conclude
that $u^{(\alpha)}=D^\alpha u^{(0)}$ and as a result
$u\U n \to u \in C^k(\overline{\Omega})$. That is, the unit ball
$B\U 1 \subset C^{k,\gamma }$ is sequentially compact and thus compact
when embedded in $C^k(\overline{\Omega})$. This proves this point.

4.  The composition of the inclusions on the last line is compact as the
composition of a compact and a continuous operator is compact. This
concludes the proof.

◻


The main utility of all these compact embeddings is that given a
sequence $u\U n$ whose derivatives are bounded in certain $L^p$ norms we
can extract convergent subsequences in appropriate spaces. We end this
post (modulo appendices) with one of the most useful inequalities which
we will make use of in future posts


**Theorem 14** (Poincaré inequality). Let $u \in W^{1,p}\U 0(U)$ where
$U$ is bounded in one direction. Then

<div>
$$\begin{aligned}
\left\lVert u \right\rVert\U {W^{1,p}(U)}\leq C\left\lVert \nabla u \right\rVert\U {W^{1,p}(U \to \mathbb{R}^d)}.
\end{aligned}$$
</div>





Proof. By density (which holds by definition of $W^{k,p}\U 0(U)$) of it
is sufficient to reason for $u \in C\U c^\infty(U)$ and pass to the limit.
By relabeling we may suppose $U$ is bounded along the $x\U d$ axis. That
is, for some finite $a<b$

<div>
$$\begin{aligned}
U \subset \mathbb{R}^{d-1} \times [a,b].
\end{aligned}$$
</div>

The idea is to use the fundamental theorem of
calculus together with the compact support of $u$. This allows us to
rewrite

<div>
$$\begin{aligned}
\left| u(x) \right|= \left| \int\U {a}^{x\U d} \partial\U d u(x',t) \,\mathrm{d}t \right| \leq \left(\int\U {\mathbb{R}}\left| \partial \U d u(x',t) \right|^p \,\mathrm{d}t\right)^\frac{1}{p}(x\U d-a)^{\frac{1}{p'}}  .
\end{aligned}$$
</div>

Taking $L^p(\mathbb{R}^d)$ norms above gives


<div>
$$\begin{aligned}
\left\lVert u \right\rVert\U {L^p(\mathbb{R}^d)}\leq \left\lVert \partial \U du \right\rVert\U {L^p(\mathbb{R}^d)}\frac{p'}{p+p'}(b-a)^{\frac{p+p'}{p'}} \lesssim  \left\lVert \nabla u \right\rVert\U {L^p(\mathbb{R}^d \to \mathbb{R}^d)} .
\end{aligned}$$
</div>

This concludes the proof. ◻


# Convolutions and regularization

The convolution of two functions $f,g$ can be thought of as "blurring"
$f$ by averaging it against $g$. In the case where $g$ is smooth, this
blurring has the effect of smoothing out any sharp edges and
irregularities in $f$. This allows us to approximate irregular functions
by smooth ones and serves as an important technical tool in our
analysis.


**Definition 16** (Convolution of functions). Given $f$ and $g$ we
define the convolution of $f,g$ to be the function $f \star g$


<div>
$$\begin{align}
\label{convo}
f \star g := \int f(y)g(x-y) \,\mathrm{d}y
\end{align}$$
</div>




The definition given by (\ref{convo})  is purposefully vague. We still need to specify what
spaces $f,g$ belong to so that $f\star g$ is a well-defined element (of a
further unspecified space). This can be done as follows.

 <a name="Young">
**Proposition 4** </a>  (Young's convolution inequality). Consider the
definition in (\ref{convo})  and let $p,q,r \in  [1, \infty]$. Then it holds that

1.  If $f \in L^1(\mathbb{R}^d)$ and $g \in L^p(\mathbb{R}^d)$ then
$f\star g \in L^p(\mathbb{R}^d)$ with

<div>
$$\begin{aligned}
\left\lVert f\star g \right\rVert\U {L^p(\mathbb{R}^d)}\leq \left\lVert f \right\rVert\U {L^1(\mathbb{R}^d)}\left\lVert g \right\rVert\U {L^p(\mathbb{R}^d)}.
\end{aligned}$$
</div>



2.  Suppose that

<div>
$$\begin{aligned}
\frac{1}{p}+\frac{1}{q}=1+\frac{1}{r}; \quad f \in L^p(\mathbb{R}^d); \quad g \in L^q(\mathbb{R}^d)    .
\end{aligned}$$
</div>

Then $f\star g \in L^r(\mathbb{R}^d)$ with


<div>
$$\begin{aligned}
\left\lVert f\star g \right\rVert\U {L^r(\mathbb{R}^d)}\leq \left\lVert f \right\rVert\U {L^p(\mathbb{R}^d)}\left\lVert g \right\rVert\U {L^q(\mathbb{R}^d)}.
\end{aligned}$$
</div>



In any of the above cases $f\star g=g\star f$.



Proof. The first point follows from the triangle inequality for the
Bochner integral (in this context this is also called Minkowski's
integral inequality) as

<div>
$$\begin{aligned}
\left\lVert \int\U {\mathbb{R}^d}f(y)g(\cdot -y) \,\mathrm{d}y \right\rVert\U {L^p(\mathbb{R}^d)}\leq\int\U {\mathbb{R}^d}\left\lVert f(y)g(\cdot -y) \,\mathrm{d}y \right\rVert\U {L^p(\mathbb{R}^d)}= \left\lVert f \right\rVert\U {L^1(\mathbb{R}^d)} \left\lVert g \right\rVert\U {L^p(\mathbb{R}^d)}.
\end{aligned}$$
</div>

To see the second point fix $f$ and define the
linear operator $T\U fg:= f\star g$. Then, for $g \in  L^1(\mathbb{R}^d)$ and
$g \in  L^{p'}(\mathbb{R}^d)$ respectively

<div>
$$\begin{aligned}
\left\lVert T\U f g \right\rVert\U {L^p(\mathbb{R}^d)} \leq \left\lVert f \right\rVert\U {L^p(\mathbb{R}^d)} \left\lVert g \right\rVert\U {L^1(\mathbb{R}^d)}; \quad    \left\lVert T\U f g \right\rVert\U {L^\infty(\mathbb{R}^d)} \leq \left\lVert f \right\rVert\U {L^p(\mathbb{R}^d)} \left\lVert g \right\rVert\U {L^{p'}(\mathbb{R}^d)};  .
\end{aligned}$$
</div>

Where the first inequality is point one and the
second follows from Cauchy Schwartz. Now applying [Riesz-Thorin's
interpolation
theorem]( https://en.wikipedia.org/wiki/Riesz%E2%80%93Thorin_theorem#:~:text=the%20sumset%20formulation.-,Riesz%E2%80%93Thorin,-interpolation%20theorem%C2%A0%E2%80%94%C2%A0)
concludes the proof. ◻


The definition of convolution can be extended to even more settings, for
example, suppose that $g$ is the density of some finite (possibly
signed) measure $\mu$ and $f$ is bounded, then

<div>
$$\begin{aligned}
f\star \mu(x):= f\star g(x)= \int\U {\mathbb{R}^d}f(x-y) g(y)\,\mathrm{d}y = \int\U {\mathbb{R}^d} f(x-y)\,\mathrm{d}\mu (y) .\end{aligned}$$
</div>




**Definition 17** (Convolution of function with measure). Let $\mu$ be
a finite signed Borel measure on $\mathbb{R}^d$ and
$f \in L^p(\mathbb{R}^d)$ then we define the convolution


<div>
$$\begin{aligned}
f\star \mu (x) :=\int\U {\mathbb{R}^d} f(x-y)\,\mathrm{d}\mu (y) \in L^p(\mathbb{R}^d).
\end{aligned}$$
</div>




Note that, once more by the triangle inequality, the convolution is
well-defined with

<div>
$$\begin{aligned}
\left\lVert f\star  \mu  \right\rVert\U {L^p(\mathbb{R}^d)} \leq \left\lVert f \right\rVert\U {L^p(\mathbb{R}^d)} \left\lVert \mu  \right\rVert\U {TV} .\end{aligned}$$
</div>


Now, if we consider $f,g$ to be the densities of some finite (signed)
measures $\mu,\nu$ then we obtain that for bounded $h$

<div>
$$\begin{align}
\label{push}
(h, \mu \star \nu) & := \int\U {\mathbb{R}^d} h(x) f\star g(x) \,\mathrm{d}x = \int\U {\mathbb{R}^d}\int\U {\mathbb{R}^d}  h(x+y) f(x)  g(y)\,\mathrm{d}x \,\mathrm{d}y\\
& = \int\U {\mathbb{R}^d \times\mathbb{R}^d} f(x+y) \,\mathrm{d}(\mu \otimes \nu)(x,y)\notag .\end{align}$$
</div>


That is, the convolution of $\mu$ with $\nu$ is the
[pushforward](https://en.wikipedia.org/wiki/Pushforward_measure) of the
product measure $\mu \otimes \nu$ with the sum $S(x,y)$.


**Definition 18** (Convolution of measures). Let $\mu ,\nu$ be two
finite signed measures on $\mathcal{B}(\mathbb{R}^d)$. Then the
convolution of $\mu \star \nu$ is the pushforward

<div>
$$\begin{aligned}
\mu \star \nu := S\# (\mu \otimes\nu).
\end{aligned}$$
</div>




The language of random variables can give some good motivation for this


**Example 3**. Let $X,Y$ be random variables with law $\mu ,\nu$ then
$X+Y$ has law $\mu \star \nu$. Furthermore, if $X, Y$ are independent and
$\mu,\nu$ are absolutely continuous with densities $f,g$ then $X+Y$ is
absolutely continuous with density $f\star g$.



Proof. The first part is by definition of pushforward. To show that
$\mu \star \nu$ has density $f\star g$ it suffices to read the reasoning in
equation (\ref{push})
backward. ◻


Through the random variable interpretation, we also see that if
$\mu,\nu$ have all their mass in $A, B$ then their convolution must have
all its mass in $A+B$. That is,

 <a name="Support">
**Lemma 3** </a> . Let $f,g,\mu,\nu$ be such that the convolution is
well-defined. Then

<div>
$$\begin{aligned}
\mathbf{supp}(f\star g)=\mathbf{supp}(f)+\mathbf{supp}(g); \quad \mathbf{supp}(\mu\star \nu )=\mathbf{supp}(\mu )+\mathbf{supp}(\nu).
\end{aligned}$$
</div>





Proof. This follows directly from the definition of convolution. ◻


One technical point is that to define the convolution of two objects it
is required that they be defined globally. For example if
$U \subsetneq \mathbb{R}^d$, we can't convolve $f \in L^p(\mathbb{R}^d)$
with $g \in L\U 1(U)$ as the integral

<div>
$$\begin{aligned}
\int\U {\mathbb{R}^d}f(y)g(x-y) \,\mathrm{d}y\end{aligned}$$
</div>

requires
we evaluate $f$ on all of $\mathbb{R}^d$. One workaround is, if
$\phi\in L^1(\mathbb{R}^d)$ with
$\mathbf{supp}(\phi)\subset  \overline{B(0,\epsilon ) }$ we can extend
$f$ to be equal to some $g \in L^p(\mathbb{R})$ outside of $U$


<div>
$$\begin{aligned}
\tilde{f}(x)=\begin{cases}
f(x) \quad & x \in U     \\
g(x) \quad & x \not\in U
\end{cases}.\end{aligned}$$
</div>

Then, the convolution
$\tilde{f}\star g$ is well defined and equal to

<div>
$$\begin{aligned}
\tilde{f}\star \phi(x) = \int\U {B(x,\epsilon )\cap U} f(y)\phi(x-y) \,\mathrm{d}y+\int\U {B(x,\epsilon )\cap U^c} g(y)\phi(x-y) \,\mathrm{d}y .\end{aligned}$$
</div>


As we can see, the convolution in general depends on how we extend $f$
outside of $U$. However, it is independent of the extension for $x$ in


<div>
$$\begin{aligned}
U\U \epsilon :=\left\{x \in  U : d(x,\partial U)< \epsilon \right\}.\end{aligned}$$
</div>


With

<div>
$$\begin{aligned}
\tilde{f}\star \phi(x) = \int\U {B(x,\epsilon )} f(y)\phi(x-y) \,\mathrm{d}y , \quad\forall x \in  U\U \epsilon   .\end{aligned}$$
</div>


For this reason, we will employ the following notation.

 <a name="Convolution support">
**Definition 19** </a> . Given $f \in L^p(U)$ and $\phi\in L^1(\mathbb{R}^d)$
with $\mathbf{supp}(\phi)\subset  \overline{B(0,\epsilon ) }$ we define
$f\star \phi \in L^p(U\U \epsilon )$ as

<div>
$$\begin{aligned}
f\star \phi(x):= \int\U {B(x,\epsilon )}f(y)\phi(x-y) \,\mathrm{d}y .
\end{aligned}$$
</div>




Convolution of distributions with test functions can also be considered.
A similar reason to previously leads us to the following definition


**Definition 20**. Let $T \in \mathcal{D}'(\mathbb{R}^d)$ and
$\varphi \in C\U c^\infty(\mathbb{R}^d)$. Then we define the convolution
$T\star \varphi \in \mathcal{D}^\star (\mathbb{R}^d)$ by

<div>
$$\begin{aligned}
T\star \varphi(\phi):=T(\widetilde{\varphi}\star \phi) \quad \text{ where } \widetilde{\varphi}(x):=\varphi(-x) .\end{aligned}$$
</div>




In the above we can also swap all occurrences of
$C\U c^\infty(\mathbb{R}^d)$ and $\mathcal{D}'(\mathbb{R}^d)$ by
$\mathcal{S}(\mathbb{R}^d)$ and $\mathcal{S}'(\mathbb{R}^d)$
respectively. An interesting fact is that the convolution of a
distribution with a function is itself a function.


**Proposition 5**. Convolution of distribution and test function is
smooth:

1.  Let
$\varphi \in \mathcal{D}(\mathbb{R}^d), w \in \mathcal{D}'(\mathbb{R}^d)$
then
$\omega \star  \varphi \in  C^\infty \U {\mathrm{loc}}(\mathbb{R}^d)$.

2.  Let
$\varphi \in \mathcal{S}(\mathbb{R}^d), w \in \mathcal{S}'(\mathbb{R}^d)$
then
$\omega \star  \varphi \in  C^\infty \U {\mathrm{loc}}(\mathbb{R}^d)$.


The previous definitions all go through word by word in the case where
we substitute the domain from Euclidean space $\mathbb{R}^d$ to a [LCA
group with Haar
measure](https://nowheredifferentiable.com/2023-01-29-PDE-1-Fourier/#:~:text=Since-,every,-locally%20compact%20Hausdorff)
$\mu$. For example

<div>
$$\begin{aligned}
f\star g(x):= \int\U {G}f(y)g(x-y) \,\mathrm{d}\mu (y).\end{aligned}$$
</div>

A
typical case is when $G=\mathbb{T}^d$ with the Lebesgue measure or
$G=\mathbb{Z}^d$ with the counting measure. These respectively give


<div>
$$\begin{aligned}
f\star g(x)=\int\U {\mathbb{T}^d}f(y)g(x-y) \,\mathrm{d}y; \quad      f\star g(k):= \sum\U {j\in \mathbb{Z}^d} f(j)g(k-j)  .\end{aligned}$$
</div>


The same results are also obtained. In fact, save the commutation
$f\star g=g\star f$, the above results hold even if $G$ is not Abelian. In this
case, one considers the [left or right Haar
measure](https://en.wikipedia.org/wiki/Haar_measure#:~:text=%5Bedit%5D-,There,-is%2C%20up).
See for example [8](
https://www.gbv.de/dms/goettingen/377412414.pdf) 444R.

# <a name="smooth section">  Smoothing in $L^p$  </a>

In this section, we examine how convolution can be used to approximate
functions by smoother ones. This is of great practical use as it allows
us to

1.  Consider an appropriate space of functions for our problem, smooth
or otherwise.

2.  Perform formal manipulations using the standard rules of calculus as
if all functions in this space were smooth and compactly supported
until we obtain a desired result.

3.  Pass to the limit to recover the expression for the whole class of
functions.

A crucial tool in this program is the following:

 <a name="app def">
**Definition 21** </a> . We say that a family of functions
$\\{\phi\U n\\}\U {n= 1}^\infty \subset L^1(\mathbb{R}^d)$ is an
**approximation to unity** if

-   Norm 1: $\left\lVert \phi\U n \right\rVert\U {L^1(\mathbb{R}^d)}=1$.

-   Decreasing support: $\mathbf{supp}(\phi\U n) \subset B(0, 1 /n)$.

If $\phi\U n \in C\U c^\infty(\mathbb{R}^d)$ we say that $\phi\U n$ are
smooth.



**Observation 5**. The above definition is frequently also given
letting the index set range over $\epsilon \in \mathbb{R}\U +$ and taking
$\mathbf{supp}(\phi\U \epsilon ) \subset B(0,\epsilon )$. This is
equivalent and simply leads to taking $\epsilon \to 0$ instead of
$n \to \infty$.


The first question is whether a smooth approximation to the identity
exists. In the following example, we answer this in the affirmative.


**Example 4**. Let $\varphi \in C\U c^\infty(\mathbb{R}^d)$ then


<div>
$$\begin{aligned}
\phi\U n:= \frac{n^d }{\left\lVert \varphi \right\rVert\U {L^1(\mathbb{R}^d)}}\varphi(nx)\end{aligned}$$
</div>


is a smooth approximation of the identity. Additionally,


<div>
$$\begin{align}
\label{bump example}
\varphi(x):=  \exp({\frac{1}{\left| x \right|^2-1}}) 1\U {B(0,1)} \in C\U c^\infty(\mathbb{R}^d)
\end{align}$$
</div>




By Proposition [4](#Young)
$(L^1(\mathbb{R}^d),\star )$ is a [Banach
algebra](https://en.wikipedia.org/wiki/Banach_algebra). However, it is a
non-unital one. That is there does not exist an element $e$ such that


<div>
$$\begin{aligned}
f\star e=f , \quad\forall f \in L^1(\mathbb{R}^d).\end{aligned}$$
</div>


However, we will soon see that in a limiting sense, an identity for the
convolution exists. First, we need the following lemma.

 <a name="Uryshon">
**Lemma 4** </a> . The space $C\U c(\mathbb{R}^d)$ is dense in
$L^p(\mathbb{R}^d)$ for all $p \in [1,\infty)$.



Proof. Consider $f \in  L^p(\mathbb{R}^d)$. If $f =1\U A$ for some
measurable set $A$ with finite measure then, by the outer and inner
regularity of the Lebesgue measure we may take $U, K$ open and compact
respectively with $U \subset A \subset K$ and

<div>
$$\begin{aligned}
\lambda  (K)-\lambda  (A) <\epsilon .
\end{aligned}$$
</div>

Where we wrote $\mu$ for the Lebesgue measure on
$\mathbb{R}^d$. By [Urysohn's
lemma](https://en.wikipedia.org/wiki/Urysohn%27s_lemma#:~:text=for%20any%20two-,non%2Dempty,-closed%20disjoint%20subsets)
there exists a continuous function $\varphi \in C\U c(U)$ such that
$\varphi \leq 1$ and $\varphi$ is $1$ on $K$. Then,

<div>
$$\begin{aligned}
\left\lVert f- \varphi \right\rVert\U {L^p(\mathbb{R}^d)} \leq \epsilon .
\end{aligned}$$
</div>

Since the space of simple functions is dense in
$L^p(\mathbb{R}^d)$ this concludes the proof. ◻


The name "approximation of unity" in Definition
[21](#app def) is justified by
the following proposition.

 <a name="app pn">
**Proposition 6** </a> . Let $f \in L^p(\mathbb{R}^d)$ where
$p \in [1,\infty)$ and consider $g \in C\U c(\mathbb{R}^d)$ and an
approximation to unity $\phi\U n$. Then it holds that

<div>
$$\begin{aligned}
\lim\U {n \to \infty}g\star \phi\U n=g \in  C\U c(\mathbb{R}^d);\quad \lim\U {n \to \infty}f\star \phi\U n=f \in  L^p(\mathbb{R}^d).
\end{aligned}$$
</div>





Proof. Consider $\epsilon >0$. Using that $\phi\U n$ has mass $1$ and is
supported on $B(0,1/n)$.

<div>
$$\begin{aligned}
g\star \phi\U n(x)-g(x) & = \int\U {B(0, \frac{1}{n})}(g(x-y)-g(x)) \phi\U n(y) \,\mathrm{d}y
.
\end{aligned}$$
</div>

Now taking norms and $n$ large enough gives


<div>
$$\begin{align}
\label{nm}
\left\lVert g\star \phi\U n-g \right\rVert\U {L^\infty(\mathbb{R}^d)} \leq \int\U {B(0, \frac{1}{n})} \left\lVert g(\cdot -y) -g \right\rVert\U {L^\infty(\mathbb{R}^d)} \phi\U n(y) \,\mathrm{d}y\leq \epsilon   .
\end{align}$$
</div>

Where in the last inequality we used that $g$ is
uniformly continuous and $\phi\U n$ has mass $1$. Since $\epsilon >0$ was
any, this shows the first part of the proposition.

We now prove the second part. By Lemma
[4](#Uryshon) we can choose
$g$ such that

<div>
$$\begin{aligned}
\left\lVert g-f \right\rVert\U {L^p(\mathbb{R}^d)}<\epsilon .
\end{aligned}$$
</div>



Now, since $K\U n:=\mathbf{supp}(g\star  \phi\U n) \subset K + B(0, 1 /n)$, whose
measure is bounded by some $M>0$, the inequality in
(\ref{nm})  shows that


<div>
$$\begin{aligned}
\left\lVert g\star \phi\U n-g \right\rVert\U {L^p(\mathbb{R}^d)}^p \leq \int\U {K\U n} \epsilon^p   \,\mathrm{d}y\leq M\epsilon^p  .
\end{aligned}$$
</div>

Now using the triangle inequality and Young's
convolution inequality [4](#Young) gives

<div>
$$\begin{aligned}
\left\lVert f\star \phi\U n-f \right\rVert\U {L^p(\mathbb{R}^d)} & \leq\left\lVert (f-g)\star \phi\U n \right\rVert\U {L^p(\mathbb{R}^d)}+\left\lVert g\star \phi\U n-g \right\rVert\U {L^p(\mathbb{R}^d)} \\
& +\left\lVert g-f \right\rVert\U {L^p(\mathbb{R}^d)}\leq \epsilon + M^{\frac{1}{p}}\epsilon +\epsilon .
\end{aligned}$$
</div>

This shows the second part and concludes the
proof. ◻


The question is why would we want to approximate a function by its
convolutions with some smooth functions the answer is given in the
following two results.

 <a name="smooth">
**Proposition 7** </a>  (Smoothing effect). Let
$f \in L^1\U {\text{loc}}(\mathbb{R}^d)$ and
$\phi \in C\U c^\infty(\mathbb{R}^d)$. Then
$f\star \phi \in C^\infty(\mathbb{R}^d)$ with

<div>
$$\begin{aligned}
D^\alpha(f \star \phi)=f\star D^\alpha \phi , \quad\forall \alpha \in \mathbb{N}^d.
\end{aligned}$$
</div>

Furthermore, if $f$ is compactly supported then
$f\star \phi \in  C\U c^\infty(\mathbb{R}^d)$.



Proof. By induction, it suffices to consider the case
$D^\alpha = \partial \U i$ for some $1 \leq i \leq d$. This case can be
proved by a [differentiation under the integral
sign](https://nowheredifferentiable.com/2023-01-29-PDE-1-Fourier/#:~:text=Proposition%202%20(-,Differentiation,-under%20the%20integral)
as, given $\left| x \right|\leq M$

<div>
$$\begin{aligned}
\partial \U {x\U i} f(y)\phi(x-y) \leq f(y)\left\lVert \phi \right\rVert\U {C^\infty(K)} 1\U {K+B(0,M)}(y) \in L^1(\mathbb{R}^d)
\end{aligned}$$
</div>

Where $K$ is the support of $\varphi$. ◻


 <a name="local smoothing">
**Observation 6** </a>  (Local smoothing). The smoothing effect also holds
when $f$ is only defined on some open set $U$. Then, with the notation
of Definition [19](#Convolution support), $f\star \phi \in C^\infty(U\U \epsilon )$
with an identical proof showing

<div>
$$\begin{aligned}
D^\alpha(f \star \phi)=f\star D^\alpha \phi \text{ on } U\U \epsilon .
\end{aligned}$$
</div>




 <a name="density thm">
**Theorem 15** </a> . It holds that

<div>
$$\begin{aligned}
\overline{C\U c^\infty(\mathbb{R}^d)}= L^p(\mathbb{R}^d); \quad \overline{C\U c^\infty(\mathbb{R}^d)} = C\U c(\mathbb{R}^d).
\end{aligned}$$
</div>

Where the closures are respectively in the
$L^p(\mathbb{R}^d)$ and the uniform topology $($given by
$\left\lVert \cdot  \right\rVert\U {\infty})$.



Proof. This follows immediately from Proposition
[6](#app pn) and Proposition
[7](#smooth). ◻



**Exercise 27**. Let $U$ be an open subset of $\mathbb{R}^d$, show that


<div>
$$\begin{aligned}
\overline{C\U c^\infty(U)}= L^p(U); \quad \overline{C\U c^\infty(U)} = C\U c(U).
\end{aligned}$$
</div>




<div class="exercise-container">
<button class="exercise-button" onclick="toggleExercise(this)">Hint</button>
<div class="exercise-text">
Let $f$ be the non-smooth function to approximate, multiply
it first by a mollifier $\eta\U n \in C\U c^\infty(U)$ equal to $1$ in
$V\U n\subset U$ (see Example [5](#bump example2)). Convolve to get

<div>
$$\begin{aligned}
\varphi\U n:=(f \eta\U n )\star \rho \U n.\end{aligned}$$
</div>

Show as in Theorem
[15](#density thm) that
$\varphi\U n$ converges appropriately.
</div>
</div>

The above can be generalized to non-Euclidean spaces


**Theorem 16**. Let $(X,\mu )$ be a measure space such that $X$ is
locally convex and Hausdorff and $\mu$ is inner and outer regular. Then


<div>
$$\begin{aligned}
\overline{C\U c(X)} =L^p(X).
\end{aligned}$$
</div>

Suppose additionally that $X$ is a group, that $\mu$
is the left or right Haar measure, and that there exists an
approximation to unity $\phi\U n$ on $X$. Then

<div>
$$\begin{aligned}
\overline{C\U c^\infty(X)} =L^p(X);\quad \overline{C\U c^\infty(X)} =C\U c(X).
\end{aligned}$$
</div>





Proof. The first part can be proved by the same method as in Lemma
[4](#Uryshon) (note that
Uryshon's lemma [still
holds](https://planetmath.org/ApplicationsOfUrysohnsLemmaToLocallyCompactHausdorffSpaces)
for LCH spaces). The second part follows by copying the proof of
Propositions [6](#app pn) and
[7](#smooth). ◻


The assumption of the existence of an approximation of unity is perhaps
the most delicate, but it can be applied for example in the following
case.

 <a name="Stone">
**Corollary 1** </a> . It holds that

<div>
$$\begin{aligned}
\overline{C^\infty(\mathbb{T}^d)}= L^p(\mathbb{T}^d); \quad \overline{C^\infty(\mathbb{T}^d)} = C(\mathbb{T}^d).
\end{aligned}$$
</div>




Note that the second part of Corollary [1](#Stone) also follows from the [Stone-Weierstrass
theorem](https://en.wikipedia.org/wiki/Stone%E2%80%93Weierstrass_theorem).
Similar results hold in the space of distributions.


**Proposition 8**. Let $T\in \mathcal{D}'(\mathbb{R}^d)$ and
$\varphi\U n$ be an approximation to unity. Then

<div>
$$\begin{aligned}
\lim\U {n \to \infty} T\star  \phi\U n= T \in \mathcal{D}'(\mathbb{R}^d).
\end{aligned}$$
</div>

As a result,
$\overline{C\U c^\infty(\mathbb{R}^d)}=\mathcal{D}'(\mathbb{R}^d)$.


The proof can be found in [9](https://bookstore.ams.org/gsm-105#:~:text=A%20First%20Course%20in%20Sobolev%20Spaces&text=Sobolev%20spaces%20are%20a%20fundamental,BV%20functions%20of%20one%20variable.) page 308.

# <a name="local to global">  Global to local and back again  </a>

Often it is advantageous to work locally and then reason in the general
case by some kind of approximation. A useful tool in this respect are
bump functions.


**Definition 22**. A **bump function** (also called **cutoff
function**) is a function $\eta \in C\U c^\infty(\mathbb{R}^n)$.


Constructing bump functions that have some desired support is a tool we
use frequently throughout. Here we provide two examples to show how this
may be done. Other constructions are of course possible.

 <a name="bump example2">
**Example 5** </a> . Given two open sets $V,U$ with $V \Subset U$ there
exists $\eta \in C\U c^\infty(\mathbb{R}^d)$ with support in $U$, equal to
$1$ on $V$ and with $0\leq \eta \leq 1$.



Proof. Since $V \Subset U$, there exists a compact $K$ with


<div>
$$\begin{aligned}
V \subset K \subset U;\quad d\U u:=d(U,K)>0; \quad d\U V:=d(V,K)>0.
\end{aligned}$$
</div>



Now, by [Urysohn's
lemma](https://en.wikipedia.org/wiki/Urysohn%27s_lemma#:~:text=for%20any%20two-,non%2Dempty,-closed%20disjoint%20subsets)
there exists a continuous function $f \in C\U c(\mathbb{R}^n)$ such that
$0\leq\varphi \leq 1$ and $\varphi$ is $1$ on $K$. If we now take an
approximation of unity $\left\\{\phi\U n\right\\}\U {n=1}^\infty$ and choose
$N$ large enough so that $\min \left\\{d\U U,d\U V\right\\} > \frac{1}{N}$ we
can obtain the desired function as $\eta=f\star \phi\U {N}$. ◻



**Example 6**. There exists a sequence of
$\eta\U n \in C\U c^\infty(\mathbb{R}^d)$ such that

<div>
$$\begin{aligned}
\eta\U n(x) =\begin{cases}
1 \text{ if }  &\left| x \right|\leq n  \\
0 \text{ if }  &\left| x \right|\geq 2n \\
\end{cases}.
\end{aligned}$$
</div>

And
$\left\lVert \eta\U n \right\rVert\U {C^k(\mathbb{R}^d)} \leq \left\lVert \eta\U 1 \right\rVert$.



Proof. Let $\eta\U 1 \in C\U c^\infty(\mathbb{R}^d)$ be any (for example
that of (\ref{bump example}) ). Then we can take $\eta\U n(x):=\eta(x /n)$. ◻


In the opposite direction. One is often in the situation where it is
possible to derive some local properties for a given object (think
manifolds). To recover a global result one needs some way to piece
together the local results. A useful tool in this respect is partitions
of unity.


**Definition 23**. Given a manifold $M$ and an o pen covering
$\\{U\U \alpha\\}\U {\alpha \in  J}$ of $M$ we say that $\\{\rho\U i\\}\U {i\in  I}$
is a **partition of unity on $\\{U\U \alpha\\}\U {\alpha \in  J}$** if:

1.  $\mathbf{supp}(\rho\U i)\subset U\U \alpha$ for some $\alpha \in J$.

2.  For each $x \in M$, it holds that
$x \in \mathbf{supp}(\rho\U \alpha)$ for only a finite amount of
$\alpha \in I$.

3.  $\sum\U {i \in I}\rho \U i =1.$


Partitions of unity are often used in differential geometry as follows

1.  Work in some open subset $\mathbb{R}^n$ (or the upper half space
$\mathbb{R}^n\U +$ if our manifold has boundary) to prove the
existence of some object $g$ with desired properties.

2.  Cover the manifold $M$ with coordinate charts $U\U \alpha$ and
translate the euclidean result via the identification with
$U\U \alpha$ to obtain locally defined $g\U \alpha$.

3.  Obtain a globally defined object $g$ by using the partition of unity
to piece together the local objects

<div>
$$\begin{aligned}
g=\sum\U {\alpha \in I}\rho\U \alpha g\U \alpha .
\end{aligned}$$
</div>



In addition to the approximation and extension theorems in Section
[8](#extension section), partitions of unity can be used to show
that: every manifold has a [Riemannian
metric](https://en.wikipedia.org/wiki/Riemannian_manifold), show that a
function is smooth on some none-open set $S \subset M$ iff it is the
restriction of a smooth function defined on a neighborhood of $S$, prove
the existence of an outward pointing vector on manifolds with boundary,
define integration over an orientable manifold $M$, prove [Stoke's
theorem](https://en.wikipedia.org/wiki/Generalized_Stokes_theorem).

 <a name="partition">
**Theorem 17** </a> . Let $M$ be a smooth manifold (in particular we assume
$M$ is Hausdorff), then every open covering
$\left\\{U\U \alpha\right\\}\U {\alpha \in  J}$ has a partition of unity
$\left\\{\rho \U n\right\\}\U {n=1}^\infty$.


The proof is based on the existence of bump functions (something we have
already proved for $\mathbb{R}^d$) and is straightforward in the case
that $M$ is compact. The general case can be reduced to the compact
setting by obtaining a covering by relatively compact open sets
$\left\\{U\U i\right\\}\U {i=0}^\infty$ of $M$ such that

<div>
$$\begin{aligned}
V\U {i} \Subset V\U {i+1}.\end{aligned}$$
</div>

And then working with the
compact $\overline{V\U {i+1}} \setminus V\U {i}$. See [10](https://link.springer.com/chapter/10.1007/978-1-4419-7400-6_3)
Appendix C for the details.

# <a name="boundary">  Manifolds with boundary  </a>

We will be defining differential equations on open domains
$\Omega \subset \mathbb{R}^n$. In this case $\overline{\Omega}$ will be
a "manifold with boundary" whose regularity will determine what results
we have access to. The prototypical example of a manifold with a
boundary is the upper half space

<div>
$$\begin{aligned}
\mathcal{H}^d:=\left\{x=(x\U 1,\ldots,x\U d)\in \mathbb{R}^d: x\U d \geq 0\right\} .\end{aligned}$$
</div>


Here the inequality is not strict so that the boundary of
$\mathcal{H}^d$ is included in itself. Since $\mathcal{H}^d$ is not open
we need to define what is meant by saying that a function is
differentiable on such a set.

 <a name="smooth non open">
**Definition 24** </a> . Let $S \subset \mathbb{R}^d$ be an arbitrary set. We
say that a function $f:S \to \mathbb{R}$ is $k$-times differentiable at
$p$ if there exists a function
$\widetilde{f}:\mathbb{R}^d \to \mathbb{R}$ which is $k$ times
differentiable at $p$ and such that $\widetilde{f}=f$ on $S$.



**Definition 25**. If $f$ is $k$-times differentiable at every point of
$S$ we say that $f \in C^k(S)$.


 <a name="ext">
**Exercise 28** </a> . Show that $f\in  C^k(S)$ if and only if there exists
an extension $\widetilde{f}\in C^k(\mathbb{R}^d)$ of $f$ which is equal
to $f$ on $S$.


<div class="exercise-container">
<button class="exercise-button" onclick="toggleExercise(this)">Hint</button>
<div class="exercise-text">
Use a partition of unity.
</div>
</div>

A manifold with boundary $M$ is just a generalization of
$\mathcal{H}^d$, where we impose that $M$ is "locally equal" to
$\mathcal{H}^d$. That is, there exists a covering of $M$ by open sets
$V\U \alpha$ and a collection of homeomorphisms with the subspace
topology from $\mathcal{H}^d$

<div>
$$\begin{align}
\label{chart}
\Phi\U \alpha : V\U \alpha \xrightarrow{\sim}\Phi(V\U \alpha).\end{align}$$
</div>


And where for compatibility we impose that for each $\alpha,\beta$ the
function

<div>
$$\begin{align}
\label{diff}
\Phi\U \beta \circ\Phi\U \alpha^{-1}: \Phi\U \alpha(V\U \alpha\cap V\U \beta ) \longmapsto \Phi\U \beta (V\U \alpha\cap V\U \beta ).\end{align}$$
</div>


Are diffeomorphisms on $\mathcal{H}^d$ (again with the subspace
topology). Here $\mathcal{A}=\left\\{(U\U \alpha,\Phi\U \alpha)\right\\}$ is
an atlas of $M$. We say that $\mathcal{A}$ is $C^k$ if the
diffeomorphisms in (\ref{diff})  are $C^k$ (see Definition
[24](#smooth non open)).


**Definition 26**. We say that $(M,\mathcal{A})$ is a $C^k$ manifold
with boundary if $M$ is a second countable Hausdorff space and
$\mathcal{A}$ is a $C^k$ atlas.


The boundary of $M$ is its points that are mapped to the boundary
$\left\\{x\U d=0\right\\}$ in $\mathcal{H}^d$.


**Definition 27**. Given a point $p \in M$ we say that $p$ is a
boundary point if for some (and thus every chart)
$\Phi\U \alpha(p) \in \partial \mathcal{H}^{d}$. We call the set of all
boundary points the boundary of $M$ and denote it by $\partial M$.



**Exercise 29**. Show that the restricted atlas
$\left.\Phi\U \alpha\right|\U {\partial M}$ makes $\partial M$ a $d-1$
dimensional manifold without boundary.


<div class="exercise-container">
<button class="exercise-button" onclick="toggleExercise(this)">Hint</button>
<div class="exercise-text">
By definition of boundary

<div>
$$\begin{align}
\label{chart2}
\left.\Phi\U \alpha\right|\U {\partial M}: V\U \alpha \cap M \to \partial \mathcal{H}^{d-1} \simeq \mathbb{R}^{d-1}.
\end{align}$$
</div>

And the coordinate changes are $C^k$ as the
restriction of a $C^k$ map is $C^k$.
</div>
</div>

In our case we will always take $M$ to be a subset of $\mathbb{R}^d$, in
this case, different variations of the above definition are possible.
For example, by the inverse function theorem and Exercise
[28](#ext), we can extend the
functions $\Phi\U \alpha$ to diffeomorphisms on $U\U \alpha$ open in
$\mathbb{R}^d$ so that (\ref{chart}) -(\ref{chart2})  now read

<div>
$$\begin{align}
\label{alt0}
\Phi\U \alpha : U\U \alpha \xrightarrow{\sim}\Phi(U\U \alpha); \quad    \Phi\U \alpha : U\U \alpha \cap M \xrightarrow{\sim}\Phi\U \alpha(U\U \alpha) \cap \mathcal{H}^d .\end{align}$$
</div>


Additionally, by the implicit function theorem there exists for each
coordinate set $U\U \alpha$ functions
$\gamma\U \alpha \in C^k(\mathbb{R}^{d-1})$ such that, relabeling the
coordinates and decreasing the size of $U\U \alpha$ if necessary,


<div>
$$\begin{align}
\label{alt1}
\partial M \cap U\U \alpha & =\left\{x \in U\U \alpha : x\U d=\gamma\U \alpha(x\U 1,\ldots,x\U {d-1}) \right\}\end{align}$$
</div>


Let us write $x=(x',x\U d)$, by the Taylor expansion

<div>
$$\begin{aligned}
\Phi\U \alpha(x',\gamma \U \alpha(x')+\epsilon)=\Phi\U \alpha(x)+\frac{\partial \Phi}{\partial x\U d}(x)\epsilon +O(\left\lVert \epsilon  \right\rVert^2)  .\end{aligned}$$
</div>


We deduce that, once more reducing the size of $U\U \alpha$ if necessary
and depending on the sign of $\partial \U d \Phi$ on $U\U \alpha$, one and
only one of the following two hold

<div>
$$\begin{align}
\label{alt3}
(M \setminus \partial M) \cap U\U \alpha & =\left\{x \in U\U \alpha : x\U d>\gamma\U \alpha(x\U 1,\ldots,x\U {d-1}) \right\}                 \\
(M \setminus \partial M) \cap U\U \alpha & =\left\{x \in U\U \alpha : x\U d<\gamma\U \alpha(x\U 1,\ldots,x\U {d-1}) \right\}\notag.\end{align}$$
</div>


The equivalent formulations in (\ref{alt0})  and in (\ref{alt1}) -(\ref{alt3})  are used in the main exposition. Finally, in our case,
we will typically take $M =\overline{\Omega}$ where
$\Omega \subset \mathbb{R}^d$ is some open set. In this case, we adopt
the following terminology.


**Definition 28**. We say that an open set $\Omega\subset \mathbb{R}^d$
has $C^k$ boundary of $\overline{\Omega}$ is a $C^k$ manifold with
boundary.


In the above case, the topological and manifold boundaries of $\Omega$
necessarily coincide as homeomorphisms map topological boundaries to
topological boundaries.
A pdf of version of this page is provided below:
<object data="/assets/blank.pdf" width="1000" height="1000" type='application/pdf'></object>
