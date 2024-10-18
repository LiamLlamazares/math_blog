---
layout: post
title: Parabolic PDE. Well posedness and regularity
subtitle: A journey through time and space
thumbnail-img: /assets/img/Evans_PDE.jpg
share-img: /assets/img/Evans_PDE.jpg
tags: [PDEs]
authorpost: L.Llamazares-Elias
---

# Three point summary

-   A parabolic PDE describes how a function evolves over time under the
influence of an elliptic operator. Unlike their elliptic
counterparts, parabolic PDEs are typically
<a href="https://nowheredifferentiable.com/2024-02-28-PDEs-6-Elliptic_PDE._Well_posedness_and_regularity/#:~:text=is%20well%2Dposed.-,Definition%202,-(Well%2Dposedness">well-posed</a>.%20We).
For well-behaved coefficients, a unique solution always exists and
depends continuously on the initial data.

-   Solutions to parabolic PDEs can be viewed as functions mapping an
instant in time to a function in a Banach space. From this
viewpoint, the PDE becomes an infinite dimensional ODE. The Galerkin
method is a powerful tool to prove the well-posedness of the problem
and approximate its solutions using a finite-dimensional ODE that
approximates the original infinite-dimensional problem.

-   The solution is smoother than the initial data and will always be at
least continuous in time and (weakly) differentiable in space. If
the coefficients of the PDE are smooth, the solution will be smooth
as well.

# Notation

-   As in the rest of the series, we will let $U$ denote an arbitrary
open subset of $\mathbb{R}^d$. That is, it may be bounded or
unbounded with no conditions on the regularity of the boundary (if
it exists). To denote a smooth domain, we will use the notation
$\Omega$.

-   We will be working with functions of time and space $u(t,x)$ defined
on some time interval $I=[0, T]$ and spatial domain $U$. We will
denote by $u(t)$ the function $u(t,\cdot):U\to \mathbb{R}$.

-   Given a topological vector space $X$ with dual $X'$ and
$x \in X, w \in X'$ we write the duality pairing

<div>
$$\begin{aligned}
(x,w):= w(x).

\end{aligned}$$
</div>



# Introduction

In the <a href="https://nowheredifferentiable.com/2024-02-28-PDEs-6-Elliptic_PDE._Well_posedness_and_regularity/">previous post of this
series</a>,
we studied the well-posedness and regularity of solutions to an elliptic
PDE of the form

<div>
$$\begin{aligned}
\begin{cases}
\mathcal{L}u = f & \text{in } U     \\
u = 0   & \text{on } \partial U
\end{cases}
\end{aligned}$$
</div>

where the second order differential operator
$\mathcal{L}$ was given in divergence form as

<div>
$$\begin{align}
\label{elliptic operator 0}
-\nabla \cdot (\mathbf{A} \nabla u)+ \nabla \cdot (\mathbf{b} u)+cu.
\end{align}$$
</div>

and verified the ellipticity condition. After defining
the weak formulation of the problem, we naturally obtained the function
spaces we were interested in and, under some restrictions on the
coefficients, proved the existence and uniqueness of solutions. When
solutions were not guaranteed to be unique, we studied the spectrum of
$\mathcal{L}$, and in all cases, we showed that the solution had
improved regularity as compared to the coefficients of the PDE.

In this post we now look to mimic the previous analysis but for
parabolic PDEs. We define the operator

<div>
$$\begin{align}
\label{elliptic operator}
\mathcal{L}u:= -\nabla \cdot (\mathbf{A} \nabla u)+ \mathbf{b} \cdot \nabla u+cu,
\end{align}$$
</div>

(by Leibnit'z rule one can move between
(\ref{elliptic operator 0})  and
(\ref{elliptic operator}) ) and consider the parabolic PDE


<div>
$$\begin{align}
\label{parabolic}
\begin{cases}
\partial\U t u + \mathcal{L}u = f & \text{in } I\times U      \\
u(0) = g         & \text{on } U          \\
u = 0          & \text{on } I\times \partial U,
\end{cases}
\end{align}$$
</div>

where $I=[0,T]$ is the time interval of interest and
$0<T< \infty$. Here, we need an extra initial condition $u(0) = g$ that
tells us the initial state of the system. The operator $\mathcal{L}$ has
the same form as in
(\ref{elliptic operator}) , however now the coefficients
$\mathbf{A}(t, \mathbf{x}), \mathbf{b}(t, \mathbf{x}), c(t, \mathbf{x})$ are allowed to
depend on both time and space. In the next sections, we will define the
weak formulation of the problem and study the well-posedness and
regularity of solutions. As we will see, within the functions spaces of
interest, (\ref{parabolic})  is always well-posed. This is in contrast to
elliptic PDEs, where well-posedness was not guaranteed in general.

# Weak formulation

## Banach valued functions

To define weak solutions to
(\ref{parabolic}) , it is convenient to switch our viewpoint.
Instead of thinking of $u$ as a real-valued function of time and space,
we think of it as a Banach space valued function of time


<div>
$$\begin{aligned}
u: I \to X, \quad t \mapsto u(t),
\end{aligned}$$
</div>

where $X$ is some Banach space of function on $U$ (such
as $L^2(U), H\U 0^1(U),...$) and we use the notation $u(t)(x):= u(t,x)$.
This way of viewing $u$ is an essential tool in the theory of evolution
PDEs, which transform the PDE
(\ref{parabolic})  into an infinite dimensional linear ODE.

To be able to proceed, we need to define an integral on functions valued
in Banach spaces. This integral is called the <a href="https://nowheredifferentiable.com/2022-05-27-The-Bochner-integral/">Bochner
integral</a>.
To briefly summarize, given a separable Banach space $X$ and
$p \in [1, \infty]$ we define

<div>
$$\begin{align}
\label{dual}
L^p(I \to X)= \left\{f: I \to X: f \text{ measurable and } \left\lVert f \right\rVert\U {L^p(I \to X)}< \infty\right\},
\end{align}$$
</div>

where functions equal almost everywhere are identified,
and the norm is defined as

<div>
$$\begin{aligned}
\left\lVert f \right\rVert\U {L^p(I,X)}  &:= \left( \int\U I \left\lVert f(t) \right\rVert\U X^p \,\mathrm{d}t \right)^{1/p}, \quad p \in [1, \infty),\\
\|f\|\U {L^{\infty}(I\rightarrow X)}&:=\inf \{r>0: \mu(\|f\|>r)=0\}.
\end{aligned}$$
</div>

