Name:		texlive-expressg
Version:	29349
Release:	2
Summary:	Diagrams consisting of boxes, lines, and annotations
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/metapost/contrib/macros/expressg
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/expressg.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/expressg.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/expressg.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A MetaPost package providing facilities to assist in drawing
diagrams that consist of boxes, lines, and annotations.
Particular support is provided for creating EXPRESS-G diagrams,
for example IDEF1X, OMT, Shlaer-Mellor, and NIAM diagrams. The
package may also be used to create UML and most other Box-Line-
Annotation charts, but not Gantt charts directly.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/metapost/expressg/aam.mp
%{_texmfdistdir}/metapost/expressg/expeg.mp
%{_texmfdistdir}/metapost/expressg/expressg.mp
%doc %{_texmfdistdir}/doc/metapost/expressg/README
%doc %{_texmfdistdir}/doc/metapost/expressg/aamfigs.pdf
%doc %{_texmfdistdir}/doc/metapost/expressg/aamfigs.tex
%doc %{_texmfdistdir}/doc/metapost/expressg/expeg.pdf
%doc %{_texmfdistdir}/doc/metapost/expressg/expeg.tex
%doc %{_texmfdistdir}/doc/metapost/expressg/expressg.pdf
%doc %{_texmfdistdir}/doc/metapost/expressg/n2mps.sh
%doc %{_texmfdistdir}/doc/metapost/expressg/n2mpsprl.prl
#- source
%doc %{_texmfdistdir}/source/metapost/expressg/expressg.dtx
%doc %{_texmfdistdir}/source/metapost/expressg/expressg.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar metapost doc source %{buildroot}%{_texmfdistdir}
