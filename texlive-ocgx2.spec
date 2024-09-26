Name:		texlive-ocgx2
Version:	72300
Release:	1
Summary:	Drop-in replacement for 'ocgx' and 'ocg-p'
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/ocgx2
License:	lppl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ocgx2.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ocgx2.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package serves as a drop-in replacement for the packages
ocgx by Paul Gaborit and ocg-p by Werner Moshammer for the
creation of PDF Layers. It re-implements the functionality of
the ocg, ocgx, and ocg-p packages and adds support for all
known engines and back-ends including: LaTeX - dvips -
ps2pdf/Distiller (Xe)LaTeX(x) - dvipdfmx pdfLaTeX and LuaLaTeX
. It also ensures compatibility with the media9 and animate
packages.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/ocgx2
%doc %{_texmfdistdir}/doc/latex/ocgx2

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
