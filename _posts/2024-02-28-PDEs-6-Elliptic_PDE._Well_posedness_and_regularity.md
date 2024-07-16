---
layout: post
title: Elliptic PDE. Well posedness and regularity
subtitle: From Rough Beginnings to Smooth Endings
thumbnail-img: /assets/img/Evans_PDE.jpg
share-img: /assets/img/Evans_PDE.jpg
tags: [PDEs]
authorpost: L.Llamazares-Elias
---

#  Three point summary

-   Elliptic partial differential equations (PDE) are PDE with no time
variable and whose leading order derivatives satisfy a positivity
condition.

-   Using Lax Milgram's theorem, we can prove the existence and
uniqueness of weak (distributional) solutions if the reaction term
dominates the transport term. Using the Fredholm alternative, we can
characterize the spectrum of the elliptic operator and the existence
of solutions.

-   Under suitable smoothness assumptions on the coefficients and
domain, the solution map of the PDE adds two derivatives to the
input function. This improved regularity allows us to recover
classical solutions if the coefficients are smooth enough.

# Why should I care?

Many problems arising in physics, such as the Laplace and Poisson
equation, are elliptic PDE. Furthermore, the tools used to analyze them
can be extrapolated to other settings, such as parabolic PDE (depending
on your viewpoint this may be a bit circular). The analysis also helps
contextualize and provide motivation for theoretical tools such as
Hilbert spaces, compact operators and Fredholm operators.

# Notation

We will use Vinogradov notation $f \lesssim g$ to mean that there exists
a constant $C>0$ such that $f \leq Cg$. If we want to emphasize that the
constant depends on a parameter $\alpha$, we will write
$f \lesssim\U \alpha g$.

We fix $U \subset \mathbb{R}^d$ to be an open subset of $\mathbb{R}^n$
with <b>no conditions</b> on the regularity of $\partial U$. If we need to
impose regularity on the boundary, we will write $\Omega$ instead of
$U$. Finally, we will write

<div>
$$\begin{aligned}
\nabla \cdot (\mathbf{A}\nabla)=\sum\U {i,j=1}^d \partial\U i A\U {ij} \partial \U j.
\end{aligned}$$
</div>



# Introduction

Welcome back to the second post on our series of PDE. In post
<a href="https://nowheredifferentiable.com/2023-12-23-PDEs-4-Physical_derivation_of_parabolic_and_elliptic_PDE/">4</a>,
we gave a physical derivation of PDE (both parabolic and elliptic) that
justify why we are interested in such equations. In posts
<a href="https://nowheredifferentiable.com/2023-01-29-PDE-1/">1</a>,
<a href="https://nowheredifferentiable.com/2023-05-30-PDE-2-Hilbert/">2</a>,
<a href="https://nowheredifferentiable.com/2023-07-12-PDEs-3-Sobolev_spaces/">3</a>,
<a href="https://nowheredifferentiable.com/2024-02-27-PDEs-5-Fractional_Sobolev_spaces/">5</a>
of the series we built up the theoretical framework necessary to define
Sobolev spaces, spaces of weakly differentiable functions to which we
could extend the concept of differentiation (I know, the order is a bit
messed up). We are now going to use the previous theory to study these
equations.

# The problem: Mathematical framework

We consider the following problem: given a bounded open set
$U \subset \mathbb{R}^n$ and some coefficients $\mathbf{A},\mathbf{b},c$, we
want to solve the following elliptic PDE

<div>
$$\begin{align}
\label{PDE}
\begin{cases}
\mathcal{L}u:=  -\nabla \cdot (\mathbf{A} \nabla u)+ \nabla \cdot (\mathbf{b} u)+cu=f, & \text{in } U,          \\
u=0,                                                                    & \text{on } \partial U,
\end{cases}
\end{align}$$
</div>

where $f: U \to \mathbb{R}$ is some known function, $u$
is the solution we want to find. In the case where $U = \mathbb{R}^d$
the boundary condition is vacuous as
$\partial \mathbb{R}^d = \emptyset$.

We recall from post
<a href="https://nowheredifferentiable.com/2023-12-23-PDEs-4-Physical_derivation_of_parabolic_and_elliptic_PDE/">4</a>
that physically; we can interpret $u$ as the density of some substance,
$\mathbf{A}$ as a diffusion matrix, $\mathbf{b}$ as a transport vector, $c$ as a
reaction coefficient and $f$ as the source term. For the mathematical
theory, we will need some conditions on the coefficients. Primarily, we
require that $\mathbf{A}$ is elliptic.


<b>Definition 1</b> (Ellipticity). Given
$\mathbf{A}: U \to \mathbb{R}^{d \times d}, \mathbf{b}: U \to \mathbb{R}^d$ and
$c:U \to \mathbb{R}$ we say that the operator

<div>
$$\begin{align}
\label{operator}
\mathcal{L}u:= -\nabla \cdot (\mathbf{A} \nabla u)+ \nabla \cdot (\mathbf{b} u)+c
\end{align}$$
</div>

is elliptic if there exists $\alpha>0$ such that


<div>
$$\begin{align}
\label{elliptic}
\xi ^T\mathbf{A}(x) \xi \geq \alpha \left| \xi  \right|^2 , \quad\forall \xi \in \mathbb{R}^d , \quad\forall x \in U .

\end{align}$$
</div>

We also say that $\mathbf{A}$ is elliptic.


There are some points to clear up. Firstly, if this is the first time
you've encountered the ellipticity condition in
(\ref{elliptic}) ,
then it may seem a bit strange. With the previous physical
interpretation, the ellipticity condition
(\ref{elliptic})
says that diffusion occurs from the region of <a href="https://nowheredifferentiable.com/2023-12-23-PDEs-4-Physical_derivation_of_parabolic_and_elliptic_PDE/#:~:text=This%20is%20the-,process,-that%20causes%20the">higher to lower
density</a>.
Mathematically speaking,
(\ref{elliptic})
will prove necessary to apply <a href="https://nowheredifferentiable.com/2023-05-30-PDE-2-Hilbert/#:~:text=degenerate.%20As%20a-,particular,-example%2C%20a%20symmetric">Lax Milgram's
theorem</a>
and obtain regularity estimates on $u$.

Next, when developing the mathematical theory of any equation, the first
step is to establish whether the equation is well-posed.


<b>Definition 2</b> (Well-posedness). We say that an equation is
well-posed if

1.  It has a solution.

2.  The solution is unique.

3.  The solution depends continuously on the data.


The above definition originates from the work of Hadamard and is
standard in the context of PDE. The three properties above make the
problem nice to work with and may be familiar from the basic theory of
ODE. However, not all problems are well-posed. Ill-posedness often
arises when one works with inverse problems, such as the backward heat
equation, where one tries to recover the initial heat distribution from
the final one.

The well-posedness of any given PDE is highly contingent on the space
considered. In our case, we still need to define which function space
our coefficients $\mathbf{A,b},c$ live in and what space $\mathcal{L}$ acts
on. It would be natural to assume that we need $\mathbf{A}$ and $\mathbf{b}$ to
be differentiable. However, the following will suffice.

 <a name="Ass1">
<b>Assumption 1</b> </a> . We assume that $A\U {ij}, b\U i, c \in L^\infty (U)$ for
all $i,j=1,\ldots,d$. Furthermore, $\mathbf{A}$ is symmetric
($A\U {ij}=A\U {ji}$) and elliptic.


In the future, $i,j$ will always run from $1$ to $d$, where $d$ is the
dimension of the space.


<b>Observation 1</b>. We lose no generality by assuming that $\mathbf{A}$ is
symmetric as $\partial \U {ij} u =\partial \U {ji} u$. If $\mathbf{A}$ is not
symmetric, we can replace $\mathbf{A}$ by $(\mathbf{A}+\mathbf{A}^T)/2$ and equation
(\ref{PDE})  will remain
unchanged.


The first part of Assumption <a href="#Ass1">1</a> will make it easy to get bounds on $\mathcal{L}$, and
the second part will prove useful when we look at the spectral theory of
$\mathcal{L}$. Now, to make sense of our problem
(\ref{PDE}) , we need to
define what we mean by a solution. Here, the theory of Sobolev Spaces
and the Fourier transform prove crucial. We will work with the following
space.

 <a name="dual definition 2">
<b>Definition 3</b> </a>  (Negative Sobolev space). Given $k \in \mathbb{N}$ we
define

<div>
$$\begin{aligned}
H^{-k}(U ):= H\U 0^k(U )'

\end{aligned}$$
</div>




For more details on why we denote the dual using negative exponents, see
the <a href="https://nowheredifferentiable.com/2024-02-27-PDEs-5-Fractional_Sobolev_spaces/#fractional%20laplacian:~:text=%E2%97%BB-,Dual%20of%20Sobolev%20spaces,-and%20correspondence%20with">relevant
section</a>
in the previous post on fractional Sobolev spaces. We
<a href="https://nowheredifferentiable.com/2024-02-27-PDEs-5-Fractional_Sobolev_spaces/#:~:text=some%20particular%20cases.-,Theorem%2018,-(Representation%20of">recall</a>
also that every element in $H^{-k}(U)$ can be written as the sum of
derivatives up to order $k$ of a function in $L^2(U)$.

 <a name="domain L">
<b>Exercise 1</b> </a> . Suppose $A\U {ij}, b\U i, c \in L^\infty(U)$. Then,
$\mathcal{L}$ defines a bounded linear operator

<div>
$$\begin{aligned}
\mathcal{L}: H\U 0^{1}(U)\to H^{-1} (U).

\end{aligned}$$
</div>




<div class="exercise-container">
<button class="exercise-button" onclick="toggleExercise(this)">Hint</button>
<div class="exercise-text">
By definition of the weak derivative, show that given
$v \in C\U c^\infty(U)$,

<div>
$$\begin{aligned}
(v, \mathcal{L}u) = \int\U {U} \mathbf{A} \nabla v \cdot \nabla u + \int\U {U} \mathbf{b} \cdot \nabla v u + \int\U {U} cvu.

\end{aligned}$$
</div>

Use this to conclude that,

<div>
$$\begin{aligned}
\left| (v, \mathcal{L}u) \right| \lesssim \left\lVert v \right\rVert\U {H^1(U)}\left\lVert u \right\rVert\U {H^1(U)}.

\end{aligned}$$
</div>

So, $\mathcal{L}u \in H^{-1}(U)$ is well defined and
$\mathcal{L}$ is bounded. Extend by density to $H\U 0^1(U)$.
</div>
</div>

Exercise <a href="#domain L">1</a>
allows us to define the weak formulation of
(\ref{PDE})  and study its
well-posedness using Lax Milgram's theorem. We will do this in the next
section.

# Weak solutions and well-posedness

By Exercise <a href="#domain L">1</a>,
we can make sense of the equation $\mathcal{L}u =f$ for all
$f \in H^{-1}(U)$.


<b>Definition 4</b> (Weak formulation). Given $f \in H^{-1}(U)$, we say
that $u~\in~H\U 0^1(U)$ solves equation
(\ref{PDE})  if


<div>
$$\begin{align}
\label{weak def}
B(u,v):= (v, \mathcal{L}u)=\int\U {U}\mathbf{A} \nabla u \cdot \nabla v + \int\U {U} \mathbf{b} \cdot ( \nabla u) v + \int\U {U} cuv= (v,f), \quad \forall v \in H\U 0^1(U).

\end{align}$$
</div>




