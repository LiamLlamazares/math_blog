---
layout: post
title: Physical derivation of parabolic and elliptic PDE
subtitle: Just have to balance the mass
thumbnail-img: /assets/img/Marsden_fluid_mechanics.jpg
share-img: /assets/img/Marsden_fluid_mechanics.jpg
tags: [PDEs]
authorpost: L.Llamazares-Elias
---

# Summary

Partial differential equations (PDEs) are a fundamental tool that can be
used to describe the evolution and stationary state of a physical
system. These PDEs can be derived by understanding the processes that
cause the "mass" of the system to vary via a balance equation. Namely
diffusion, advection, reaction and sources.

# Notation

Following the convention in fluid mechanics, vectors in $\mathbb{R}^d$
are written in bold to differentiate them from scalars in $\mathbb{R}$.
Given $u \in C^1(\mathbb{R}^d)$ and
$\mathbf{v} \in C^1(\mathbb{R}^d \to \mathbb{R}^d)$ we write the gradient
and divergence as

<div>
$$\begin{aligned}
\nabla u :=(\partial \U 1 u,\ldots, \partial \U d u), \quad \nabla \cdot \mathbf{v}:= \sum\U {i=1}^{d} \partial \U i v\U i.
\end{aligned}$$
</div>

For example, the Laplacian $\Delta$ is equal to
$\nabla \cdot \nabla$.

# Introduction

Welcome to the fourth post on our series on PDEs. In previous posts, we
built up the theory of function spaces necessary to address the
fundamental problems of these equations. However, before we dive into
more mathematical waters, it is convenient to get a sense of where these
equations come from and what each term within the PDEs means. This can
help us understand more deeply the equations and motivates the theory to
follow.

We begin by giving a physical derivation of the parabolic equation

<div>
$$\begin{align}
\label{PDE}
\partial\U t u-\nabla \cdot (\mathbf{A}\nabla u) +\mathbf{b} \cdot \nabla u + cu = f,
\end{align}$$
</div>

and its stationary version

<div>
$$\begin{aligned}
-\nabla \cdot (\mathbf{A}\nabla u) +\mathbf{b} \cdot \nabla u + cu =f,
\end{aligned}$$
</div>

by calculating the rate of change of the "mass" of the
system in terms of its flow. Then, we introduce boundary effects and
wrap up with some examples.

# A physical derivation

**Warning, proceed with caution**: the following section contains a
physical derivation of (\ref{PDE}) . As a result, some physical intuition and approximate
reasoning is used. All functions are supposed smooth and integrable as
needed. This disclaimer out of the way, let's consider a spatial domain
$\Omega \subset \mathbb{R}^d$ filled with fluid in which some solute is
dissolved. Our goal is to describe the concentration (density) of the
solute $u(t,\mathbf{x})$ as the system evolves in time and space. We know
that the amount of fluid within any subregion $V \subset  \Omega$ is

<div>
$$\begin{aligned}
m(t)=\int\U {V} u(t,\mathbf{x}) \,\mathrm{d}\mathbf{x}  .
\end{aligned}$$
</div>

This mass changes as the solute moves around $\Omega$.
By conservation of mass, the mass of solute $m(t+h)$ at a small instant
of time later is equal to the mass $m(t)$ present at time $t$ plus the
mass of any other solute that entered the domain in that small time

<div>
$$\begin{aligned}
m(t+h)=m(t)+ \text{mass that entered at time } t .
\end{aligned}$$
</div>

The solute can only enter $V$ if there is some external
source, such as a pipe adding a mass $f(t,\mathbf{x})$ of solute at point
$\mathbf{x}$, or by flowing its boundary $\partial V$. We now consider this
second case. Let $\mathbf{F}(t,\mathbf{x} )$ describe the magnitude and velocity
of the flow (flux) of the solute and consider a point $\mathbf{x}$ on the
boundary. If the flux $\mathbf{F}(t,\mathbf{x} )$ is orthogonal to the outward
pointing unit normal $\mathbf{n}(\mathbf{x})$ at $\mathbf{x}$ (that is, tangent to
$\partial  V$ at $\mathbf{x}$), no fluid enters $V$ through $\mathbf{x}$.
Whereas if the flux is parallel to $\mathbf{n}(\mathbf{x})$, all of the flow at
$\mathbf{x}$ enters $V$ if $\mathbf{F}(t,\mathbf{x})$ is pointed in the opposite or
leaves if $\mathbf{F}(t,\mathbf{x})$ and $\mathbf{n}(\mathbf{x})$ have the same
direction. Otherwise, we get something in between, depending on the
angle that $\mathbf{F}(t,\mathbf{x})$ and $\mathbf{n}(\mathbf{x})$ form. This situation
can be described as follows