Then, hte spaces $L^p(I \to X)$ are Banach spaces and
functions $f$ in $L^1(I \to X)$ have a well defined Bochner integral


<div>
$$\begin{aligned}
\int\U I f(t) \,\mathrm{d}t \in X.
\end{aligned}$$
</div>

This integral generalizes the Lebesgue integral and is
also constructed by approximating the integrable functions by simple
functions of the form $\sum\U {i=1}^n 1\U {A\U i} x\U i$ where $A\U i$ are sets
with finite measure and $x\U i \in X$.

Many familiar properties carry over to the Bochner integral. Namely,
integration is a continuous linear operator on $L^1(I \to X)$.
Furthermore, given $p \in [1,\infty)$ and $v \in L^{p'}(I \to X')$,
where $p'$ is the conjugate exponent of $p$, we can define the duality
pairing

<div>
$$\begin{aligned}
(u,v):= \int\U I (u(t),v(t))\U X \,\mathrm{d}t, \quad u \in L^p(I \to X).
\end{aligned}$$
</div>

With this identification, the dual of $L^p(I \to X)$ is
equal to $L^{p'}(I \to X')$ . We will also use that if
$\phi\U n \in C^\infty(I)$ is a <a href="https://nowheredifferentiable.com/2023-07-12-PDEs-3-Sobolev_spaces/#smooth%20section:~:text=is%20an-,approximation,-to%20unity%20if">smooth approximation of
unity</a>
then, for $p \in [1, \infty)$

<div>
$$\begin{align}
\label{approximation}
\lim\U {n \to \infty} u \star  \phi\U n \to u \text{ in } L^p(I \to X),\quad \quad \lim\U {n \to \infty} u \star  \phi\U n=u \text{ almost everywhere }.
\end{align}$$
</div>



To make the notation more readable we will use the convention of
denoting function spaces in temporal and spatial domains by the
subindexes $t,x$. For example, we write

<div>
$$\begin{aligned}
L^2\U t H^1\U {0,x} & := L^2(I \to H^1\U 0(U)), \quad L^2\U t H^{-1}\U {x} := L^2(I \to H^{-1}(U))   \\
L\U {t,x}^\infty & := L^\infty(I \times U), \quad\quad\qquad\quad  L^2\U x     := L^2(U).
\end{aligned}$$
</div>

Due to the previous discussion we have that


<div>
$$\begin{align}
\label{duality}
L^2\U t H^1\U {0,x}(U)' = L^2\U t H^{-1}\U {x}(U).
\end{align}$$
</div>



A tricky aspect of PDE is figuring out what space $X$ should be? The
choice of $X$ needs to be guided by what bounds one can obtain in the
norm of $X$. As we will see when we derive energy bounds for $u$, the
space $X=H\U 0^1(U)$ is the natural Banach space to consider in this
setting.

## Weak solutions

As may have become familiar at this point of the series, to derive the
weak formulation of our problem
(\ref{parabolic}) , we suppose that $u$ is smooth, multiply the
equation by a test function $v \in C\U c^\infty(I\times U)$ and integrate
over $I\times U$. We obtain that, in addition to the condition $u(0)=g$


<div>
$$\begin{align}
\label{weak 0}
\int\U I \int\U U u' v + \int\U I \int\U U (\mathbf{A} \nabla u) \cdot \nabla v + \int\U I \int\U U (\mathbf{b} \cdot \nabla u ) v + \int\U I \int\U U c u v = \int\U I \int\U U f v,
\end{align}$$
</div>

where for brevity in the notation we omitted the
customary $\,\mathrm{d}x\,\mathrm{d}t$ in the integrals and wrote
$u'= \partial \U t u$. Equivalently, with the notation for the duality
pairing, we can write (\ref{weak 0})  and the boundary condition as