In (\ref{weak def})  we used the "duality notation" $(v,f):= f(v)$ for
$f \in X, v \in X'$ (here $X= H\U 0^1(U)$). We have now reformulated our
problem to something that looks very similar to the setup of Lax
Milgram's theorem and can use this to prove the well-posedness of
(\ref{PDE})  under certain
conditions.

 <a name="well-posed 1">
<b>Theorem 5</b> </a> . Let $U \subset \mathbb{R}^d$ be an arbitrary open set.
Suppose Assumption <a href="#Ass1">1</a>
holds and let $\mathbf{b}=0$ . Then, equation
(\ref{PDE})  is well-posed,
and we have the homeomorphism

<div>
$$\begin{aligned}
\mathcal{L}: H\U 0^1(U) \xrightarrow{\sim}H^{-1}(U).

\end{aligned}$$
</div>

If $U$ is bounded, the above also holds for $c\geq 0$.



<b>Proof.</b> The continuity of $B$ is a consequence of Exercise
<a href="#domain L">1</a>. It remains to
see that $B$ is coercive. For smooth $u \in C\U c^\infty(U)$ we have that


<div>
$$\begin{align}
\label{b=0}
B(u,u) & = \int\U {U}\mathbf{A} \nabla u \cdot \nabla u + \int\U {U} cu^2 \geq \alpha \left\lVert \nabla u \right\rVert^2\U {L^2(U \to \mathbb{R}^d)} + \int\U {U}c u^2 \gtrsim \left\lVert u \right\rVert^2\U {H^1\U 0(U)}.

\end{align}$$
</div>

Where in the first inequality, we used the ellipticity
assumption on $\mathbf{A}$, and in the last inequality, we used <a href="https://nowheredifferentiable.com/2023-07-12-PDEs-3-Sobolev_spaces/#:~:text=in%20future%20posts-,Theorem,-14%20(Poincar%C3%A9%20inequality">Poincaré's
inequality</a>
if $U$ is bounded. The result now follows from <a href="https://nowheredifferentiable.com/2023-05-30-PDE-2-Hilbert/#:~:text=an%20inner%20product.-,Theorem,-7%20(Lax%20Milgram">Lax Milgram's
theorem</a>. ◻


Theorem <a href="#well-posed 1">5</a> is an example of the advantages of working
with a weak formulation instead of solutions differentiable in a
classical sense. The weak formulation allows us not only to make sense
of our equation (\ref{PDE})
for a wider class of coefficients but also provides a natural framework
to study the well-posedness of (\ref{PDE}) .


<b>Exercise 2</b>. Show that, under the conditions of Theorem
<a href="#well-posed 1">5</a>, if
$U$ is bounded, there is a countable basis of eigenfunctions for
$\mathcal{L}$.


<div class="exercise-container">
<button class="exercise-button" onclick="toggleExercise(this)">Hint</button>
<div class="exercise-text">
By <a href="https://nowheredifferentiable.com/2023-07-12-PDEs-3-Sobolev_spaces/#:~:text=Theorem%2014%20(-,Rellich,-for%20trace%200">Rellich's
theorem</a>
$\mathcal{L}^{-1}: L^2(U) \to L^2(U)$ is compact and, since $\mathbf{b}$ is
$0$, $\mathcal{L}$ is also is self adjoint. As a result, so there is a
countable basis of eigenvectors in $L^2(U)$.
</div>
</div>

In Theorem <a href="#well-posed 1">5</a>, we somewhat unsatisfyingly had to impose the
extra assumption that $\mathbf{b}$ was identically zero and that $c > 0$.
These extra assumptions can be done away with but at the cost of
modifying our initial problem by a correction term $\gamma$ so we can
obtain a coercive operator $B\U \gamma$.

 <a name="mod">
<b>Theorem 6</b> </a>  (Modified problem). Let $U \subset \mathbb{R}^d$ be any
open set and let Assumption <a href="#Ass1">1</a> hold. Then, there exists some constant $\nu \geq 0$
(depending on the coefficients) such that for all $\gamma \geq \nu$ the
operator $\mathcal{L}\U \gamma := \mathcal{L}+ \gamma \mathbf{I}$ is positive
definite and defines a homeomorphism

<div>
$$\begin{aligned}
\mathcal{L}\U \gamma : H\U 0^1(U) \xrightarrow{\sim}H^{-1}(U).

\end{aligned}$$
</div>




That is, the problem $\mathcal{L}u +\gamma u =f$ is well-posed for all
$\gamma > \nu$.


<b>Proof.</b> Once more, the proof will go through the Lax-Milgram theorem,
where now we work with the bilinear operator $B\U \gamma$ associated with
$\mathcal{L}\U \gamma$

<div>
$$\begin{aligned}
B\U \gamma (u,v):= (u, \mathcal{L}\U \gamma u)=B(u,v) + \gamma (u,v).

\end{aligned}$$
</div>

The calculation proceeds similarly to
(\ref{b=0}) . We recall the
Cauchy inequality

<div>
$$\begin{align}
\label{Cauchy}
ab\leq\frac{\varepsilon }{2} a^2+ \frac{1}{2 \varepsilon } b^2 , \quad\forall a,b \in \mathbb{R}, \quad \varepsilon >0,

\end{align}$$
</div>

which can be checked directly by using that
$(c-d)^2 \geq 0$. Applying (\ref{Cauchy})  to $a=\nabla u$ and $b= v$, shows that


<div>
$$\begin{aligned}
B(u,u) & = \int\U {U}(\mathbf{A} \nabla u) \cdot \nabla u + \int\U {U} \mathbf{b}\cdot (\nabla u) u + \int\U {U} cu^2 \geq \alpha \left\lVert \nabla u \right\rVert^2\U {L^2(U \to \mathbb{R}^d)}                          \\
& - \frac{1}{2}\left\lVert \mathbf{b} \right\rVert\U {L^\infty(U)} \left(\varepsilon \left\lVert \nabla u \right\rVert\U {L^2(U)}^2+ \varepsilon ^{-1}\left\lVert u \right\rVert^2\U {L^2(U)}\right)- \left\lVert c \right\rVert\U {L^\infty(U)}\left\lVert u \right\rVert^2\U {L^2(U)} .

\end{aligned}$$
</div>

Taking $\varepsilon$ small enough (smaller than
$\alpha \left\lVert \mathbf{b} \right\rVert\U {L^\infty(U)}^{-1}$ to be
precise) and gathering up terms gives

<div>
$$\begin{align}
\label{b not 0}
B(u,u) \geq \frac{\alpha}{2} \left\lVert \nabla u \right\rVert^2\U {L^2(U \to \mathbb{R}^d)} -\nu \left\lVert u \right\rVert^2\U {L^2(U)}.

\end{align}$$
</div>

Where we defined
$\nu = \left\lVert \mathbf{b} \right\rVert\U {L^\infty(U)} \varepsilon ^{-1}+\left\lVert c \right\rVert\U {L^\infty(U)}$.
The theorem follows from (\ref{b not 0})  as for all $\gamma > \nu$

<div>
$$\begin{align}
\label{pd}
B\U \gamma (u,u)=B(u,u)+ \gamma \left\lVert u \right\rVert^2\U {L^2(U)} \geq\frac{\alpha}{2} \left\lVert \nabla u \right\rVert^2\U {L^2(U \to \mathbb{R}^d)}+(\gamma - \nu) \left\lVert u \right\rVert^2\U {L^2(U)}\gtrsim \left\lVert u \right\rVert^2\U {H\U 0^1(U)} .

\end{align}$$
</div>

Equation (\ref{pd})  also shows that $\mathcal{L}\U \gamma$ is positive
definite and the proof is complete. ◻


## Fredholm alternative

We now analyze further what we can say about the well-posedness of
(\ref{PDE}) . What has to
happen for the equation to be ill-posed? If there are multiple
solutions, what does the space of solutions look like? As we will see,
this is intimately linked to the spectrum of the operator $\mathcal{L}$
and the Fredholm alternative will provide the answers we are looking
for,

We begin by considering $\mathcal{L}u =\lambda u+f$, which is a small
generalization of our original problem
(\ref{PDE}) . We take
$\gamma > \left| \lambda  \right|$ large enough as in Theorem
<a href="#mod">6</a> and note that


<div>
$$\begin{align}
\label{above}
\mathcal{L}u = \lambda u + f \iff \mathcal{L}\U \gamma u =(\gamma+\lambda)u +f.
\end{align}$$
</div>

Now write $\mu:=(\gamma+\lambda)$ and rename
$v:=\mu u +f$. An algebraic manipulation shows that
(\ref{above})  is
equivalent to

<div>
$$\begin{align}
\label{below}
(\mathbf{I}- \mu \mathcal{L}\U \gamma ^{-1} )v =f,
\end{align}$$
</div>

where $\mathbf{I}$ is the identity operator. Suppose now
that $U$ is bounded, then, by <a href="https://nowheredifferentiable.com/2023-07-12-PDEs-3-Sobolev_spaces/#:~:text=Theorem%2014%20(-,Rellich,-for%20trace%200">Rellich's
theorem</a>,
we know that the following inclusion is compact

<div>
$$\begin{aligned}
i: H^1(U) \hookrightarrow L^2(U).
\end{aligned}$$
</div>

As a result, by Theorem
<a href="#well-posed 1">5</a>, we
deduce that $\mathcal{L}\U \gamma^{-1}: L^2(U) \to L^2(U)$, which we are
now viewing as an operator on $L^2(U)$, is compact. More precisely,


<div>
$$\begin{aligned}
K:= i \circ \left.\mathcal{L}\U \gamma ^{-1}\right|\U {L^2(U)}
\end{aligned}$$
</div>

is compact and the reasoning in
(\ref{above}) ,
(\ref{below})  shows
that, given $f \in L^2(U)$, and $u \in H\U 0^1(U)$

<div>
$$\begin{align}
\label{reasoning}
\mathcal{L}u = \lambda u+f\iff Tv:=(\mathbf{I}-\mu K)v =f.
\end{align}$$
</div>

Equation
(\ref{reasoning})  is exactly the form the <a href="https://nowheredifferentiable.com/2023-05-30-PDE-2-Hilbert/#:~:text=Theorem%2010%20(-,Fredholm,-alternative">Fredholm
alternative</a>
takes ($\mu$ can be incorporated into the compact operator $K$) and
justifies the following.

 <a name="well-posedness Fredholm">
<b>Theorem 7</b> </a> . Let $U\subset \mathbb{R}^d$ be bounded, let
$\mathcal{L}$ verify Assumption <a href="#Ass1">1</a>, and $\lambda \in \mathbb{R}, f \in L^2(U)$ be any.
Consider the problems

<div>
$$\begin{align}
\label{original}
\mathcal{L}u & = \lambda u + f \quad \text{and} \quad u \in H\U 0^1(U)                            \\
\mathcal{L}u & = \lambda u \quad \hspace{17pt}\text{and} \quad u \in H\U 0^1(U) \label{originalh}

\end{align}$$
</div>

Then, the following hold:

1.  Equation (\ref{original})  is well-posed if and only if
(\ref{originalh})  has no non-zero solutions. That is, if and
only if $\lambda \notin \sigma(\mathcal{L})$.

2.  The spectrum $\sigma (\mathcal{L})$ is discrete. If
$\sigma(\mathcal{L})= \\{\lambda\U n \\}\U {n=1}^\infty$ is infinite, then
$\lambda \U n \to +\infty$.

3.  The dimensions of the following spaces are equal

