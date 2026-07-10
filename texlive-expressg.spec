%global tl_name expressg
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.5
Release:	%{tl_revision}.1
Summary:	Diagrams consisting of boxes, lines, and annotations
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/metapost/contrib/macros/expressg
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/expressg.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/expressg.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/expressg.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A MetaPost package providing facilities to assist in drawing diagrams
that consist of boxes, lines, and annotations. Particular support is
provided for creating EXPRESS-G diagrams, for example IDEF1X, OMT,
Shlaer-Mellor, and NIAM diagrams. The package may also be used to create
UML and most other Box-Line-Annotation charts, but not Gantt charts
directly.