<div>
$$\begin{align}
\label{weak}
(v, u')+ (\nabla v, \mathbf{A} \nabla u) + ( v, \mathbf{b}\nabla u) + (v, cu) = (v, f), \quad u(0) = g.
\end{align}$$
</div>

For the following theory we need some assumption on the
coefficients and the data. Firstly, we give the following definition


<b>Definition 1</b>. We say that $\mathbf{A}$ is parabolic if there exists a
constant $\alpha>0$ such that

<div>
$$\begin{align}
\label{parabolicity}
(\mathbf{A}(t,\mathbf{x}) \mathbf{\xi}) \cdot \mathbf{\xi} \geq \alpha \left| \xi \right|^2 \quad \forall (t,\mathbf{x}) \in I \times \Omega,\, \mathbf{\xi} \in \mathbb{R}^d.

\end{align}$$
</div>




This is the parabolic analog of the ellipticity condition we required in
the previous post. Physically speaking, it guarantees that diffusion
does not go to zero and occurs from regions of larger concentration to
lower concentration.

 <a name="ass">
<b>Assumption 1</b> </a> . We assume that $\mathbf{A}$ is parabolic and for all
$i,j=1,\dots,d$

<div>
$$\begin{aligned}
A\U {ij}, b\U i , c \in L^\infty\U {t,x}, \quad f \in L^2\U t H^{-1}\U x, \quad g \in L^2\U x.

\end{aligned}$$
</div>




The boundedness of $\mathbf{A},\mathbf{b},c$ is expedient so that the integrals
in (\ref{weak})  are well
defined.

For (\ref{weak})  to make
sense and verify the boundary condition $u=0$ on $\partial U$, we give
the following definition.

 <a name="weak def">
<b>Definition 2</b> </a>  (Weak solution). Under Assumption
<a href="#ass">1</a>, we say that $u$ is a
weak solution of the parabolic problem
(\ref{parabolic})  if

<div>
$$\begin{aligned}
u \in L^2\U t H^1\U {0,x}, \quad u' \in L^2\U t H^{-1}\U x,

\end{aligned}$$
</div>

and (\ref{weak})  is verified for all $v \in L^2\U tH^1\U {0,x}$.


With the above definition, all the terms
(\ref{weak})  are well
defined, where the duality pairing is to be interpreted as the one given
by (\ref{duality}) .
Furthermore, the boundary condition $u=0$ on $\partial U$ is
automatically satisfied as $u(t) \in H\U 0^1(U)$ for almost all $t$ and a
quick sanity check shows that the various functional spaces in
definition <a href="#weak def">2</a> are
logical as if $u \in L^2\U t H^1\U {0,x}$ then
$\mathcal{L}u \in L^2\U t H^{-1}\U x$ and from
(\ref{parabolic})  we should also have $u' \in L^2\U t H^{-1}\U x$. It
only remains to justify that $u(0)$ is well-defined. This is proved in
the following lemma.

 <a name="continuity weak">
<b>Lemma 3</b> </a> . Let $u \in L\U t^2H\U {x}^1$ with $u' \in L\U tH\U x^{-1}$. Then,
$u \in C\U t L\U x^2$ with

<div>
$$\begin{aligned}
\left\lVert u \right\rVert\U {C\U t L\U x^2} \lesssim \left\lVert u(0) \right\rVert\U {L\U x^2}+ \left\lVert u \right\rVert\U {L\U t^2H\U {x}^1}+ \left\lVert u' \right\rVert\U {L\U tH\U x^{-1}}.

\end{aligned}$$
</div>





<b>Proof.</b> Let $\phi\U n \in C\U c^ \infty(I)$ be a smooth approximation to
the identity and define $u\U n(t):=(u\star  \phi\U n)(t)$ (we use the convention
of extending $u$ by zero outside of $I$ so the convolution is well
defined). Then, $u\U n \in C^\infty\U t L\U x^2$ converges almost everywhere
and in $L\U t^2 H\U x^1$ to $u$ and $u\U n '$ converges in $L\U t^2 H\U x^{-1}$ to
$u'$ (see (\ref{approximation}) ).Given $n , m >0$ write
$w\U {n,m}:= u\U n - u\U m$. We have that,

<div>
$$\begin{aligned}
\qty(\left\lVert u\U n(t) \right\rVert^2\U {L\U x^2})' = 2\left\langle u\U n(t),u\U n'(t)\right\rangle\U {L^2\U x}.

\end{aligned}$$
</div>

As a result, by the fundamental theorem of calculus,
given any $s,t \in I$,

<div>
$$\begin{aligned}
\left\lVert w\U {n,m}(t) \right\rVert\U {L^2\U x}^2 = \left\lVert w\U {n,m}(s) \right\rVert\U {L^2\U x}^2 +2\int\U {s}^t \left\langle w\U {n,m}(r),w\U {n,m}'(r)\right\rangle\U {L^2\U x} \,\mathrm{d}r.

\end{aligned}$$
</div>

Taking any $s$ such that $u\U n(s) \to u(s)$ and the max
over $t$ gives

<div>
$$\begin{align}
\label{Cauchy}
\limsup\U {n , m \to \infty} \max\U {t \in I}\left\lVert w\U {n,m}(t)  \right\rVert\U {L^2\U x}^2 \lesssim 0 + \limsup\U {n , m \to \infty}\int\U {I} \left\lVert w\U {n,m}(r)  \right\rVert\U {H^1\U x}^2 \,\mathrm{d}r + \int\U {I} \left\lVert w'\U {n,m}(r) \right\rVert\U {H^{-1}\U x}^2 \,\mathrm{d}r=0,

\end{align}$$
</div>

where in the last equality we used that $u\U n ,u'\U n$
converge to $u,u'$ in the respective norms.

Equation (\ref{Cauchy})  shows that $u\U n$ is a Cauchy sequence in the Banach
space $C\U t L\U x^2$ and, as a result, converges to a continuous function
$v$ in $C\U t L\U x^2$. Since it also converges almost everywhere to $u$, we
must have that $v=u$. This shows that $u \in C\U t L\U x^2$.

To prove the bound of the theorem, suppose first that $u$ is smooth in
$t$. Then, by the fundamental theorem of calculus and the definition of
the dual norm

<div>
$$\begin{aligned}
\left\lVert u(t) \right\rVert\U {L\U x^2}^2 & = \left\lVert u(0) \right\rVert\U {L\U x^2}^2 + 2\int\U I \left\langle u'(r),u(r)\right\rangle\U {L\U x^2} \,\mathrm{d}r \\&\leq \left\lVert u(0) \right\rVert\U {L\U x^2}^2 + 2 \int\U I \left\lVert u'(r) \right\rVert\U {L^2\U tH\U x^{-1}}\left\lVert u(r) \right\rVert\U {L^2\U tH\U x^1} \,\mathrm{d}r.

\end{aligned}$$
</div>

The bound follows Cauchy-Schwartz, and the non-smooth
case follows by approximating $u$ by smooth $u\U n = u\star phi\U n$. ◻


# Well-posedness of the problem

We now aim to show that the problem
(\ref{parabolic}) , or more precisely its weak formulation
(\ref{weak}) , is
well-posed.

## A naive approach

As we have discussed in the previous section, equation
(\ref{parabolic})  can be seen as an infinite dimensional linear
ODE. As a result, we could hope that the theory of linear ODE will give
us a solution. Working directly we would write
$F(u):= -\mathcal{L}u + f$ and the equation
(\ref{parabolic})  as

<div>
$$\begin{align}
\label{ode}
u'(t)= F(u(t)), \quad u(0) = g.
\end{align}$$
</div>

Then, writing once more $X =H\U 0^1(U)$, we could try to
emulate Picard's theorem for scalar-valued ODEs to obtain a fixed point
for

<div>
$$\begin{aligned}
\Phi: C([0,\epsilon ] \to X) \to C([0,\epsilon ] \to X), \quad u \mapsto \Phi(u)(t) := g + \int\U I F(u(s)) \,\mathrm{d}s.
\end{aligned}$$
</div>

The only problem with this is that $F$ does not map $X$
to $X$. As a result, the mapping $\Phi$ is not well defined. If the
initial data is smooth, we could hope to set $X = C\U c^\infty(U)$, and
then $F$ would map $X$ to $X$. However, $C^\infty\U c(U)$ is not a Banach
space, so further modifications would be required. As a result, we need
a more refined approach. In the next section, we use the Galerkin method
to prove the problem's well-posedness.

## Galerkin solutions

Instead of working directly in infinite dimensions, we project our
problem onto a finite-dimensional space spanned by $n$ basis functions
$\left\\{\phi\U i\right\\}\U {i=1}^n$. If we are able to solve the projected
problem, we hope that as the number of basis functions $n$ increases,
the solution will converge to the true solution. This is the idea behind
the Galerkin method, which is widely used in the numerical study of
PDEs.


<b>Exercise 1</b>. Use that $L^2(U)$ is separable to show that it has a
smooth orthonormal basis of functions
$\left\\{\phi\U i\right\\}\U {i=1}^\infty$. that is,

<div>
$$\begin{aligned}
\left\langle\phi\U i, \phi\U j\right\rangle\U {L^2(U)} = \delta\U {ij}, \quad \phi\U i \in C^\infty\U c(U).
\end{aligned}$$
</div>




<div class="exercise-container">
<button class="exercise-button" onclick="toggleExercise(this)">Hint</button>
<div class="exercise-text">
Since $L^2(U)$ is separable, it has a countable dense subset
$\left\\{f\U i\right\\}\U {i=1}^\infty \subset L^2(U)$. Since $C\U c^\infty(U)$
is dense in $L^2(U)$, for each $f\U i$ there exists a sequence
$\left\\{\phi\U {i,n}\right\\}\U {n=1}^\infty \subset C\U c^\infty(U)$ that
converges to $f\U i$ in $L^2(U)$. Then, the set
$\left\\{\phi\U {i,n}\right\\}\U {i,n}$ is a countable dense subset of
$L^2(U)$, and we can apply the Gram-Schmidt process to obtain an
orthonormal basis.

Alternatively, if $U$ is bounded and smooth, $\Delta ^{-1}$ is compact
and self-adjoint. Hence, it has a countable orthonormal basis of
eigenfunctions which are smooth by the <a href="https://nowheredifferentiable.com/2024-02-28-PDEs-6-Elliptic_PDE._Well_posedness_and_regularity/#:~:text=for%20smooth%20coefficients.-,Theorem%2016">previous
post</a>
and induction.
</div>
</div>

Let $\left\\{\phi\U i\right\\}\U {i=1}^\infty\subset C^\infty\U c(U)$ be an
orthonormal basis of $L^2(U)$, let
$V\U n:= \text{span}\left\\{\phi\U i\right\\}\U {i=1}^n$ and let


<div>
$$\begin{aligned}
\mathcal{S}\U n:= C(I \to V\U n)= \left\{\sum\U {j=1}^n \lambda \U j(t) \phi\U j: \lambda\U j \in C(I)\right\}.
\end{aligned}$$
</div>

Consider the problem of finding $u\U n \in \mathcal{S}\U n$
such that, for all $i=1,....,n$ and $t \in I$

<div>
$$\begin{align}
\label{galerkin}
\left\langle\phi\U i, u'\U n(t)\right\rangle\U {L^2\U x} + B(\phi\U i,u\U n(t);t) & = (\phi \U i, f(t)),\quad
\left\langle\phi\U i, u\U n(0)\right\rangle\U {L^2\U x}           = \left\langle\phi\U i,g\right\rangle\U {L\U x^2},
\end{align}$$
</div>

where $\left\langle\cdot ,\cdot \right\rangle\U {L^2\U x}$
denotes the inner product in $L^2\U x$, $(\cdot,\cdot)$ is the pairing of
an element in $H^1\U {x,0}$ with an element in its dual and
$B(\cdot ,\cdot ,t)$ is the bilinear form on $H^1\U 0(U)$ defined by


<div>
$$\begin{aligned}
B(w,v; t) := \int\U U \mathbf{A}(t) \nabla v \cdot \nabla w + (\mathbf{b}(t) \cdot \nabla v) w + c(t) v w \,\mathrm{d}x .
\end{aligned}$$
</div>

Equation
(\ref{galerkin})
is known as the Galerkin problem.


<b>Theorem 4</b> (Well-posedness of the Galerkin problem). Under
Assumption <a href="#ass">1</a>, the Galerkin
problem (\ref{galerkin})  is well-posed. That is, a unique solution $u\U n$
exists and depends continuously on the initial data. Furthermore,


<div>
$$\begin{align}
\label{bound}
\left\lVert u\U n \right\rVert\U {C\U t L\U x^2} +\left\lVert u\U n \right\rVert\U {L^2\U tH\U {x}^1} + \left\lVert u\U n' \right\rVert\U {L^2\U tH\U {x}^{-1}} \lesssim\U {\mathbf{A,b},c,T} \left\lVert f \right\rVert\U {L^2\U t H\U x^{-1}}+ \left\lVert g \right\rVert\U {L\U x^2}.

\end{align}$$
</div>





<b>Proof.</b> We divide the proof into three parts. Existence, continuity,
and uniqueness.

a)  Existence of solutions: Since the $\phi\U i$ are orthonormal and we
impose $u\U n \in \mathcal{S}\U n$, solving
(\ref{galerkin})  is equivalent to finding
$\mathbf{\lambda}\U n\in C(I \to \mathbb{R}^n)$ such that


