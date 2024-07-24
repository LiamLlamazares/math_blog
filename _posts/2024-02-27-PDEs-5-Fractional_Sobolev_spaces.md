---
layout: post
title: Fractional Sobolev spaces
subtitle: Filling in the gaps
thumbnail-img: /assets/img/Leoni_fractional.jpg
share-img: /assets/img/Leoni_fractional.jpg
tags: [PDEs]
authorpost: L.Llamazares-Elias
---

# Summary

1.  There are three ways to define Sobolev spaces with fractional
    regularity $s$ and integrability $p$:

1.  The spaces $W^{s,p}(\Omega ), B^{s,p}(\Omega )$ are defined by
    using the analogous to the definition of Hölder spaces. Both
    spaces are equal when $s$ is not an integer.

1.  The space $H^{s,p}(\Omega )$ is defined by using the Fourier
    transform and coincides with $W^{s,p}(\Omega )$ for integer $s$.

1.  All these spaces coincide with $H^s(\Omega )$ when $p=2$.

1.  There is a natural correspondence between negative regularity and
    the dual. Additionally, negative regularity can be obtained by
    differentiating functions with higher regularity.

1.  Fractional sobolev spaces appear naturally in the study of PDEs. For
    example, the trace of Sobolev functions $W^{s,p}(\Omega)$ is equal
    to the fractional space $B^{s-1/p,p}(\partial \Omega)$. And finer
    embeddings and regularity results can be obtained by using these
    spaces.

# Introduction

