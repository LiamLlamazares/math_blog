---
layout: post
title: What is a Hilbert space?
subtitle: An appendix for a series on PDEs
thumbnail-img: /assets/img/Narici.jpg
share-img: /assets/img/Narici.jpg
tags: [PDEs]
authorpost: L.Llamazares
---

#  Three line summary

-   Hilbert spaces are Banach spaces with an inner product. They
    correspond to an infinite dimensional version of $\mathbb{R}^n$ or
    $\mathbb{C}^n$.

-   Much of Euclidean geometry carries over to Hilbert spaces including
    orthogonality, projections, orthonormal basis, and Pythagoras'
    theorem.

-   Compact operators are a simple kind of operator that can be
    approximated by infinite dimensional ones.

# Why should I care?

Hilbert spaces come with beautiful geometry and give us tools that are
not available in ordinary Banach spaces. These allow us to prove the
existence of infinite dimensional equations and even pose them as
minimization problems. When you can use a Hilbert space to analyze your
problem your life is always a lot easier.

# Notation

Given $\lambda \in \mathbb{C}$ we will write $\overline{\lambda }$ for
the conjugate of $\lambda$.

Given a subset $A$ of some topological space, it is also common to write
$\overline{A}$ for the closure of $A$. Though this is a slight abuse of
notation we will do the same as the meaning will always be clear from
context.

Given two topological vector spaces $X, Y$ we write $\mathcal{L}(X, Y)$
for the space of continuous linear operators from $X$ to $Y$ and $X'$
for the space of continuous linear functions to the base field of $X$.

# Introduction

In writing the next post in the series of PDEs I realized that there
were many results from functional analysis which had not been discussed
and would be necessary. As such, this post is meant as a short, yet
rather longer than I intended, introduction to the basic theory that
will be required.