<div>
$$\begin{align}  \label{galerkin 2}
\mathbf{\lambda}\U n'(t) + \mathbf{B}\U n(t) \mathbf{\lambda}\U n(t) = \mathbf{f}\U n(t), \quad \mathbf{\lambda}\U n(0) = \mathbf{g}\U n,

\end{align}$$
</div>

where we define the matrix
$\mathbf{B}\U n(t) \in R^{n \times n}$ and vectors
$\mathbf{f}\U n(t), \mathbf{g}\U n \in \mathbb{R}^n$ as

<div>
$$\begin{aligned}
\U {ij}:= B(\phi\U i, \phi\U j;t), \quad [\mathbf{f}\U n(t)]\U i:= (\phi\U i, f(t)), \quad [\mathbf{g\U n}]\U i:= \left\langle\phi\U i,g\right\rangle\U {L\U x^2}.

\end{aligned}$$
</div>

The equivalence of solving
(\ref{galerkin})  and
(\ref{galerkin 2})  is obtained by setting
$u\U n(t) = \sum\U {j=1}^n [\mathbf{\lambda}\U n]\U j \phi\U j$.

Since $\phi \U i \in C\U c^\infty(U)$, by the boundedness of the
coefficients in Assumption <a href="#ass">1</a>, and by the construction of $\mathbf{B}\U n,\mathbf{f}\U n$. It
holds that $\mathbf{B}\U n \in L^\infty\U t$ and $\mathbf{f}\U n \in L^2\U t$. As a
result, according to standard ODE theory, there exists a unique
continuous solution $\mathbf{\lambda }$ to
(\ref{galerkin 2}) . One can even write out the explicit
expression for $\mathbf{\lambda }$ using Duhamel's formula,


