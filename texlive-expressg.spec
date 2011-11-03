# revision 15878
# category Package
# catalog-ctan /graphics/metapost/contrib/macros/expressg
# catalog-date 2007-01-05 12:56:21 +0100
# catalog-license lppl
# catalog-version 1.5
Name:		texlive-expressg
Version:	1.5
Release:	1
Summary:	Diagrams consisting of boxes, lines, and annotations
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/metapost/contrib/macros/expressg
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/expressg.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/expressg.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/expressg.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
A MetaPost package providing facilities to assist in drawing
diagrams that consist of boxes, lines, and annotations.
Particular support is provided for creating EXPRESS-G diagrams,
for example IDEF1X, OMT, Shlaer-Mellor, and NIAM diagrams. The
package may also be used to create UML and most other Box-Line-
Annotation charts, but not Gantt charts directly.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar metapost doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