<div>
$$\begin{aligned}
m(t+h)=m(t) +h \left( \int\U {V} f(t,\mathbf{x} ) \,\mathrm{d}x- \int\U {\partial V} \mathbf{F}(t, \mathbf{x})\cdot \mathbf{n}(\mathbf{x} )    \,\mathrm{d}\mathbf{x}  \right),
\end{aligned}$$
</div>

where the minus sign means that if the solute is flowing
in the same direction as $\mathbf{n}$, mass decreases, and if it flows in
the opposite direction, mass increases, as $\mathbf{n}(\mathbf{x})$ points
outwards. Rearranging terms and taking limits when $h$ goes to zero
gives

<div>
$$\begin{aligned}
\partial \U t m(t)=\int\U {V}f(t,\mathbf{x} ) \,\mathrm{d}\mathbf{x}   -\int\U {\partial V}  \mathbf{F}(t, \mathbf{x})\cdot \mathbf{n}(\mathbf{x} )    \,\mathrm{d}\mathbf{x}  .
\end{aligned}$$
</div>

Now, the mass of the solute in $V$ is just the integral
of the density over $V$. Using this and the [divergence
theorem](https://en.wikipedia.org/wiki/Divergence_theorem#:~:text=%5Bedit%5D-,For,-bounded%20open%20subsets)
gives

<div>
$$\begin{align}
\label{balance integral}
\int\U {V}\partial \U t u(t,\mathbf{x} )  \,\mathrm{d}\mathbf{x} = \int\U {V}f(t,\mathbf{x} ) \,\mathrm{d}x -\int\U {V}  \nabla \cdot  \mathbf{F}(t, \mathbf{x})\   \,\mathrm{d}\mathbf{x}
\end{align}$$
</div>

This is the integral form of the balance equation. To
obtain the non-integral form, note that, since
(\ref{balance integral}) holds for all $V \subset  U$, the
integrands must be equal (almost) everywhere, that is

<div>
$$\begin{align}
\label{balance}
\partial \U t u(t,\mathbf{x} )   = f(t,\mathbf{x})-\nabla \cdot  \mathbf{F}(t, \mathbf{x})
\end{align}$$
</div>

We would now like to express the flux in terms of the
properties of the fluid and domain. We recall that $\mathbf{F}$ determines
the magnitude and direction of the flow of the solute. We distinguish
two possible reasons for the movement of the solute.

a) Diffusion: This is the process that causes the solute to move from
areas of lower to higher concentration. A possible physical
approximation is to consider the diffusion to be proportional to the
gradient of the density, that is

<div>
$$\begin{aligned}
\mathbf{F}\U {\text{diffusion}} = -\mathbf{A}\nabla u  .

\end{aligned}$$

</div>

Here, $\mathbf{A}(\mathbf{x} ) \in \mathbb{R}^{d\times d}\U +$
is called the diffusivity, diffusion coefficient or viscosity
depending on the context and is a positive definite matrix. The
diffusivity encodes the preference of the solute to flow in one
direction or another depending on the properties of the domain
itself. If $\mathbf{A}$ has orthonormal eigensystem

<div>
$$\begin{aligned}
\{(\mathbf{e\U 1},\lambda \U 1 ),(\mathbf{e}\U 2, \lambda \U 2 ),\ldots, (\mathbf{e}\U 3 ,\lambda \U d)\} .

\end{aligned}$$

</div>

Then

<div>
$$\begin{align}  \label{diffusion}
\mathbf{F}\U {\text{diffusion}} = -\mathbf{A}\nabla u=-  \lambda \U j(\nabla u\cdot \mathbf{e}\U j )\mathbf{e}\U j .

\end{align}$$

</div>

That is, the solute diffuses in the direction of
$\mathbf{e}\U j$ with speed proportional to $\lambda\U j$. For example, if
$\mathbf{A}$ is a constant multiple of the identity, there is no
preferred direction of flow. In this case, one says that the flow is
homogeneous. The minus sign in
(\ref{diffusion}) together with the imposition that $\mathbf{A}$ is
positive definite means that diffusion occurs from areas of lower to
higher concentration.