<div>
$$\begin{align}  \label{duhamel}
\mathbf{\lambda}\U n(t) = e^{\int\U 0^t \mathbf{B}\U n(s) \,\mathrm{d}s } \mathbf{g}\U n + \int\U 0^t e^{ \int\U {s}^t \mathbf{B}\U n(r) \,\mathrm{d}r} \mathbf{f}\U n(s) \,\mathrm{d}s.

\end{align}$$
</div>

This proves existence.

b)  Continuity in the data: The plan will be to apply Gronwall's
inequality. By (\ref{galerkin})  and the linearity of the inner product, we
obtain

<div>
$$\begin{align}  \label{sol un}
\left\langle u\U n(t),u\U n'(t)\right\rangle\U {L^2\U x}+B(u\U n(t),u\U n(t);t) = (u\U n(t), f(t)).

\end{align}$$
</div>

Now, since $u\U n$ is smooth and by differentiating
under the integral sign,

<div>
$$\begin{align}  \label{derivative}
\left\langle u\U n(t),u\U n'(t)\right\rangle\U {L^2\U x} = \frac{1}{2}\qty(\left\lVert u\U n(t) \right\rVert\U {L\U x^2}^2)'.

\end{align}$$
</div>

Using Cauchy's inequality
$ab \leq \frac{1}{2} (\epsilon a^2+\epsilon^{-1} b^2)$, the
boundedness of the coefficients and the ellipticity of $\mathbf{A}$
shows that, for some constants $\beta , \nu >0$

<div>
$$\begin{align}  \label{B bound}
B(u\U n(t),u\U n(t);t) \geq \gamma \left\lVert u\U n(t) \right\rVert\U {H^1\U x}^2 - \nu\left\lVert u\U n(t) \right\rVert\U {L^2\U x}^2

\end{align}$$
</div>

(this is the same as <a href="https://nowheredifferentiable.com/2024-02-28-PDEs-6-Elliptic_PDE._Well_posedness_and_regularity/#:~:text=%20.%20We-,recall,-the%20Cauchy%20inequality">what was
proved</a>
as in the elliptic case). Whereas, by definition of the dual and by
Cauchy's inequality, the bound of the right-hand side of
(\ref{sol un})  is,


<div>
$$\begin{align}  \label{rhs bound}
\left| (u\U n(t), f(t)) \right| \leq \left\lVert u\U n(t) \right\rVert\U {H\U {x}^1} \left\lVert f(t) \right\rVert\U {H\U x^{-1}}\leq \frac{1}{2} \left\lVert u\U n(t) \right\rVert\U {H\U {x}^1}^2 + \frac{1}{2} \left\lVert f(t) \right\rVert\U {H\U x^{-1}}^2.

\end{align}$$
</div>

Using
(\ref{derivative}) ,
(\ref{B bound})
and (\ref{rhs bound})  in equation
(\ref{sol un})  we
obtain that

<div>
$$\begin{align}  \label{i0}
\qty(\left\lVert u\U n(t) \right\rVert\U {L\U x^2}^2)' + \left\lVert u\U n(t) \right\rVert\U {H^1\U x}^2 \lesssim \left\lVert u\U n(t) \right\rVert^2\U {L\U x^2} + \left\lVert f(t) \right\rVert\U { H\U x^{-1}}^2.

\end{align}$$
</div>

In particular,

<div>
$$\begin{align}  \label{i00}
\qty(\left\lVert u\U n(t) \right\rVert\U {L\U x^2}^2)' \lesssim \left\lVert u\U n(t) \right\rVert^2\U {L\U x^2} + \left\lVert f(t) \right\rVert\U {H\U x^{-1}}^2.

\end{align}$$
</div>

Given differentiable $v:I \to \mathbb{R}$ aa
constants $\alpha\in \mathbb{R}$ and integrable $\beta \in L^1(I)$,
Gronwall's inequality states that

<div>
$$\begin{aligned}
v'(t) \leq \alpha v(t) + \beta \quad \Rightarrow \quad v(t) \leq e^{\alpha t}v(0) + \int\U I e^{\alpha(t-s)}\beta(s)\,\mathrm{d}s.

\end{aligned}$$
</div>

Applying this to
(\ref{i00})  gives


<div>
$$\begin{align}  \label{i1}
\left\lVert u\U n(t) \right\rVert\U {L\U x^2}^2 \lesssim e^{\alpha t}\qty(\left\lVert g \right\rVert\U {L\U x^2}^2 + \int\U I \left\lVert f(t) \right\rVert^2\U { H\U x^{-1}}\,\mathrm{d}t) \lesssim \left\lVert g \right\rVert\U {L\U x^2}^2 + \left\lVert f \right\rVert\U {L^2\U t H\U x^{-1}}^2.

\end{align}$$
</div>

Taking the maximum in
(\ref{i1})  gives the first
part of the bound in (\ref{bound})

<div>
$$\begin{align}  \label{ub}
\left\lVert u\U n \right\rVert^2\U {C\U t L\U x^2} \lesssim \left\lVert g \right\rVert^2\U {L\U x^2} + \left\lVert f(t) \right\rVert^2\U {L^2\U t H\U x^{-1}}.

\end{align}$$
</div>

To bound the second term in
(\ref{bound})  we
combine (\ref{i1})  with
(\ref{i0})  to obtain


<div>
$$\begin{align}  \label{hb0}
\qty(\left\lVert u\U n(t) \right\rVert\U {L\U x^2}^2)' + \left\lVert u\U n(t) \right\rVert\U {H^1\U x}^2 \lesssim \left\lVert g \right\rVert^2\U {L\U x^2} + \left\lVert f(t) \right\rVert^2\U {H\U x^{-1}}.

\end{align}$$
</div>

Integrating over $I$ in
(\ref{hb0})  and applying
the fundamental theorem of calculus together with
(\ref{ub})  gives


<div>
$$\begin{align}  \label{hb}
\left\lVert u\U n(t) \right\rVert\U {L\U t^2H^1\U x}^2:= \int\U I \left\lVert u\U n(t) \right\rVert\U {H^1\U x}^2 \,\mathrm{d}t \lesssim \left\lVert g \right\rVert^2\U {L\U x^2} + \left\lVert f \right\rVert^2\U {L^2\U t H\U x^{-1}}.