<div>
$$\begin{aligned}
N:= \left\{u \in H\U 0^1(U): \mathcal{L}u = \lambda u\right\}, \quad N^\star := \left\{w \in L^2(U): \mathcal{L}^\star  w = \lambda w\right\},

\end{aligned}$$
</div>



4.  Equation, (\ref{original})  has a solution if and only if
$f \in (N^\star )^\perp$ $($equivalently
$\left\langle w,f\right\rangle=0$ for all $w \in N^\star  )$.



<b>Proof.</b> Given $f \in L^2(U)$ and $\lambda \in \mathbb{R}$ as before, we
consider $\gamma > \left| \lambda  \right|$ large and define


<div>
$$\begin{aligned}
\mathcal{L}\U \gamma := \mathcal{L}+ \gamma \mathbf{I}, \quad  K:= i \circ \left.\mathcal{L}\U \gamma ^{-1}\right|\U {L^2(U)}, \quad  \mu := \gamma + \lambda, \quad T := (\mathbf{I}- \mu K)

\end{aligned}$$
</div>

, where $i : H^1(U) \hookrightarrow L^2(U)$ is the
inclusion. Consider the following two problems,

<div>
$$\begin{align}
\label{fred}
Tv & = f  \quad \text{and} \quad  v \in L^2(U),              \\
Tv & = 0 \quad \text{and} \quad  v \in L^2(U). \label{fredh}

\end{align}$$
</div>

The reasoning in
(\ref{reasoning})  showed that a solution $u$ to
(\ref{original})
gives a solution to (\ref{fred})  via the transformation $v=\mu u +f$. The converse
needs to be clarified, as given $v \in L^2(U)$, the inverse
transformation $u = \mu ^{-1}(v-f)$ may not return a function in
$H\U 0^1(U)$. However, if $v$ solves
(\ref{fred}) , then $u$
verifies

<div>
$$\begin{aligned}
Tv=v-\mu K v=\mu u +f - \mu K v=f.

\end{aligned}$$
</div>

Cancelling out the $f$ and dividing by $\mu$ we obtain
that

<div>
$$\begin{aligned}
u =Kv.

\end{aligned}$$
</div>

By Theorem <a href="#well-posed 1">5</a> we know that
$Kv = \mathcal{L}\U \gamma ^{-1} v \in H\U 0^1(U)$ for all $v \in L^2(U)$ .
As a result, $u$ solves problem
(\ref{original}) ,
and by the transformation $v \leftrightarrow u$ problem
(\ref{fred})  has a
solution if and only if problem
(\ref{original})
has a solution. Taking $f=0$, we also obtain that $u$ solves problem
(\ref{originalh})  if and only $v$ solves problem
(\ref{fredh}) . In
conclusion,

<div>
$$\begin{aligned}
\eqref{original} \text{ is } \mathrm{w.p} \iff \eqref{fred} \text{ is } \mathrm{w.p} \iff \mathrm{ker}(T) =0 \iff \mathrm{ker}(\mathcal{L}-\lambda \mathbf{I} )=0,

\end{aligned}$$
</div>

where the second equivalence is due to the Fredholm
alternative, and the third can be verified by an algebraic manipulation.
This proves the first point.

To see the second point, note that, by definition of $T$, equation
(\ref{fredh})  has
non-zero solutions if and only if $\mu ^{-1} \in \sigma (K)$. Since $K$
is compact, $\sigma(K)$ is discrete and if $\sigma (K)$ is infinite,
then its eigenvalues, which we denote by
$\left\\{\mu \U n^{-1}\right\\}\U {n=1}^\infty$, go to $0$. Furthermore, since
by Theorem <a href="#mod">6</a> $K$ is
positive definite, $\mu\U n >0$ and the claim follows by the
correspondence $\lambda\U n =\mu\U n -\gamma$.

For the third and fourth points, we use that, as we have already proved,
$\mathrm{ker}(T)=N$. Additionally,

<div>
$$\begin{aligned}
T^\star  =(\mathbf{I}-\mu K^\star ) =\mathbf{I}-\mu (\mathcal{L}^\star + \gamma )^{-1},

\end{aligned}$$
</div>

from where

<div>
$$\begin{aligned}
\quad \mathrm{ker}(T^\star )=\mathrm{ker}(\mathcal{L}^\star  -\lambda \mathbf{I})= N^\star .

\end{aligned}$$
</div>

Applying the Fredholm alternative concludes the proof. ◻


Setting $\lambda =0$ in Theorem
<a href="#well-posedness Fredholm">7</a>, we recover our original problem
and obtain the following corollary.


<b>Corollary 8</b>. Equation (\ref{PDE})  is well-posed unless the homogeneous problem
$\mathcal{L}u=0$ has a non-zero solution (that is,
$\mathrm{ker}(\mathcal{L})\neq 0$). The space of solutions then has
dimension $\mathrm{ker}(\mathcal{L})$, which is also equal to the
dimension of $\mathrm{ker}(\mathcal{L}^\star )$. Finally,
(\ref{PDE})  will have a
solution if and only if $f$ is orthogonal to the kernel of
$\mathcal{L}^\star $.


In particular, to study the existence of solutions to
(\ref{PDE}) , it is enough to
study the uniqueness of solutions to
(\ref{PDE}) !


<b>Exercise 3</b>. In Theorem
<a href="#well-posedness Fredholm">7</a> we used that, for $\gamma$ large
enough, $K= \mathcal{L}\U {\gamma }^{-1}$ is compact. However,
$\mathcal{L}\U {\gamma }^{-1}$ is invertible with inverse
$\mathcal{L}\U \gamma$. As a result
$\mathbf{I}=\mathcal{L}\U \gamma \circ \mathcal{L}\U \gamma ^{-1}$ is compact.
How is this possible?


<div class="exercise-container">
<button class="exercise-button" onclick="toggleExercise(this)">Hint</button>
<div class="exercise-text">
In fact, $\mathcal{L}\U \gamma^{-1}$ is only invertible as an
operator from $H^{-1}(U) \to H^1\U 0(U)$. However, it is not invertible as
an operator from $K: L^2(U) \to L^2(U)$. Given $f \in L^2(U)$, it is not
generally possible to find an $u \in L^2(U)$ such that
$\mathcal{L}\U \gamma u =f$.
</div>
</div>


<b>Exercise 4</b>. Where does the proof of Theorem
<a href="#well-posedness Fredholm">7</a> break down if we replace $U$ with
$\mathbb{R}^d$?


<div class="exercise-container">
<button class="exercise-button" onclick="toggleExercise(this)">Hint</button>
<div class="exercise-text">
Can you apply <a href="https://nowheredifferentiable.com/2023-07-12-PDEs-3-Sobolev_spaces/#:~:text=Theorem%2014%20(-,Rellich,-for%20trace%200">Rellich's
theorem</a>
to unbounded domains? What is the spectrum of the Laplacian on
$\mathbb{R}^d$?
</div>
</div>


<b>Exercise 5</b>. Show using Theorem
<a href="#well-posedness Fredholm">7</a> that equation
(\ref{fred})  (the
generalization of (\ref{PDE}) ) is well-posed saved for at most a discrete set of
$\lambda$.


<div class="exercise-container">
<button class="exercise-button" onclick="toggleExercise(this)">Hint</button>
<div class="exercise-text">
Combine the first and second points of Theorem
<a href="#well-posedness Fredholm">7</a>.
</div>
</div>


<b>Exercise 6</b>. Show the necessity of point 4 in Theorem
<a href="#well-posedness Fredholm">7</a> using only linear algebra.


<div class="exercise-container">
<button class="exercise-button" onclick="toggleExercise(this)">Hint</button>
<div class="exercise-text">
Suppose $\mathcal{L}u = \lambda u+f$ and $w \in N^\star $. Then,


<div>
$$\begin{aligned}
\left\langle w,f\right\rangle = \left\langle w,\mathcal{L}u -\lambda u\right\rangle = \left\langle w,\mathcal{L}u\right\rangle -\lambda \left\langle w,u\right\rangle =\left\langle\mathcal{L}^\star  w,u\right\rangle -\lambda \left\langle w,u\right\rangle= 0.

\end{aligned}$$
</div>


</div>
</div>

# Higher regularity

We have so far seen that, under the previous assumptions, solutions to
(\ref{PDE})  are in
$H\U 0^1(U)$. However, analogously to the classical setting, we may expect
that $u$ is two degrees of regularity smoother than $f$. That is that
$u \in H^2(U)$. This improved regularity is true, but only with the
caveat that the domain $U$ is sufficiently regular. Counterexamples with
non-smooth domains exist. See <a href="https://www.sciencedirect.com/science/article/pii/S002212369793158X/pdf?md5=c646200fe7117dd7d25d27439f36b342&pid=1-s2.0-S002212369793158X-main.pdf">Savare, 1998</a>.

We will also see how, for smoother coefficients, we can iterate to
obtain a higher regularity of $u$. As a result, when the coefficients of
(\ref{PDE})  are smooth, $u$
will be as well, and we will obtain a classical solution to problem
(\ref{PDE}) .

## Finite differences

In our study of regularity, we will make use of the difference
quotients. Given a function $u \in L^p(\mathbb{R}^d)$, we define the
difference quotients in the $j$-th direction as

<div>
$$\begin{aligned}
D\U j^h u := \frac{u(x+ he\U j)-u(x)}{h},\quad  e\U j=(0,\ldots,\overset{(j)}{1},\ldots,0).
\end{aligned}$$
</div>

If $u$ is differentiable, then
$D\U j^h u \to \partial\U j u$ as $h \to 0$. The following lemma shows that,
on $\mathbb{R}^d$, the difference quotients of $u$ are bounded if and
only if $u$ is weakly differentiable.

 <a name="difference quotients 1">
<b>Lemma 9</b> </a>  (Difference quotients and regularity). Let
$p \in (1, +\infty)$, and $C >0$ be some constant. Then, the following
hold.

1.  If $u \in L^p(\mathbb{R}^d)$ and for all $h$ sufficiently small
$\left\lVert D\U j^h u \right\rVert\U {L^p(\mathbb{R}^d)} \leq C$. Then
$u \in W^{1,p}(\mathbb{R}^d)$.

2.  If $u \in W^{1,p}(\mathbb{R}^d)$. Then,
$\left\lVert D\U j^h u \right\rVert\U {L^p(\mathbb{R}^d)} \leq \left\lVert \partial\U j u \right\rVert\U {L^p(\mathbb{R}^d)}$.



<b>Proof.</b> We begin by proving the first point. Since $L^p(\mathbb{R}^d)$
is reflexive, every bounded sequence in $L^p(\mathbb{R}^d)$ has a weakly
convergent subsequence. Thus, we can find $h\U n$ and
$v \in L^p(\mathbb{R}^d)$ such that $D\U j^{h\U n} u \rightharpoonup v$
weakly in $L^p(\mathbb{R}^d)$. We want to show that $v = \partial\U j u$.
To this aim, let $\varphi \in C\U c^\infty(\mathbb{R}^d)$. Then,


<div>
$$\begin{align}
\label{weak int parts}
\int\U {\mathbb{R}^d} v \varphi & = \lim\U {n \to \infty} \int\U {\mathbb{R}^d} D\U j^{h\U n} u \varphi = \lim\U {n \to \infty} \int\U {\mathbb{R}^d} u(x)\frac{\varphi(x-h\U n e\U j)- \varphi (x)}{h\U n}\,\mathrm{d}x
\\&= \int\U {\mathbb{R}^d} u(x)\lim\U {n \to \infty} -D\U j^{-h\U n} \varphi \,\mathrm{d}x =-\int\U {\mathbb{R}^d} u \partial\U j \varphi,\notag