I'm going to assume you know nothing (please don't feel insulted) and go
over the main ideas and results. Much of the material may be familiar so
please feel free to skim briefly through the results or skip entirely.
There is a lot of theory to cover so the proofs will only be sketched.
For more details see for example [1](https://books.google.co.uk/books?hl=en&lr=&id=wCHtLumoGY4C&oi=fnd&pg=PR3&dq=narici+bachman&ots=vxU8cRul6s&sig=tGyszvXv-1psk-qyJ8ruM6S7l5I&redir\U esc=y#v=onepage&q=narici%20bachman&f=false).

# A brief recap of Hilbert spaces

Firstly what is a Hilbert space? To answer that question let's start
with what kind of spaces we want to model.


**Example 1**. The Euclidean space $\mathbb{R}^n$ together with the
inner product

<div>
 $$\begin{aligned}
            x \cdot y:= x\U 1 y\U 1+\ldots x\U n y\U n.

\end{aligned}$$
</div>





**Example 2**. The complex Euclidean space $\mathbb{C}^n$ together with
the inner product

<div>
 $$\begin{aligned}
            \left\langle x,y\right\rangle:= x\U 1 \overline{y\U 1}+\ldots x\U n \overline{y\U n}.

\end{aligned}$$
</div>



You might be wondering why we took the conjugate in the definition of
the inner product above. That is simply because we want the inner
product to define a norm by

<div>
 $$\begin{aligned}
        \lVert x \rVert^2:= \left\langle x,x\right\rangle.

\end{aligned}$$
</div>

  In the cases above note that this is the standard
Euclidean norm

<div>
 $$\begin{aligned}
        \lVert x \rVert^2= \left\langle x,x\right\rangle= \left| x\U 1 \right| ^2+\ldots +\left| x\U n \right|^2 .

\end{aligned}$$
</div>

  A Hilbert space is just this construction generalized to
infinite dimensions. Firstly, the inner product is generalized as
follows.


**Definition 1**. Given a vector space $V$ over $\mathbb{K}$ where
$\mathbb{K}=\mathbb{R}$ or $\mathbb{K}=\mathbb{C}$, an inner product is
a mapping

<div>
 $$\begin{aligned}
            \left\langle\cdot ,\cdot \right\rangle: V \times V \to \mathbb{K}; \quad (x,y)\to \left\langle x,y\right\rangle.

\end{aligned}$$
</div>

  Such that the following hold for all $x,y,z \in V$ and
all $\lambda \in \mathbb{K}$

1.  Linearity:
    $\left\langle\lambda x+y,z\right\rangle= \lambda \left\langle x,z\right\rangle+ \left\langle y,z\right\rangle$.

2.  Conjugate symmetry
    $\left\langle x,y\right\rangle= \overline{\left\langle y,x\right\rangle}$.

3.  Positivity $\left\langle x,x\right\rangle =0$ if and only if
    $x=0$.


In what follows we will take always take the base field to be
$\mathbb{K}$, that is, we will consider real and complex vector spaces
as the theory is the same. In the real case, the conjugate function just
being the identity. Note that the first two properties also imply
"antilinearity" of the second component as

<div>
 $$\begin{aligned}
        \left\langle z,\lambda x+  y\right\rangle=\overline{\left\langle\lambda  x+ y,z\right\rangle}= \overline{\lambda }\left\langle z,x\right\rangle+ \lambda \U 2\left\langle z,y\right\rangle.

\end{aligned}$$
</div>

  A vector space with an inner product is called an inner
product space. This inner product gives us a concept of geometry.


**Definition 3**. Given an inner product space $V$ we define


<div>
 $$\begin{aligned}
            \lVert x \rVert:= \sqrt{\left\langle x,x\right\rangle}.

\end{aligned}$$
</div>

  Furthermore, we say that $x,y$ are orthogonal if
$\left\langle x,y\right\rangle=0$.


With this definition, Pythagoras's theorem follows directly, as if $x,y$
are orthogonal then by the linearity of the inner product.


<div>
 $$\begin{aligned}
        \lVert x+y \rVert^2 = \left\langle x+y,x+y\right\rangle= \lVert x \rVert^2 +\lVert y \rVert^2.

\end{aligned}$$
</div>

  An important property of the inner product is the
following

 <a name="CS">
**Proposition 1** </a>  (Cauchy Schwartz). Let $V$ be an inner product space,
then it holds that

<div>
 $$\begin{aligned}
            \left\langle x,y\right\rangle\leq \lVert x \rVert\lVert y \rVert.

\end{aligned}$$
</div>




In particular, this implies that the inner product is continuous
jointly, and in each component. An inner product space keeps the key
properties of Euclidean space, namely the vector space structure and
inner product. The third key property is that of completeness.


**Definition 4**. A Hilbert space is a complete inner product space
$(H, \left\langle\cdot ,\cdot \right\rangle)$. Where completeness is
respect to the inner product norm

<div>
 $$\begin{aligned}
            \lVert x \rVert^2:= \left\langle x,x\right\rangle.

\end{aligned}$$
</div>




Cool! Now we know what is a Hilbert space. Some examples that have come
up in previous posts are the space of [square-integrable
functions](https://nowheredifferentiable.com/2022-05-27-The-Bochner-integral/#:~:text=we%20can%20integrate.-,Our,-next%20definitions%20are)
valued in another Hilbert space $H$ with the inner product


<div>
 $$\begin{aligned}
        \left\langle f,g\right\rangle\U {L^2(\Omega \to H)}:= \int\U {\Omega} \left\langle f,g\right\rangle d\mu .

\end{aligned}$$
</div>

  Another are the [Sobolev
spaces](https://nowheredifferentiable.com/2022-05-27-The-Bochner-integral/#:~:text=we%20can%20integrate.-,Our,-next%20definitions%20are)
$H^s(\mathbb{R}^d)$ with the inner product

<div>
 $$\begin{aligned}
        \left\langle f,g\right\rangle\U {H^s(\mathbb{R}^d)}:= \int\U {\mathbb{R}^d} \left\langle\omega\right\rangle^{2s} \widehat{f}(\xi ) \overline{\widehat{g}(\xi )}d\xi  .

\end{aligned}$$
</div>

  (I apologize for using the same notation for the
Japanese bracket and the inner product). One result that carries over
from Euclidean spaces to Hilbert spaces is the existence of projections.

 <a name="projection">
**Theorem 1** </a>  (Projection theorem). Let $F$ be a closed convex subset
of a Hilbert space $H$. Then, given $h \in H$ there exists a unique
$f \in F$ such that

<div>
 $$\begin{aligned}
            \min\U {g \in F}\lVert h-g \rVert= \lVert h-f \rVert.

\end{aligned}$$
</div>

  Furthermore, if $F$ is a (vector) subspace, then it
holds that $f$ is the unique element in $F$ such that $h-f$ is
orthogonal to $F$. That is $f\in F$ is the only one verifying


<div>
 $$\begin{aligned}
            h-f \in F^\perp:= \left\{g \in H : \left\langle g,F\right\rangle=\{0\}\right\}.

\end{aligned}$$
</div>





Proof. The idea of the proof is to consider a sequence $f\U n$ that
approaches the minimum distance

<div>
 $$\begin{aligned}
            d(f\U n,h)\to d(h,F).

\end{aligned}$$
</div>

  The inner product comes in to show that $f\U n$ is a
Cauchy sequence. Since $H$ is complete it converges to some $f$. Then
our assumptions on $F$ come in. Firstly, since $F$ is closed shows
$f \in F$. Secondly, since $F$ is convex one can get uniqueness. The
uniqueness is once more a consequence of the properties of the inner
product. ◻


A consequence of the above theorem is that orthogonal complements in
Hilbert spaces exist.

 <a name="complement theorem">
**Theorem 2** </a>  (Orthogonal complement). Let $V$ be a closed subspace of
a vector space $H$. Then we have that

<div>
 $$\begin{aligned}
            V \oplus V^\perp & \longrightarrow H   \\
            (v\U 1,v\U 2)        & \longmapsto v\U 1+v\U 2
            .
\end{aligned}$$
</div>

  Is a bijective isomorphism where we consider on
$V \oplus V^\perp$ the inner product

<div>
 $$\begin{aligned}
            \left\langle(v\U 1,v\U 2),(v\U 1',v\U 2')\right\rangle= \left\langle v\U 1,v\U 1'\right\rangle+ \left\langle v\U 2,v\U 2'\right\rangle.

\end{aligned}$$
</div>





Proof. Given $h \in  H$ we know that there exists a unique closest
point $v\U 1 \in V$ to $V$ (the projection of $h$ onto $v$). Furthermore,
$v\U 2:=h-v \in V^\perp$ so we get the decomposition

<div>
 $$\begin{aligned}
            h=v\U 1 +v\U 2.

\end{aligned}$$
</div>

  This proves bijectivity, whereas the isomorphism
property follows quickly from the orthogonality of $v\U 1,v\U 2$. ◻


An important corollary of this is the following

 <a name="cor">
**Corollary 1** </a> . Let $V$ be a vector space, then

<div>
 $$\begin{aligned}
            \overline{V}=H \iff \overline{V}^\perp =\left\{0\right\} .

\end{aligned}$$
</div>




Note that the imposition that $V$ is closed in Theorem
[2](#complement theorem) is necessary. Finite-dimensional
subspaces are always closed, but infinite-dimensional subspaces may not
be. For example, consider $H=L^2(I)$ for some bounded $I$ and take $V$
to polynomials on $I$ . By the
[Stone-Weierstrass](https://en.wikipedia.org/wiki/Stone%E2%80%93Weierstrass\U theorem)
theorem $V$ is dense in $H$. That is $H=\overline{V}$, whereas


<div>
 $$\begin{aligned}
        H \neq V \oplus V^\perp =V \oplus \left\{0\right\} .

\end{aligned}$$
</div>

  Another property of Euclidean space that Hilbert spaces
reproduce is that of the existence of an orthonormal basis


**Definition 5**. Let $H$ be a Hilbert space and $I$ some index set. We
say that $\mathcal{B}=\left\\{\phi\U \alpha\right\\}\U {\alpha \in  I}$ is an
orthonormal basis of $H$ if

<div>
 $$\begin{aligned}
            \left\langle\phi\U \alpha,\phi\U \beta \right\rangle= \delta \U {\alpha, \beta }, \quad\forall \alpha,\beta \in I.

\end{aligned}$$
</div>

  And for every element $f \in H$ there exist
$\lambda \U \alpha \in  \mathbb{C}$ such that

<div>
 $$\begin{align}
\label{sum}
            f= \sum\U {\alpha \in I} \lambda \U \alpha \phi\U \alpha .

\end{align}$$
</div>




Note that we impose no conditions on the Index set $I$ which may be
countable or uncountable.


**Definition 6**. Given an index set $I$ and a normed vector space $X$
we say that $x\U \alpha$ is absolutely summable to $x$ and write


<div>
 $$\begin{aligned}
            x= \sum\U {\alpha\in I}x\U \alpha

\end{aligned}$$
</div>

  if given $\epsilon >0$ there exists some finite subset
$J\U 0 \in I$ such that for every $J$ containing $J\U 0$ it holds that


<div>
 $$\begin{aligned}
            \lVert x-\sum\U {\alpha\notin J} x\U \alpha \rVert<\epsilon  .

\end{aligned}$$
</div>




If $I$ is countable, the definition says that
$\sum\U {\alpha \in I} x\U \alpha$ converges to $x$ regardless of the order
in which we sum. In fact, the following shows that, even if we start
with an uncountable sequence we will always end up back in this case.


**Proposition 2**. Let $X$ be a normed space and
$\left\\{x\U \alpha\right\\}\U {\alpha \in I} \subset  X$ be absolutely
summable to $x$, then only a countable number of the terms $x\U \alpha$
are non-zero. Let us take the nonzero terms and relabel them
$\left\\{x\U n\right\\}\U {n \in \mathbb{N}}$, then

<div>
 $$\begin{aligned}
            x= \sum\U {n=0}^{\infty} x\U n.

\end{aligned}$$
</div>





Proof. Take $J\U n$ such that

<div>
 $$\begin{aligned}
            \lVert x-\sum\U { \alpha \notin J\U n} x\U \alpha \rVert< \frac{1}{n}   .

\end{aligned}$$
</div>

  Then $J:= \cup\U n J\U n$ is countable (it is a countable
union of countable sets) and a small reasoning shows that $J$ are the
non-zero terms of $I$. The fact that the nonzero $x\U n$ sum to $x$ is
just a consequence of the definition of absolute summability. ◻


Now that we made sense of the sum over a potentially uncountable number
of basis elements in (\ref{sum}) , it remains to address the question of the existence of
orthonormal basis.

 <a name="existence">
**Theorem 3** </a>  (Existence of orthonormal basis). Every Hilbert space has
an orthonormal basis $\mathcal{B}$.



Proof. The proof is formally identical to the proof that every vector
space has a basis space . Let $\mathcal{A}$ be the collection of all
orthonormal subsets of $H$. That is, $\mathcal{A}$ is comprised of sets
of the form

<div>
 $$\begin{aligned}
            \mathcal{S}=\left\{\left\{\phi\U \alpha\right\}\U {\alpha \in  J}:  \left\langle\phi\U \alpha,\phi\U \beta \right\rangle= \delta \U {\alpha, \beta }, \quad\forall \alpha,\beta \in J\right\} .

\end{aligned}$$
</div>

  Such that $\phi\U \alpha$ are orthonormal. Given an
ordered chain
$\mathcal{S}\U 0\subset \mathcal{S}\U 1\subset \mathcal{S}\U 2\subset \cdots$
we have the bound

<div>
 $$\begin{aligned}
            \mathcal{S}\U 0\subset \mathcal{S}\U 1\subset \mathcal{S}\U 2\subset \cdots \subset \bigcup\U {n=0}^\infty \mathcal{S}\U n  .

\end{aligned}$$
</div>

  As a result by [Zorn's
lemma](https://en.wikipedia.org/wiki/Zorn%27s\U lemma) there exists a
maximal element $\mathcal{B}$. If $\mathcal{B}$ is not complete (that is
(\ref{sum})  doesn't hold),
then there exists $f \in \overline{\mathcal{B}}^\perp$. By taking
$f /\lVert f \rVert$ and forming
$\mathcal{B}':=\mathcal{B}\cup \left\\{f \lVert f \rVert\right\\}$ we
obtain that $\mathcal{B}\subsetneq \mathcal{B}' \in \mathcal{A}$. This
contradicts the maximality of $\mathcal{B}$ and concludes the proof. ◻


The next result is the natural generalization of Pythagoras's theorem to
Hilbert spaces.

 <a name="Parseval">
**Theorem 4** </a>  (Parseval). Let $H$ be a Hilbert space with orthonormal
basis $\mathcal{B}=\left\\{\phi\U \alpha\right\\}\U {\alpha\in I}$. Then for
every $f \in  H$ it holds that

<div>
 $$\begin{aligned}
            f= \sum\U {\alpha \in  I} \left\langle f,\phi\U \alpha\right\rangle\phi\U \alpha;\quad \lVert f \rVert^2=\sum\U {\alpha\in I} \lVert \phi\U \alpha \rVert^2.

\end{aligned}$$
</div>





Proof. We have that by the orthonormality of $\phi\U \alpha$ and the
continuity of the inner product

<div>
 $$\begin{aligned}
            \left\langle f-\sum\U {\alpha \in  I} \left\langle f,\phi\U \alpha\right\rangle\phi\U \alpha, \phi\U \alpha\right\rangle=\left\langle f,\phi\U \alpha\right\rangle-\left\langle f,\phi\U \alpha\right\rangle=0.

\end{aligned}$$
</div>

  As a result,
$f-\sum\U {\alpha \in  I} \left\langle f,\phi\U \alpha\right\rangle\phi\U \alpha$
is orthogonal to the closure of the span of $\mathcal{B}$, which by
assumption is $H$. By Corollary [1](#cor) we conclude that

<div>
 $$\begin{aligned}
            f-\sum\U {\alpha \in  I} \left\langle f,\phi\U \alpha\right\rangle\phi\U \alpha=0.

\end{aligned}$$
</div>

  This proves the first part of the theorem. The second
follows by the first together with the orthonormality of
$\phi\U \alpha$. ◻


The above shows that, on fixing a basis, every Hilbert space can be
identified with a space of square-integrable sequences by the bijective
isometry

<div>
 $$\begin{aligned}
        H\to \ell ^2(I); \quad f \to \left\{\left\langle f,\phi\U {\alpha}\right\rangle\right\}\U {\alpha \in I}.

\end{aligned}$$
</div>

  In particular, every Hilbert space with a countable
basis is isometric to $\ell ^2(\mathbb{N})$. However, the identification
is not "canonical" as it depends on the bases chosen. The next example
is all pervasive (in fact it has [even invaded our
blog](https://nowheredifferentiable.com/2023-01-29-PDE-1/))


**Example 3** (Plancherel). The Hilbert space of square integrable
complex valued periodic functions
$L^2(\mathbb{R}^d /\mathbb{Z}^d \to \mathbb{C})$ has orthonormal basis


<div>
 $$\begin{aligned}
            \left\{\phi\U k(x)\right\}\U {k \in \mathbb{Z}^d}:=\left\{e^{2\pi i  k \cdot x }\right\}\U {k \in \mathbb{Z}^d}.

\end{aligned}$$
</div>

  Thus, every function
$f \in L^2(\mathbb{R}^d /\mathbb{Z}^d)$ can be written as


<div>
 $$\begin{aligned}
            f(x)= \sum\U {k \in  \mathbb{Z}^d}\widehat{f}(k)e^{2\pi i  k \cdot x } .

\end{aligned}$$
</div>

  Where $\widehat{f} \in \ell ^2(\mathbb{Z}^d)$ is known
as the Fourier transform of $f$ and defined by

<div>
 $$\begin{aligned}
            \widehat{f}(k):= \left\langle f, \phi\U k\right\rangle= \int\U {\mathbb{R}^d/ \mathbb{Z}^d} f(x)e^{-2 \pi i k \cdot x} \,\mathrm{d}x .

\end{aligned}$$
</div>




Another interesting property of Euclidean space is that every element of
the dual $\ell :\mathbb{C}^n \to \mathbb{C}$ is represented by a vector
in the space, that is

<div>
 $$\begin{aligned}
        \ell (x)= \left\langle x,y\U \ell \right\rangle, \quad\forall  x \in \mathbb{C}^n.

\end{aligned}$$
</div>

  Here one can calculate directly that $y\U \ell$ is the
conjugate of the "matrix" defined by $\ell$ as a linear function


<div>
 $$\begin{aligned}
        y\U \ell =(\overline{\ell (e\U 1)},\ldots,\overline{\ell (e\U n)}) .

\end{aligned}$$
</div>

  Where $e\U i$ is the standard orthonormal basis of
$\mathbb{C}^n$. In Hilbert spaces, the same result holds for Hilbert
spaces

 <a name="riesz theorem">
**Theorem 5** </a>  (Riesz representation ). Let $H$ be a Hilbert space, then
given $\ell \in H'$ there exists a unique $f\U \ell \in H$ such that


<div>
 $$\begin{align}
\label{riesz}
            \left\langle h,f\U \ell \right\rangle, \quad\forall h \in H.

\end{align}$$
</div>

  Furthermore,
$\lVert f\U \ell  \rVert=\lVert \ell  \rVert$.



Proof. Consider an orthonormal basis
$\left\\{\phi\U \alpha\right\\}\U {\alpha \in  I}$ for $H$. Then, just as in
Euclidean space we have that

<div>
 $$\begin{aligned}
            f\U \ell =\sum\U {\alpha \in I}\overline{\ell (\phi\U \alpha)}\phi\U \alpha  .

\end{aligned}$$
</div>

  The fact that $f\U \ell$ verifies
(\ref{riesz})  is a
direct application of the (anti)-linearity and continuity of the inner
product. Uniqueness following from the fact that if $f\U \ell , g\U \ell$
both verify the equality then for all $h \in h$

<div>
 $$\begin{aligned}
            \left\langle h, f\U \ell -g\U \ell \right\rangle= \ell (h)-\ell (h)=0.

\end{aligned}$$
</div>

  This can only occur if $f\U \ell -g\U \ell =0$ (hint take
$h= f\U \ell -g\U \ell$). To verify the norm we can use that, for all
$h \in  H$ with norm $1$

<div>
 $$\begin{aligned}
            \ell   \left(\frac{f\U \ell }{\lVert f\U \ell  \rVert} \right)= \left\langle\frac{f\U \ell }{\lVert f\U \ell  \rVert} ,f\U \ell \right\rangle=\lVert f\U \ell  \rVert; \quad \ell(h)= \left\langle h, f\U \ell \right\rangle\leq \lVert h \rVert\lVert f\U \ell  \rVert= \lVert f\U \ell  \rVert.

\end{aligned}$$
</div>

  The equality shows that
$\lVert \ell  \rVert\geq \lVert f\U \ell  \rVert$ whereas the inequality
shows the converse $\lVert \ell  \rVert\leq \lVert f\U \ell  \rVert$,
proving the theorem. ◻


The previous theorem says that we have an antilinear isometry


<div>
 $$\begin{aligned}
        \Phi\U 1:    H\to H';\quad f\U \ell  \to \ell .

\end{aligned}$$
</div>

  This allows us to identify $H$ with $H'$. The
identification is canonical as it does not depend on the bases chosen.
Yes, we fixed a basis to prove it but the vector $f\U \ell$ is unique
independently of the basis. This allows us to make $H'$ into a Hilbert
space in a canonical way


**Proposition 3**. Let $H$ be a Hilbert space, then $H'$ is also a
Hilbert space, with inner product given by

<div>
 $$\begin{aligned}
            \left\langle\ell\U 1 , \ell\U 2 \right\rangle\U {H'}=\left\langle f\U {\ell \U 2},f\U {\ell\U 1 }\right\rangle\U H.

\end{aligned}$$
</div>




Where we had to "swap the order" of the representatives of
$\ell\U 1, \ell\U 2$ due to the anti-linearity of the mapping
$\ell \to f\U \ell$. Since $H'$ is also a Hilbert space we can apply
Riesz's theorem to $H'$ to show that $H''$ is also a Hilbert space and
there exists a canonical antilinear isometry

<div>
 $$\begin{aligned}
        \Phi\U 2:  H'\to H''; \ell\U \varphi \to \varphi .

\end{aligned}$$
</div>

  By construction, of $\Phi\U 1,\Phi\U 2$ it holds that


<div>
 $$\begin{aligned}
        \Phi\U 2 \circ \Phi\U 1 (f) (\ell )= \ell(f).

\end{aligned}$$
</div>

  That is, $H$ is identified canonically with $H''$ and,
the identification is such that

<div>
 $$\begin{aligned}
        f(\ell )=\ell (f).

\end{aligned}$$
</div>

  In other words.


**Theorem 6**. Every Hilbert space is reflexive.


Consider now a Hilbert space $H$ and a linear operator $T: H \to H$.
Then, for each $g \in H$ we can define the linear form



<div>
 $$\begin{aligned}
        \ell\U g := \left\langle T\cdot ,g\right\rangle.

\end{aligned}$$
</div>

  As a result, there exists a unique representative of
$\ell \U g$ in $H$ which, to track the dependence on $g$, we denote by
$h\U g$. That is, $h\U g$ verifies

<div>
 $$\begin{aligned}
        \left\langle T f,g\right\rangle= \left\langle f,h\U g\right\rangle, \quad\forall f \in H.

\end{aligned}$$
</div>

  A small reasoning shows that $h\U g$ is a linear function
of $g$, that is, there exists $T^\star :H \to H$ with $T^\star g=h\U g$, or in other
words

<div>
 $$\begin{align}
\label{adjoint}
        \left\langle Tf,g\right\rangle=\left\langle f, T^\star g\right\rangle , \quad\forall f,g \in  H.

\end{align}$$
</div>




**Definition 7**. Given $T \in \mathcal{L}(H)$ we denote by $T^\star $ the
unique element verifying (\ref{adjoint})  . If $T=T^\star $ we say that $T$ is self adjoint.


If we think in terms of complex numbers, the adjoint of an element
$\lambda  \in \mathbb{C}$ is $\overline{\lambda }$ and $T$ is self
adjoint if and only if it is real. If now we consider the case where $H$
is $\mathbb{C}^n$ and $T$ is given by some matrix $A$ then
$A^\star =A^\dagger:= \overline{A^T}$. As in these finite dimensional cases,
the following proof is not difficult.


**Proposition 4**. Let $T \in \mathcal{L}(H)$ with $H$ a Hilbert space.
Then $T^\star \in \mathcal{L}(H)$ with
$\left\lVert T \right\rVert=\left\lVert T^\star \right\rVert$.


Hilbert spaces provide us a way to guarantee existence and uniqueness to
a wide class of problems, an important tool is Lax-Milgram's theorem. We
first need two definitions


**Definition 8**. We say that a mapping

<div>
 $$\begin{aligned}
            B:V \times V \to \mathbb{K}

\end{aligned}$$
</div>

  on a vector space $V$, is sesquilinear if $B$ is linear
in the first component and antilinear in the second. That is, for all
$x,y,z \in V$ and $\lambda \in \mathbb{K}$:

<div>
 $$\begin{aligned}
            {B(\lambda x+y,z)}= \lambda B({x,z})+ B({y,z}); \quad B(x,\lambda y+z)= \overline{\lambda} B({x,z})+ B({y,z}) .

\end{aligned}$$
</div>





**Definition 9**. Let $V$ be a normed vector space then we say that a
sesquilinear form $B$ is $\alpha$ coercive if it is continuous and there
exists a constant $\alpha>0$ such that

<div>
 $$\begin{aligned}
            B(f,f)\geq \alpha\lVert f \rVert^2 \quad\forall f \in  H.

\end{aligned}$$
</div>




The coercivity condition essentially imposes that the bilinear form is
not degenerate. As a particular example, a symmetric sesquilinear form
is an inner product.

 <a name="Lax theorem">
**Theorem 7** </a>  (Lax Milgram). Let $B, L$ be respectively an $\alpha$
coercive sesquilinear form and a linear form on a Hilbert space $H$.
Then there exists an invertible linear operator $\mathcal{L}:H \to H$
and $f \in H$ such that

<div>
 $$\begin{aligned}
            B(v,u)=\left\langle v,\mathcal{L}u\right\rangle; \quad L(v)=\left\langle v,f\right\rangle.

\end{aligned}$$
</div>

  As a result, equation

<div>
 $$\begin{align}
\label{lax eq}
            B(v,u)=L(v) \quad\forall v \in H

\end{align}$$
</div>

  has a unique solution $u= \mathcal{L}^{-1} f$.
Furthermore, the solution operator $\mathcal{L}^{-1}$ is continuous with


<div>
 $$\begin{aligned}
            \lVert \mathcal{L}^{-1} \rVert\leq \alpha^{-1} .

\end{aligned}$$
</div>





Proof. For each fixed $u \in H$, we have that
$\ell\U u :=B(\cdot ,u) \in  H'$. As a result by Riesz's representation
theorem (Theorem [5](#riesz theorem)) there exists a unique $f\U {\ell \U u} \in H$
such that

<div>
 $$\begin{align}
\label{f}
            B(v,u)= \ell \U u(v)= \left\langle v, f\U {\ell \U u}\right\rangle .

\end{align}$$
</div>

  Furthermore, it can be simply verified that the mapping
$u \to f\U {\ell \U u}$ is linear in $u$. That is, there exists
$\mathcal{L}: H\to H$ such that

<div>
 $$\begin{align}
\label{g}
            \mathcal{L}u =f\U {\ell \U u} \quad\forall  u \in H.

\end{align}$$
</div>

  The existence of the representative $f \in  H$ of $L$ is
once more by Riesz's representation theorem. We now show that
$\mathcal{L}$ verifies the desired properties. Firstly $\mathcal{L}$ is
continuous as, given $u\in  H$

<div>
 $$\begin{aligned}
            \lVert \mathcal{L}u \rVert^2=\left\langle\mathcal{L}u,  \mathcal{L}u\right\rangle=B(\mathcal{L}u, u)\leq \lVert B \rVert \lVert u \rVert\lVert  \mathcal{L}u \rVert.

\end{aligned}$$
</div>

  So dividing by $\lVert \mathcal{L}u \rVert$ on either
side shows that $\lVert \mathcal{L} \rVert \leq \lVert B \rVert$. Now,
$\mathcal{L}$ is injective as if $\mathcal{L}u=0$ then

<div>
 $$\begin{aligned}
            0=\left\langle u, \mathcal{L}u\right\rangle= B(u,u) \geq \alpha \lVert u \rVert^2 .

\end{aligned}$$
</div>

  We now prove surjectivity of $\mathcal{L}$. Consider
$u \in  \Im(\mathcal{L})^\perp$, then it holds that

<div>
 $$\begin{align}
\label{est}
            \left\langle u, \mathcal{L}u\right\rangle= B(u,u)\geq \alpha \lVert u \rVert^2.

\end{align}$$
</div>

  As a result, we deduce from the corollary of the
orthogonal complement theorem [1](#cor) that $\overline{\Im(\mathcal{L})}=0$. Thus, if we show
that $\mathcal{L}$ is closed invertibility follows. The estimate in
(\ref{est})  together with
Cauchy Schwartz show that for all $u \in H$

<div>
 $$\begin{aligned}
            \lVert  \mathcal{L}u \rVert\geq \lVert u \rVert.

\end{aligned}$$
</div>

  As if $\mathcal{L}u\U n \in  \Im (\mathcal{L})$ is a
Cauchy sequence then so must be $u\U n$. By completeness of $\mathcal{L}$,
the sequence $u\U n$ converges to some $u \in  H$ and we deduce, by
continuity of $\mathcal{L}$, that
$\mathcal{L}u\U n \to \mathcal{L}u \in \Im (\mathcal{L})$. In consequence,
$\mathcal{L}$ is invertible, finally to show the bound on
$\mathcal{L}^{-1}$ let us write $u =\mathcal{L}^{-1} f$ then


<div>
 $$\begin{aligned}
            \alpha \lVert u \rVert^2 \leq B(u,u) = \left\langle u,f\right\rangle\leq \lVert u \rVert\lVert f \rVert .

\end{aligned}$$
</div>

  Dividing on either side by $\alpha \lVert u \rVert$
concludes the proof. ◻


If we had assumed that $B$ were anti-symmetric then the proof would have
been simplified as $B$ would define an inner product
$\left\langle\cdot ,\cdot \right\rangle\U B$. Applying Riesz's theorem to
this inner product (as opposed to the original one) would transform our
equation (\ref{lax eq})  into

<div>
 $$\begin{aligned}
        \left\langle v,u\right\rangle\U B= \left\langle v,f\right\rangle , \quad\forall v\in H.

\end{aligned}$$
</div>

  That is, to solve
(\ref{lax eq})  it
would suffice to take $u=f$. In the case where $B$ is symmetric and
real, we can also find $u$ by solving a minimization problem


**Proposition 5** (Minimization formulation). Let
$B: H\times H \to \mathbb{R}$ be a symmetric coercive bilinear operator
on a real Hilbert space $H$. Then, problem
(\ref{lax eq})  is
equivalent to minimizing

<div>
 $$\begin{aligned}
            J(u):= \frac{1}{2}B(u,u)-L(u) .

\end{aligned}$$
</div>





Proof. To prove that a solution to
(\ref{lax eq})
minimizes $J$ we can develop $J(u+v)$ and simplify it using
$B(v,u)=L(v)$ to obtain

<div>
 $$\begin{aligned}
            J(u+v) \geq J(u) , \quad\forall  v \in H.

\end{aligned}$$
</div>

  To prove that a minimum of $J$ solves $\eqref{lax eq}$
one can show by taking limits as $\lambda  \to 0$ in the expression


<div>
 $$\begin{aligned}
            J(u) \leq J(u+ \lambda (h-u)).

\end{aligned}$$
</div>

  That for all $h$

<div>
 $$\begin{aligned}
            L(h-u) \leq B(u,h-u).

\end{aligned}$$
</div>

  Taking $h=u+v$ and $h=u-v$ where $v$ is any shows
$-L(v) \leq -B(u,v)$ and $L(v) \leq B(u,v)$, which concludes the
proof. ◻


# A little bit of operator theory

Finally, we wrap up with some operator theory. This will be revisited in
a more detailed blog post on spectral theory. For now, we give the
essentials.


**Definition 10**. We say that a linear operator $K: X \to Y$ where
$X,Y$ are two metric spaces is compact if $T(B)$ is relatively compact
for all bounded $B \subset  X$.


The above will be abbreviated $K \in  \mathcal{K}(X,Y)$. Note that,
since every compact set is bounded $K$ must be bounded and thus
continuous. That is

<div>
 $$\mathcal{K}(X,Y)\subset \mathcal{L}(X,Y).$$
</div>

  In
practice, the following equivalent characterizations are useful.

 <a name="equivalent">
**Proposition 6** </a> . Let $X,Y$ be two metric spaces, then the following
are equivalent

a)  $K \in \mathcal{K}(X,Y)$.

b)  $K(B\U X)$ is relatively compact where
    $B\U X=\\{ x \in X : \lVert x \rVert<1\\}$ is the unit ball in $X$.

c)  From every sequence $Kx\U n$ where $x\U n \in B\U X$ one can extract a
    subsequence $K {x\U {n\U j}}$ converging in $Y$.



Proof. The prove the first two points are equivalent we observe that
every bounded set $B \subset  X$ is contained in $\lambda B\U X$ for
$\lambda$ big enough. A general fact from topology is that closed
subsets of compact sets are compact. This is enough to conclude the
equivalence.

To prove that the last two points are equivalent we recall that in
metric spaces compact is equvalent to sequentially compact. ◻


An important property of compact operators is that they are preserved by
continuous ones.

 <a name="comp">
**Proposition 7** </a> . Let
$K \in \mathcal{K}(X,Y), T\U 1\in \mathcal{L}(W,X), T\U 2 \in L(Y,Z)$. Where
$W,X,Y,Z$ are metric spaces , then $K\circ T\U 1$ and $T\U 2 \circ K$ are
compact



Proof. This follows by the last equivalent characterization in
Proposition [6](#equivalent). ◻


We already saw that the space of compact operators $\mathcal{K}(X,Y)$ is
a subset of the space of linear operators. The structure of
$\mathcal{K}(X,Y)$ as a subspace is as follows


**Proposition 8**. Let $X,Y$ be metric spaces then $\mathcal{K}(X,Y)$
is a vector space. Furthermore, if $Y$ is completee then
$\mathcal{K}(X,Y)$ is closed in $\mathcal{L}(X,Y)$. That is, if $K\U n$
are compact and $K\U n \to K \in \mathcal{L}(X,Y)$ then $K$ is compact.



Proof. The first part again follows fromb the last equivalent
characterization in Proposition [6](#equivalent). The second part relies on the fact that in
complete spaces compact and [totally
bounded](https://en.wikipedia.org/wiki/Totally\U bounded\U space#:~:text=not%20in%20general.-,In,-metric%20spaces%5B)
are equivalent. ◻


The reason we are interested in compact operators is that they are
particularly simple. Note that every finite-dimensional operator (that
is operators whose image is finite-dimensional) is compact by the
Heine-Borel theorem. In fact, a good way of thinking of compact
operators is to see them as finite-dimensional operators . Or more
precisely, as the limit of them


**Proposition 9**. Let $K \in  \mathcal{K}(X,H)$ where $H$ is a
separable Hilbert space . Then there exists a sequence of
finite-dimensional operators $K\U n$ such that

<div>
 $$\begin{aligned}
            \lim\U {n \to \infty}K\U n=K.

\end{aligned}$$
</div>





Proof. Since $H$ is separable there exists a countable orthonormal
basis $\left\\{\phi\U n\right\\}\U {n \in \mathbb{N}}$. If we denote $T\U n$ for
the projection of $K$ onto the space generated by
$\left\\{\phi\U 1,\ldots,\phi\U n\right\\}$ then, by Parseval's Theorem
pointwise convergence holds

<div>
 $$\begin{aligned}
            K\U n(x) \to K(x) , \quad\forall x \in  H.

\end{aligned}$$
</div>

  Consider the unit ball $B\U X$ in $X$. Then $K(B\U X)$ is
relatively compact. So $K(B\U X)$ is totally bounded and given
$\epsilon >0$ we can form a finite $\epsilon$ net $Kx\U 1,\ldots,Kx\U m$ of
$K(B\U X)$. By pointwise convergence, we can now take $n\U 0$ large enough
so that for all $N \geq n\U 0$

<div>
 $$\begin{aligned}
            \lVert K(x\U j)-K\U N(x\U j) \rVert , \quad\forall j=1,\ldots,m.

\end{aligned}$$
</div>

  Now for any $x\in B\U X$ we can find $x\U j$ such that
$\lVert Tx\U j-Tx \rVert< \epsilon$. Using the triangle inequality


<div>
 $$\begin{aligned}
            \lVert Kx-K\U N x \rVert \leq \lVert Kx-K x\U j \rVert+ \lVert K x\U j-K\U N x\U {j} \rVert+ \lVert K\U N x\U j-K\U N x \rVert < 3\epsilon .

\end{aligned}$$
</div>

  This concludes the proof. ◻


For us, an important example of compact operators will be the solution
operator $\mathcal{L}^{-1}$ of a PDE. This is because of the following
theorem

 <a name="Rellich">
**Theorem 8** </a>  (Rellich-Kondrachov). Let $U \subset \mathbb{R}^n$ be a
bounded open domain in $\mathbb{R}^n$ with smooth boundary. Then, given
$s >0$ it holds that the natural inclusion

<div>
 $$\begin{aligned}
            i: H^{s+ \sigma }(U) \hookrightarrow H^s(U)

\end{aligned}$$
</div>

  is compact for all $\sigma >0$.


For the proof of a more general version see [2](https://books.google.co.uk/books?id=wI4fAwAAQBAJ&printsec=frontcover&hl=fr&source=gbs\U ge\U summary\U r&cad=0#v=onepage&q&f=false) page
334. It is important to observe the restriction that $U$ is bounded is
necessary and the theorem no longer holds if $U$ is replaced by
$\mathbb{R}^n$.

 <a name="addd">
**Corollary 2** </a>  (Adding differentiability is compact). Let
$U \subset \mathbb{R}^n$ be a bounded open domain in $\mathbb{R}^n$ with
smooth boundary and $s, \sigma >0$, then every continuous operator


<div>
 $$\begin{aligned}
            T:H^{s+ \sigma }(U) \hookrightarrow H^s(U)

\end{aligned}$$
</div>

  is compact.



Proof. We have that $T= i \circ T$ so we conclude by
Rellich-Kondrachov's theorem [8](#Rellich) and the preservation of compact operators by
continuous ones (Proposition [7](#comp)). ◻


Compact operators also have a nice spectral theory. Where we recall that
the spectrum of an operator $T$ is defined as

<div>
 $$\begin{aligned}
        \sigma (T):=\left\{\lambda \in \mathbb{K}: \lambda \mathbf{Id}-T \text{ is not invertible } \right\} .

\end{aligned}$$
</div>

  Firstly, the spectrum of a compact operator is equal to
it's eigenvalues. Secondly the following holds


**Theorem 9** (Spectral theorem). Let $K \in \mathcal{K}(H)$ be compact
and self adjoint on a Hilbert space $H$. Then $T$ diagonalizes in an
orthonormal basis. That is, there exists an orthonormal basis
$\left\\{\phi\U \alpha\right\\} \U {\alpha \in  I}$ and
$\lambda \U \alpha \in \mathbb{K}$ such that

<div>
 $$\begin{aligned}
            Kx=\left(\sum\U {\alpha \in I}^{\infty} \lambda \U \alpha \phi\U \alpha\otimes \phi\U \alpha\right) x  =\sum\U {\alpha \in  I} \lambda \U \alpha \left\langle x,\phi\U \alpha\right\rangle\phi\U \alpha .

\end{aligned}$$
</div>




A more general result is possible but requires more theory so we reserve
it for another day. That said, this type of discrete representation of
$T$ is very useful and links up with the theory of trace class and
Hilbert-Schmidt operators which we will discuss more in the future.

To end it all off we state without proof a theorem that will be useful
in proving properties about the solution space to the solution of PDEs


**Theorem 10** (Fredholm alternative). Let $H$ be a Hilbert space and
$K \in \mathcal{K}(H)$. Consider $T:= Id-K$ then it holds that


<div>
 $$\begin{aligned}
            T \text{ is injective } \iff  T \text{ is surjective}.

\end{aligned}$$
</div>

  Furthermore, it holds that

a)  $\mathbf{ker}(T)$ is finite dimensional.

b)  $T$ is closed.

c)  $\Im (T)=\mathbf{ker}(T^\star )^\perp$.

d)  $\mathrm{dim}(\mathbf{ker}(T))=\mathrm{dim}(\mathbf{ker}(T^\star ))$


We delay the proof till another day, in the meantime, see
[3](https://math24.files.wordpress.com/2013/02/partial-differential-equations-by-evans.pdf) page 725.


    
    </div>