\end{align}$$
</div>

To bound $u\U n'$ consider any $v \in H\U {0,x}^1$, and
write $v=v\U n+v\U n^\perp$ where $v\U n$ is the projection of $v$ onto
$V\U n$ with the inner product on $H^1\U x$. Since $v\U n^\perp$ is
orthogonal to $u\U n'(t)\in V\U n$ for each $t$, from
(\ref{galerkin})  we have

<div>
$$\begin{aligned}
\left\langle u\U n'(t),v\right\rangle\U {L^2\U x} & = \left\langle u\U n'(t),v\U n\right\rangle\U {L^2\U x}= (f(t),v\U n)- B(u\U n(t),v\U n;t)                                                                \\
& \lesssim \left\lVert f(t) \right\rVert\U {H\U x^{-1}}\left\lVert v\U n(t) \right\rVert\U {H^1\U x} + \left\lVert  u\U n(t) \right\rVert\U {H^1\U x}\left\lVert v\U n \right\rVert\U {H^1\U x} \lesssim \left(\left\lVert f(t) \right\rVert\U {H\U x^{-1}} + \left\lVert  u\U n(t) \right\rVert\U {H^1\U x}\right)\left\lVert v \right\rVert\U {H^1\U x},

\end{aligned}$$
</div>

where we used that
$\left\lVert v\U n \right\rVert\U {H^1\U x}= \left\lVert v \right\rVert\U {H^1\U x}- \left\lVert v\U n^\perp \right\rVert\U {H^1\U x} \leq \left\lVert v \right\rVert\U {H^1\U x}$.
We deduce that

<div>
$$\begin{align}  \label{i2}
\left\lVert u\U n'(t) \right\rVert\U {H^{-1}\U x} \lesssim \left\lVert f(t) \right\rVert\U {H\U x^{-1}} + \left\lVert  u\U n(t) \right\rVert\U {H^1\U x}.

\end{align}$$
</div>

Integrating the square over $I$ and using
(\ref{hb})  in
(\ref{i2})  gives


<div>
$$\begin{align}  \label{i3}
\left\lVert u\U n'(t) \right\rVert^2\U {L\U t^2H^{-1}\U x} \lesssim \left\lVert f(t) \right\rVert^2\U {L^2\U t H\U x^{-1}} + \left\lVert g \right\rVert^2\U {L\U x^2}.

\end{align}$$
</div>

Now, combining (\ref{ub})  and (\ref{hb}) , (\ref{i3})  and taking square roots, we obtain the desired bound
(\ref{bound}) .

c)  Uniqueness: To conclude uniqueness, let $u\U n^{{1}}, u\U n^{{2}}$ be
two solutions to the Galerkin problem. Then,
$w\U n := u\U n^{{1}}-u\U n^{{2}}$ verifies the homogeneous problem


<div>
$$\begin{aligned}
\left\langle w\U n',v\right\rangle\U {L^2\U x} + B(w\U n,v;t) = 0, \quad \forall v \in V\U n, \quad \text{and} \quad w\U n(0) = 0.

\end{aligned}$$
</div>

The same reasoning that proved
(\ref{i00}) , where now
$f=0$, shows that

<div>
$$\begin{aligned}
\qty(\left\lVert w\U n(t) \right\rVert\U {L\U x^2}^2)' \lesssim \left\lVert w\U n(t) \right\rVert^2\U {L\U x^2}.

\end{aligned}$$
</div>

Now, applying Grönwall's inequality and by the
initial condition $w\U n(0)=0$, we obtain for some constant $C>0$


<div>
$$\begin{align}  \label{w0}
\left\lVert w\U n(t) \right\rVert\U {L\U x^2} \leq e^{Ct} \left\lVert w\U n(0) \right\rVert\U {L\U x^2} = 0.

\end{align}$$
</div>

This shows that $w\U n=0$ and hence
$u\U n^{{1}}=u\U n^{{2}}$. This proves uniqueness and concludes the
proof.

◻


Having proved the well-posedness of the Galerkin problem, we can now
show that the parabolic problem is well-posed. A common technique in PDE
is to modify your initial problem $P$ by some quantity $\epsilon$ to
obtain a problem $P\U  \epsilon$ that is easier to solve. Suppose one can
find solutions to $P\U  \epsilon$ that are bounded. In that case, a
converging subsequence can typically be extracted and, under appropriate
conditions, will converge to a solution to the original problem $P$.
This is exactly what we show now.


<b>Theorem 5</b> (Well posedness of the parabolic problem). Under
Assumption <a href="#ass">1</a>, the
parabolic problem (\ref{parabolic})  is well-posed. That is, there exists a unique
weak solution $u$, which depends continuously on the initial data with


<div>
$$\begin{align}
\label{bound P}
\left\lVert u \right\rVert\U {C\U t L\U x^2} +\left\lVert u \right\rVert\U {L^2\U tH\U {x}^1} + \left\lVert u' \right\rVert\U {L^2\U tH\U {x}^{-1}} \lesssim\U {\mathbf{A,b},c,T} \left\lVert f \right\rVert\U {L^2\U t H\U x^{-1}}+ \left\lVert g \right\rVert\U {L\U x^2}.

\end{align}$$
</div>





<b>Proof.</b> Let $\left\\{u\U n\right\\}\U {n=1}^\infty$ be the sequence of
solutions to the Galerkin problem
(\ref{galerkin})
guaranteed by Theorem (\ref{galerkin}) . By said theorem, $u\U n$ and $u'\U n$ are bounded
sequences in $L\U t^2H\U {0,x}^1$ and $L\U t^2 H\U x^{-1}$ respectively. Since
these spaces are Hilbert spaces, they are reflexive, and we deduce by
the <a href="https://en.wikipedia.org/wiki/Banach%E2%80%93Alaoglu_theorem">Banach-Alaoglu
theorem</a>
that respective subsequences converge in their respective spaces to some
$u \in L\U tH\U {0,x}^1$ and $\widetilde{u} \in L\U t H\U x^{-1}$. That is,