If diffusion is the only cause of movement in the fluid,
$\mathbf{F}= - \mathbf{A}\nabla u$ and substituting into the balance
equation (\ref{balance}) gives the (non-homogeneous) heat equation

<div>
$$\begin{aligned}
\partial\U tu= \nabla \cdot (\mathbf{A}\nabla u)+f .

\end{aligned}$$

</div>

b) Advection: Another possible cause for the flow of the solute
within $\Omega$ is that the fluid itself is moving with some
velocity $\mathbf{v}$, transporting along the particles of the solute.
The flux due to advection is

<div>
$$\begin{aligned}
\mathbf{F}\U {\text{advection} }= u \mathbf{v} .

\end{aligned}$$

</div>

The flux is thus made up of the sum of a diffusion and advection
component:

<div>
$$\begin{aligned}
\mathbf{F}=\mathbf{F}\U {\text{diffusion} }+ \mathbf{F}\U {\text{advection} } =- \mathbf{A}\nabla u+ u \mathbf{v}   .
\end{aligned}$$
</div>

Substituting this into the balance equation
(\ref{balance})
gives

<div>
$$\begin{align}
\label{balance2}
\partial\U t u=\nabla \cdot (\mathbf{A}\nabla u) -\nabla \cdot  (u \mathbf{v})+ f.
\end{align}$$
</div>

Finally, we may have a change in the concentration of
the solute due to the solute reacting with another substance. For
example, $u$ could be the density of a contaminant which we are
eliminating from the fluid via a chemical process. Alternatively, $u$
could be a radioactive substance which is decaying. The reaction term
is typically denoted by $R(u)$. In the simplest case, $R(u)$ is linear
in $u$, equal to $-ru$ where the sign of $r$ determines whether the
concentration of solute decreases (if $r>0$, as in the previous
scenarios) or increases (if $r<0$, for example, $u$ could represent the
concentration of a population of algae). Adding this reaction term to
our balance equation (\ref{balance2}) gives

<div>
$$\begin{aligned}
\underbrace{\partial\U t u}\U {\text{Rate of change} }= \underbrace{\nabla \cdot (\mathbf{A}\nabla u)}\U {\text{Diffusion}} - \underbrace{\nabla \cdot ( \mathbf{v}u)}\U {\text{Advection}} -\underbrace{ru}\U {\text{Reaction}}  +\underbrace{f}\U {\text{Source}},
\end{aligned}$$
</div>

where all terms are functions of $t,\mathbf{x}$. Applying
the chain rule we may decompose

<div>
$$\begin{aligned}
\nabla \cdot ( \mathbf{v}u)= \mathbf{v}\cdot \nabla u+ (\nabla \cdot \mathbf{v})u .
\end{aligned}$$
</div>

The first summand represents the transport of the solute
due to the movement of the fluid, and the second the transport due to
the contraction of the fluid, if $\nabla \cdot \mathbf{v}<0$, or its
expansion, if $\nabla \cdot \mathbf{v}=0$. If $\nabla \cdot \mathbf{v} =0$, the
fluid neither expands nor compresses and is called incompressible. In
any case, writing (for notational consistency)
$\mathbf{b} :=\mathbf{v}, c=r+\nabla \cdot \mathbf{v}$ gives

<div>
$$\begin{align}
\label{parabolic}
\partial\U t u-\nabla \cdot (\mathbf{A}\nabla u) +\mathbf{b} \cdot \nabla u + c u= f  .
\end{align}$$
</div>

Equation
(\ref{parabolic}) is a prototypical parabolic equation. Suppose now
that our system has and reaches an equilibrium state (a state in which
the concentration of solute stays constant in time once reached). Then
$\partial \U t u=0$ and we obtain

<div>
$$\begin{align}
\label{elliptic}
-\nabla \cdot (\mathbf{A}\nabla u) + \mathbf{b} \cdot \nabla u+cu = f,
\end{align}$$
</div>

Equations
(\ref{parabolic}) , and
(\ref{elliptic})
are, respectively, the parabolic and elliptic PDE we were aiming for
and, as we have just seen, each of their parts has a precise physical
meaning in terms of diffusion, advection, reaction and source.

# Boundary conditions

In an application, the system we are studying will evolve within some
smooth bounded domain $\Omega$. In order for a unique solution to be
defined it is necessary to impose a boundary condition for what $u$ is
allowed to do on $\Omega$ (as well as an initial condition
$u(0,\mathbf{x})=u\U 0(\mathbf{x})$ in the parabolic case
(\ref{parabolic}) ).