In previous posts, we covered the theory of [Sobolev
spaces](https://nowheredifferentiable.com/2023-07-12-PDEs-3-Sobolev_spaces/)
$W^{k,p}(\Omega )$ where $k$ is an integer. In the case $k=2$ and when
$\Omega =\mathbb{R}^d$ we saw that this space coincided with
$H^k(\mathbb{R}^d)$. Furthermore, [we also
saw](https://nowheredifferentiable.com/2023-01-29-PDE-1-Fourier/) how to
define $H^s(\mathbb{R}^d)$ when $s$ was any real number. This motivates
the following two questions.

1.  How can we define $H^s(\Omega )$ when $\Omega$ is not $\mathbb{R}^d$
    and $s$ is not an integer ?

2.  Is it possible to extend such a definition to other orders of
    integrability $p$?

In this post, we aim to answer these questions. We will see that both of
these questions can be answered in the affirmative. If the domain
$\Omega$ is smooth enough, the first point can be resolved by
restricting functions in $H^s(\mathbb{R}^d)$ to $\Omega$. The second
point is trickier and, in fact, like any good trick question, has
multiple answers. Three, to be precise. This leads to the theory of
Bessel spaces, Sobolev-Slobodeckij spaces and Besov spaces

<div>
$$\begin{aligned}
H^{s,p}(\Omega ),W^{s,p}(\Omega ),B^{s,p}(\Omega ).
\end{aligned}$$
</div>

We will cover the basic properties of these spaces as
well as their relationship to each other with a special focus on
$W^{s,p}(\Omega )$ which is the most widely used. We will see how these
spaces can be used to obtain finer regularity results, such as in the
trace theorem or Sobolev embeddings. The material in this post is mostly
based on [Leoni, 2020](https://www.google.co.uk/books/edition/A_First_Course_in_Fractional_Sobolev_Spa/lh2_EAAAQBAJ?hl=en&gbpv=1&dq=giovanni+leoni+fractional+sobolev&pg=PP1&printsec=frontcover), [Agranovich, 2020](https://link.springer.com/book/10.1007/978-3-319-14648-5),
[Di, 2020](https://www.sciencedirect.com/science/article/pii/S0007449711001254), [Triebel, 2020](https://link.springer.com/book/10.1007/978-3-0346-0419-2). The material can be quite
technical, and there are multiple $800$ plus page books on the subject,
so in many cases, we will state the main results, providing references
for the proofs, as well as proving some of the more tractable results.

## Preliminaries

In terms of notation, we will always denote $U$ by an arbitrary open
subset of $\mathbb{R}^d$ whereas $\Omega \subset \mathbb{R}^d$ will be
open with a smooth enough boundary (in a sense to be made precise
later).

We make frequent use of the fact that, as
[shown](https://nowheredifferentiable.com/2023-07-12-PDEs-3-Sobolev_spaces/#:~:text=we%20would%20like%20to%20see%20what%20some%20of%20them%20look%20like.)
in a previous post, functions in $L^p(U)$ can be identified as elements
of the larger space of distributions
$\mathcal{D}'(U ):= C\U c^\infty(U)'$. This is done by identifying a
function $f \in L^p(U)$ with the linear functional

<div>
$$\begin{aligned}
T\U f:\phi \mapsto \int\U U f\phi \,\mathrm{d}x.
\end{aligned}$$
</div>

This identification between $f$ and $T\U f$ allows us to
extend by
[duality](https://nowheredifferentiable.com/2023-01-29-PDE-1-Fourier/#:~:text=is%20called%20the-,duality,-method%20and%20appears)
operators that are defined on $C\U c^\infty(U)$ to $L^p(U)$. For example,
given $u \in L^p(U) \in \mathcal{D}'(\Omega )$ we can define its Fourier
transform $\mathcal{F}u$ and $\alpha$-th derivative $D^\alpha u$ to be
the distributions defined by

<div>
$$\begin{aligned}
(\varphi ,\mathcal{F}u):=(\mathcal{F}^{-1}\varphi ,u),\quad (\varphi ,D^\alpha u):=(-1)^{\left| \alpha \right|}(D^\alpha \varphi ,u), \quad \forall \varphi \in C\U c^\infty(U).
\end{aligned}$$
</div>

The above definition is justified by the fact that if it
turns out that $u$ is smooth and integrable enough after all, this
coincides with the usual definitions of $\mathcal{F}, D^\alpha$.

# Fractional Sobolev spaces: three definitions

The definitions developed in the next three subsections can be found in
[Agranovich, 2020](https://link.springer.com/book/10.1007/978-3-319-14648-5) page 222.

## Sobolev-Slobodeckij spaces

 <a name="soledkij def">
<b>Definition 1</b> </a>  (Sobolev-Slobodeckij spaces). Let $s=k+\gamma$ where
$k \in \mathbb{N}\U 0$, and $\gamma \in [0,1)$. Then, given
$p \in [1,\infty)$ and an arbitrary open $U \subset \mathbb{R}^d$ we
define

<div>
$$\begin{aligned}
W^{s ,p}(U):= \left\{u \in W^{k ,p}(U): \left\lVert u \right\rVert\U {W^{s,p}(U)}<\infty\right\},

\end{aligned}$$

</div>

where

<div>
$$\begin{align}
\label{norm def}
\left\lVert u \right\rVert\U {W^{s,p}(U)}:= \left(\left\lVert u \right\rVert\U {W^{k,p}(U)}^p+ \sum\U {\left| \alpha \right|=k }\int\U {U}\int\U {U}\frac{\left| D^\alpha u(x+y)-D^\alpha u(x) \right|^p}{\left| y \right|^{d+\gamma p}}\,\mathrm{d}x \,\mathrm{d}y\right)^\frac{1}{p}.

\end{align}$$

</div>

For $p = \infty$, we define
$W^{s,\infty}(U):= C^{k,\gamma}(U)$. The norm is then given by

<div>
$$\begin{aligned}
\left\lVert u \right\rVert\U {W^{s,\infty}(U)}= \left\lVert u \right\rVert\U {C^{k}(U)}+ \sum\U {\left| \alpha \right| =k}  \sup \U {x, y \in U, x \neq y} \frac{|D^\alpha u(x)- D^\alpha u(y)|}{|x-y|^\gamma }.

\end{aligned}$$

</div>

We will later define $W^{s,p}(U)$ also for negative $s$ (see Definition
<a href="#negative s Slobodeckij">13</a>). We observe that the above
definition coincides with our usual definition of Sobolev space when
$s=k \in \mathbb{N}\U 0$ and mimics that of the Hölder spaces, coinciding
exactly when $p=\infty$.

<b>Exercise 1</b>. Show that $W^{s,p}(U)$ is a Banach space.

<div class="exercise-container">
<button class="exercise-button" onclick="toggleExercise(this)">Hint</button>
<div class="exercise-text">
To show that $|| \cdot ||\U {W^{s,p}(U)}$ is a norm apply
Minkowski's inequality to $u$ and to

<div>
$$\begin{aligned}
f\U u(x,y):=\frac{D^\alpha u(x+y)-D^\alpha u(x)}{y^{\frac{d}{p}+\gamma}}.

\end{aligned}$$

</div>

Given a Cauchy sequence show that, since $L^p(U)$ is
complete, $u\U n \to u$ in $L^p(U)$ and that $f\U {u\U n} \to f\U u$ in
$L^p(U\times U)$ to conclude that $u\U n \to u$ in $W^{s,p}(U)$.

</div>
</div>

Though the Sobolev-Slobodeckij spaces can be defined for any open set
$U$, they are most useful when $U=\mathbb{R}^d$ or $U$ is regular
enough. Otherwise, basic properties such as the following break down

 <a name="inclusion ordered by regularity">
<b>Proposition 2</b> </a>  (Inclusion ordered by regularity). Let $\Omega$ be an
[extension
domain](https://nowheredifferentiable.com/2023-07-12-PDEs-3-Sobolev_spaces/#:~:text=extend%20Sobolev%20functions)
for $W^{1,p}$. Then, for $p \in [1,\infty)$ and $0<s<s'$ it holds that

<div>
$$\begin{aligned}
W^{s',p}(\Omega )\hookrightarrow W^{s,p}(\Omega ).

\end{aligned}$$

</div>

The proof can be found in [Di, 2020](https://www.sciencedirect.com/science/article/pii/S0007449711001254) page 10. The regularity
of the domain is necessary to be able to extend functions in
$W^{1,p}(\Omega )$ to $W^{1,p}(\mathbb{R}^d)$. The result is not true
otherwise, and an example is given in this same reference.

## Bessel potential spaces

We now give a second definition of fractional Sobolev spaces through the
Fourier transform. Here, it is immediately possible to define everything
for negative $s$.

<b>Definition 3</b>. Let $s\in\mathbb{R}$ and
$u \in \mathcal{S}'(\mathbb{R}^d)$. We define the Bessel potential
operator $\Lambda^s$ by

<div>
$$\begin{aligned}
\Lambda^s u := \mathcal{F}^{-1}\left(\left\langle\xi\right\rangle^s \widehat{u}(\xi)\right).

\end{aligned}$$

</div>

In the definition above, we used the notation
$\left\langle\xi\right\rangle:=\sqrt{1+|\xi|^2}$. As we saw when we
studied Sobolev spaces through the [Fourier
transform](https://nowheredifferentiable.com/2023-01-29-PDE-1-Fourier/#:~:text=Sobolev%20spaces-,Sobolev%20spaces,-form%20a%20particular),
using the fact that $\mathcal{F}$ is an isometry which transforms
differentiation into polynomial multiplication

<div>
$$\begin{align}
\label{motivation Bessel}
u \in H^k(\mathbb{R}^d) \iff \Lambda^k u \in L^2(\mathbb{R}^d).
\end{align}$$
</div>

Equation
(\ref{motivation Bessel}) motivates the following extension to
general $p$.

 <a name="bessel potential def">
<b>Definition 4</b> </a>  (Bessel potential spaces on $\mathbb{R}^d$ ). Let
$s \in \mathbb{R}$ and $p \in (1,\infty)$, we define the Bessel
potential space

<div>
$$\begin{aligned}
H^{s,p}(\mathbb{R}^d):=\left\{u \in \mathcal{S}^{\prime}(\mathbb{R}^d): \Lambda ^s u \in L^p(\mathbb{R}^d)\right\},

\end{aligned}$$

</div>

and give it the norm

<div>
$$\begin{aligned}
\left\lVert u \right\rVert\U {H^{s,p}(\mathbb{R}^d)}:= \left\lVert \Lambda^s u \right\rVert\U {L^p(\mathbb{R}^d)}.

\end{aligned}$$

</div>

By construction, $H^{k,2}(\mathbb{R}^d)=H^{k}(\mathbb{R}^d)$.

<b>Exercise 2</b>. Show that $\Lambda^s\Lambda^r=\Lambda^{s+r}$. Use this
to show that the following is an invertible isomorphism

<div>
$$\begin{aligned}
\Lambda^r: H^{r+s,p}(\mathbb{R}^d) \xrightarrow{\sim}H^{s,p}(\mathbb{R}^d).

\end{aligned}$$

</div>

<div class="exercise-container">
<button class="exercise-button" onclick="toggleExercise(this)">Hint</button>
<div class="exercise-text">
Use that
$\left\langle\xi\right\rangle^s\left\langle\xi\right\rangle^r=\left\langle\xi\right\rangle^{s+r}$
and show that the inverse of $\Lambda^r$ is $\Lambda^{-r}$.
</div>
</div>

We now extend this to open domains

 <a name="bessel potential def Omega">
<b>Definition 5</b> </a>  (Bessel potential spaces on $\Omega$). Let
$U  \subset \mathbb{R}^d$ be open. We define

<div>
$$\begin{aligned}
H^{s,p}(U ):=\left\{u \in \mathcal{D}^{\prime}(U ): \text{ there exists } v \in H^{s,p}(\mathbb{R}^d) \text{ with } \left.v\right|\U {U }=u\right\},

\end{aligned}$$

</div>

and give it the norm

<div>
$$\begin{aligned}
\left\lVert u \right\rVert\U {H^{s,p}(U )}:= \inf \left\{\left\lVert v \right\rVert\U {H^{s,p}(\mathbb{R}^d)}: \left.v\right|\U {U }=u\right\}.

\end{aligned}$$

</div>

The restriction above is in the sense of distributions. That is, we
define the restriction of $u$ to $U$ as the distribution $v$ such that

<div>
$$\begin{aligned}
(\phi,u):=(\phi,v), \quad \forall \phi \in C\U c^\infty(U ).
\end{aligned}$$
</div>

<b>Observation 1</b>. It is tempting to define
$\left\lVert u \right\rVert\U {H^{s,p}(U )}:=\left\lVert \Lambda^s v \right\rVert\U {L^p(U )}$.
However, since the Fourier transform, and thus $\Lambda^s$, is a
nonlocal operator, the norm would depend on the extension $v$ of $u$ to
$\mathbb{R}^d$ and be ill-defined.

<b>Observation 2</b>. It would also make sense to define $H^{s,p}(U )$
through complex interpolation. This is likely different from the above
definition, however, as we will later see, this will coincide with the
definition above when $\Omega$ is smooth enough (for example Lipschitz).
See also [Leoni, 2020](https://www.google.co.uk/books/edition/A_First_Course_in_Fractional_Sobolev_Spa/lh2_EAAAQBAJ?hl=en&gbpv=1&dq=giovanni+leoni+fractional+sobolev&pg=PP1&printsec=frontcover) page 328 for a similar remark.

## Besov spaces

 <a name="besov def">
<b>Definition 6</b> </a>  (Besov spaces). Let $s=k\U {-}+\gamma$ where
$k\U {-} \in \mathbb{N}\U 0$, and $\gamma \in (0,1]$. Then, given
$p \in [1,\infty)$ and $\Omega  \subset \mathbb{R}^d$ be an arbitrary
open set we define

<div>
$$\begin{aligned}
B^{s ,p}(U):= \left\{u \in W^{k\U {-} ,p}(U): \left\lVert u \right\rVert\U {B^{s,p}(U)}<\infty\right\},

\end{aligned}$$

</div>

where

<div>
$$\begin{aligned}
\left\lVert u \right\rVert\U {B^{s,p}(U)}:= \left(\left\lVert u \right\rVert\U {W^{k\U {-},p}(U)}^p+ \sum\U {\left| \alpha \right|=k\U - }\int\U {U}\int\U {U}\frac{\left| D^\alpha u(x+y)-D^\alpha u(x) \right|^p}{\left| y \right|^{d+\gamma p}}\,\mathrm{d}x \,\mathrm{d}y\right)^\frac{1}{p}.

\end{aligned}$$

</div>

For $p = \infty$, we define
$B^{s,\infty}(U):= C^{k\U {-},\gamma}(U)$.

The above definition is extremely similar in form to that of the
Sobolev-Slobodeckij spaces <a href="#soledkij def">1</a>. In fact, it is equivalent when
$s \notin \mathbb{N}$. The difference is that in the definition of Besov
spaces <a href="#besov def">6</a>, we
require that $\gamma >0$. As a result, always $k\U {-}<s$. We have chosen
to indicate this fact by the index "$-$" on $k\U {-}$. An equivalent
definition is possible which extends the above to negative values of $s$

 <a name="besov def negative">
<b>Definition 7</b> </a>  (Besov spaces, negative $s$). Let $s \in \mathbb{R}$
and choose any $\sigma \not\in \mathbb{N}\U 0$ with $\sigma >0$. Then,
given $p \in [1,\infty)$ we define

<div>
$$\begin{aligned}
\|u\|\U {B^{s,p}(\mathbb{R}^d)}=\|\Lambda^{s-\sigma} u\|\U {W^{\sigma,p}(\mathbb{R}^d)}.

\end{aligned}$$

</div>

The requirement $\sigma >0$ is necessary as
$B^{s,p}(\mathbb{R}^d)\neq H^{s,p}(\mathbb{R}^d)$.

<b>Exercise 3</b>. Show that $\Lambda ^r$ defines an invertible isomorphism

<div>
$$\begin{aligned}
\Lambda ^r: B^{s,p}(\mathbb{R}^d)\xrightarrow{\sim}H^{s-r,p}(\mathbb{R}^d).

\end{aligned}$$

</div>

<div class="exercise-container">
<button class="exercise-button" onclick="toggleExercise(this)">Hint</button>
<div class="exercise-text">
Use definition <a href="#besov def negative">7</a> and that
$W^{\sigma,p}(\Omega )= B^{\sigma,p }$ for non-integer $\sigma$.
Finally, $\Lambda^r$ has inverse $\Lambda^{-r}$.
</div>
</div>

The definition of $B^{s,p}(\mathbb{R}^d)$ can then be extended to
general open sets $\Omega$ and $U$ in the same way as for the Bessel
potential spaces, once more the same observations apply.

 <a name="besov def on U">
<b>Definition 8</b> </a>  (Besov spaces on $\Omega$). Let
$\Omega  \subset \mathbb{R}^d$ be an smooth. We define,

<div>
$$\begin{aligned}
B^{s,p}(\Omega):=\left\{u \in \mathcal{D}^{\prime}(\Omega ): \text{ there exists } v \in B^{s,p}(\mathbb{R}^d) \text{ such that } \left.v\right|\U {\Omega }=u\right\},

\end{aligned}$$

</div>

and give it the norm

<div>
$$\begin{aligned}
\left\lVert u \right\rVert\U {B^{s,p}(\Omega)}:= \inf \left\{\left\lVert v \right\rVert\U {B^{s,p}(\mathbb{R}^d)}: \left.v\right|\U {\Omega }=u\right\}.

\end{aligned}$$

</div>

<b>Observation 3</b>. Different authors use different notations for these
spaces. For example, in [Triebel, 2020](https://link.springer.com/book/10.1007/978-3-0346-0419-2), the notation
$W^{s,p}(\mathbb{R}^d):= B^{s,p}(\mathbb{R}^d)$ is used. With this
notation, one has that, for $p \neq 2$, and $k \in \mathbb{N}\U 0$,

<div>
$$\begin{aligned}
W^{k,p}(\mathbb{R}^d) \neq \left\{ u \in \mathcal{D}'(\mathbb{R}^d) : D^\alpha u \in L^p(\mathbb{R}^d) \quad \forall \left| \alpha \right|\leq   k\right\}= W^{k,p}(\mathbb{R}^d).

\end{aligned}$$

</div>

This clashes with the definition of integer-valued
Sobolev spaces, so we do not use this notation. Other notations which
can be found are the notation $B^{s,p}= \Lambda^{p}\U s$ and
$H^{s,p}= \mathcal{L}^{p}\U s$. See [Stein, 2020](https://www.degruyter.com/document/doi/10.1515/9781400883882/html) and
[Biccari, 2020](https://link.springer.com/chapter/10.1007/978-3-319-97613-6_12).

## Extension domains

Though it is possible to define fractional spaces for any open set,
these are most useful when the domain is regular enough. We begin by
characterizing the set of extension domains for $W^{s,p}$. The following
result can be found in [Leoni, 2020](https://www.google.co.uk/books/edition/A_First_Course_in_Sobolev_Spaces/qoA8DwAAQBAJ?hl=en&gbpv=0) page 313.

 <a name="plump sets">
<b>Theorem 9</b> </a>  (Plump sets are extension domains). Let
$\Omega \subseteq \mathbb{R}^N$ be an open connected set, and consider
$p\in [1,+\infty]$, and $\gamma\in (0,1)$. Then, $\Omega$ is an
extension domain for $W^{\gamma, p}(\Omega)$ if and only if there exists
a constant $C>0$ such that

<div>
$$\lambda_d(B(x, r) \cap \Omega) \geq C r^d$$
</div>

for all $x \in \Omega$ and all $0<r \leq 1$. Where $\lambda\U d$ is the
Lebesgue measure on $\mathbb{R}^d$.

For higher orders of regularity, the following is sufficient: see
[Leoni, 2020](https://www.google.co.uk/books/edition/A_First_Course_in_Fractional_Sobolev_Spa/lh2_EAAAQBAJ?hl=en&gbpv=1&dq=giovanni+leoni+fractional+sobolev&pg=PP1&printsec=frontcover) and [Sawano, 2020](https://link.springer.com/book/10.1007/978-981-13-0836-9) section 5.1.

<b>Theorem 10</b>. Let $\Omega \subset \mathbb{R}^d$ be open with
[uniformly Lipschitz
boundary](https://nowheredifferentiable.com/2023-07-12-PDEs-3-Sobolev_spaces/#:~:text=has-,uniformly%20Lipschitz%20boundary,-if%20there%20exists)
and consider $p\in [1,\infty), s\in[1,\infty)$. Then, $\Omega$ is an
extension domain for $W^{s,p},H^{s,p},B^{s,p}$.

## Interpolation

Both the Sobolev-Slobodeckij and Bessel potential spaces can be viewed
as a way to fill the gaps between integer-valued Sobolev spaces. The
following uses the concept of [complex
interpolation](https://en.wikipedia.org/wiki/Interpolation_space). We
will not go into detail as the results will not be essential to us, but
merely serve as a nice way to understand the relationship between the
spaces.

 <a name="interpolation">
<b>Proposition 11</b> </a>  (Interpolation ). Let
$s\U 1 \neq s\U 2 >0, p \in (1, \infty)$, $0<\theta<1$ and

<div>
$$\begin{aligned}
s=s\U 1(1-\theta)+s\U 2 \theta, \quad p=p\U 1(1-\theta)+p\U 2 \theta.

\end{aligned}$$

</div>

Then, given an extension domain $\Omega$ it holds that

<div>
$$\begin{aligned}
H^{s,p}(\Omega )=\left[H^{s\U 1,p\U 1}(\Omega), H^{s\U 2,p\U 2}(\Omega)\right]\U {\theta},\quad B^{s,p}(\Omega )=\left[B^{s\U 1,p}(\Omega ), B^{s\U 2, p}(\Omega )\right]\U \theta,

\end{aligned}$$

</div>

where $[X,Y]\U \theta$ denotes the complex interpolation
space.

The result can be found in [Triebel, 2020](https://link.springer.com/book/10.1007/978-3-0346-0419-2) page 45 for
$\Omega = \mathbb{R}^d$. The general result follows by extension. In
particular, if we write $k:=\left\lfloor s \right\rfloor$ and
$\gamma:=s-k$, then

<div>
$$\begin{aligned}
H^{s,p}(\Omega ) & =\left[H^{k,p}(\Omega), H^{k+1,p}(\Omega)\right]\U {\gamma }= \left[L^p(\Omega ), H^{k+1,p}(\Omega)\right]\U {s/(k+1) }  \\
B^{s,p}(\Omega ) & =\left[B^{k,p}(\Omega), B^{k+1,p}(\Omega)\right]\U {\gamma }= \left[L^p(\Omega ), B^{k+1,p}(\Omega)\right]\U {s/(k+1) }.
\end{aligned}$$
</div>

# Relationship between the definitions

The following result shows the inclusions between
$W^{s,p}(\Omega ),H^{s,p}(\Omega ),B^{s,p}(\Omega )$ and can be found in
[Agranovich, 2020](https://link.springer.com/book/10.1007/978-3-319-14648-5) page 224 and in [Stein, 2020](https://www.degruyter.com/document/doi/10.1515/9781400883882/html) page 155.

 <a name="equivalence fractional spaces">
<b>Theorem 12</b> </a> . Let $s \geq 0, \epsilon >0$ and $\Omega$ an extension
domain for $H^{s+\epsilon,p},B^{s+\epsilon,p}$. Then,

<div>
$$\begin{aligned}
H^{s+\epsilon,p}(\Omega ) & \subset B^{s,p}(\Omega )  \subset H^{s,p}(\Omega )\quad \forall p \in (1,2]       \\
B^{s+\epsilon,p}(\Omega ) & \subset H^{s,p}(\Omega )  \subset B^{s,p}(\Omega )\quad \forall p \in [2,\infty),

\end{aligned}$$

</div>

where the above inclusions are continuous and dense.
Furthermore,

<div>
$$\begin{align}
\label{Slobodeckij equivalence}
W^{s,p}(\Omega )= \begin{cases}
H^{s,p}(\Omega ) & \text{ if } s \in \mathbb{N}\U 0    \\
B^{s,p}(\Omega ) & \text{ if } s \notin \mathbb{N}\U 0
\end{cases}.

\end{align}$$

</div>

In consequence, for $p=2$,

<div>
$$\begin{align}
\label{p=2}
H^{s,2}(\Omega )=W^{s,2}(\Omega )=B^{s,2}(\Omega ).

\end{align}$$

</div>

The equality in
(\ref{Slobodeckij equivalence}) shows that, as long as we
understand the behaviour of $H^{s,p}(\Omega )$ and $B^{s,p}(\Omega )$,
we can completely determine that of $W^{s,p}(\Omega )$. It also
justifies the following extension of $W^{s,p}(\Omega )$ to negative
regularity.

 <a name="negative s Slobodeckij">
<b>Definition 13</b> </a>  (Slobodeckij space negative $s$). Let
$\Omega \subset \mathbb{R}^d$ be an extension domain for
$H^{s,p}(\Omega ), B^{s,p}(\Omega )$. Then, given $p \in [1,\infty)$ and
any $s \in \mathbb{R}$ we define

<div>
$$\begin{aligned}
W^{s,p}(\Omega )= \begin{cases}
H^{s,p}(\Omega ) & \text{ if } s \in \mathbb{Z}\U 0    \\
B^{s,p}(\Omega ) & \text{ if } s \notin \mathbb{Z}\U 0
\end{cases}.

\end{aligned}$$

</div>

The equality for $p=2$ in (\ref{p=2}) justifies that, for sufficiently regular domains, all
three spaces are written $H^s(\Omega )$. We will prove the left-hand
side of this equivalence in Exercise
<a href="#equivalence of fractional spaces">4</a>. For $p\neq 2$, the
inclusions are, in general, strict. An example is constructed in
[Stein, 2020](https://www.degruyter.com/document/doi/10.1515/9781400883882/html) page 161 exercise 6.8.

 <a name="equivalence of fractional spaces">
<b>Exercise 4</b> </a>  (Equivalence of fractional spaces). Show without using
Theorem <a href="#equivalence fractional spaces">12</a> that

<div>
$$\begin{aligned}
H^{s,2}(\mathbb{R}^d)=W^{s,2}(\mathbb{R}^d).

\end{aligned}$$

</div>

<div class="exercise-container">
<button class="exercise-button" onclick="toggleExercise(this)">Hint</button>
<div class="exercise-text">
We want to show that the norms are equivalent. That is, that

<div>
$$\begin{aligned}
\left\lVert u \right\rVert\U {H^{s,2}(\mathbb{R}^d)}\sim\left\lVert u \right\rVert\U {W^{s,2}(\mathbb{R}^d)}.

\end{aligned}$$

</div>

We already know this is the case when $s$ is an integer,
so it suffices to show that the norms are equivalent for
$s= \gamma  \in (0,1)$. That is, that

<div>
$$\begin{aligned}
|u|\U {\gamma ,2}^2\sim \int\U {\mathbb{R}^d}|\xi|^{2 \gamma }|\mathcal{F} u(\xi)|^2 d \xi , \quad\forall \gamma \in (0,1).

\end{aligned}$$

</div>

By Plancherel's theorem and a calculation of the Fourier
transform of the translation, we have

<div>
$$\begin{aligned}
|u|\U {\gamma ,2}^2 & =\int\U {\mathbb{R}^d}\int\U {\mathbb{R}^d}\frac{\left| u(x+y)-u(y) \right|^2}{\left| x \right|^{d+2\gamma    }}\,\mathrm{d}x \,\mathrm{d}y                                                                                                       = \int\U {\mathbb{R}^d}\frac{\left\lVert \mathcal{F}\{u(x+\cdot )-u\} \right\rVert^2\U {L^2(\mathbb{R}^d)}}{\left| x \right|^{d+2\gamma }}\,\mathrm{d}x \\
& =\int\U {\mathbb{R}^d}\int\U {\mathbb{R}^d}  \frac{|e^{2 \pi i x \cdot \xi}-1|^2}{\left| x \right|^{d+2\gamma    }}|\widehat{u}(\xi)|^2\,\mathrm{d}x\,\mathrm{d}\xi                                                                                                                                                                     \\&=2\int\U {\mathbb{R}^d}\left(\int\U {\mathbb{R}^d}  \frac{1-\cos(2\pi \xi\cdot x)}{\left| x \right|^{d+2\gamma }}\,\mathrm{d}x\right)|\widehat{u}(\xi)|^2\,\mathrm{d}\xi.

\end{aligned}$$

</div>

To treat the inner integral, we note that it is
rotationally invariant, and so, by rotating $\xi$ to the first axis and
later changing variable $x \to x / \left| \xi \right|$, we get

<div>
$$\begin{aligned}
\int\U {\mathbb{R}^d}  \frac{1-\cos(2\pi \xi\cdot x)}{\left| x \right|^{d+2\gamma  }}\,\mathrm{d}x & =\int\U {\mathbb{R}^d}  \frac{1-\cos(2\pi \left| \xi \right|x\U 1 )}{\left| x \right|^{d+2\gamma }}\,\mathrm{d}x                                          \\
& =\left| \xi \right|^{2 \gamma } \int\U {\mathbb{R}^d}  \frac{1-\cos(2\pi  x\U 1) }{\left| x \right|^{d+2\gamma    }}\,\mathrm{d}x\sim \left| \xi \right|^{2 \gamma }.

\end{aligned}$$

</div>

The last integral is finite as, since $d+2\gamma >d$,
the tails $\left| \xi \right|\to\infty$ are controlled, and since
$1-\cos(2\pi x\U 1)\sim x\U 1^2\leq \left| x \right|^2$ the integrand has
order $-d+2(1-\gamma)>-d$ for $\left| \xi \right|\sim 0$ . That said,
substituting this back into the previous expression gives the desired
result.

</div>
</div>

<b>Exercise 5</b>. Use the previous exercise
<a href="#equivalence of fractional spaces">4</a> to show that if $\Omega$
is an extension domain for $H^{s}$, then

<div>
$$\begin{aligned}
H^{s,2}(\Omega )=W^{s,2}(\Omega ).

\end{aligned}$$

</div>

<div class="exercise-container">
<button class="exercise-button" onclick="toggleExercise(this)">Hint</button>
<div class="exercise-text">
By definition
<a href="#bessel potential def">4</a> choose a sequence
$v\U n \in H^{s,2}(\mathbb{R}^d)$ such that
$\left\lVert v\U n \right\rVert\U {H^{s,2}(\mathbb{R}^d)} \to \left\lVert u \right\rVert\U {H^{s,2}(\Omega )}$
in $H^s(\Omega )$. Then,

<div>
$$\begin{aligned}
\left\lVert u \right\rVert\U {H^{s,2}(\Omega)}= \lim\U {n\to\infty}\left\lVert v\U n \right\rVert\U {H^{2,2}(\mathbb{R}^d)}\sim \lim\U {n\to\infty}\left\lVert v\U n \right\rVert\U {W^{s,2}(\mathbb{R}^d)}\geq \left\lVert u \right\rVert\U {W^{s,2}(\Omega )}.

\end{aligned}$$

</div>

To obtain the reverse inequality, use the existence of a
continuous extension operator
$E: W^{s,2}(\Omega )\to W^{s,2}(\mathbb{R}^d)$ to obtain

<div>
$$\begin{aligned}
\left\lVert u \right\rVert\U {W^{s,2}(\Omega )}\sim \left\lVert Eu \right\rVert\U {W^{s,2}(\mathbb{R}^d)}\geq \left\lVert u \right\rVert\U {H^{s,2}(\mathbb{R}^d)}.

\end{aligned}$$

</div>

</div>
</div>

The above suggests that, for $p=2$, the integrals appearing in the
definition of the Slobodeckij spaces
<a href="#soledkij def">1</a>
correspond to differentiating a fractional amount of times. This indeed
is the case

<b>Definition 14</b>. Given $s \in [0,+\infty)$ and
$u \in \mathcal{S}(\mathbb{R}^d)$ we define the fractional Laplacian as

<div>
$$\begin{aligned}
(-\Delta )^{s }u(x):= \mathcal{F}^{-1}(\left| 2\pi\xi \right|^{2 s }\widehat{u}(\xi )).

\end{aligned}$$

</div>

 <a name="fractional laplacian">
<b>Proposition 15</b> </a> . For $\gamma  \in (0,1)$ and
$u \in H^{\gamma }(\mathbb{R}^d)$ it holds that

<div>
$$\begin{aligned}
(-\Delta )^{\gamma }u(x)=C\int\U {\mathbb{R}^d}\frac{u(x)-u(x+y)}{\left| y \right|^{d+2\gamma}}\,\mathrm{d}y,

\end{aligned}$$

</div>

where $C$ is a constant that depends on $d,\gamma$.

<b>Proof.</b> The above equality may seem odd at first if we compare it with
the integral in <a href="#soledkij def">1</a> where a square appears in the numerator, which
gives us our $2$ in the $2 \gamma$. However, it is justified by the fact
that, by the change of variables $y \to -y$,

<div>
$$\begin{aligned}
\int\U {\mathbb{R}^d}\frac{u(x)-u(x+y)}{\left| y \right|^{d+2\gamma}}\,\mathrm{d}y=\int\U {\mathbb{R}^d}\frac{u(x)-u(x-y)}{\left| y \right|^{d+2\gamma}}\,\mathrm{d}y.

\end{aligned}$$

</div>

So, we can get the second order difference in the
numerator by adding the two integrals.

<div>
$$\begin{align}
\label{second order}
\int\U {\mathbb{R}^d}\frac{u(x)-u(x+y)}{\left| y \right|^{d+2\gamma}}\,\mathrm{d}y=-\frac{1}{2}\int\U {\mathbb{R}^d}\frac{u(x+y)-2u(x)+u(x-y)}{\left| y \right|^{d+2\gamma}}\,\mathrm{d}y.

\end{align}$$

</div>

We will conclude the proof if we show that

<div>
$$\begin{aligned}
\left| \xi \right|^{2\gamma }\widehat{u}(\xi )\sim \mathcal{F}\left(\int\U {\mathbb{R}^d}\frac{u(x)-u(x+y)}{\left| y \right|^{d+2\gamma}}\,\mathrm{d}y\right).

\end{aligned}$$

</div>

Using
(\ref{second order}) and proceeding as in Exercise
<a href="#equivalence fractional spaces">12</a> gives

<div>
$$\begin{aligned}
& \mathcal{F}\left(\int\U {\mathbb{R}^d}\frac{u(x)-u(x+y)}{\left| y \right|^{d+2\gamma}}\,\mathrm{d}y\right)= -\frac{1}{2} \int\U {\mathbb{R}^d}\left(\int\U {\mathbb{R}^d}\frac{e^{2\pi i y \cdot \xi}-2+e^{-2\pi i y \cdot \xi}}{\left| y \right|^{d+2\gamma}}\,\mathrm{d}y\right) \widehat{u}(\xi)\,\mathrm{d}\xi       \\
& =\int\U {\mathbb{R}^d}\left(\int\U {\mathbb{R}^d}\frac{1-\cos(2\pi y \cdot \xi)}{\left| y \right|^{d+2\gamma}}\,\mathrm{d}y\right) \widehat{u}(\xi)\,\mathrm{d}\xi =\int\U {\mathbb{R}^d}  \frac{1-\cos(2\pi  y\U 1) }{\left| y \right|^{d+2\gamma    }}\,\mathrm{d}y\int\U {\mathbb{R}^d}\left| \xi \right|^{2 \gamma }\widehat{u}(\xi)\,\mathrm{d}\xi \\& \sim \left| \xi \right|^{2 \gamma }\widehat{u}(\xi)\,\mathrm{d}\xi.

\end{aligned}$$

</div>

This completes the proof and shows that the explicit
expression for $C$ is

<div>
$$\begin{aligned}
C=\frac{1}{(2\pi)^{2 \gamma }}\int\U {\mathbb{R}^d}  \frac{1-\cos(2\pi  y\U 1) }{\left| y \right|^{d+2\gamma }}\,\mathrm{d}y.

\end{aligned}$$

</div>

◻

# Dual of Sobolev spaces and correspondence with negative regularity

Negative orders of regularity correspond to the dual of Sobolev spaces.
This is best seen in the integer case. We first introduce the notation
$W^{s,p}\U 0(U),H^{s,p}\U 0(U),B^{s,p}\U 0(U)$ for the closure of
$C\U c^\infty(U)$ in $W^{s,p}(U),H^{s,p}(U),B^{s,p}(U)$ respectively. We
also introduce the notation $p' = p/(p-1)$ for the conjugate exponent of
$p$. We then have the following result (see [Evans, 2020](https://math24.files.wordpress.com/2013/02/partial-differential-equations-by-evans.pdf) pages
326-344 for the case $p=2$).

 <a name="dual of integer sobolev">
<b>Theorem 16</b> </a> . For all $k \in \mathbb{Z}$ and $p \in [1,\infty)$ and
$\Omega$ an extension domain for $W^{k,p}$, it holds that

<div>
$$\begin{aligned}
H^{k,p}\U 0(\Omega )' = H^{-k,p'}(\Omega ), \quad W^{k,p}\U 0(\Omega )' = W^{-k,p'}(\Omega ).

\end{aligned}$$

</div>

The first equality will be discussed in the next subsection and is most
easily proved when $\Omega =\mathbb{R}^d$, in which case one can use the
homeomorphism
$\Lambda ^s: H^{r,p}(\mathbb{R}^d )\xrightarrow{\sim}H^{r-s,p}(\mathbb{R}^d )$
together with the reflexivity of $L^p(\mathbb{R}^d )$. The second
equality is a direct consequence of the integer order equality
$W^{k,p}(\Omega )=H^{k,p}(\Omega )$ of Theorem
<a href="#equivalence fractional spaces">12</a>. For fractional order
regularities, we have the following result, which can be found in
[Agranovich, 2020](https://link.springer.com/book/10.1007/978-3-319-14648-5) page 228.

<b>Theorem 17</b>. Given $s>0, p \in [1,\infty)$ and $\Omega$ an extension
domain, it holds that the spaces
$W^{s,p}(\Omega ),H^{s,p}(\Omega ),B^{s,p}(\Omega )$ are reflexive
Banach spaces with duals

<div>
$$\begin{aligned}
W^{s,p}(\Omega )'=  W^{-s,p'}\U {\overline{\Omega } }(\mathbb{R}^d ), \quad H^{s,p}(\Omega )' = H^{-s,p'}\U {\overline{\Omega } }(\mathbb{R}^d ), \quad B^{s,p}(\Omega )' = B^{-s,p'}\U {\overline{\Omega } }(\mathbb{R}^d ).

\end{aligned}$$

</div>

where given a space of distributions $X$ on
$\mathbb{R}^d$ we define $X\U {\overline{\Omega }}$ as the space of
distributions on $\mathbb{R}^d$ which are supported in
$\overline{\Omega }$. In particular, for $\Omega =\mathbb{R}^d$,

<div>
$$\begin{aligned}
W^{s,p}(\mathbb{R}^d )'=    W^{-s,p'}(\mathbb{R}^d ), \quad H^{s,p}(\mathbb{R}^d )' = H^{-s,p'}(\mathbb{R}^d ), \quad B^{s,p}(\mathbb{R}^d )' = B^{-s,p'}(\mathbb{R}^d ).

\end{aligned}$$

</div>

<b>Observation 4</b>. Some authors define given $s>0$ and
$p \in [1,\infty)$

<div>
$$\begin{align}
\label{alternative negative}
W^{-s,p'}(\Omega )':=   W^{s,p}\U 0(\Omega )'.

\end{align}$$

</div>

See, for example, [Biccari, 2020](https://link.springer.com/chapter/10.1007/978-3-319-97613-6_12), [Leoni, 2020](https://www.google.co.uk/books/edition/A_First_Course_in_Fractional_Sobolev_Spa/lh2_EAAAQBAJ?hl=en&gbpv=1&dq=giovanni+leoni+fractional+sobolev&pg=PP1&printsec=frontcover)
page 228. The definition in
(\ref{alternative negative}) is equivalent to Definition
<a href="#negative s Slobodeckij">13</a> when $\Omega = \mathbb{R}^d$ or when
$s \in k$. However, in other cases, the two definitions are not
equivalent.

## The dual of $H^{s,p}(\mathbb{R}^d)$ and $B^{s,p}(\mathbb{R}^d)$

For some motivation, we start by considering the case
$\Omega =\mathbb{R}^d$. Note that, in this setting,
$H\U 0^{s,p}(\mathbb{R}^d)=H^{s,p}(\mathbb{R}^d)$.

 <a name="dual exercise">
<b>Exercise 6</b> </a>  (Dual identification). Prove the identification
$H^{-s,p'}(\mathbb{R}^d)=H^{s,p}(\mathbb{R}^d)'$ for $s>0$ and
$p \in [1,\infty)$.

<div class="exercise-container">
<button class="exercise-button" onclick="toggleExercise(this)">Hint</button>
<div class="exercise-text">
Consider the mapping
$H\U 0^{-s,p'}(\mathbb{R}^d) \to H^{s,p}\U 0(\mathbb{R}^d)'$ given by
$f \mapsto \ell\U f$ where

<div>
$$\begin{aligned}
\ell\U f(u):= \int\U {\mathbb{R}^d}(\Lambda^s u)(\Lambda ^{-s}f).

\end{aligned}$$

</div>

Show that this mapping is well-defined and continuous.
To see that it is invertible, show that, by duality, given
$\ell \in H^{s,p}(\mathbb{R}^d)'$ and $u \in H^{s,p}(\mathbb{R}^d)$, it
holds that

<div>
$$\begin{aligned}
(u,\ell )=(\Lambda ^s u,\Lambda ^{-s}\ell ).

\end{aligned}$$

</div>

Since $\Lambda ^s u \in L^p(\mathbb{R}^d)$ we deduce
that $\Lambda ^{-s}\ell \in L^{p}(\mathbb{R}^d)'$ and so by the Riesz
representation theorem there exists $f\U \ell \in L^{p'}(\mathbb{R}^d)$
such that $\Lambda ^{-s}\ell =\left\langle\cdot,f\U \ell\right\rangle$.
Show that the inverse of the previous mapping is

<div>
$$\begin{aligned}
H^{s,p}(\mathbb{R}^d)'                & \longrightarrow H^{-s,p'}(\mathbb{R}^d); \quad \ell = \left\langle\cdot, \Lambda^s  f\U \ell\right\rangle \to \Lambda^s  f\U \ell.
\end{aligned}$$
</div>

</div>
</div>

<b>Exercise 7</b>. Since $H^{s}(\mathbb{R}^d)$ is a Hilbert space, by the
Riesz representation theorem, we have the identification
$H^s(\mathbb{R}^d) = H^{s}(\mathbb{R}^d)'$. As a result, by the previous
exercise $H^{-s}(\mathbb{R}^d)= H^s(\mathbb{R}^d)$ How is this possible?

<div class="exercise-container">
<button class="exercise-button" onclick="toggleExercise(this)">Hint</button>
<div class="exercise-text">
It does <b>not</b> hold that
$H^{-s}(\mathbb{R}^d)= H^s(\mathbb{R}^d)$. The problem occurs when
considering too many identifications at once, as we are identifying
duals using different inner products. By following the mappings, we
obtain isomorphisms

<div>
$$\begin{aligned}
& H^{s}(\mathbb{R}^d) \xrightarrow{\sim}H^s(\mathbb{R}^d)' \xrightarrow{\sim}H^{-s}(\mathbb{R}^d)                                                 \\
& u \longmapsto   \left\langle\cdot, u\right\rangle\U {H^s(\mathbb{R}^d)}= \left\langle\cdot, \Lambda^{2s} u \right\rangle \mapsto \Lambda ^{2s} u.

\end{aligned}$$

</div>

However, the composition
$H^s(\mathbb{R}^d) \xrightarrow{\sim}H^{-s}(\mathbb{R}^d)$ is
$\Delta ^{2s}$, which is hardly the identity mapping.

</div>
</div>

For another example where confusion with this kind of identification can
arise, see remark 3 on page 136 of [Brezis, 2020]("https://en.wikipedia.org/wiki/Continuous_linear_extension").

## The dual of $H^{s,p}\U 0(\Omega)$

Given an extension domain $\Omega$ and $s \in \mathbb{R}$ , one can
define extension and restriction operators,

<div>
$$\begin{aligned}
E:H^{s,p}(\Omega ) \to H^{s,p}(\mathbb{R}^d), \quad \rho: H^{s,p}(\mathbb{R}^d) \to H^{s,p}(\Omega ),
\end{aligned}$$
</div>

which verify $\rho \circ E = \mathbf{I}\U {H^s(\Omega )}$. As
a result, the restriction is surjective, and we can factor
$H^{s,p}(\Omega )$ as

<div>
$$\begin{align}
\label{ismorphism}
H^{s,p}(\Omega )\simeq H^{s,p}(\mathbb{R}^d)\backslash H^s\U {\Omega^c}(\mathbb{R}^d ),
\end{align}$$
</div>

where given a closed set $K \subset \mathbb{R}^d$ we
define

<div>
$$\begin{aligned}
H^{s,p}\U K(\mathbb{R}^d):= \left\{u \in H^{s,p}(\mathbb{R}^d): \mathrm{supp}(u) \subset K\right\},
\end{aligned}$$
</div>

the support being understood [in the sense of
distributions](https://nowheredifferentiable.com/2023-07-12-PDEs-3-Sobolev_spaces/#:~:text=Support%20of%20a%20distribution)
Now, given a Banach space $X$ and a closed subspace
$Y \hookrightarrow X$, elements of $X'$ can be restricted to $Y$,
obtaining functionals in $Y'$. The kernel of this restriction is
$Y^\circ:=\left\\{\ell \in X': Y \subset \mathrm{ker}(\ell)\right\\}$.
Since, by the Hahn Banach theorem, the restriction is surjective, we
obtain the
[factorization](https://math.la.asu.edu/~quigg/teach/courses/578/2008/notes/adjoints.pdf)

<div>
$$\begin{align}
\label{dual isomormphism}
Y' \simeq X'\backslash Y^\circ.
\end{align}$$
</div>

Applying this to
$Y= H^{k,p}\U 0(\Omega )\hookrightarrow H^{k,p}(\mathbb{R}^d) =X$ we
obtain the result of Theorem
<a href="#dual of integer sobolev">16</a>.

<div>
$$\begin{aligned}
H^{k,p}\U 0(\Omega )' \simeq H^{k,p}(\mathbb{R}^d)'\backslash H^{k,p}\U {\Omega^c}(\mathbb{R}^d)'\simeq H^{-k,p'}(\mathbb{R}^d)\backslash H^{-k,p'}\U {\Omega^c}(\mathbb{R}^d )\simeq H^{-k,p'}(\Omega ),
\end{aligned}$$
</div>

where the second equality is by Exercise
<a href="#dual exercise">6</a> and
the third by (\ref{ismorphism}) . This shows that the dual of
$H^{k,p}\U 0(\Omega )$ is $H^{-k,p'}(\Omega )$. By also using the integer
order equivalence of Theorem
<a href="#equivalence fractional spaces">12</a>, we obtain Theorem
<a href="#dual of integer sobolev">16</a>.

As a final note, if our domain has a boundary, $H\U 0^k(\Omega )'$ and
$H^k(\Omega )'$ are not equal. Rather,

<div>
$$\begin{aligned}
H^{k,p}(\Omega )'\simeq H\U {\overline{\Omega } }^{-k,p'}(\mathbb{R}^d), \quad H^{-k,p'}(\Omega ) \simeq H^{-k,p'}(\mathbb{R}^d)\backslash H^{-k,p'}\U {\Omega ^c }(\mathbb{R}^d).
\end{aligned}$$
</div>

See [Taylor, 2020](https://books.google.co.uk/books?id=wI4fAwAAQBAJ&printsec=frontcover&hl=fr&source=gbs_ge_summary_r&cad=0#v=onepage&q&f=false) Section 4 for more details.

# Representation theorems

We know that we can homeomorphically map the spaces
$H^{s,p}(\mathbb{R}^d )$ and $B^{s,p}(\mathbb{R}^d )$ to the lower order
spaces $H^{s-r,p}(\mathbb{R}^d )$ and $B^{s-r,p}(\mathbb{R}^d )$ by
application of $\Lambda ^r$ (differentiating $r$ times). In other words,
spaces of lower-order regularity are obtained by differentiating
functions with higher regularity. We show how to extend this idea to
smooth domains in some particular cases.

 <a name="riesz representation">
<b>Theorem 18</b> </a>  (Representation of $W\U 0^{k,p}(\Omega )'$). Let
$\Omega \subset \mathbb{R}^d$ be an extension domain for $W^{k,p}$ where
$k \in \mathbb{N}$ and $p \in [1,\infty)$. Then, every element in
$W^{-k,p'}(\Omega )=W^{k,p}\U 0(\Omega )'$ is the unique extension of a
distribution of the form

<div>
$$\begin{aligned}
\sum\U {1\leq\left| \alpha \right|\leq k} D^\alpha u\U \alpha\in \mathcal{D}'(\Omega ),\quad \text{where }    u\U \alpha \in L^{p'}(\Omega ).

\end{aligned}$$

</div>

<b>Proof.</b> Define the mapping

<div>
$$\begin{aligned}
T: W^{k,p}(\Omega ) & \longrightarrow L^p(\Omega \to \mathbb{R}^d)                \\
u                   & \longmapsto(D^\alpha u)\U {1 \leq\left| \alpha \right|\leq k}.

\end{aligned}$$

</div>

Where the notation says that we send $u$ to the vector
formed by all its derivatives. By our definition of the norm on
$W^{k,p}(\Omega )$, we have that $T$ is an isometry and, in particular,
continuously invertible on its image. Denote the image of $T$ by
$X:=\mathrm{Im}(T)$. Given $\ell \in W^{-k,p'}(\Omega )$ we define

<div>
$$\begin{aligned}
\ell\U 0: X \to \mathbb{R}, \quad \ell\U 0(\mathbf{w}):= \ell(T^{-1}\mathbf{w}), \quad \forall \mathbf{w} \in X.

\end{aligned}$$

</div>

By Hahn Banach's theorem, we can extend $\ell\U 0$ from
$X$ to a functional $\ell\U 1 \in  L^p(\Omega \to \mathbb{R}^d)'$ and by
the Riesz representation theorem, we have that there exists a unique
$\mathbf{f}=(f\U \alpha)\U {1\leq \left| \alpha \right|\leq k }\in L^{p'}(\Omega \to \mathbb{R}^d)$
such that

<div>
$$\begin{aligned}
\ell\U 1(\mathbf{w})=\int\U {\Omega}\mathbf{w}\cdot \mathbf{h}, \quad \forall \mathbf{w} \in L^p(\Omega \to \mathbb{R}^d).

\end{aligned}$$

</div>

By construction, it holds that, for all
$v \in W^{k,p}(\Omega )$

<div>
$$\begin{aligned}
\ell(v)=\ell\U 0(Tv)=\int\U {\Omega}Tv\cdot \mathbf{f}=\sum\U {1\leq\left| \alpha \right|\leq k}\int\U {\Omega}f\U \alpha D^\alpha v .

\end{aligned}$$

</div>

In particular, this holds for
$v \in \mathcal{D}(\Omega )$ and if we set
$u\U \alpha:=(-1)^\alpha f\U \alpha$ we obtain that for all
$v \in \mathcal{D}(\Omega )$

<div>
$$\begin{align}
\label{representation}
\ell(v)=\left(v,\sum\U {1\leq\left| \alpha \right|\leq k} D^\alpha u\U \alpha\right)=: \omega(v)

\end{align}$$

</div>

(we recall the notation $(v,\omega)$ for the duality
pairing). By definitions of the norm on $W^{k,p}(\Omega )$ and Cauchy
Schwartz, we have that $\omega$ is continuous with respect to the norm
on $W^{k,p}(\Omega )$ and so we may extend it uniquely to the closure of
$\mathcal{D}(\Omega )$ in $W^{k,p}(\Omega )$ which is
$W^{k,p}\U 0(\Omega )$. By
(\ref{representation}) , the extension is necessarily $\omega$. This
completes the proof. ◻

The above theorem shows that $W^{-k,p'}(\Omega )$ can be equivalently
formed by differentiating $k$ times functions in $L^{p'}(\Omega )$. The
proof also sheds some light as to why $W^{-s,p'}(\Omega )$ is the dual
of $W^{k,p}\U 0(\Omega )$ and not the dual of $W^{k,p}(\Omega )$. The
reason is that given a sufficiently regular distribution in
$\mathcal{D}'(\Omega )$, it has a unique continuous extension to an
element of $W\U 0^{k,p}(\Omega )'$, but not to an element of
$W^{k,p}(\Omega )'$. We note however that, though the extension from
$\mathcal{D}'(\Omega )$ to $W^{-s,p}(\Omega )$ is unique, the functions
$u\U \alpha$ will not be, for example, if $\left| \alpha \right|>0$ it is
possible to add a constant to $u\U \alpha$ and still obtain the same
result.

<b>Exercise 8</b>. Show that for $s= \gamma +k$ where
$k \in \mathbb{N}\U 0, \gamma \in [0,1)$ and $p \in [1,\infty)$ and an
extension domain for $H^{s,p}$, every element in $H^{-s,p'}(\Omega )$
can be written in the form $\left.w\right|\U {\partial \Omega }$, where

<div>
$$\begin{aligned}
w=\sum\U {0\leq\left| \alpha \right|\leq k} \Lambda^{\gamma } D^\alpha u\U \alpha\in \mathcal{D}'(\mathbb{R}^d ),\quad \text{where }    u\U \alpha \in L^{p'}(\mathbb{R}^d ).

\end{aligned}$$

</div>

<div class="exercise-container">
<button class="exercise-button" onclick="toggleExercise(this)">Hint</button>
<div class="exercise-text">
Use that
$\Lambda ^{\gamma }: H^{s,p}(\mathbb{R}^d) \to H^{k ,p}(\mathbb{R}^d)$
is an isomorphism and the just proved theorem
<a href="#riesz representation">18</a> together with the integer equivalence
in Theorem <a href="#equivalence fractional spaces">12</a> to show that

<div>
$$\begin{aligned}
H^{s,p}(\mathbb{R}^d)' = \left\{ \sum\U {0\leq\left| \alpha \right|\leq k} \Lambda^{\gamma } D^\alpha u\U \alpha\in \mathcal{D}'(\mathbb{R}^d ),\quad \text{where }    u\U \alpha \in L^{p'}(\mathbb{R}^d )\right\}.

\end{aligned}$$

</div>

Now conclude by the definition of $H^{-s,p'}(\Omega )$
for open domains <a href="#bessel potential def Omega">5</a>.

</div>
</div>

The above results extend to Besov spaces; see [Agranovich, 2020](https://link.springer.com/book/10.1007/978-3-319-14648-5)
page 227. This gives,

<b>Theorem 19</b>. Let
$k \in \mathbb{N}\U 0, \gamma \in [0,1), \theta \in (0,1)$ and
$p \in [1,\infty)$ where $\Omega$ is an extension domain for
$B^{\theta   ,p}, H^{\gamma ,p}$. Then,

<div>
$$\begin{aligned}
B^{\theta  -k,p}(\Omega ) & = \left\{ \sum\U {0\leq\left| \alpha \right|\leq k} D^\alpha u\U \alpha\in \mathcal{D}'(\Omega ),\quad \text{where }    u\U \alpha \in B^{\theta  ,p}(\Omega )\right\} \\
H^{\gamma -k,p}(\Omega )  & = \left\{ \sum\U {0\leq\left| \alpha \right|\leq k} D^\alpha u\U \alpha\in \mathcal{D}'(\Omega ),\quad \text{where }    u\U \alpha \in H^{\gamma ,p}(\Omega )\right\}  \\
W^{\gamma -k,p}(\Omega )  & = \left\{ \sum\U {0\leq\left| \alpha \right|\leq k} D^\alpha u\U \alpha\in \mathcal{D}'(\Omega ),\quad \text{where }    u\U \alpha \in W^{\gamma ,p}(\Omega )\right\}.

\end{aligned}$$

</div>

# Some applications: Trace, embeddings and regularity

## Trace operator

Consider $f \in L^p(\Omega )$ a PDE of the form

<div>
$$\begin{align}
\label{PDE}
\mathcal{L}u =f \text{ in } \Omega , \quad \left.u\right|\U {\partial \Omega }= g.
\end{align}$$
</div>

Then, it is necessary to know exactly what boundary data
$g$ is admissible. Suppose that $\mathcal{L}$ is of order $k$ so we
require $u \in W^{k,p}(\Omega )$. Will
(\ref{PDE}) have a solution?
To be able to answer this question, we need to know the image of the
trace operator. If $g \notin \operatorname{Tr}(W^{k,p}(\Omega ))$, then
there is no hope of finding a solution. The following theorem
characterizes the image of the trace operator and can be found in
[Agranovich, 2020](https://link.springer.com/book/10.1007/978-3-319-14648-5) page 228 and [Leoni, 2020](https://www.google.co.uk/books/edition/A_First_Course_in_Fractional_Sobolev_Spa/lh2_EAAAQBAJ?hl=en&gbpv=1&dq=giovanni+leoni+fractional+sobolev&pg=PP1&printsec=frontcover) page 390.

 <a name="trace theorem">
<b>Theorem 20</b> </a>  (Fractional trace theorem). Let
$\Omega \subset \mathbb{R}^d$ be open with $C^{0,1}$ boundary. Then, for
all $p\in (1,\infty), s\in (1/p,\infty)$, the trace operator
$\operatorname{Tr}$ can be extended from $C(\overline{\Omega } )$ to a
bounded operator

<div>
$$\begin{aligned}
\operatorname{Tr}: H^{s,p}(\Omega ) \to B^{s-1/p,p}(\partial\Omega), \quad \operatorname{Tr}: B^{s,p}(\Omega ) \to B^{s-1/p,p}(\partial\Omega).

\end{aligned}$$

</div>

Furthermore, given $g \in B^{s-1/p,p}(\partial\Omega)$,
there exists $u \in W^{s,p}(\Omega )$ such that $\operatorname{Tr}(u)=g$
with

<div>
$$\begin{aligned}
\left\lVert u \right\rVert\U {W^{s,p}(\Omega )}\lesssim \left\lVert g \right\rVert\U {B^{s-1/p,p}(\partial\Omega)}.

\end{aligned}$$

</div>

Note that, since we have equality of $W^{s,p}(\Omega )$ with
$H^{s,p}(\Omega )$ and $B^{s,p}(\Omega )$ for integer and non-integer
$s$ respectively, we can also extend

<div>
$$\begin{aligned}
\operatorname{Tr}: W^{s,p}(\Omega ) \to B^{s-1/p,p}(\partial\Omega).
\end{aligned}$$
</div>

## Fractional Sobolev embeddings

In this section, we state the fractional analogue of the Sobolev
embedding theorems for regularity $\gamma \in (0,1)$. Here, the
[analogous](https://nowheredifferentiable.com/2023-07-12-PDEs-3-Sobolev_spaces/#global:~:text=concludes%20the%20proof.%C2%A0%E2%97%BB-,Exercise,-24%20.%20Given)
of the exponent $p\U k^{\star }$ is

<b>Definition 21</b>. Given $p \in [1,\infty)$ and $s>0$, with
$s\in (d/p, \infty)$, we define the Sobolev critical exponent $p\U s^\star $
by

<div>
$$\begin{aligned}
\frac{1}{p\U s ^\star }:=\frac{1}{p}-\frac{s }{d}.

\end{aligned}$$

</div>

The natural extension of the Sobolev embedding theorem to the fractional
case is the following. First, we introduce the following notation for
the fractional seminorm.

<div>
$$\begin{aligned}
\left| u \right|\U {W^{\gamma, p}(\Omega )}:=\int\U {\mathbb{R}^d}\int\U {\mathbb{R}^d}\frac{\left| u(x+y)-u(y) \right|}{\left| x \right|^{d+\gamma p}}\,\mathrm{d}x \,\mathrm{d}y.
\end{aligned}$$
</div>

See [Leoni, 2020](https://www.google.co.uk/books/edition/A_First_Course_in_Fractional_Sobolev_Spa/lh2_EAAAQBAJ?hl=en&gbpv=1&dq=giovanni+leoni+fractional+sobolev&pg=PP1&printsec=frontcover) page 262 for the following result.

 <a name="subcritical embedding">
<b>Theorem 22</b> </a>  (Fractional Sobolev-Gagliardo-Niremberg). Given an
extension domain $\Omega$ for $W^{\gamma,p}$ and
$\gamma \in (0,1), p \in [1,\infty)$, it holds that

<div>
$$\begin{aligned}
\|u\|\U {L^{p\U \gamma^\star }(\Omega )} \lesssim |u|\U {W^{\gamma, p}(\Omega )}, \quad\forall \gamma <  \frac{d}{p}

\end{aligned}$$

</div>

In particular, by interpolation, for all
$q \in [p,p\U \gamma^\star ]$.

<div>
$$\begin{aligned}
\|u\|\U {L^{q}(\Omega )} \lesssim \left\lVert u \right\rVert\U {W^{\gamma, p}(\Omega )}, \quad\forall \gamma <  \frac{d}{p}.

\end{aligned}$$

</div>

The critical case $\gamma=\frac{d}{p}$ corresponding to
$p\U \gamma^\star =\infty$ is now (see [Leoni, 2020](https://www.google.co.uk/books/edition/A_First_Course_in_Fractional_Sobolev_Spa/lh2_EAAAQBAJ?hl=en&gbpv=1&dq=giovanni+leoni+fractional+sobolev&pg=PP1&printsec=frontcover) page 265)

 <a name="critical embedding">
<b>Theorem 23</b> </a> . Given an extension domain $\Omega$ for $W^{\gamma,p}$
and $\gamma \in (0,1), q \in [p,\infty)$, it holds that

<div>
$$\begin{aligned}
\|u\|\U {L^q(\Omega )} \lesssim\|u\|\U {W^{\gamma, p}(\Omega)}, \quad \gamma =  \frac{d}{p}.

\end{aligned}$$

</div>

<b>Exercise 9</b>. Using Theorem
<a href="#subcritical embedding">22</a> prove Theorem
<a href="#critical embedding">23</a>

<div class="exercise-container">
<button class="exercise-button" onclick="toggleExercise(this)">Hint</button>
<div class="exercise-text">
We are in the subcritical case for $r<d/p=\gamma$. Extend
$u$ to $\mathbb{R}^d$ to form $\widetilde{u}$. Then, by Proposition
<a href="#inclusion ordered by regularity">2</a>, we have

<div>
$$\begin{aligned}
\|u\|\U {L^{p\U r^\star }(\Omega )}\leq \|u\|\U {L^{p\U r^\star }(\mathbb{R}^d )}  \lesssim \left\lVert u \right\rVert\U {W^{r, p}(\mathbb{R}^d )}\leq \left\lVert u \right\rVert\U {W^{\gamma, p}(\mathbb{R}^d  )}\lesssim \left\lVert u \right\rVert\U {W^{\gamma, p}(\Omega )}.

\end{aligned}$$

</div>

Conclude by finding $r$ such that $p\U r^\star =q$.

</div>
</div>

The supercritical case $\gamma>d/p$ can be found in
[Agranovich, 2020](https://link.springer.com/book/10.1007/978-3-319-14648-5) page 224 and [Leoni, 2020](https://www.google.co.uk/books/edition/A_First_Course_in_Fractional_Sobolev_Spa/lh2_EAAAQBAJ?hl=en&gbpv=1&dq=giovanni+leoni+fractional+sobolev&pg=PP1&printsec=frontcover) page 275. To
simplify the notation we use the convention that $C^r$ stands for
$C^{\lfloor r \rfloor, r-\lfloor r \rfloor}$.

 <a name="morrey embedding">
<b>Theorem 24</b> </a>  (Morrey's fractional embedding). Let $\Omega$ be an
extension domain for $W^{s,p}$, we have a continuous embedding

<div>
$$\begin{aligned}
W^{s,p}(\Omega) \hookrightarrow  C^{s-d/p}(\Omega), \quad\forall s> \frac{d}{p}.

\end{aligned}$$

</div>

This embedding also holds for $s=d / p$ provided that
$s-d/p$ is non-integer.

As in the non-fractional case, one can also consider higher smoothness
on the right-hand side (see [Leoni, 2020](https://www.google.co.uk/books/edition/A_First_Course_in_Fractional_Sobolev_Spa/lh2_EAAAQBAJ?hl=en&gbpv=1&dq=giovanni+leoni+fractional+sobolev&pg=PP1&printsec=frontcover) page 290).

 <a name="higher smoothness embedding">
<b>Theorem 25</b> </a>  (Sobolev embedding into higher smoothness). Let $\Omega$
be an extension domain for $W^{\gamma,p}$. Then, given
$p\U 1, p\U 2 \in [1,\infty)$ and $0\leq \gamma\U 1<\gamma\U 2< 1$, it holds
that

<div>
$$\begin{aligned}
\left\lVert u \right\rVert\U {W^{\gamma\U 1,p\U 1}(\Omega )}\lesssim \left\lVert u \right\rVert\U {W^{\gamma\U 2,p\U 2}(\Omega )}, \quad\forall \gamma\U 2 - \frac{d}{p\U 2} = \gamma\U 1 - \frac{d}{p\U 1}.

\end{aligned}$$

</div>

<b>Exercise 10</b>. Justify via a scaling argument that the condition
$\gamma\U 2 - \frac{d}{p\U 2} = \gamma\U 1 - \frac{d}{p\U 1}$ is necessary for
the embedding in Theorem
<a href="#higher smoothness embedding">25</a>.

<div class="exercise-container">
<button class="exercise-button" onclick="toggleExercise(this)">Hint</button>
<div class="exercise-text">
Extend to a function on $\mathbb{R}^d$, then swap $u$ with
$u\U \lambda (x):=u(\lambda x)$and apply the change of variables
$(x,y)\to \lambda (x,y)$.
</div>
</div>

Finally, interpolation results are also possible. See [Leoni, 2020](https://www.google.co.uk/books/edition/A_First_Course_in_Fractional_Sobolev_Spa/lh2_EAAAQBAJ?hl=en&gbpv=1&dq=giovanni+leoni+fractional+sobolev&pg=PP1&printsec=frontcover)
page 300.

 <a name="interpolation embedding">
<b>Theorem 26</b> </a> . Let $\Omega$ be an extension domain for $W^{\gamma,p}$
and consider $p\U 1,p\U 2 \in (1,\infty), 0 \leq \gamma\U 1<\gamma\U 2 \leq 1,$
and $0<\theta<1$. Then

<div>
$$\begin{aligned}
\|u\|\U {W^{s, p}(\mathbb{R}^d)} \lesssim\|u\|\U {W^{\gamma\U 1, p\U 1}(\mathbb{R}^d)}^\theta\|u\|\U {W^{\gamma\U 2, p\U 2}(\mathbb{R}^d)}^{1-\theta}

\end{aligned}$$

</div>

for all
$u \in W^{\gamma\U 1, p\U 1}(\mathbb{R}^d) \cap W^{\gamma\U 2, p\U 2}(\mathbb{R}^d)$,
where $\frac{1}{p}=\frac{\theta}{p\U 1}+\frac{1-\theta}{p\U 2}$ and
$s=\theta \gamma\U 1+$ $(1-\theta) \gamma\U 2.$

The above results can also be formulated in terms of the Sobolev
seminorm. For example, Theorem
<a href="#interpolation embedding">26</a> can be formulated as

<div>
$$\begin{aligned}
\left| u \right|\U {W^{s, p}(\mathbb{R}^d)} \lesssim \left| u \right|\U {W^{\gamma\U 1, p\U 1}(\mathbb{R}^d)}^\theta\left| u \right|\U {W^{\gamma\U 2, p\U 2}(\mathbb{R}^d)}^{1-\theta}.
\end{aligned}$$
</div>

Higher order embeddings and interpolations can be
obtained from the previous cases with regularity parameter below 1 in
combination with the integer case.

 <a name="fractional rellich">
<b>Exercise 11</b> </a>  (Fractional Rellich-Kondrachov). Let $\Omega$ be an
extension domain for $W^{s,p}$, then, given
$s \geq 0, p \in [1, \infty)$. Set $k=\left\lfloor s \right\rfloor$ and
$\gamma =s-k$. Then, it holds that

<div>
$$\begin{aligned}
& W^{s, p}(\Omega) \hookrightarrow L^q(\Omega), \quad \forall q \in [1, p\U k^\star ) \quad \text { and } s<\frac{d}{p} \\
& W^{s, p}(\Omega) \hookrightarrow L^q(\Omega), \quad \forall q \in[p, \infty) \quad \text { and } s=\frac{d}{p} \\
& W^{s, p}(\Omega) \hookrightarrow C^{s-d/p}(\bar{\Omega})\hspace{61pt}\text { and } s>\frac{d}{p},

\end{aligned}$$

</div>

<div class="exercise-container">
<button class="exercise-button" onclick="toggleExercise(this)">Hint</button>
<div class="exercise-text">
Observe that

<div>
$$\begin{aligned}
\frac{1}{(p\U \gamma ^\star )\U k^\star }=\frac{1}{p\U \gamma }-\frac{k}{d}=\frac{1}{p}-\frac{s}{d}= \frac{1}{p\U s^\star }.

\end{aligned}$$

</div>

The result follows from Theorem
<a href="#subcritical embedding">22</a>, Theorem
<a href="#morrey embedding">24</a> together with the
[integer-case](https://nowheredifferentiable.com/2023-07-12-PDEs-3-Sobolev_spaces/#est32:~:text=Combining%20the%20three%20results)
embeddings. For the first case, by Theorem
<a href="#subcritical embedding">22</a>, we have

<div>
$$\begin{aligned}
\left\lVert D^\alpha u \right\rVert\U {L^{p\U \gamma ^\star }(\Omega )}\lesssim \left\lVert D^\alpha u \right\rVert\U {W^{\gamma ,p}(\Omega )} \lesssim \left\lVert u \right\rVert\U {W^{s,p}(\Omega )}, \quad \forall \left| \alpha \right|\leq k.

\end{aligned}$$

</div>

Then, using the integer case, we conclude

<div>
$$\begin{aligned}
\left\lVert u \right\rVert\U {L^{p\U s^\star }(\Omega )}=\left\lVert u \right\rVert\U {L^{(p\U \gamma ^\star )\U k ^\star }(\Omega )}\lesssim \left\lVert u \right\rVert\U {W^{k,p\U \gamma ^\star }(\Omega )}\lesssim \left\lVert u \right\rVert\U {W^{s,p}(\Omega )}.

\end{aligned}$$

</div>

For the second case, by Theorem
<a href="#subcritical embedding">22</a> and reasoning with derivatives up to
order $k$, we obtain similarly

<div>
$$\begin{aligned}
\left\lVert u \right\rVert\U {W^{k,p\U \gamma ^\star }(\Omega )}\lesssim \left\lVert u \right\rVert\U {W^{s,p}(\Omega )},

\end{aligned}$$

</div>

where by a calculation $k = d / p\U \gamma ^\star $. So, we
conclude once more by using the integer case. For the final
case, we use Theorem <a href="#morrey embedding">24</a> directly.

</div>
</div>

Below we plot the Sobolev critical exponent $p\U s^\star $ for $p=2$ and
$d=1,2,3$. As we can see, it decreases with $d$ and increases with $s$.
This means that the larger the dimension the more regularity we need to
obtain a bound on the same $L^q(\mathbb{R}^d)$ norm. The integrability
increasing to infinity around the critical threshold $s=d/p$.

<img src="{{'assets/img/Figures/regularity_coefficient.svg'| relative_url }}" alt="Sobolev critical exponent for p=2 and d=1,2,3 " width="90%" id="fig:regularity_coefficient">

<b>Exercise 12</b>. Let $\Omega$ be an extension domain for $W^{s\U 1,p}$.
Show that, given $p\U 1, p\U 2 \in [1,\infty)$ and $0 \leq s\U 2<s\U 1 <\infty$,
it holds that

<div>
$$\begin{aligned}
W^{s\U 1, p\U 1}(\Omega ) \hookrightarrow W^{s\U 2, p\U 2}(\Omega ), \quad s\U 1 - \frac{d}{p\U 1} = s\U 2 - \frac{d}{p\U 2}.

\end{aligned}$$

</div>

<div class="exercise-container">
<button class="exercise-button" onclick="toggleExercise(this)">Hint</button>
<div class="exercise-text">
Set $k\U i =\left\lfloor s\U i \right\rfloor$ and
$\gamma\U i =s\U i-k\U i$. Apply Theorem
<a href="#higher smoothness embedding">25</a> to the derivatives of order up
to $k\U 2$ to obtain

<div>
$$\begin{aligned}
\left\lVert D^\alpha u \right\rVert\U {W^{\gamma\U 2, p\U 2}(\Omega )}\lesssim \left\lVert D^\alpha u \right\rVert\U {W^{\gamma \U 1,p\U 1}(\Omega )} \leq \left\lVert u \right\rVert\U {W^{s\U 1,p\U 1}(\Omega )}, \quad \forall \left| \alpha \right|\leq k\U 2.

\end{aligned}$$

</div>

Deduce that

<div>
$$\begin{aligned}
\left\lVert u \right\rVert\U {W^{s\U 2,p\U 2}(\Omega )}\lesssim \left\lVert u \right\rVert\U {W^{s\U 1,p\U 1}(\Omega )}.

\end{aligned}$$

</div>

</div>
</div>

For more higher order embeddings see also [Leoni, 2020](https://www.google.co.uk/books/edition/A_First_Course_in_Fractional_Sobolev_Spa/lh2_EAAAQBAJ?hl=en&gbpv=1&dq=giovanni+leoni+fractional+sobolev&pg=PP1&printsec=frontcover) Section
11.4. Finally, embeddings can be similarly formulated for Besov spaces.
See [Sawano, 2020](https://link.springer.com/book/10.1007/978-981-13-0836-9) page 219 for the following result.

<b>Theorem 27</b> (Embedding for Besov spaces). Let $\Omega$ be an
extension domain, and consider
$1 \leq p\U 1<p\U 2 \leq \infty, - \infty <s\U 2<s\U 1<\infty$. Then,

<div>
$$\begin{aligned}
B^{s\U 1,p\U 1}(\Omega) \hookrightarrow B^{s\U 2,p\U 2}(\Omega), \quad s\U 1-\frac{n}{p\U 1}=s\U 2-\frac{n}{p\U 2} .

\end{aligned}$$

</div>

This and other results can be formulated for the more general spaces
$B^{s,p}\U q$. Where $B^{s,p}= B^{s,p}\U p$. See, [Triebel, 2020](https://link.springer.com/book/10.1007/978-3-0346-0419-2),
[Agranovich, 2020](https://link.springer.com/book/10.1007/978-3-319-14648-5), [Sawano, 2020](https://link.springer.com/book/10.1007/978-981-13-0836-9).

We conclude this post by commenting that given a second-order PDE with
smooth coefficients, such as

<div>
$$\begin{aligned}
- \Delta u =f \text{ in } \Omega , \quad \left.u\right|\U {\partial \Omega }= 0.
\end{aligned}$$
</div>

One expects that $u$ is two degrees more regular than
$f$. That is, if $f \in W^{s,p}(\Omega )$, then we should have
$u \in W^{s+2,p}(\Omega )$. This is indeed the case locally. However, to
obtain smoothness up to the boundary, one also needs $\partial \Omega$
to be regular enough. In this case, Lipschitz continuity of $\Omega$ is
not sufficient, even if $f \in C^\infty(\overline{\Omega } )$ (see for
example [Savare, 2020](https://www.sciencedirect.com/science/article/pii/S002212369793158X/pdf?md5=c646200fe7117dd7d25d27439f36b342&pid=1-s2.0-S002212369793158X-main.pdf)). We may comment on this later in a
future post.

A (possibly not updated) pdf of version of this page is provided [here](/assets/pdfs/PDEs/fractional_sobolev_spaces.pdf).