<div>
$$\begin{aligned}
u= \lim\U {k \to \infty}u\U {n\U k} \in L\U t^2H\U {0,x}^1, \quad \widetilde{u}= \lim\U {k \to \infty}u\U {n\U k} \in L\U t^2 H\U x^{-1}.

\end{aligned}$$
</div>

We first show that $\widetilde{u} = u'$. We have that,
given $\phi \in C\U c^\infty(I \times U)$

<div>
$$\begin{aligned}
(\phi,\widetilde{u}')\lim\U {k \to \infty} \qty(\phi, u\U {n\U k}') & = \lim\U {k \to \infty} \qty(-\phi', u\U {n\U k}) = \qty(-\phi', u) ,

\end{aligned}$$
</div>

where in the first equality we used the weak convergence
of $u'\U {n\U k}$ to $\widetilde{u}$ in $L\U t H\U x^{-1}$, in the second
equality we used the definition of weak derivative, and in the last we
used the convergence of $u\U {n\U k}$ to $u$ in $L\U t^2H\U {0,x}^1$. This shows
that $u' = \widetilde{u}$ almost everywhere. We now show that $u$ solves
the weak problem (\ref{weak}) . By construction of the Galerkin solutions in
(\ref{galerkin})
and integrating over $I$, we deduce for any $v \in \mathcal{S}\U {n\U k}$