\end{align}$$
</div>

where in the first equality, we used the weak
convergence of $D\U j^{h\U n}u$ to $v$; in the second, we separated the
integral in two and used the change of variable $x \to x-h\U n e\U j$ on the
first of the integrals (from now on we will call this "discrete
integration by parts"). The final equality follows from the smoothness
of $\varphi$. Since $\varphi \in C\U c^\infty(\mathbb{R}^d)$ was
arbitrary, we have that $v=\partial\U j u$ almost everywhere. Since
$u \in L^p(\mathbb{R}^d)$, this shows that
$u \in W^{1,p}(\mathbb{R}^d)$.

For the second point, suppose that $u$ is smooth; then, by the
fundamental theorem of calculus,

<div>
$$\begin{aligned}
D\U j^h u(x) = \int\U 0^1 \partial\U j u(x+the\U j) \,\mathrm{d}t.

\end{aligned}$$
</div>

Taking norms and using <a href="https://en.wikipedia.org/wiki/Minkowski_inequality#:~:text=.-,Minkowski%27s,-integral%20inequality%5B">Minkowski's integral
inequality</a>
we obtain

<div>
$$\begin{aligned}
\left\lVert D\U j^h u \right\rVert\U {L^p(\mathbb{R}^d)} \leq \int\U 0^1 \left\lVert \partial\U j u(\cdot+the\U j) \right\rVert\U {L^p(\mathbb{R}^d)} \,\mathrm{d}t= \int\U {0}^1 \left\lVert \partial\U j u \right\rVert\U {L^p(\mathbb{R}^d)} \,\mathrm{d}t=\left\lVert \partial\U j u \right\rVert\U {L^p(\mathbb{R}^d)},

\end{aligned}$$
</div>

where in the second equality, we used the change of
variables $x \to x-the\U j$. We conclude by using the density of smooth
functions in $W^{1,p}(\mathbb{R}^d)$ to take limits in the above
inequality. ◻


The result can be extended to arbitrary open subsets
$U \subset \mathbb{R}^d$. In this case, one can only obtain local
regularity as the translation $u(x+h e\U j)$ is not well defined on the
whole of $U$. We recall the notation $V \Subset U$ to mean that $V$ is a
subset of $U$ with $\bar{V} \subset U$.

 <a name="difference quotients 2">
<b>Lemma 10</b> </a>  (Difference quotients and local regularity). Let
$p \in (1, +\infty)$, $C>0$ be a constant and $V \Subset U$ open. Then,
the following hold.

1.  If $u \in L^p(U)$ and for all $h$ sufficiently small
$\left\lVert D\U j^h u \right\rVert\U {L^p(V)} \leq C$. Then,
$u \in W^{1,p}(V)$.

2.  If $u \in W^{1,p}(U)$. Then,
$\left\lVert D\U j^h u \right\rVert\U {L^p(V)} \leq \left\lVert \partial\U j u \right\rVert\U {L^p(U)}$
for all $h<\,\mathrm{d}(V,\partial U)$.



<b>Exercise 7</b>. Prove Lemma
<a href="#difference quotients 2">10</a>.


<div class="exercise-container">
<button class="exercise-button" onclick="toggleExercise(this)">Hint</button>
<div class="exercise-text">
Adapt the proof of Lemma
<a href="#difference quotients 1">9</a>. Take $\varphi \in C\U c^\infty(V)$
for the first point. For the second point, use the <a href="https://nowheredifferentiable.com/2023-07-12-PDEs-3-Sobolev_spaces/#:~:text=drawings%20is%20recommended.-,Theorem%203,-(Local%20approximation%20by">local
density</a>
of smooth functions in $W^{1,p}(U)$.
</div>
</div>

## Regularity on $\mathbb{R}^d$

By using second-order finite difference, we now show that the solution
to (\ref{PDE})  is in
$H^2(\mathbb{R}^d)$ if we impose additionally that $\mathbf{A}$ is
continuously differentiable.

 <a name="improved reg Rd">
<b>Theorem 11</b> </a>  (Improved regularity on $\mathbb{R}^d$ ). Suppose that
$A\U {ij}\in C^1(\mathbb{R}^d)$ is elliptic and that
$b\U i \in L^\infty(\mathbb{R}^d ), c \in L^\infty(\mathbb{R}^d)$ . Then,
if $u \in H^1(\mathbb{R}^d)$ solves $\mathcal{L}u=f$, it holds that
$u \in H^2(\mathbb{R}^d)$ with

<div>
$$\begin{aligned}
\left\lVert u \right\rVert\U {H^2(\mathbb{R}^d)} \lesssim\U {\mathbf{A},\mathbf{b},c} \left\lVert f \right\rVert\U {L^2(\mathbb{R}^d)}+\left\lVert u \right\rVert\U {L^2(\mathbb{R}^d)}.

\end{aligned}$$
</div>





<b>Proof.</b> The idea is to use difference quotients to approximate the
second derivative of $u$

<div>
$$\begin{aligned}
v:= -D\U j^{-h} D\U j^h u = \frac{u(x+he\U k)-2u(x)+u(x-he\U k)}{h^2}.

\end{aligned}$$
</div>

Since $v \in H^1(U)$, we can substitute $v$ into the
weak formulation (\ref{weak def}) , do a discrete integration by parts and use
Cauchy's inequality to show that
$\left\lVert D\U j^h \nabla u \right\rVert\U {L^2(\mathbb{R}^d)}$ is
bounded. Using Lemma <a href="#difference quotients 1">9</a>, we will then conclude that
$u \in H^{2}(\mathbb{R}^d)$ and finish off the proof. We now put this
plan into action. From (\ref{weak def}) , we have that

<div>
$$\begin{align}
\label{start}
\int\U {\mathbb{R}^d} \mathbf{A} \nabla u \cdot \nabla v =\int\U {\mathbb{R}^d} (f- \mathbf{b} \cdot \nabla u -cu)v.

\end{align}$$
</div>

Applying a discrete integration by parts to the
left-hand side of (\ref{start})  as in
(\ref{weak int parts}) , we obtain

<div>
$$\begin{aligned}
\int\U {\mathbb{R}^d} \mathbf{A} \nabla u \cdot \nabla v = \int\U {\mathbb{R}^d} D\U j^h( \mathbf{A} \nabla u) \cdot (D\U j^h \nabla u)= \int\U {\mathbb{R}^d} \mathbf{A}^h D\U j^h \nabla u \cdot D\U j^h \nabla u+ \int\U {\mathbb{R}^d} (D\U j^h\mathbf{A}) \nabla u \cdot D\U j^h \nabla u,

\end{aligned}$$
</div>

where in the last equality, we used the notation
$\mathbf{A}^h(x):=\mathbf{A}(x+h)$ and the product rule for difference quotients
(this can be checked by basic algebra). Using the ellipticity of
$\mathbf{A}$ and Cauchy's inequality
(\ref{Cauchy})  to put
$\varepsilon$ on the higher order negative term $D\U j^h \nabla  u$ we
obtain that for some constant $C$

<div>
$$\begin{align}
\label{first}
\int\U {\mathbb{R}^d} \mathbf{A} \nabla u \cdot \nabla v \geq \alpha \left\lVert D\U j^h \nabla u \right\rVert\U {L^2(\mathbb{R}^d)}^2 -\frac{C}{\varepsilon }\left\lVert  \nabla u \right\rVert\U {L^2(\mathbb{R}^d)}^2-\varepsilon \left\lVert D\U j^h \nabla u \right\rVert\U {L^2(\mathbb{R}^d)}^2,

\end{align}$$
</div>

where we used that, since
$\mathbf{A} \in C^1(\mathbb{R}^d)$, the term $D\U j^h \mathbf{A}$ is bounded.
Setting $\varepsilon =\alpha /3$ in
(\ref{first})  we obtain
that

<div>
$$\begin{align}
\label{second}
\int\U {\mathbb{R}^d} \mathbf{A} \nabla u \cdot \nabla v \geq \frac{2\alpha}{3} \left\lVert D\U j^h \nabla u \right\rVert\U {L^2(\mathbb{R}^d)}^2-\frac{3C}{\alpha}\left\lVert \nabla u \right\rVert\U {L^2(\mathbb{R}^d)}^2.

\end{align}$$
</div>

We now estimate the right-hand side of
(\ref{start}) . We have
that, by Cauchy's inequality and the second point of Lemma
<a href="#difference quotients 1">9</a>,

<div>
$$\begin{aligned}
\int\U {\mathbb{R}^d} (f- \mathbf{b} \cdot \nabla u -cu)v \leq \frac{C}{\varepsilon }\left(\left\lVert f \right\rVert^2\U {L^2(\mathbb{R}^d)}+ \left\lVert \nabla u \right\rVert^2\U {L^2(\mathbb{R}^d)}+\left\lVert u \right\rVert^2\U {L^2(\mathbb{R}^d)}\right)+\varepsilon \left\lVert D\U j^h \nabla u \right\rVert\U {L^2(\mathbb{R}^d)}^2.

\end{aligned}$$
</div>

Once more, setting $\varepsilon =\alpha /3$ gives


<div>
$$\begin{align}
\label{third}
\int\U {\mathbb{R}^d} (f- \mathbf{b} \cdot \nabla u -cu)v \leq \frac{3C}{\alpha }\left(\left\lVert f \right\rVert^2\U {L^2(\mathbb{R}^d)}+ \left\lVert \nabla u \right\rVert^2\U {L^2(\mathbb{R}^d)}+\left\lVert u \right\rVert^2\U {L^2(\mathbb{R}^d)}\right)+\frac{\alpha }{3}\left\lVert D\U j^h \nabla u \right\rVert\U {L^2(\mathbb{R}^d)}^2.

\end{align}$$
</div>

Using (\ref{second})  and (\ref{third})  in (\ref{start})  shows that, for some constant $\widetilde{C}$,


<div>
$$\begin{align}
\label{fourth}
\left\lVert D\U j^h \nabla u \right\rVert\U {L^2(\mathbb{R}^d)}^2 \leq \frac{\widetilde{C} }{\alpha^2 }\left(\left\lVert f \right\rVert^2\U {L^2(\mathbb{R}^d)}+ \left\lVert \nabla u \right\rVert^2\U {L^2(\mathbb{R}^d)}+\left\lVert u \right\rVert^2\U {L^2(\mathbb{R}^d)}\right).

\end{align}$$
</div>

Equation (\ref{fourth})  is almost the desired result save the presence of
$\left\lVert \nabla u \right\rVert\U {L^2(\mathbb{R}^d)}$ on the
right-hand side. However, by setting $v= u$ in
(\ref{start})  and once
more using Cauchy's inequality, we obtain that

<div>
$$\begin{align}
\label{fifth}
\left\lVert \nabla u \right\rVert\U {L^2(\mathbb{R}^d)}^2 \lesssim\U {\mathbf{A},\mathbf{b},c} \left\lVert f \right\rVert^2\U {L^2(\mathbb{R}^d)}+ \left\lVert  u \right\rVert^2\U {L^2(\mathbb{R}^d)}.

\end{align}$$
</div>

Combining (\ref{fourth})  and (\ref{fifth})  gives the bound

<div>
$$\begin{aligned}
\left\lVert D\U j^h \nabla u \right\rVert\U {L^2(\mathbb{R}^d)}^2 \lesssim\U {\mathbf{A},\mathbf{b},c} \left\lVert f \right\rVert^2\U {L^2(\mathbb{R}^d)}+ \left\lVert  u \right\rVert^2\U {L^2(\mathbb{R}^d)}.

\end{aligned}$$
</div>

Applying the first point of Lemma
<a href="#difference quotients 1">9</a> and taking square roots concludes
the proof. ◻


By induction, we can obtain higher-order regularity. For notational
convenience, we write

<div>
$$\begin{aligned}
X^k:= H^k(\mathbb{R}^d) \cap W^{k,\infty}(\mathbb{R}^d).
\end{aligned}$$
</div>

This space corresponds to functions that are $k$ times
weakly differentiable with bounded and square-integrable derivatives up
to order $k$.

 <a name="higher regularity Rd">
<b>Theorem 12</b> </a>  (Regularity on $\mathbb{R}^d$ ). Suppose that
$\mathcal{L}$ is elliptic and that its coefficients verify


<div>
$$\begin{aligned}
A\U {ij} \in C^{1}(\mathbb{R}^d)\cap X^{k+1}, \quad b\U i,c \in X^k, \quad f \in H^k(\mathbb{R}^d).

\end{aligned}$$
</div>

Then, if $u \in H^1(\mathbb{R}^d)$ solves
$\mathcal{L}u=f$, it holds that $u \in H^{k+2}(\mathbb{R}^d)$ with


<div>
$$\begin{aligned}
\left\lVert u \right\rVert\U {H  ^{k+2}(\mathbb{R}^d)} \lesssim\U {\mathbf{A},\mathbf{b},c} \left\lVert f \right\rVert\U {H^k(\mathbb{R}^d)}+\left\lVert u \right\rVert\U {L^2(\mathbb{R}^d)}.

\end{aligned}$$
</div>





<b>Proof.</b> The theorem holds for $k=0$ by Theorem
<a href="#improved reg Rd">11</a>. Suppose by hypothesis of induction that
the theorem holds up to order $k$. Let

<div>
$$\begin{align}
\label{coefficients k1}
A\U {ij} \in C^{1}(\mathbb{R}^d)\cap X^{k+2}, \quad b\U i,c \in X^{k+1}, \quad f \in H^{k+1}(\mathbb{R}^d).

\end{align}$$
</div>

Then, by the induction hypothesis
$u \in H^{k+2}(\mathbb{R}^d)$ with

<div>
$$\begin{align}
\label{hi}
\left\lVert u \right\rVert\U {H^{k+2}(U)} \lesssim\U {\mathbf{A},\mathbf{b},c} \left\lVert f \right\rVert\U {H^k(\mathbb{R}^d)}+\left\lVert u \right\rVert\U {L^2(\mathbb{R}^d)}.

\end{align}$$
</div>

Consider a multi-index $\alpha$ with $|\alpha|=k+1$ and
$\widetilde{v } \in C\U c^\infty(\mathbb{R}^d)$. Then, substituting
$v := (-1)^{\left| \alpha \right| } D^\alpha \widetilde{v}$ in the weak
formulation (\ref{weak def})  we obtain by integrating by parts that


<div>
$$\begin{aligned}
\int\U {\mathbb{R}^d} D^\alpha(\mathbf{A} \nabla u) \cdot \nabla \widetilde{v} +\int\U {\mathbb{R}^d} D^\alpha(\mathbf{b} \nabla u) \cdot \nabla \widetilde{v} +\int\U {\mathbb{R}^d} D^\alpha (c u) \widetilde{v} =\int\U {\mathbb{R}^d} D^\alpha f \widetilde{v}.

\end{aligned}$$
</div>

Let us write $\widetilde{u}:= D^\alpha u$. Applying the
chain rule repeatedly and keeping only the derivatives of order $k+3$ of
$u$ on the left-hand side to obtain

<div>
$$\begin{align}
\label{weak solk}
B(\widetilde{u},\widetilde{v} ) = \int\U {\mathbb{R}^d} \mathbf{A} \nabla D^\alpha u \cdot \nabla \widetilde{v} +\int\U {\mathbb{R}^d} \mathbf{b} \nabla D^\alpha u \cdot \nabla \widetilde{v} +\int\U {\mathbb{R}^d} c D^\alpha u \widetilde{v} =\int\U {\mathbb{R}^d} \widetilde{f} \widetilde{v}= (\widetilde{f} ,\widetilde{v}),

\end{align}$$
</div>

where $\widetilde{f}$ involves only $D^\alpha f$ as well
as sums and products of derivatives up to order $k+2$ of $u,\mathbf{A}$ and
up to order $k+1$ of $\mathbf{b}$ and $c$. As a result, by the conditions on
the coefficients in
(\ref{coefficients k1})  and the induction hypothesis
$u \in H^{k+2}(\mathbb{R}^d)$, we have that
$\widetilde{f} \in L^2(\mathbb{R}^d)$ with

<div>
$$\begin{align}
\label{Hkr}
\|{\widetilde{f}}\|\U {L^2(\mathbb{R}^d)} \lesssim\U {\mathbf{A},\mathbf{b},c} \left\lVert f \right\rVert\U {H^{k+1}(\mathbb{R}^d)}+\left\lVert u \right\rVert\U {L^2(\mathbb{R}^d)}.

\end{align}$$
</div>

By equation
(\ref{weak solk}) , $\widetilde{u}$ is a solution to problem
(\ref{PDE})  and applying the
case $k=0$ (Theorem <a href="#improved reg Rd">11</a>) together with
(\ref{hi})  and
(\ref{Hkr})  shows that
$\widetilde{u} \in H^{2}(\mathbb{R}^d)$ with

<div>
$$\begin{aligned}
\left\lVert \widetilde{u} \right\rVert\U {H^{2}(\mathbb{R}^d)} \lesssim\U {\mathbf{A},\mathbf{b},c} \|\tilde{f}\|\U {L^2(\mathbb{R}^d)}+\left\lVert \widetilde{u} \right\rVert\U {L^2(\mathbb{R}^d)} \lesssim\U {\mathbf{A},\mathbf{b},c} \left\lVert f \right\rVert\U {H^{k+1}(\mathbb{R}^d)}+\left\lVert u \right\rVert\U {L^2(\mathbb{R}^d)}.

\end{aligned}$$
</div>

Since $\alpha$ was any coefficient of order $k+1$, we
deduce that $u \in H^{k+3}(\mathbb{R}^d)$ with

<div>
$$\begin{aligned}
\left\lVert u \right\rVert\U {H^{k+3}(\mathbb{R}^d)} \lesssim\U {\mathbf{A},\mathbf{b},c} \left\lVert f \right\rVert\U {H^{k+1}(\mathbb{R}^d)}+\left\lVert u \right\rVert\U {L^2(\mathbb{R}^d)}.

\end{aligned}$$
</div>

The equation above is the hypothesis of induction for
$k+1$, and the proof is complete. ◻


Iterating the above theorem, we obtain that if the coefficients of
$\mathcal{L}$ are smooth, then the solution to
(\ref{PDE})  is smooth as
well. And $u$ is a classical solution to
(\ref{PDE}) .

 <a name="infinite interior regularity">
<b>Theorem 13</b> </a>  (Infinite regularity on $\mathbb{R}^d$). Let
$A\U {ij}, b\U i,c \in C^{\infty}(\mathbb{R}^d)$ with $\mathbf{A}$ elliptic.
Then, if $u \in H^1(U)$ solves $\mathcal{L}u=f$, it holds that
$u \in C^\infty(\mathbb{R}^d)$



<b>Proof.</b> By Theorem <a href="#higher regularity 2">15</a>, we have that $u \in H^k(\mathbb{R}^d)$
for all $k \in \mathbb{N}$. By <a href="https://nowheredifferentiable.com/2023-07-12-PDEs-3-Sobolev_spaces/#:~:text=three%20results%20gives-,Theorem%2013,-(Rellich%2DKondrachov">Sobolev
embeddings</a>
we deduce that $u \in C^\infty(\mathbb{R}^d)$. ◻


At first sight, it may seem as if the above results can be extended to
solutions of (\ref{PDE})  on
$U \subsetneq \mathbb{R}^d$ with the following reasoning. However, there
is a mistake in the reasoning. Can you spot it?


<b>Exercise 8</b>. The following argument is <b>false</b>. Show the flaw in
the reasoning.

Let $U \subset \mathbb{R}^d$ be any open subset. Suppose that
$A\U {ij}\in C^1(\overline{U} )$ is elliptic and that
$b\U i, c \in L^\infty(U)$ . Let $u \in H\U 0^1(U)$ solve $\mathcal{L}u=f$.
The
<a href="https://nowheredifferentiable.com/2023-07-12-PDEs-3-Sobolev_spaces/#:~:text=smooth%20unbounded%20domains.-,Exercise%2021,-(Extension%20trace%200">extension</a>
$\widetilde{u}$ to $\mathbb{R}^d$ by zero of $u$ is in
$H^1(\mathbb{R}^d)$. The coefficients $b,c$ can likewise be extended by
$0$ to functions
$\widetilde{\mathbf{b}}, \widetilde{c} \in  L^\infty(\mathbb{R}^d)$.
Likewise for $f$ to $\widetilde{f} \in L^2(\mathbb{R}^d)$ and by
Assumption, $\mathbf{A}$ is the restriction to $U$ of some function
$\widetilde{A} \in C^1(\mathbb{R}^d)$. We have that

<div>
$$\begin{align}
\label{extension}
\widetilde{\mathcal{L}} \widetilde{u} := -\nabla \cdot (\widetilde{A} \nabla \widetilde{u})+ \widetilde{b} \cdot \nabla \widetilde{u} + \widetilde{c} \widetilde{u} =\widetilde{f} .

\end{align}$$
</div>

As a result by Theorem
<a href="#improved reg Rd">11</a>
it holds that $\widetilde{u} \in H^2(\mathbb{R}^d)$ with


<div>
$$\begin{aligned}
\left\lVert u \right\rVert\U {H^2(U)}=  \left\lVert \widetilde{u}  \right\rVert\U {H^2(\mathbb{R}^d)} \lesssim\U {\mathbf{A},\mathbf{b},c} \left\lVert f \right\rVert\U {L^2(\mathbb{R}^d)}+\left\lVert u \right\rVert\U {L^2(\mathbb{R}^d)}.

\end{aligned}$$
</div>




<div class="exercise-container">
<button class="exercise-button" onclick="toggleExercise(this)">Hint</button>
<div class="exercise-text">
Are you sure that $\widetilde{u}$ solves
(\ref{extension}) ? Consider for example the case
$\mathbf{A}= \mathbf{I}, \mathbf{b}=c=0$. For $\widetilde{u}$ to solve
(\ref{extension})  it is necessary that for all
$\varphi \in C\U c^\infty(\mathbb{R}^d)$

<div>
$$\begin{aligned}
\int\U {\mathbb{R}^d} \nabla \widetilde{u} \cdot \nabla \varphi = \int\U {\mathbb{R}^d} \widetilde{f} \varphi.

\end{aligned}$$
</div>

That is, that

<div>
$$\begin{aligned}
\int\U {U} \nabla u \cdot \nabla \varphi = \int\U {U} f \varphi, \quad \forall \varphi \in C^\infty(\mathbb{R}^d).

\end{aligned}$$
</div>

Whereas we only know that $u$ solves
(\ref{weak def}) .
That is,

<div>
$$\begin{aligned}
\int\U {U} \nabla u \cdot \nabla \varphi = \int\U {U} f \varphi, \quad \forall \varphi \in C\U c^\infty(U).

\end{aligned}$$
</div>

This equality does not imply the previous one. The
problem is that extension by zero does not respect the second derivative
of functions in $H\U 0^1(\mathbb{R}^d)$. For example, if
$u \in H^2(U) \cap H\U 0^1(U)$ we do not necessarily have that
$\widetilde{u}$ is in $H^2(\mathbb{R}^d)$. Consider for example
$U=(-1,1)$ and $u(x)=1-\frac{1}{2} x^2$. Then, $u$ solves our equation
(\ref{PDE})  with $f=1$.
However, $\widetilde{u}$ is not in $H^2(\mathbb{R})$ and given
$\varphi \in C\U c^\infty(\mathbb{R})$

<div>
$$\begin{aligned}
\int\U {\mathbb{R}}\widetilde{u} ' \varphi ' = -\int\U {-1}^1 x \varphi' =-(\varphi (1)-\varphi(-1) )+ \int\U {-1}^1 \varphi \neq \int\U {-1}^1 \varphi = \int\U \mathbb{R}\widetilde{f} \varphi.

\end{aligned}$$
</div>


</div>
</div>

## Interior regularity

We have just seen that a direct generalization of Theorem
<a href="#improved reg Rd">11</a>
to unbounded domains is not possible using an extension by zero.
However, by adapting the proof of Theorem
<a href="#improved reg Rd">11</a>, one can prove the analogous result.

In this case, however, one has to be careful as the difference quotients
may not be well defined at the boundary. As a result, it is necessary to
work locally and use a <a href="https://nowheredifferentiable.com/2023-07-12-PDEs-3-Sobolev_spaces/#:~:text=22.%20A-,bump%20function,-(also%20called%20cutoff">bump
function</a>.
This makes the proofs a bit messier, though the idea is the same. We
sketch the proof, which can also be found in <a href="https://math24.files.wordpress.com/2013/02/partial-differential-equations-by-evans.pdf">Evans, 2022</a> page
326

 <a name="higher regularity">
<b>Theorem 14</b> </a>  (Improved interior regularity). Let $u \in H^1(U)$ be a
solution to $\mathcal{L}u =f$ where $f \in L^2(U)$,
$\mathbf{A} \in C^1(\overline{U} )$ is elliptic and $v\U i,c \in L^\infty(U)$.
Then, $u \in H^2 \U {\mathrm{loc}} (U)$ and

<div>
$$\begin{aligned}
\left\lVert u \right\rVert\U {H^2 \U {\mathrm{loc}}(U)} \lesssim\U {\mathbf{A},\mathbf{b},c} \left\lVert f \right\rVert\U {L^2(U)}+\left\lVert u \right\rVert\U {L^2(U)}.

\end{aligned}$$
</div>




Note that we do not require $u$ to be in $H^1\U 0(U)$.


<b>Proof.</b> Let $V \Subset U$ be open and let $\eta$ be a bump function
supported on $W$ and identically equal to $1$ on $V$. For $h$ small we
have that

<div>
$$\begin{align}
\label{difference bounded}
v = - D\U j^h \eta^2 D\U j^h u \in H^2(V),\quad  j=1,\ldots,d.

\end{align}$$
</div>

Proceeding as in the proof of Theorem
<a href="#improved reg Rd">11</a>, we obtain that

<div>
$$\begin{aligned}
\int\U V\left|D\U j^h \nabla u\right|^2 d x \leq \int\U U \eta^2\left|D\U j^h D u\right|^2 d x \lesssim C \int\U U f^2+u^2+|\nabla u|^2.

\end{aligned}$$
</div>

Applying the first point of Lemma
<a href="#difference quotients 2">10</a> we obtain that
$u \in H^2\U {\mathrm{loc}}(U)$ with

<div>
$$\begin{align}
\label{H2loc}
\left\lVert u \right\rVert\U {H^2 \U {\mathrm{loc}} (U)} \lesssim\U {\mathbf{A},\mathbf{b},c} \left\lVert f \right\rVert\U {L^2(U)}+\left\lVert u \right\rVert\U {H^1(U)}.

\end{align}$$
</div>

Analogously, we also obtain by setting $v= \eta ^2 u$
that

<div>
$$\begin{align}
\label{H1loc}
\int\U V |\nabla u|^2 \leq\int\U U \eta ^2 |\nabla u|^2 \lesssim \left\lVert f \right\rVert\U {L^2(U)}+\left\lVert u \right\rVert\U {H^1(U)}.

\end{align}$$
</div>

Combining (\ref{H2loc})  and (\ref{H1loc}) , we obtain the desired result. ◻


As we did in the case $U=\mathbb{R}^d$, we can obtain higher-order
regularity by induction. As before, we now write

<div>
$$\begin{aligned}
X^k(U):= H^k(U) \cap W^{k,\infty}(U).
\end{aligned}$$
</div>

In the case that $U$ is bounded then
$X^k(U)=W^{k,\infty}(U)$.

 <a name="higher regularity 2">
<b>Theorem 15</b> </a>  (Interior regularity). Suppose that $\mathcal{L}$ is
elliptic and that its coefficients verify

<div>
$$\begin{aligned}
A\U {ij} \in C^{1}(\overline{U} )\cap X^{k+1}(U), \quad b\U i,c \in X^k(U), \quad f \in H^k(U).

\end{aligned}$$
</div>

Then, if $u \in H^1(U)$ solves $\mathcal{L}u=f$, it
holds that $u \in H^{k+2}\U {\mathrm{loc}} (U)$ with

<div>
$$\begin{aligned}
\left\lVert u \right\rVert\U {H ^{k+2}\U {\mathrm{loc}} (U)} \lesssim\U {\mathbf{A},\mathbf{b},c} \left\lVert f \right\rVert\U {H^k(U)}+\left\lVert u \right\rVert\U {L^2(U)}.

\end{aligned}$$
</div>





<b>Exercise 9</b>. Prove Theorem
<a href="#higher regularity 2">15</a>.


<div class="exercise-container">
<button class="exercise-button" onclick="toggleExercise(this)">Hint</button>
<div class="exercise-text">
The theorem holds for $k=0$ by Theorem
<a href="#higher regularity">14</a>. Suppose by hypothesis of induction that
the theorem holds up to order $k$. Let

<div>
$$\begin{align}
\label{coefficients k12}
A\U {ij} \in C^{1}(\overline{U} )\cap X^{k+2}(U), \quad b\U i,c \in X^{k+1}(U), \quad f \in H^{k+1}(U).

\end{align}$$
</div>

Then, by the induction hypothesis
$u \in H^{k+2}\U {\mathrm{loc}} (U)$ with

<div>
$$\begin{align}
\label{hi2}
\left\lVert u \right\rVert\U {H^{k+2}\U {\mathrm{loc}}(U)} \lesssim\U {\mathbf{A},\mathbf{b},c} \left\lVert f \right\rVert\U {H^k(U)}+\left\lVert u \right\rVert\U {L^2(U)}.

\end{align}$$
</div>

Let $V\Subset U$ be open, consider a multi-index
$\alpha$ with $|\alpha|=k+1$ and $\widetilde{v } \in C\U c^\infty(V)$.
Then, substituting
$v := (-1)^{\left| \alpha \right| } D^\alpha \widetilde{v}$ in the weak
formulation (\ref{weak def})  we obtain by integrating by parts that


<div>
$$\begin{aligned}
\int\U {V} D^\alpha(\mathbf{A} \nabla u) \cdot \nabla \widetilde{v} +\int\U {V} D^\alpha(\mathbf{b} \nabla u) \cdot \nabla \widetilde{v} +\int\U {V} (D^\alpha c u) \widetilde{v} =\int\U {V} D^\alpha f \widetilde{v}.

\end{aligned}$$
</div>

Let us write $\widetilde{u}:= D^\alpha u$. Applying the
chain rule repeatedly and keeping only the derivatives of order $k+2$ of
$u$ on the left-hand side to obtain

<div>
$$\begin{align}
\label{weak solk2}
B(\widetilde{u},\widetilde{v} ) = \int\U {V} \mathbf{A} \nabla D^\alpha u \cdot \nabla \widetilde{v} +\int\U {V} \mathbf{b} \nabla D^\alpha u \cdot \nabla \widetilde{v} +\int\U {V} c D^\alpha u \widetilde{v} =\int\U {V} \widetilde{f} \widetilde{v}= (\widetilde{f} ,\widetilde{v}),

\end{align}$$
</div>

where $\widetilde{f}$ involves only $D^\alpha f$ as well
as sums and products of derivatives up to order $k+2$ of $u,\mathbf{A}$ and
up to order $k+1$ of $\mathbf{b}$ and $c$. As a result, by the conditions on
the coefficients in
(\ref{coefficients k12})  and the induction hypothesis
$u \in H \U {\mathrm{loc}}^{k+2}(U)$, we have that
$\widetilde{f} \in L^2(V)$ with

<div>
$$\begin{align}
\label{Hk}
\|{\widetilde{f}}\|\U {L^2(V)} \lesssim\U {\mathbf{A},\mathbf{b},c} \left\lVert f \right\rVert\U {H^{k+1}(U)}+\left\lVert u \right\rVert\U {L^2(U)}.

\end{align}$$
</div>

By equation
(\ref{weak solk2}) , $\widetilde{u}$ is a solution to
(\ref{PDE})  on $V$ and
applying (\ref{hi2})  and
(\ref{Hk})  shows that
$\widetilde{u} \in H^{2} \U {\mathrm{loc}}(V)$ with

<div>
$$\begin{aligned}
\left\lVert \widetilde{u} \right\rVert\U {H^{2}\U {\mathrm{loc}} (V)} \lesssim\U {\mathbf{A},\mathbf{b},c} \|\tilde{f}\|\U {L^2(V)}+\left\lVert \widetilde{u} \right\rVert\U {L^2(V)} \lesssim\U {\mathbf{A},\mathbf{b},c} \left\lVert f \right\rVert\U {H^{k+1}(U)}+\left\lVert u \right\rVert\U {L^2(U)}.

\end{aligned}$$
</div>

Since $\alpha$ was any coefficient of order $k+1$, we
deduce that $u \in H^{k+3}(W)$ with

<div>
$$\begin{aligned}
\left\lVert u \right\rVert\U {H^{k+3}\U {\mathrm{loc}} (V)} \lesssim\U {\mathbf{A},\mathbf{b},c} \left\lVert f \right\rVert\U {H^{k+1}(U)}+\left\lVert u \right\rVert\U {L^2(U)}.

\end{aligned}$$
</div>

Since $V\Subset U$ is any, we deduce that


<div>
$$\begin{aligned}
\left\lVert u \right\rVert\U {H^{k+3}\U {\mathrm{loc}} (U)} \lesssim\U {\mathbf{A},\mathbf{b},c} \left\lVert f \right\rVert\U {H^{k+1}(U)}+\left\lVert u \right\rVert\U {L^2(U)}.

\end{aligned}$$
</div>

The above is the hypothesis of induction for $k+1$ and
completes the proof.
</div>
</div>

Using Sobolev embeddings we obtain once more infinite regularity for
smooth coefficients.

 <a name="infinite interior regularity2">
<b>Theorem 16</b> </a>  (Infinite interior regularity). Let
$A\U {ij}, b\U i,c \in C^{\infty}(\overline{U} )$ with $\mathbf{A}$ elliptic.
Then, if $u \in H^1(U)$ solves $\mathcal{L}u=f$, it holds that
$u \in C \U {\mathrm{loc}}^\infty(U)$.



<b>Proof.</b> By Theorem <a href="#higher regularity 2">15</a>, we have that $u \in H^k(U)$ for all
$k \in \mathbb{N}$. By Sobolev embeddings we have that
$u \in C^\infty\U {\mathrm{loc}}(U)$. ◻


## Regularity at the boundary

Regularity at the boundary can also be obtained; however, in this case,
it is necessary to impose the boundary condition
$\left.u\right|\U {\partial \Omega }=0$. We can then work on bounded
smooth domains $\Omega$ by reasoning first on
$B(0,1) \cap \mathbb{R}^d\U +$ and then using a finite covering of
$\overline{\Omega }$ and a change of coordinates to translate these
results back to $\Omega$.

We summarize and sketch the proofs of the main results, which are
analogous to the interior regularity results of Theorems
<a href="#higher regularity">14</a>,
<a href="#higher regularity 2">15</a> and
<a href="#infinite interior regularity2">16</a>.The details For the partition
to be finite, it is further necessary for $\Omega$ to be bounded. We
sketch the proof which can be found in <a href="https://math24.files.wordpress.com/2013/02/partial-differential-equations-by-evans.pdf">Evans, 2022</a> pages
$334-343$ and <a href="https://link.springer.com/book/10.1007/978-3-642-61798-0">Gilbarg, 1977</a> pages 183-188.

 <a name="improved regularity boundary">
<b>Theorem 17</b> </a>  (Improved regularity at the boundary). Let
$\Omega \subset \mathbb{R}^d$ be bounded with
$\partial \Omega  \in   C^2$. Let $A\U {ij} \in C^{1}(\overline{\Omega})$
be elliptic and $b\U i,c \in L^\infty(\Omega)$. Let $u \in H^1\U 0(\Omega)$
be a weak solution to (\ref{PDE}) . Then, $u \in H^2(\Omega)$ with

<div>
$$\begin{aligned}
\left\lVert u \right\rVert\U {H^2(\Omega)} \lesssim\U {\mathbf{A},\mathbf{b},c, \Omega } \left\lVert f \right\rVert\U {L^2(\Omega)}+\left\lVert u \right\rVert\U {L^2(\Omega)}.

\end{aligned}$$
</div>





<b>Proof.</b> Since $\partial \Omega$ is of class $C^2$, given
$x\U 0 \in \partial \Omega$ there exists $R>0$ and a twice differentiable
diffeomorphism

<div>
$$\begin{aligned}
\varphi : B\U R(x\U 0) \xrightarrow{\sim}\varphi (B\U R(x\U 0)) \subset \mathbb{R}^d,

\end{aligned}$$
</div>

that maps the interior of $B\U R(x\U 0)$ to the interior of
$\mathbb{R}^d\U +$ and the boundary to the boundary. That is,


<div>
$$\begin{aligned}
\widetilde{\Omega}:= \varphi (B\U R(x\U 0) \cap \Omega ) & =\varphi (B\U R(x\U 0)) \cap \left\{x\U d>0\right\} \\ \partial \widetilde{\Omega }\U 0:= \varphi (B\U R(x\U 0) \cap \partial  \Omega ) &=\varphi (B\U R(x\U 0)) \cap \left\{x\U d=0\right\}.

\end{aligned}$$
</div>

Let us define $\widetilde{u}:= u \circ \varphi ^{-1}$ on
$\widetilde{\Omega }$. Then, $\widetilde{u}$ verifies a PDE of the same
form as our original PDE (\ref{PDE}) . Where now the boundary condition holds only on the
straight part straight part $\partial \widetilde{\Omega }\U 0$.


<div>
$$\begin{aligned}
\begin{cases}
\widetilde{\mathcal{L}}\widetilde{u} =\widetilde{f} & \text{in } \widetilde{\Omega }             \\
\widetilde{u}=0                & \text{on } \partial \widetilde{\Omega }\U 0.
\end{cases}

\end{aligned}$$
</div>

Since our boundary condition does not hold on the
curved part of the boundary
$\partial \widetilde{\Omega }\U 1:=  \partial \widetilde{\Omega }\setminus \partial \widetilde{\Omega }\U 0$,
to integrate by parts we need to introduce a bump function $\eta$ which
is zero on $\partial \widetilde{\Omega }\U 1$.

Let $0<r<R$ and define $\widetilde{V}:= \varphi(B\U r(x\U 0) \cap \Omega )$.
Now choose a bump function $\eta \in C\U c^\infty(\mathbb{R}^d)$ with
compact support in $\varphi (B\U R(x\U 0))$ (in particular, $\eta =0$ on
$\partial \widetilde{\Omega }\U 1$) and identically equal to $1$ on
$\widetilde{V}$. Then, for small $h$, we define as in
(\ref{difference bounded})  the function

<div>
$$\begin{aligned}
\widetilde{v} := -D\U j^h \eta^2 D\U j^h \widetilde{u} \in H^2\U 0(\widetilde{\Omega }) \quad j=1,\ldots,d-1.

\end{aligned}$$
</div>

Here, the increments are only well defined for
$j \neq d$. Proceeding as in the proof of Theorem
<a href="#higher regularity">14</a>, we obtain that, for $i,j=1,\ldots,d-1$,


<div>
$$\begin{align}
\label{not d bound}
\left\lVert \partial\U i \partial \U j \widetilde{v} \right\rVert\U {L^2(\widetilde{V} )} \lesssim\U {\mathbf{A}, \mathbf{b}, c} \|\widetilde{f}\|\U {L^2(\widetilde{\Omega })}+\|\widetilde{u}\|\U {L^2(\widetilde{\Omega })} \lesssim\U {\mathbf{A}, \mathbf{b}, c, \varphi } \left\lVert f \right\rVert\U {L^2(\Omega)}+\left\lVert u \right\rVert\U {L^2(\Omega)}.

\end{align}$$
</div>

Since
$\widetilde{u} \in H^2\U {\mathrm{loc}}(\widetilde{V} )$ by Theorem
<a href="#higher regularity">14</a>, we have that the equality
$\widetilde{\mathcal{L}}\widetilde{u}=f$ holds almost everywhere in
$\widetilde{V}$. As a result,

<div>
$$\begin{aligned}
A\U {dd} \partial\U d\partial\U d \widetilde{u}= \widetilde{F},

\end{aligned}$$
</div>

where $\widetilde{F}$ only involves derivatives up to
order $1$ in $x\U d$ of $u$ and up to order $2$ in $x\U 1,\dots, x\U {d-1}$ of
$u$. Using the ellipticity of $\mathbf{A}$ with $\xi=(0,\dots,0,1)$ in
(\ref{elliptic})
we obtain that, almost everywhere in $\widetilde{V}$,

<div>
$$\begin{aligned}
\partial\U d\partial\U d \widetilde{u} \lesssim \widetilde{F}.

\end{aligned}$$
</div>

Taking norms and using
(\ref{not d bound})  gives

<div>
$$\begin{aligned}
\left\lVert \widetilde{u}  \right\rVert\U {H^2(\widetilde{V} )} \lesssim\U {\mathbf{A},\mathbf{b},c, \varphi } \left\lVert f \right\rVert\U {L^2(\Omega)}+\left\lVert u  \right\rVert\U {L^2(\Omega)}.

\end{aligned}$$
</div>



If we write $V\U {x\U 0}:= \varphi ^{-1} (\widetilde{V} )$, we have that
$u \in H^2(V\U {x\U 0})$ with

<div>
$$\begin{aligned}
\left\lVert u \right\rVert\U {H^2(V\U {x\U 0})} \lesssim\U {\mathbf{A},\mathbf{b},c, \varphi } \left\lVert f \right\rVert\U {L^2(\Omega)}+\left\lVert u \right\rVert\U {L^2(\Omega)}.

\end{aligned}$$
</div>

Since $\partial \Omega$ is compact, we can cover
$\Omega$ with a finite number of such sets $V\U {x\U 0}$ plus some open
$W \Subset \Omega$. We conclude the proof by using the interior
regularity result of Theorem
<a href="#higher regularity">14</a> to bound
$\left\lVert u \right\rVert\U {H^2(W)}$. ◻


The following can now be proved by induction, just as in Theorems
<a href="#higher regularity">14</a> and
<a href="#higher regularity 2">15</a>.

 <a name="higher regularity boundary">
<b>Theorem 18</b> </a>  (Higher regularity at the boundary). Let
$\Omega \subset \mathbb{R}^d$ be bounded with
$\partial \Omega  \in   C^{k+2}$. Let
$A\U {ij} \in C^1(\overline{\Omega})\cap W^{k, \infty}(\Omega)$ be
elliptic and $b\U i,c \in H^k(\Omega)\cap W^{k,\infty}(\Omega)$ and
$f \in H^k(\Omega )$ . Let $u \in H^1\U 0(\Omega)$ be a weak solution to
(\ref{PDE}) . Then,
$u \in H^{k+2}(\Omega)$ with

<div>
$$\begin{aligned}
\left\lVert u \right\rVert\U {H^{k+2}(\Omega)} \lesssim\U {\mathbf{A},\mathbf{b},c, \Omega } \left\lVert f \right\rVert\U {H^k(\Omega)}+\left\lVert u \right\rVert\U {L^2(\Omega)}.

\end{aligned}$$
</div>




Once more, by Sobolev embeddings we obtain infinite regularity at the
boundary.


<b>Theorem 19</b> (Infinite regularity at the boundary). Let
$\Omega \subset \mathbb{R}^d$ be bounded of class $C^{\infty}$. Let
$A\U {ij}, b\U i,c \in C^{\infty}(\overline{\Omega})$ with $\mathbf{A}$
elliptic. Let $u \in H^1\U 0(\Omega)$ be a weak solution to
(\ref{PDE}) . Then,
$u \in C^\infty(\overline{\Omega})$.


# Other boundary conditions

So far, we have only worked with homogeneous Dirichlet boundary
conditions. However, it often makes more sense to work with the
non-homogeneous case. We also show how to extend the results to Neumann
or Robin <a href="https://nowheredifferentiable.com/2023-12-23-PDEs-4-Physical_derivation_of_parabolic_and_elliptic_PDE/#:~:text=reaction%20and%20source.-,Boundary%20conditions,-In%20an%20application">boundary
conditions</a>.
In this section, we will see how to adapt the results of the previous
section to these cases.

## Non-homogeneous Dirichlet boundary conditions

Consider the problem with non-homogeneous Dirichlet boundary conditions
on a domain $\Omega$ with with Lipschitz boundary, written
$\partial \Omega \in  C^{0,1}$

<div>
$$\begin{align}
\label{PDE Dirichlet}
\begin{cases}
\mathcal{L}u =f & \text{in } \Omega ,          \\
u=g      & \text{on } \partial \Omega .
\end{cases}
\end{align}$$
</div>

For
(\ref{PDE Dirichlet})  to hold, it is necessary that $g$ is the
restriction to $\partial \Omega$ of some function $\widetilde{g}$ called
a lifting of $\widetilde{g}$ onto $\Omega$ (in particular it is the
restriction of $u$ to $\partial \Omega$ ). That is,
$\widetilde{g}  \in \mathrm{Tr}(H^m(\Omega ))$ where $\mathrm{Tr}$ is
the trace operator and $m$ is the desired regularity of $u$. By <a href="https://nowheredifferentiable.com/2024-02-27-PDEs-5-Fractional_Sobolev_spaces/#:~:text=2020%20page%20390.-,Theorem%2020,-(Fractional%20trace%20theorem">theory
of the trace
operator</a>,
we know that this is equivalent to $g \in H^{m-1/2}(\partial \Omega )$.
Then, by forming $w:= u-\widetilde{g}$ we obtain that $w$ solves the
homogeneous Dirichlet problem

<div>
$$\begin{aligned}
\begin{cases}
\mathcal{L}w =\widetilde{f} & \text{in } \Omega ,          \\
w=0           & \text{on } \partial \Omega ,
\end{cases}
\end{aligned}$$
</div>

where

<div>
$$\begin{aligned}
\widetilde{f}:= f-\mathcal{L}\widetilde{g}= f -\nabla \cdot (\mathbf{A} \nabla \widetilde{g}) -\mathbf{b} \cdot \nabla \widetilde{g} -c \widetilde{g} \in H ^{-1} (\Omega ).
\end{aligned}$$
</div>

The transformation $u \leftrightarrow w$ maintains
regularity up to order $m$ for $g \in H^{m-1/2}(\Omega )$ and as a
result, we can apply all the previous results on well-posedness, the
spectrum of $\mathcal{L}$ and regularity to the problem
(\ref{PDE Dirichlet}) . For example, the following holds.


<b>Theorem 20</b>. Let $\Omega$ be a bounded domain with $C^{0,1}$
boundary then

1.  The non-homogeneous Dirichlet problem
(\ref{PDE Dirichlet})  is well-posed for
$g \in H^{1/2}(\partial \Omega )$ if and only if the homogeneous
problem (\ref{PDE})  is
well posed.

2.  The Fredholm alternative (Theorem
<a href="#well-posedness Fredholm">7</a>) holds where we replace
$H\U 0^1(\Omega )$ by the subspace of $H^1(\Omega )$ whose trace is
equal to $g$.

3.  If $g \in H^{k+3/2}(\partial \Omega )$, then
$u \in H^{k+2}(\Omega )$ under the same conditions of Theorem
<a href="#higher regularity boundary">18</a> on $\Omega$ and the
coefficients of $\mathcal{L}$.


## Neumann and Robin boundary conditions

Consider a bounded domain $\Omega$ with boundary of type $C^{0,1}$
(Lipschitz boundary). The elliptic Robin boundary condition problem is


<div>
$$\begin{align}
\label{PDE Neumann}
\begin{cases}
\mathcal{L}u =f                                   & \text{in } \Omega ,          \\
\mathbf{A} \nabla u \cdot \mathbf{n} =g + \sigma u & \text{on } \partial \Omega ,
\end{cases}.
\end{align}$$
</div>

The Neumann boundary condition problem is the case where
$\sigma =0$. An integration by parts shows that the weak formulation of
(\ref{PDE Neumann})  is

<div>
$$\begin{align}
\label{weak def Neumann}
B(u,v):= \int\U {\Omega } \mathbf{A} \nabla u \cdot \nabla v +\int\U {\Omega } \mathbf{b} \nabla u \cdot \nabla v +\int\U {\Omega } c u v+ \int\U {\partial \Omega } \sigma u v  =\int\U {\Omega } f v +\int\U {\partial \Omega } g v=: \ell (v).
\end{align}$$
</div>

For the weak form to be well defined we need for $f$ to
be in the dual space $H^1(\Omega )'$ (this is
<a href="https://nowheredifferentiable.com/2024-02-27-PDEs-5-Fractional_Sobolev_spaces/#:~:text=Theorem%2016.-,As,-a%20final%20note">different</a>
from $H^{-1}(\Omega ):= H^1(\Omega )'$)and
$g \in H^{-1/2}(\partial \Omega )$ . A similar reasoning to previously
shows the following.


<b>Theorem 21</b>. Let $\Omega$ be a bounded domain,
$f \in H^{1}(\Omega )', g \in H^{-1/2}( \partial \Omega )$ and
$\sigma \in L^\infty(\partial \Omega )$.

1.  Let $\mathbf{b}=0$ and $c, \sigma  \geq 0$. Suppose both $c, \sigma$
are not identically zero. Then the Robin boundary condition problem
(\ref{weak def Neumann})  has a unique solution
$u \in H^1(\Omega )$.

2.  The well posedness of the modified problem
$\mathcal{L}u + \lambda u=f$ and the Fredholm alternative of Theorem
<a href="#mod">6</a> and Theorem
<a href="#well-posedness Fredholm">7</a> hold swapping everywhere
$H\U 0^1(U)$ with $H^1(\Omega )$ and $H^{-1}(\Omega )$ with
$H^{1}(\Omega )'$.

3.  Let $\partial \Omega \in C^{k+2}$. If $u$ solves
(\ref{PDE Neumann})  and

<div>
$$\begin{aligned}
& A\U {ij} \in C^{1}(\Omega )\cap W^{k+1, \infty}(\Omega ), \quad b\U i,c \in W^{k, \infty}(\Omega ), \quad \sigma \in W^{k+1, \infty}(\partial \Omega ) \\
& f \in H^{k}(\Omega ), \quad g \in H^{k+1/2}(\partial \Omega ).

\end{aligned}$$
</div>

Then, $u \in H^{k+2}(\Omega )$ with


<div>
$$\begin{aligned}
\left\lVert u \right\rVert\U {H^{k+2}(\Omega )} \lesssim\U {\mathbf{A},\mathbf{b},c, \sigma,  \Omega } \left\lVert f \right\rVert\U {H^k(\Omega )}+\left\lVert g \right\rVert\U {H^{k+1/2}(\partial \Omega )}+\left\lVert u \right\rVert\U {L^2(\Omega )}.

\end{aligned}$$
</div>





<b>Proof.</b> Under the conditions of Point $1$, the bilinear form $B$ is
coercive (this can be show by a proof by contradiction see for example
<a href="https://archive.org/details/MikhailovPartialDifferentialEquations">Mikhailov, 1978</a> page 146). As a result, the Lax-Milgram theorem implies
the existence of a unique solution $u \in H^1(\Omega )$.

The second point is a repetition of what was already shown for the
homogeneous Dirichlet problem, for large $\lambda$, the modified
bilinear form $B\U \lambda$ si coercive and the Fredholm alternative
holds.

The third point can be seen by first repeating the proof of Theorem
<a href="#improved regularity boundary">17</a> where with the notation of
this theorem, now $\widetilde{u}$ solves

<div>
$$\begin{aligned}
\begin{cases}
\mathcal{L}\widetilde{u} =\widetilde{f}                                             & \text{in } \widetilde{\Omega },            \\
\mathbf{A} \nabla \widetilde{u} \cdot \mathbf{n} =\widetilde{g} + \widetilde{\sigma} \widetilde{u} & \text{on } \partial \widetilde{\Omega\U 0 }.
\end{cases}

\end{aligned}$$
</div>

As a result, integrating by parts against
$\widetilde{v}:=D\U j^{-h}\eta^2 D\U j^h \widetilde{u}$ is valid for small
$h$ and $j \neq d$ and gives

<div>
$$\begin{aligned}
\int\U {\widetilde{V}} \widetilde{\mathbf{A}} \nabla \widetilde{u} \cdot \nabla \widetilde{v} +\int\U {\widetilde{V}} \widetilde{\mathbf{b}} \nabla \widetilde{u} \cdot \nabla \widetilde{v} +\int\U {\widetilde{V}} \widetilde{c} \widetilde{u} \widetilde{v} +\int\U {\partial \widetilde{\Omega\U 0 }} \widetilde{\sigma} \widetilde{u} \widetilde{v} =\int\U {\widetilde{V}} \widetilde{f} \widetilde{v}+ \int\U {\partial \widetilde{\Omega\U 0 }} \widetilde{g} \widetilde{v}.

\end{aligned}$$
</div>

Using a discrete integration by parts, Cauchy's
inequality and the regularity of the coefficients, we obtain the bound


<div>
$$\begin{aligned}
\left\lVert u \right\rVert\U {H^{2}(V\U {x\U 0} )} \lesssim \left\lVert u \right\rVert\U {H^2(\widetilde{V} )} \lesssim \left\lVert f \right\rVert\U {H^k(\Omega )}+\left\lVert g \right\rVert\U {H^{k+1/2}(\partial \Omega )}+\left\lVert u \right\rVert\U {L^2(\Omega )}.

\end{aligned}$$
</div>

Using a covering of $\Omega$ gives $u \in H^2(\Omega )$
and the result follows by induction as in Theorem
<a href="#higher regularity boundary">18</a>. ◻


### The Dirichlet problem with Neumann boundary conditions

As an example of some interest, in the simple case where $\mathbf{A}$ is the
identity and $\mathbf{b},c, g$, are zero (the Poisson equation with Neumann
boundary conditions), the weak formulation is

<div>
$$\begin{aligned}
\int\U {\Omega } \nabla u \cdot \nabla v =\int\U {\Omega } f v , \quad\forall v \in H^1(\Omega )
\end{aligned}$$
</div>

Note carefully that $B$ is not coercive on
$H^1(\Omega )$ as <a href="https://nowheredifferentiable.com/2023-07-12-PDEs-3-Sobolev_spaces/#:~:text=in%20future%20posts-,Theorem,-14%20(Poincar%C3%A9%20inequality">Poincaré's
inequality</a>
does not hold for Neumann boundary conditions.

 <a name="eigensapace">
<b>Exercise 10</b> </a> . Show that $\mathcal{L}= \Delta$ has the eigenvalue
$\lambda =0$. Show that, if $\Omega$ decomposes into $n$ connected
components $\Omega \U 1,...,\Omega \U n$, then the eigenspace of
$\lambda =0$ is $n$-dimensional and spanned by the indicator functions
$1\U {\Omega\U 1},..., 1\U {\Omega \U n}$ . In particular, the eigenspace of
$\lambda =0$ is one-dimensional if $\Omega$ is connected.


<div class="exercise-container">
<button class="exercise-button" onclick="toggleExercise(this)">Hint</button>
<div class="exercise-text">
Since $\Omega$ is bounded $1\U {\Omega \U i} \in H^1(\Omega )$
and $\Delta 1\U {\Omega\U i} =0$. Let $u \in H^1(\Omega )$ be an
eigenfunction of $\Delta$ with eigenvalue $0$. Then, by the weak
formulation of the Laplacian, we have that

<div>
$$\begin{aligned}
\int\U {\Omega } |\nabla u|^2 = 0.

\end{aligned}$$
</div>

That is, $\nabla u=0$ almost everywhere. By one
dimensional calculus we know that $u$ is constant on each connected
component and the result follows.
</div>
</div>


<b>Exercise 11</b>. Let $\Omega$ decompose into $n$ connected components
$\Omega \U 1,...,\Omega \U n$. Show that, for $f \in L^2(\Omega )$, the
Laplace equation $\Delta u =f$ has a weak solution $u \in H^1(\Omega )$
if and only if

<div>
$$\begin{aligned}
\int\U {\Omega\U i } f =0, \quad \forall i=1,...,n.

\end{aligned}$$
</div>

Furthermore, show that the solution is unique up to a
constant on each connected component $\Omega\U i$.


<div class="exercise-container">
<button class="exercise-button" onclick="toggleExercise(this)">Hint</button>
<div class="exercise-text">
Apply the final point of the Fredholm alternative (Theorem
<a href="#well-posedness Fredholm">7</a>) together with Exercise
<a href="#eigensapace">10</a>.
</div>
</div>

A (possibly not updated) pdf version of this page is provided [here](/assets/pdfs/PDEs/Elliptic_PDE_1.pdf).