**Example 1**. Consider the Poisson equation

<div>
$$\begin{align}
\label{Poisson}
\Delta u=f.

\end{align}$$

</div>

If $u$ solves
(\ref{Poisson}) ,
then $u+p$ also solves (\ref{Poisson}) where $p$ is any polynomial of degree $0$ or $1$.

There are multiple types of boundary conditions which can be specified,
each one corresponding to a particular behaviour of the system.

a) Dirichlet boundary condition: This is the additional imposition
that

<div>
$$\begin{aligned}
u=g \text{ on } \partial\Omega,

\end{aligned}$$

</div>

where $g$ is some function defined on
$\partial \Omega$ and $u$ is restricted to $\partial\Omega$ through
the trace theorem developed in [the previous
post](https://nowheredifferentiable.com/2023-07-12-PDEs-3-Sobolev_spaces/).
In the context of the diffusion of heat, $\Omega$ could be a rod
which is kept at a constant temperature at its endpoints.

b) Robin boundary condition: Here, it is imposed that

<div>
$$\begin{align}  \label{Robin}
-\mathbf{F}\cdot  \mathbf{n} =g \text{  on } \partial \Omega,

\end{align}$$

</div>

where $\mathbf{F}$ is the flux and in our case is
$\mathbf{F}=-\mathbf{A} \nabla u+ \mathbf{v}u$. This condition imposes that a
"mass" $g$ of substance (solute, heat, etc.) enters the domain at
each point of the boundary (or leaves if the minus in
(\ref{Robin}) is
omitted).

c) Neumann boundary condition: This is a particular case of the Robin
boundary condition where there is no diffusion. In this case,
(\ref{Robin})
becomes

<div>
$$\begin{aligned}
(\mathbf{A} \nabla u) \cdot n=g \text{  on } \partial \Omega.

\end{aligned}$$

</div>

The above is known as a Neumann boundary condition.
If the material is homogeneous, that is, $\mathbf{A}=\mathbf{I}$, the
special notation

<div>
$$\begin{aligned}
\frac{\partial u}{\partial \mathbf{n}}:= \nabla u \cdot  \mathbf{n} =g \text{  on } \partial \Omega,

\end{aligned}$$

</div>

is used. Here $\frac{\partial u}{\partial \mathbf{n}}$
is known as the normal derivative.

d) Mixed boundary condition: This corresponds a mix of the preceding.
That is, $\partial \Omega$ is partitioned into
$\Gamma \U 1, \Gamma \U 2$, and the following boundary conditions are
imposed.

<div>
$$\begin{aligned}
u=g\U 1 \text{  on }  \Gamma \U 1,  \text{ and }  -\mathbf{F} \cdot n=g\U 2 \text{  on }  \Gamma \U 2.

\end{aligned}$$

</div>

e) Periodic boundary conditions: Here the domain is an interval
$\Omega=(\mathbf{a}, \mathbf{b})$ and we require that for all
$k \in \\{1,\ldots,d\\}$

<div>
$$\begin{aligned}
u(x\U 1,\ldots,a\U k,\ldots, x\U d)=u({x}\U 1,\ldots,{b}\U k,\ldots, {x}\U d).

\end{aligned}$$

</div>

Equivalently, $u$ is a function of the torus
$\mathbb{R}^d/ (\mathbb{Z}^d \cdot (\mathbf{b}-\mathbf{a}))$. These boundary
conditions are typically used to approximate a system evolving on a
very large domain by working only with a representative cell
$[\mathbf{a},\mathbf{b}]$.

Finally, mathematically, it also makes sense to work with infinite
domains such as the whole Euclidean space $\mathbb{R}^d$. In this case,
rather than a boundary condition, one imposes suitable decay on the
function such as $u \in L^p(\mathbb{R}^d)$ or its derivatives such as
$u \in W^{k,p}(\mathbb{R}^d)$.

We end the post by commenting that non-linear terms may be considered in
the PDE (\ref{parabolic}) -(\ref{elliptic}) . Many examples can be found
[here](https://en.wikipedia.org/wiki/List_of_nonlinear_partial_differential_equations).
However, the mathematical theory of nonlinear PDE is much more
complicated (think Navier Stokes). The linear case, which we begin to
develop in the next post, will keep us busy for a while.

A (possibly not updated) pdf of version of this page is provided [here](/assets/pdfs/PDEs/Physical_PDE.pdf).