<div>
$$\begin{align}
\label{weak k}
(v, u'\U {n\U k})+ (\nabla v, \mathbf{A} \nabla u\U {n\U k}) + (\nabla v, \mathbf{b} u\U {n\U k}) + (v, cu\U {n\U k}) = (v, f).

\end{align}$$
</div>

As a result, taking limits in $k$ shows that, for all
$v \in \mathcal{S}\U n$

<div>
$$\begin{aligned}
(v, u')+ (\nabla v, \mathbf{A} \nabla u) + (\nabla v, \mathbf{b} u) + (v, cu) = (v, f).

\end{aligned}$$
</div>

Since the space $\mathcal{S}\U n$ is dense in
$L\U t^2H\U {0,x}^1$ we deduce that

<div>
$$\begin{aligned}
(v, u')+ (\nabla v, \mathbf{A} \nabla u) + (\nabla v, \mathbf{b} u) + (v, cu) = (v, f), \quad \forall v \in L\U t^2H\U {0,x}^1.

\end{aligned}$$
</div>

We now check that $u(0)=g$. To do so, we now consider
$v \in C^1\U tH\U {0,x}^1 \cap \mathcal{S}\U {n\U k}$ such that $v(T)=0$. Then,
integrating by parts over $I$ and using
(\ref{weak k})  gives


<div>
$$\begin{aligned}
& -(v', u\U {n\U k}) + (\nabla v, \mathbf{A} \nabla u\U {n\U k}) + (\nabla v, \mathbf{b} u\U {n\U k}) + (v, cu\U {n\U k}) \\&= (v, f)+  \left\langle v(0),g\right\rangle\U {L\U x^2}=(v, f)+  \left\langle v(0),u\U {n\U k}(0)\right\rangle\U {L\U x^2}.

\end{aligned}$$
</div>

Taking limits above and by density of $\mathcal{S}\U n$ in
$C\U t^2H\U {0,x}^1$ we obtain that

<div>
$$\begin{aligned}
\left\langle v(0),g\right\rangle\U {L\U x^2} = \left\langle v(0),u(0)\right\rangle\U {L\U x^2}, \quad \forall v \in C\U t^2H\U {0,x}^1.

\end{aligned}$$
</div>

where we used that by Lemma
<a href="#continuity weak">3</a>
$u\U {n\U k} \to u \in C\U t L\U x^2$. In particular,

<div>
$$\begin{aligned}
\left\langle w,g\right\rangle\U {L\U x^2} = \left\langle w,u(0)\right\rangle\U {L\U x^2}, \quad \forall w \in H\U {0,x}^1.

\end{aligned}$$
</div>

Since $H\U {0,x}^1$ is dense in $L\U x^2$ this shows that
$u(0)=g$ and concludes the proof. ◻



<b>Observation 1</b>. It may seem like the conclusion is impossible. After
all, we did not impose that $\left.g\right|\U {U}=0$. So how can we hope
that for $u(t)$ to be $0$ on $\partial U$ if $u(0)=g$? The solution lies
in the fact that $u \in C\U t L\U {x}^2 \cap L\U t^2H\U {0,x}^1$, but it may not
hold that $u \in C\U tH\U {0,x}^1$. As a result, we only know that
$u(t) \in H\U 0^1(U)$ for almost every $t$. And it is not required that
$u(t) \in H\U 0^1(U)$ for $t=0$.


# Numerical illustrations

In this section, we show some numerical illustrations of the
well-posedness of the parabolic problem. The code to calculate the
numerical solutions and generate the figures using Mathematica can be
found [here](/assets/code/PDEs/Galerkin_solutions.nb). We first consider
the problem

<div>
$$\begin{align}
\label{parabolic 2}
\begin{cases}
\partial\U t u - \Delta u + \cos(x) \nabla u + \sin(x) =1 & \text{in } I\times U      \\
u(0) = 1         & \text{on } U          \\
u = 0          & \text{on } I\times \partial U.
\end{cases}
\end{align}$$
</div>

where we take $U=(0,2\pi)$ and $I=(0,1)$. We use the
Galerkin method and set as basis functions the normalized eigenfunctions
of the Laplacian with zero boundary conditions on $U$,

<div>
$$\begin{aligned}
\phi\U j(x) = \frac{1}{\sqrt{\pi } } \sin(\frac{ j x}{2}), \quad j \in \mathbb{N}.
\end{aligned}$$
</div>

We show solutions for $n=3$ and $n=20$; as we can see,
as the number of basis functions increases, the solution converges to
$1$ when $t=0$ and becomes quite oscillatory at the boundary to try to
adapt to the admittedly somewhat incompatible boundary conditions.

![Galerkin solution to the parabolic problem (\ref{parabolic 2})  with $n=3$ basis
functions](Galerkin_n_3.pdf){width="80%"}

![Galerkin solution to the parabolic problem (\ref{parabolic 2})  with $n=20$ basis
functions](Galerkin_n_20.pdf){width="80%"}

We also include a figure to show how the boundary condition $g=1$ may be
approximated in $H\U 0^1(U)$ using the basis functions $\phi\U j$. We note
that the approximating sequence does not converge $H\U 0^1$ as the
derivative explodes at the boundary.

<img src="{{'assets/img/Figures/approx_boundary_l2.svg'| relative_url }}" alt="Approximation of g=1 in L^2(U) using the basis functions \phi_j \in H_0^1(U)" width="90%" id="width="80%"">

Next, we show a case where the exact solution can be calculated. We take
$U=(0,1)$ and $I=(0,1)$ and consider the problem

<div>
$$\begin{align}
\label{exact}
\begin{cases}
\partial\U t u - \Delta u + \nabla u + 1 =(-1 + x) x + t (-3 + x + x^2) & \text{in } I\times U      \\
u(0) = 1         & \text{on } U          \\
u = 0          & \text{on } I\times \partial U,
\end{cases}
\end{align}$$
</div>

The exact solution to
(\ref{exact})  is
$u(t,x) = t(x - 1)x$. We show the exact solution and the Galerkin
solution using

<div>
$$\begin{aligned}
\phi\U j(x) = \sqrt{2} \sin(\pi j x), \quad j \in \mathbb{N}.
\end{aligned}$$
</div>

as before for $n=20$ basis functions. As we can see, the
Galerkin solution and the exact solution are quite close.

![Exact solution to the parabolic problem (\ref{exact}) ](Galerkin_exact.pdf){width="80%"}

![Galerkin solution to the parabolic problem (\ref{exact})  with
$n=20$ basis functions](Galerkin_n_20_2.pdf){width="80%"}

# Regularity of the solutions

Having proved the well-posedness of the parabolic problem
(\ref{parabolic})  and its finite-dimensional Galerkin
approximation, we can now move on to study the regularity of the
solutions. The proof is similar to the one given in the <a href="https://nowheredifferentiable.com/2024-02-28-PDEs-6-Elliptic_PDE._Well_posedness_and_regularity/">elliptic
case</a>
but more technical, and we will mainly cite some main results without
proof.

As one expects from the elliptic case, the spatial regularity of the
solutions is increased by $2$. Our study of the previous section shows
that the regularity of the time derivatives of the solution is $2$
orders lower. In fact, it is two orders lower for each time derivative
taken. To be able to obtain higher regularity however, we will need to
impose some compatibility between the boundary condition $f$ and the
initial data $g$. The following can be found in Section 7.13 of
<a href="https://math24.files.wordpress.com/2013/02/partial-differential-equations-by-evans.pdf">Evans, 2022</a>


<b>Theorem 6</b>. Let $\Omega$ be a bounded domain with smooth boundary
$\partial \Omega$. Let $\mathcal{L}$ be the elliptic operator in
(\ref{elliptic operator})  and assume that the coefficients
$\mathbf{A,b},c$ are independent of time $t$ and smooth in space. Suppose
that

<div>
$$\begin{aligned}
g \in H^{2 k+1}\U x,\quad \text{and} \quad  \frac{\partial ^m f}{\partial t^m} \in L^2\U tH\U x^{2 k-2 m} \quad \text{for } m=0,...,k,

\end{aligned}$$
</div>

and the compatibility conditions

<div>
$$\begin{aligned}
g\U 0:=g \in H\U {x,0}^1 \quad g\U 1:=f(0)-\mathcal{L}g\U 0 \in H\U {x,0}^1 \quad \ldots\quad g\U j:=\frac{\partial ^{m-1} f}{\partial t^{m-1}}(0)-\mathcal{L}g\U {m-1} \in H\U {x,0}^1

\end{aligned}$$
</div>

are satisfied. Then,

<div>
$$\begin{aligned}
\frac{\partial ^m u}{\partial t^m} \in L^2\U tH\U x^{2 k+2-2 m} \quad \text{for } m=0,...,k+1,

\end{aligned}$$
</div>

and we have the estimate

<div>
$$\begin{aligned}
\sum\U {m=0}^{k+1} \left\lVert \frac{\partial^m u}{\partial t^m} \right\rVert\U {L^2\U tH\U x^{2 k+2-2 m}}\lesssim \sum\U {m=0}^k \left\lVert \frac{\partial ^m f}{\partial t^m} \right\rVert\U {L^2\U tH\U x^{2 k-2 m}}+\left\lVert g \right\rVert\U {H\U x^{2 k+1}}.

\end{aligned}$$
</div>

In consequence, if
$f \in C^\infty\U {t,x}, g \in C^\infty\U x$ then $u \in C^\infty\U {t,x}$.


We also show a result where the coefficients are allowed to depend on
time. The following can be found in Chapter $3$ of
<a href="https://api.semanticscholar.org/CorpusID:117905500">Friedman, 1983</a> and assumes that the coefficients are <a href="https://nowheredifferentiable.com/2023-07-12-PDEs-3-Sobolev_spaces/#:~:text=%2C%20we-,define,-the%20Holder%20space">Hölder
continuous</a>


<b>Theorem 7</b>. Let $\Omega$ be a bounded domain with smooth boundary
and assume that for all $t \in I$,
$A\U {ij}(t),b\U j(t), c\U j(t) \in C^{k, \alpha}(\Omega )$. If $u$ is a
classical solution of $\mathcal{L}u=f$, then
$u(t) \in C^{k+2,\alpha}(\Omega ), u'(t) \in C^{k, \alpha}(\Omega )$ for
all $t \in I$. In consequence, if
$f \in C^\infty\U {t,x}, g \in C^\infty\U x$ then $u \in C^\infty\U {t,x}$.


# Conclusions

This ends our study of parabolic partial differential equations. With
it, we bring this series on linear PDEs to a, at least momentary, end.
We began our study with the Fourier transform, then ventured into the
thick jungle of distributions, emerging into the open plains of Sobolev
spaces. There, we lingered, marveling at its vast expanse and many
corners---
layout: post
title: Parabolic PDE. Well posedness and regularity
subtitle: A journey through time and space
thumbnail-img: /assets/img/Evans_PDE.jpg
share-img: /assets/img/Evans_PDE.jpg
tags: [PDEs]
authorpost: L.Llamazares-Elias
---and there are many to choose from---such as the nature of
probability, Bayesian inference, and stochastic partial differential
equations. The road ahead is filled with possibilities, and I hope
you'll join us for this next leg of our journey.

A (possibly not updated) pdf version of this page is provided [here](/assets/pdfs/PDEs/Parabolic.pdf).